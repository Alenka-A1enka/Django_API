from django.db import models

class Users(models.Model):
    surname = models.CharField('Фамилия', max_length=100)
    name = models.CharField('Имя', max_length=100)
    login = models.CharField('Логин', max_length=50, unique=True)
    password = models.CharField('Пароль', max_length=100)
    email = models.CharField('Email', max_length=100)

    def __str__(self):
        return f'User: {self.surname} {self.name} ({self.login})'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Lessons(models.Model):
    name = models.CharField('Название урока', max_length=250)
    url = models.URLField('Ссылка на видео', unique=True)
    video_duration = models.PositiveIntegerField('Длительность видео')
    
    def __str__(self):
        return f'{self.name} - {self.video_duration}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        
        
class Products(models.Model):
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_name = models.CharField('Название продукта', max_length=250, unique=True)
    lessons = models.ManyToManyField(Lessons, null=True)
    
    def __str__(self):
        return f'{self.owner} {self.product_name}'
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    

class Access(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    available_products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.user} {self.available_products}'
    
    class Meta:
        verbose_name = 'Разрешение'
        verbose_name_plural = 'Разрешения'
        unique_together = ('user', 'available_products')
        

class LessonViews(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    datetime = models.DateTimeField('Время просмотра')
    viewing_duration = models.PositiveIntegerField('Длительность просмотра')
    status = models.BooleanField('Статус просмотра', default=False)

    def __str__(self):
        return f'{self.lesson} {self.user} {self.datetime}'
    
    class Meta:
        verbose_name = 'Просмотр'
        verbose_name_plural = 'Просмотры'
        unique_together = ('lesson', 'user')
        
class APIAllProducts(models.Model):
    lesson_name = models.CharField('Название урока', max_length=250, default='Без названия')
    lesson_url = models.URLField('Ссылка на видео', default='http://...')
    datetime = models.DateTimeField('Время просмотра')
    status = models.BooleanField('Статус просмотра', default=False)
    
    def __str__(self):
        return f'{self.lesson_name} {self.lesson_url} {self.datetime} {self.status}'
    
class APICurrentProduct(models.Model):
    lesson_name = models.CharField('Название урока', max_length=250, default='Без названия')
    lesson_url = models.URLField('Ссылка на видео', default='http://...')
    status = models.BooleanField('Статус просмотра', default=False)
    viewing_time_in_seconds = models.PositiveIntegerField('Время просмотра видео')
    datetime = models.DateTimeField('Дата последнего просмотра видео')
    
class APIProductStatistics(models.Model):
    name = models.CharField('Название продукта', max_length=250, default='Без названия')
    lessons_viewing_count = models.PositiveIntegerField('Кол-во просмотренных уроков от всех учеников')
    lessons_viewing_time = models.PositiveIntegerField('Кол-во потраченного времени на просмотр уроков')
    users_count = models.PositiveIntegerField('Кол-во учеников занимающихся на продукте')
    product_purchase_percent = models.FloatField('Процент приобретения продукта')
    

