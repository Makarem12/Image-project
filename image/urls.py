
from django.urls import path
from .views import home_view, img_details_view

urlpatterns = [
    path('', home_view, name='home'),
    path('<int:pk>', img_details_view, name="details")

]