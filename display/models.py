from django.db import models

# Create your models here.

class user_query(models.Model):
    user_name=models.CharField(max_length=50, default="name")
    user_email=models.EmailField(max_length=50,default="email")
    user_number=models.CharField(max_length=20,default="0")
    user_querry=models.CharField(max_length=1000,default="querry")

    def __str__(self):
        return self.user_name + " " + self.user_email
class hostel(models.Model):
    hostel_name=models.CharField(max_length=120, default="")
    hostel_state=models.CharField(max_length=30, default="Delhi")
    hostel_city=models.CharField(max_length=30, default="Delhi")
    hostel_area=models.CharField(max_length=120, default="Civil Lines")
    hostel_pincode=models.IntegerField(default="110054")
    hostel_address=models.CharField(max_length=120, default="Civil Lines")
    hostel_rent=models.IntegerField(default="6000")
    hostel_deposit=models.IntegerField(default="5000")
    hostel_contactnumber=models.IntegerField(default="+91")
    hostel_mess=models.IntegerField(default="1")
    hostel_mealtype=models.CharField(max_length=120, default="veg")
    hostel_ac=models.IntegerField(default="1")
    hostel_vistorentry=models.IntegerField(default="1")
    hostel_watercooler=models.IntegerField(default="1")
    hostel_roomcleaning=models.IntegerField(default="1")  
    hostel_description=models.TextField(max_length=500, default="veg food allowed, A.C provided, washing machine available, iron availble, Geyser provided")
    hostel_images1=models.ImageField(upload_to='display/img/hostel_images',default="" )
    hostel_image2=models.ImageField(upload_to='display/img/hostel_images', default="" )
    def __str__(self):
        return self.hostel_name +" " + self.hostel_area 

class  medical_storesservice(models.Model):
    medical_storesservice_name=models.CharField(max_length=80, default="")
    medical_storesservice_state=models.CharField(max_length=30, default="")
    medical_storesservice_city=models.CharField(max_length=30, default="")
    medical_storesservice_area=models.CharField(max_length=120, default="")
    medical_storesservice_address=models.CharField(max_length=120, default="")
    medical_storesservice_pincode=models.IntegerField(default="")
    medical_storesservice_price=models.IntegerField(default="0")
    medical_storesservice_contactnumber=models.IntegerField(default="+91")
    medical_storesservice_mealtype=models.CharField(max_length=120, default="veg")
    medical_storesservice_mealsperday=models.IntegerField(default=3)
    medical_storesservice_description=models.TextField(max_length=500, default="")
    medical_storesservice_images1=models.ImageField(upload_to='display/img/medical_stores_service_images' ,default="")
    medical_storesservice_image2=models.ImageField(upload_to='display/img/medical_stores_service_images' ,default="")
    def __str__(self):
        return self.medical_storesservice_name 

class  laundry(models.Model):
    laundry_name=models.CharField(max_length=80, default="")
    laundry_state=models.CharField(max_length=30, default="Delhi")
    laundry_city=models.CharField(max_length=30, default="Delhi")
    laundry_area=models.CharField(max_length=120, default="Chandini Chowk")
    laundry_address=models.CharField(max_length=120, default="")
    laundry_pincode=models.IntegerField(default="110006")
    laundry_price=models.IntegerField(default="0")
    laundry_contactnumber=models.IntegerField(default="+91")
    laundry_description=models.TextField(max_length=200, default="")
    laundry_images1=models.ImageField(upload_to='display/img/laundry_images', default="" )
    def __str__(self):
        return self.laundry_name 

class  library(models.Model):
    library_name=models.CharField(max_length=80, default="")
    library_address=models.CharField(max_length=120, default="")
    library_state=models.CharField(max_length=30, default="Delhi")
    library_city=models.CharField(max_length=30, default="Delhi")
    library_pincode=models.IntegerField(default="110006")
    library_area=models.CharField(max_length=120, default="Chandini Chowk")
    library_deposit=models.IntegerField(default="0")
    library_contactnumber=models.IntegerField(default="+91")
    library_pincode=models.IntegerField(default="00")
    library_area=models.CharField(max_length=120, default="")
    library_description=models.TextField(max_length=200, default="")
    library_images1=models.ImageField(upload_to='display/img/library_images', default="" )
    def __str__(self):
        return self.library_name 