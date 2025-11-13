from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'
    ),
    path('draft/', views.post_list_draft, name='post_list_draft'),
    path('published/', views.PostListView.as_view(), name='post_list_published'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]