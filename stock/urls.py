from django.urls import path
from . import views
from . views import StockDetailView, StockCreateView

urlpatterns = [
    path('', views.details, name='stock-home'),
    # path('details', views.details, name="stock-details")
    path('details/<int:pk>', StockDetailView.as_view(), name="stock-details-view"),
    path('details/new', StockCreateView.as_view(), name="stock-create"),
    path('details/', views.details, name="stock-details"),
    path('load', views.loadmore, name="load-more"),
    path('less', views.showless, name="show-less")
]