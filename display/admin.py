from django.contrib import admin
from .models import hostel, laundry, library, medical_storesservice, user_query,laboratory

# Register your models here.
admin.site.register(user_query)
admin.site.register(hostel)
admin.site.register(medical_storesservice)
admin.site.register(laundry)
admin.site.register(library)
admin.site.register(laboratory)