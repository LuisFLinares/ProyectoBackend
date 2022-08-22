from django.urls import path
from .views import ProductsView,DeleteProductsView, CategoriesView, DeleteCategoriesView, PurchaseView,DeletePurchaseView, PurchaseDetailView, DeletePurchaseDetailView, UploadView

urlpatterns = [
    path('products', ProductsView.as_view()),
    path('products/<pk>', DeleteProductsView.as_view()),
    path('categories',CategoriesView.as_view()),
    path('categories/<pk>', DeleteCategoriesView.as_view()),
    path('purchase', PurchaseView.as_view()),
    path('purchase/<pk>', DeletePurchaseView.as_view()),
    path('purchase-detail', PurchaseDetailView.as_view()),
    path('purchase-detail/<pk>', DeletePurchaseDetailView.as_view()),
    path('upload-image', UploadView.as_view())
]