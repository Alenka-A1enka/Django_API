from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Users, Access, APIAllProducts, LessonViews, Products, APICurrentProduct, APIProductStatistics
from .serializers import APIAllProductsSerializer, APICurrentProductSerializer, APIProductStatisticsSerializer
from rest_framework import generics


from rest_framework.response import Response
from rest_framework.views import APIView

class AllProductsView(APIView):
    def get(self, request):
        id = self.request.GET.get('id')
        
        # Если не был передан параметр, оповещаем об этом. 
        if id is None:
            return HttpResponse('Не передан параметр "id"')
        
        # Поиска объекта пользователя. 
        try:
            current_user = Users.objects.get(pk=id)
        except:
            return HttpResponse('Нет пользователя по данному id')
        
        # Получение списка доступных продуктов пользователя. 
        access = Access.objects.filter(user=current_user.id)
            
        products = []
        
        # Формирование списка продуктов
        for access_obj in access:
            products.append(access_obj.available_products)
            
        APIAllProducts.objects.all().delete() # Очистка объектов из предыдущих зарпосов. 
            
        for product in products:
            for lesson in product.lessons.all():
                # Осуществляется проход по каждому уроку продукта. 
                
                new_APIAllProducts_object = APIAllProducts() # Создание объекта модели для response. 
                new_APIAllProducts_object.lesson_name = lesson.name # Имя урока. 
                new_APIAllProducts_object.lesson_url = lesson.url # Ссылка на урок. 
                
                # Получение ссылки на объект урока
                lessonViews_object = LessonViews.objects.filter(lesson = lesson, user=current_user).first()
                
                # Если у пользователя нет просмотренных уроков, то ставим значения по умолчанию. 
                if lessonViews_object is None:
                    new_APIAllProducts_object.datetime = '0001-01-01 00:00:01' # Установка даты.
                    new_APIAllProducts_object.status = False # Установка времени. 
                
                else:
                    new_APIAllProducts_object.datetime = lessonViews_object.datetime # Установка даты. 
                    new_APIAllProducts_object.status = lessonViews_object.status # Установка времени. 
                    
                new_APIAllProducts_object.save() # Сохранение объекта. 
                
        queryset = APIAllProducts.objects.all() # Получаем все созданные объекты. 
        serializer_class = APIAllProductsSerializer(instance=queryset, many=True) # Сериализация. 
        return Response(serializer_class.data)
      
class CurrentProductView(APIView):
    def get(self, request):
        id = self.request.GET.get('id')
        product_id = self.request.GET.get('product_id')
        
        # Если не был передан хотя бы один параметр, оповещаем об этом. 
        if id is None or product_id is None:
            return HttpResponse('Не передан параметр "id" или "product_id"')
        
        # Поиска объекта пользователя. 
        try:
            current_user = Users.objects.get(pk=id)
        except:
            return HttpResponse('Нет пользователя по данному id')
        
        
        # Получение списка доступных продуктов пользователя. 
        access = Access.objects.filter(user=current_user.id)
            
        products = []
        
        # Формирование списка продуктов
        for access_obj in access:
            products.append(access_obj.available_products)
            
        
        # Поиск объекта продукта по его id
        try:
            current_product = Products.objects.get(pk=product_id)
        except:
            return HttpResponse('Нет продукта по данному id')  
            
        if current_product not in products:
            return HttpResponse('Пользователю недоступен данный продукт')
        
        
        APICurrentProduct.objects.all().delete() # Очистка объектов из предыдущих зарпосов. 
            
        for lesson in current_product.lessons.all():
            # Осуществляется проход по каждому уроку продукта. 
                
            new_APICurrentProduct_object = APICurrentProduct() # Создание объекта модели для response. 
            new_APICurrentProduct_object.lesson_name = lesson.name # Имя урока. 
            new_APICurrentProduct_object.lesson_url = lesson.url # Ссылка на урок. 
                
            # Получение ссылки на объект урока
            lessonViews_object = LessonViews.objects.filter(lesson = lesson, user=current_user).first()
                
            # Если у пользователя нет просмотренных уроков, то ставим значения по умолчанию. 
            if lessonViews_object is None:
                new_APICurrentProduct_object.datetime = '0001-01-01 00:00:01' # Установка даты.
                new_APICurrentProduct_object.status = False # Установка даты последнего просмотра. 
                new_APICurrentProduct_object.viewing_time_in_seconds = 0 # Установка времени просмотра. 
                
            else:
                new_APICurrentProduct_object.datetime = lessonViews_object.datetime # Установка даты. 
                new_APICurrentProduct_object.status = lessonViews_object.status # Установка времени. 
                new_APICurrentProduct_object.viewing_time_in_seconds = lessonViews_object.viewing_duration
                    
            new_APICurrentProduct_object.save() # Сохранение объекта. 
                
        queryset = APICurrentProduct.objects.all() # Получаем все созданные объекты. 
        serializer_class = APICurrentProductSerializer(instance=queryset, many=True) # Сериализация. 
        return Response(serializer_class.data)   
    
class StatisticsView(APIView):
    
    def get(self, request):
        products = Products.objects.all()
        
        APIProductStatistics.objects.all().delete()
        
        for product in products:
            new_APICurrentProduct_object = APIProductStatistics()
            
            # Значения по умолчанию. 
            new_APICurrentProduct_object.name = product.product_name
            new_APICurrentProduct_object.lessons_viewing_count = 0
            new_APICurrentProduct_object.lessons_viewing_time = 0
            new_APICurrentProduct_object.users_count = 0
            new_APICurrentProduct_object.product_purchase_percent = 0
            
            # Проходим по всем урокам продукта. 
            for lesson in product.lessons.all():
                
                # Получаем все данные о просмотре данного урока. 
                lesson_views = LessonViews.objects.filter(lesson=lesson)
                
                # Кол-во объектов просмотра равно кол-ву всех просмотров пользователями. 
                new_APICurrentProduct_object.lessons_viewing_count += lesson_views.count()
                
                # Проходим по всем объектам просмотров. 
                for lesson_view in lesson_views.all():
                    # Добавляем время просмотра от каждого пользователя. 
                    new_APICurrentProduct_object.lessons_viewing_time += lesson_view.viewing_duration
            
            # Получаем доступы пользователей к продукту, чтобы узнать сколько
            # пользователей занимается по продукту. 
            access = Access.objects.filter(available_products=product)
            new_APICurrentProduct_object.users_count = access.count()
            
            # Все объекты пользователей платформы. 
            users = Users.objects.all()
            users_count = users.count() # Кол-во таких объектов. 
            # Рассчет процента пользования продуктом.  
            new_APICurrentProduct_object.product_purchase_percent = \
                new_APICurrentProduct_object.users_count / users_count
            
            new_APICurrentProduct_object.save() # Сохранение объекта класса
            
        queryset = APIProductStatistics.objects.all() # Получаем все созданные объекты. 
        serializer_class = APIProductStatisticsSerializer(instance=queryset, many=True) # Сериализация. 
        return Response(serializer_class.data)  
    
        
    

