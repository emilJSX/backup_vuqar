from django.urls import path

from . import views

app_name = 'serviceapp'

urlpatterns = [
    path('service/<int:pk>/', views.XidmetlerDetailView.as_view(), name="services-detail")
]