# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from api import views

# urlpatterns=[
#     url(r'^$',views.bbs_list),
#     url(r'^(?p<pk>[0-9]+)/$',views.bbs_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

#from django.conf.urls import url    
from django.urls import path, include
from .views import KipoListApiView



urlpatterns = [
    path('api', KipoListApiView.as_view()),
]