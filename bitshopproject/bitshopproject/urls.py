from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from bitshopapp import views
from bitshopapp.sanitize import books_api, movies_api, mobiles_api, computers_api, cameras_api, home_api, toys_api, sports_api, beauty_api, clothing_api, jewel_api, bags_api, shoes_api, cars_api
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
    url(r'^news/(?P<n_id>\d+)/$', views.NewsPage, name='newsdetail'),
    url(r'^productdetails/(?P<p_id>\d+)/$', views.ProductPage, name='productdetail'),
    url(r'^results/$', views.Search, name='results'),
    url(r'^signin/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register_view, name='signup'),

    url(r'^read1/', books_api.read_file1, name='read_file1'),
    url(r'^read2/', movies_api.read_file2, name='read_file2'),
    url(r'^read3/', mobiles_api.read_file3, name='read_file3'),
    url(r'^read4/', computers_api.read_file4, name='read_file4'),
    url(r'^read5/', cameras_api.read_file5, name='read_file5'),
    url(r'^read6/', home_api.read_file6, name='read_file6'),
    url(r'^read7/', toys_api.read_file7, name='read_file7'),
    url(r'^read8/', sports_api.read_file8, name='read_file8'),
    url(r'^read9/', beauty_api.read_file9, name='read_file9'),
    url(r'^read10/', clothing_api.read_file10, name='read_file10'),
    url(r'^read11/', jewel_api.read_file11, name='read_file11'),
    url(r'^read12/', bags_api.read_file12, name='read_file12'),
    url(r'^read13/', shoes_api.read_file13, name='read_file13'),
    url(r'^read14/', cars_api.read_file14, name='read_file14'),
    url(r'^getproducts/', views.getproducts, name='getproducts')
]
urlpatterns += staticfiles_urlpatterns()
