from django.conf.urls import urls
from blog import views

urlpatterns =[
  path('about',views.AboutView.as_view(),name='about'),
]