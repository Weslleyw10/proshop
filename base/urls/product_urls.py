from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.getProducts, name='products'),
    path('<str:pk>/', views.getProduct, name='product'),
    
    path('create', views.createProduct, name='product-create'),
    path('<str:pk>/update', views.updateProduct, name='product-update'),
    path('<str:pk>/delete', views.deleteProduct, name='delete-product'),
    
    path('top', views.getTopProducts, name='top-product'),
    path('<str:pk>/reviews', views.createProductReview, name='review-product'),
    path('upload', views.uploadImage, name='product-image'),

]