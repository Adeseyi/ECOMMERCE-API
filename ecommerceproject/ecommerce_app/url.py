from django.urls import path,include
# from .views import ListCategories, DetailCategories, ListBooks, DetailBooks, ListProducts, DetailProducts
# urlpatterns = [
#     path('categories', ListCategories.as_view(), name='categories'),
#     path('categories/<int:pk>/', DetailCategories.as_view(), name='singlecategory'),
#     path('books', ListBooks.as_view(), name='books'),
#     path('books/<int:pk>/', DetailBooks.as_view(), name='singlebook'),

#     path('products', ListProducts.as_view(), name='products'),
#     path('products/<int:pk>/', DetailProducts.as_view(), name='product'),
# ]

from .views import BookViewSet
from .views import ProductViewSet
from .views import CategoriesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')

p_router = DefaultRouter()
p_router.register('products', ProductViewSet, basename='product')

c_router = DefaultRouter()
c_router.register('categories', CategoriesViewSet, basename='category')

urlpatterns=[
    path("",include(router.urls)),
    path("",include(p_router.urls)),
     path("",include(c_router.urls)),
]
