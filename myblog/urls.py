from django.urls import path, include
import myblog.views

urlpatterns = [
    path('hello_world', myblog.views.hello_world),
    path('content', myblog.views.article_content),
    path('index', myblog.views.get_index_page),
    # path('detail', myblog.views.get_detail_page),
    path('detail/<int:article_id>', myblog.views.get_detail_page),
]
