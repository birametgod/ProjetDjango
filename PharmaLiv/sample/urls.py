from django.urls import path,include
from sample.views import SampleFormView

urlpatterns = [
    path('map/', SampleFormView.as_view(), name='map_name'),
]