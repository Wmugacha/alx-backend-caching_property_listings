from django.urls import path, include
from .views import PropertyListView
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('properties/', cache_page(60 * 15)(PropertyListView.as_view()), name='property-list'),
]