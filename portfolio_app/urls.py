from django.urls import path
from . import views

urlpatterns = [
	path('', views.AllBlogsView.as_view(), name="home"),
	path('page/<int:page>/', views.home, name="home_page"),
	path('.json', views.blogs_api, name="home_api"),
	path('blog/<slug:blog_slug>/', views.blog, name="blog"),
	path('download-resume/', views.download_file, name="download-resume")
]
