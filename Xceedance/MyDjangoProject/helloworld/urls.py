from django.urls import path, include
from helloworld import views


urlpatterns = [
    path('',views.product_index,name='product_index'),
    path('<int:pk>/',views.product_detail,name='product_detail')
]
