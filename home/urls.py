from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.showProduct),
    path('product/detail/<int:id>', views.ProductDetail)
    ]