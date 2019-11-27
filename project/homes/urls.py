from django.urls import path
from . import views

urlpatterns = [
    path('api/homes/', views.HomesEndpoint.as_view()),
    path('api/singlehome/<int:zillow_id>/', views.SingleHomeEndpoint.as_view()),
    path('api/createhome/', views.CreateHomeEndpoint.as_view()),
]
