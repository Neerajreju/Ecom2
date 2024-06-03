
from django.urls import path
# import the views,py
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import loginform


urlpatterns = [
    path('', views.home, name='home'),
    path("/about/", views.About,name="about"),
    path("/contact/", views.Contact,name="contact"),
    path("/cart/", views.cart, name="cart"),
    path("/buy/", views.buy, name="buy"),

    path('category/<slug:val>',views. CategoryView.as_view(),name='category'),
    path('product-detials/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('category-title/<val>', views.CategoryTitle.as_view(), name='category-title'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
    path('adress/', views.adressView, name='adress'),
    path('logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),

                  # authentication
    path('registration/' , views.CustomerRegistrationView.as_view() , name='customeregistration'),
    path('accounts/login/' , auth_view.LoginView.as_view(template_name='app/login.html' , authentication_form=loginform) , name='login'),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)