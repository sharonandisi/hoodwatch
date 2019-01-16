from django.conf.urls import url , include
from django.conf import settings
from django.conf.urls.static import static 
from . import views


urlpatterns = [
    url('^$', views.index, name='index'),
    url('^post/', views.post, name='post'),
    url(r'^search/', views.search, name='search'),
    url(r'^profile/(?P<username>\w{0,50})$', views.profile, name='profile'),
    url(r'^edit_profile/(?P<username>\w{0,50})$', views.edit_profile, name='edit_profile'),
    url(r'^new_post$', views.new_post, name='new_post'),
    url(r'^new_business$', views.new_business, name='new_business')

]