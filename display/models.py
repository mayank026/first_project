from django.db import models

# Create your models here.

class user_query(models.Model):
    user_name=models.CharField(max_length=50, default="name")
    user_email=models.EmailField(max_length=50,default="email")
    user_number=models.CharField(max_length=20,default="0")
    user_querry=models.CharField(max_length=1000,default="querry")

    def __str__(self):
        return self.user_name + " " + self.user_email


class laboratory(models.Model):
    laboratory_name=models.CharField(max_length=120, default="")
    laboratory_state=models.CharField(max_length=30, default="Bihar")
    laboratory_city=models.CharField(max_length=30, default="Muzaffarpur")
    laboratory_area=models.CharField(max_length=120, default="Juran Chhapra")
    laboratory_pincode=models.IntegerField(default="110054")
    laboratory_address=models.CharField(max_length=120, default="Muzaffarpur")
    laboratory_contactnumber=models.IntegerField(default="+91")
    laboratory_bloodtest=models.IntegerField(default="1")
    laboratory_ctscan=models.IntegerField(default="1")
    laboratory_rent=models.IntegerField(default="500")
    laboratory_xray=models.IntegerField(default="1")
    laboratory_corona=models.IntegerField(default="1")  
    laboratory_description=models.TextField(max_length=500, default="This lab is certified  byCAP (College of American Pathologists) and Certified by ISO 9001 (International Organization of Standardization).")
    laboratory_images1=models.ImageField(upload_to='display/img/laboratory_images',default="" )
    laboratory_image2=models.ImageField(upload_to='display/img/laboratory_images', default="" )
    def __str__(self):
        return self.laboratory_name +" " + self.laboratory_area         
class docs(models.Model):
    docs_name=models.CharField(max_length=120, default="")
    docs_state=models.CharField(max_length=30, default="Delhi")
    docs_city=models.CharField(max_length=30, default="Delhi")
    docs_area=models.CharField(max_length=120, default="Civil Lines")
    docs_pincode=models.IntegerField(default="110054")
    docs_address=models.CharField(max_length=120, default="Civil Lines")
    docs_fee=models.IntegerField(default="1000")
    docs_timing=models.CharField(max_length=120, default="10:00 AM-4:00 PM")
   # docs_deposit=models.IntegerField(default="5000")
    docs_contactnumber=models.IntegerField(default="+91")
    #docs_mess=models.IntegerField(default="1")
    #docs_mealtype=models.CharField(max_length=120, default="veg")
    docs_Physician=models.IntegerField(default="1")
    docs_Dentist=models.IntegerField(default="1")
    docs_Gynaecologist=models.IntegerField(default="1")
    docs_Child=models.IntegerField(default="1")
    docs_Eye=models.IntegerField(default="1")
    docs_Surgeon=models.IntegerField(default="1")
    docs_degree=models.TextField(max_length=500, default="MBBS M.D, AIMS Delhi")
    docs_images1=models.ImageField(upload_to='display/img/hostel_images',default="" )
    #docs_image2=models.ImageField(upload_to='display/img/hostel_images', default="" )
    def __str__(self):
        return self.docs_name +" " + self.docs_area 

class  medical_storesservice(models.Model):
    medical_stores_name=models.CharField(max_length=80, default="")
    medical_stores_state=models.CharField(max_length=30, default="")
    medical_stores_city=models.CharField(max_length=30, default="")
    #medical_storesservice_area=models.CharField(max_length=120, default="")
    medical_stores_address=models.CharField(max_length=120, default="")
    medical_stores_pincode=models.IntegerField(default="")
    medical_stores_timing=models.CharField(max_length=30, default="")
    medical_stores_contactnumber=models.IntegerField(default="+91")
    medical_stores_medicinetype=models.CharField(max_length=120, default="")
   # medical_storesservice_mealsperday=models.IntegerField(default=3)
    #medical_storesservice_description=models.TextField(max_length=500, default="")
    medical_stores_images1=models.ImageField(upload_to='display/img/medical_stores_service_images' ,default="")
    medical_stores_image2=models.ImageField(upload_to='display/img/medical_stores_service_images' ,default="")
    def __str__(self):
        return self.medical_stores_name 

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