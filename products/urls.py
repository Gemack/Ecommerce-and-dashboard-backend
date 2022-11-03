from django.urls import path
from . import views


urlpatterns = [
    path('create', views.CreateProduct.as_view()),
    path('prud/<int:pk>', views.Get_Delete_Update_product.as_view()),
    path('create_get', views.Create_Get_Hot.as_view()),
    path('upd_del/<int:pk>', views.Update_Delete_Hot.as_view()),
]
