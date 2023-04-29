from django.urls import path

# from .settings import STATIC_URL
from . import views

# from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-Product'),
    path('update/<int:Product_id>', views.update_Product),
    path('delete/<int:Product_id>', views.delete_Product)
]

# if DEBUG:
#     urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
#     urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)