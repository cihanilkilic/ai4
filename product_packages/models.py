from django.db import models
from django.contrib.auth.models import User

 # PAKET İSİMLERİN OLUŞTURULMASI
class ProductPackage(models.Model):
    package_name = models.CharField(max_length=255)
    package_price = models.DecimalField(max_digits=10, decimal_places=2)
    package_duration = models.CharField(max_length=100, blank=True, null=True)  # Paket süresi eklendi
    feature_1 = models.CharField(max_length=255, blank=True, null=True)
    feature_2 = models.CharField(max_length=255, blank=True, null=True)
    feature_3 = models.CharField(max_length=255, blank=True, null=True)
    feature_4 = models.CharField(max_length=255, blank=True, null=True)
    feature_5 = models.CharField(max_length=255, blank=True, null=True)
    feature_6 = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.package_name


 # Starter Package
class StarterPackage(models.Model):
    user_full_name = models.CharField(max_length=255, blank=True, null=True)  # Kullanıcının tam adı
    purchased_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Satın alan kullanıcı
    user_email = models.EmailField(blank=True, null=True)  # Kullanıcının e-posta adresi
    package_id = models.IntegerField()  # Benzersiz olmayan ve otomatik artmayan paket ID
    package_price = models.DecimalField(max_digits=10, decimal_places=2)  # Paket fiyatı
    purchase_date = models.DateTimeField(auto_now_add=True)  # Paket alış tarihi
    expiration_date = models.DateTimeField(blank=True, null=True)  # Paket bitiş tarihi
    is_active = models.BooleanField(default=False)  # Paket etkin mi


    def __str__(self):
        return f"Starter Package - {self.purchased_by} ({self.user_email})"

 # Professional Package
class ProfessionalPackage(models.Model):
    user_full_name = models.CharField(max_length=255, blank=True, null=True)  # Kullanıcının tam adı
    purchased_by = models.ForeignKey(User, on_delete=models.CASCADE)  
    user_email = models.EmailField(blank=True, null=True)  
    package_id = models.IntegerField()  
    package_price = models.DecimalField(max_digits=10, decimal_places=2)  
    purchase_date = models.DateTimeField(auto_now_add=True)  
    expiration_date = models.DateTimeField(blank=True, null=True)  
    is_active = models.BooleanField(default=False)  


    def __str__(self):
        return f"Professional Package - {self.purchased_by} ({self.user_email})"

 # Standard Package
class StandardPackage(models.Model):
    user_full_name = models.CharField(max_length=255, blank=True, null=True)  # Kullanıcının tam adı
    purchased_by = models.ForeignKey(User, on_delete=models.CASCADE)  
    user_email = models.EmailField(blank=True, null=True)  
    package_id = models.IntegerField()  
    package_price = models.DecimalField(max_digits=10, decimal_places=2)  
    purchase_date = models.DateTimeField(auto_now_add=True)  
    expiration_date = models.DateTimeField(blank=True, null=True)  
    is_active = models.BooleanField(default=False)  



    def __str__(self):
        return f"Standard Package - {self.purchased_by} ({self.user_email})"