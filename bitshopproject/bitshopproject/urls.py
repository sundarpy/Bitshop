from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from bitshopapp import views
from bitshopapp.sanitize import api
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)

handler400 = 'bitshopapp.views.bad_request'
handler403 = 'bitshopapp.views.permission_denied'
handler404 = 'bitshopapp.views.page_not_found'
handler500 = 'bitshopapp.views.server_error'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage, name='home'),
    url(r'^category/(?P<c_id>\d+)/$', views.CategoryPage, name='categorydetail'),
    url(r'^subcategory/(?P<c_id>\d+)/(?P<s_id>\d+)/$', views.SubCategoryPage, name='subcategorydetail'),
    url(r'^newsdetail/(?P<n_id>\d+)/$', views.NewsPage, name='newsdetail'),
    url(r'^productdetails/(?P<p_id>\d+)/$', views.ProductPage, name='productdetail'),
    url(r'^results/$', views.Search, name='results'),
    url(r'^signin/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register_view, name='signup'),
    url(r'^news/$', views.News, name='news'),
    
    url(r'^signin/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register_view, name='signup'),
    url(r'^read/', api.read_file, name='read_file'),
    url(r'^getproducts/', views.getproducts, name='getproducts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
