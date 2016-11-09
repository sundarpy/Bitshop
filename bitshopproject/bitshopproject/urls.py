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
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.HomePage, name='home'),
    url(r'^home/$', views.HomePage, name='home'),

    url(r'^category/(?P<slug>[-\w\d]+)/$', views.CategoryPage, name='categorydetail'),
    url(r'^subcategory/(?P<slug1>[-\w\d]+)/(?P<slug2>[-\w\d]+)/$', views.SubCategoryPage, name='subcategorydetail'),
    url(r'^article/(?P<n_id>\d+)/$', views.NewsPage, name='newsdetail'),
    url(r'^productdetails/(?P<p_id>\d+)/$', views.ProductPage, name='productdetail'),
    url(r'^brandetails/(?P<b_id>\d+)/$', views.BrandsPage, name='brandetail'),
    url(r'^results/$', views.Search, name='results'),

    url(r'^categoryprice/(?P<slug>[-\w\d]+)/(?P<pr_id>\d+)/$', views.PriceFilterCategory, name='pricecatdetail'),
    url(r'^brandprice/(?P<b_id>\d+)/(?P<pr_id>\d+)/$', views.PriceFilterBrands, name='pricebranddetail'),
    url(r'^subcategoryprice/(?P<slug1>[-\w\d]+)/(?P<slug2>[-\w\d]+)/(?P<pr_id>\d+)/$', views.PriceFilterSubCategory, name='pricesubcatdetail'),

    url(r'^read/', api.read_file, name='read_file'),
    url(r'^read2/', api.read_file2, name='read_file2'),
    url(r'^read3/', api.read_file3, name='read_file3'),

    url(r'^categories/Men/$', views.Men, name='men'),
    url(r'^categories/Women/$', views.Women, name='women'),
    url(r'^categories/Appliances/$', views.Appliances, name='appliances'),
    url(r'^categories/Home/$', views.Home2, name='home2'),
    url(r'^categories/Electronics/$', views.Electronics, name='electronics'),

    url(r'^getproducts/', views.getproducts, name='getproducts'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
