from django.conf.urls import url
from .views import URLView


urlpatterns = [
    url(r'^$', URLView.as_view(), name='URLForm')
]
