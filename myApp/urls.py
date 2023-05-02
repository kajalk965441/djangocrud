from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-Product'),
    path('update/<int:Product_id>', views.update_Product),
    path('delete/<int:Product_id>', views.delete_Product)
]

