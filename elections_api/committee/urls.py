from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"contributions/total/", views.total_contributions, name="version"),
    url(r"all_names", views.all_names, name="version"),
]
