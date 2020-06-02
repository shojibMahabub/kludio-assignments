from django.urls import path
from . import views


urlpatterns = [
	# Auth
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    
	# list all entries
	path('home/', views.listview, name="listview"),
    
	# entry point
	path('', views.customer_entry, name="entry"),


]