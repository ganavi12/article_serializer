
from django.urls import path
from . import views

urlpatterns = [ 
    # path("article", views.article_list_create_view, name="article_list"), 
    # path("article/<int:pk>",views.article_detail_api_view,name="article_detail"),

    path("article", views.ArticleListCreateApiView.as_view(), name="article_list"),  
    path("article/<int:pk>", views.ArticleDetailApiView.as_view(), name="article_detail"),
    path("journalists", views.JournalistListCreateApiView.as_view(), name="journalist_list"),  
    # path("journalists/<int:pk>",views.JournalistDetailApiView.as_view(),name="journalist_detail"),  

]
