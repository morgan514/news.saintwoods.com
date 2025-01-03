from django.urls import path
from . import views
from .views import HomePageView, SearchResultsView
urlpatterns = [
    path("",views.index,name="index"),
    path("post/<slug>",views.post,name="post"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]