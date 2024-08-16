from rest_framework.serializers import ModelSerializer
from main.models import Banner, Contact, Product, Category

class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        
        
class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
        
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'