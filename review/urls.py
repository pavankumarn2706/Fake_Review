from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('extract_review',views.extract_review,name='extract_review')
]