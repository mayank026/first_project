from django import urls
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path("", views.home_page,name="home"),
	path("rental/",views.rental,name="rental"),
	path("medical_stores/",views.medical_stores,name="medical_stores"),
	path("miscellaneous",views.misc,name="misc"),
	path("register/",views.register,name="register"),
	path("login/",views.login,name="login"),
	path("logout/",views.logout,name="logout"),
	path("laundry/",views.laundary,name="laundry"),
	path("library/",views.lib,name="library"),
	path("aboutus/",views.about,name="aboutus"),
	path("message/",views.message,name="message"),
    path("<int:hostel_id>/hostel_detail/",views.hostel_description_page,name="hosteldesc"),
	path("<int:medical_storesservice_id>/medical_stores_detail/",views.medical_stores_description_page,name="medical_storesdesc"),
	path("<int:library_id>/library_detail/",views.library_description_page,name="librarydesc"),
	path("<int:laundry_id>/laundry_detail/",views.laundry_description_page,name="laundrydesc"),
]
