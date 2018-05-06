from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"contributions/(\d+)/total", views.total_contributions, name="total_contributions"),
    url(r"expenditures/(\d+)/total", views.total_expenditures, name="total_expenditures"),
    url(r"expenditures/categories/(\d+)/total", views.spending_categories, name="spending_categories"),
    url(r"donors/(\d+)/top", views.top_donors, name="top_donors"),
    url(r"all_names", views.all_names, name="all_names"),
]
