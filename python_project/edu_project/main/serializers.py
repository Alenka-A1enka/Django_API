from rest_framework import serializers
from .models import Users, APIAllProducts, APICurrentProduct, APIProductStatistics

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['login', 'email']
    
class APIAllProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIAllProducts
        fields = ['lesson_name', 'lesson_url', 'datetime', 'status']
        
class APICurrentProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APICurrentProduct
        fields = ['lesson_name', 'lesson_url', 'status', 'viewing_time_in_seconds', 'datetime']
        
class APIProductStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIProductStatistics
        fields = ['name', 'lessons_viewing_count', 'lessons_viewing_time', 'users_count', 'product_purchase_percent']
        
