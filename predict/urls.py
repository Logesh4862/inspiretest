from django.urls import path
from predict.views import HomePage, FindCategory


urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('findcategory', FindCategory.as_view(), name="findcategory")
]