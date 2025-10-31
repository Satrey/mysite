from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('draft/', views.post_list_draft, name='post_list_draft'),
    path('draft/<int:id>', views.post_detail_draft, name='post_detail_draft'),
    path('published/', views.post_list_published, name='post_list_published'),
    path('published/<int:id>/', views.post_detail_published, name='post_detail_published')
]