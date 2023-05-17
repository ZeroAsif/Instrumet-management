from django.contrib import admin
from django.urls import path
from instrumentapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.SignupPage,name='signup'),
    path('home/',views.HomePage,name='home'),
    path('admins/',views.Adminpage,name='admins'),
    path('addinstrument/',views.Addinstrument,name='addinstrument'),
    path('bookinstrument/',views.Bookinstrument,name='bookinstrument'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('approvel/',views.Approvel,name='approvel'),
    path('status/',views.Status,name='status'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)