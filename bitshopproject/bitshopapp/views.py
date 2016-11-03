from django.shortcuts import render, HttpResponse, Http404, render_to_response, get_object_or_404
from django.template.loader import get_template
from django.template import Context, RequestContext, loader
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.views.decorators.csrf import csrf_protect
from bitshopapp.models import *
from bitshopapp.forms import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models.aggregates import Count
from random import randint
import datetime
from datetime import date, timedelta
from itertools import chain
import json

"""==============================="""
"""=========SEARCH METHOD========="""
"""==============================="""

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def Search(request):
	"""Search."""
	limitedoffer = LimitedOffer.objects.all()
	navbar_category = Category.objects.all()
	cat = Category.objects.all()
	subcat = SubCategory.objects.all()
	mac = str(get_client_ip(request))

	try:
		q = request.GET.get('q')
	except:
		q = None

	if q:
		products_list = Product.objects.filter(title__icontains=q).order_by('?')

		recom_temp2 = Recommendation.objects.filter(mac_address=mac, rectype="S")
		count_temp2 = recom_temp2.count()
		serch =  products_list.first()

		if serch:
			if count_temp2 < 5:
				recom2_type = Recommendation(product=serch, mac_address=mac, rectype="S")
				recom2_type.save()
			else : 
				recom_x2 = Recommendation.objects.filter(mac_address=mac, rectype="S").first()
				recom_x2.delete()
				recom2_type = Recommendation(product=serch, mac_address=mac, rectype="S")
				recom2_type.save()

		productcount = products_list.count
		paginator = Paginator(products_list, 25)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		total_pages = products.paginator.num_pages+1

		prodnum = products.number
		x = products.number - 1
		y = products.number + 7
		sl = "%d:%d" % (x,y)
		current_path = request.get_full_path()
		context = {
					"query": q, 
					"count": productcount,
					"products": products,
					"limitedoffer":limitedoffer,
					"subcats":subcat, 
					"cats":cat,
					"user" : request.user,
					"navbar_category" : navbar_category,
					"sl":sl,
					"prodnum":prodnum,
					'range': range(1,total_pages),
					'current_path': current_path,
					}
		template = 'results.html'
	else:
		template = 'home.html'
		context = {"prodnum":prodnum, "subcats":subcat, "cat":cat, "navbar_category" : navbar_category,"user" : request.user,}
	return render(request, template, context)

"""==============================="""
"""===========HOME PAGE==========="""
"""==============================="""

def HomePage(request):
	"""Home Page"""
	mac = str(get_client_ip(request))
	navbar_category = Category.objects.all()
	saleoffer = SaleOffer.objects.all()
	limitedoffer = LimitedOffer.objects.all()
	category = Category.objects.all()
	sub_category = SubCategory.objects.all()
	subcategory = SubCategory.objects.filter(category=category)
	products = Product.objects.filter(subcategory=subcategory)
	news = New.objects.all().order_by('-id')
	recommended_products = Recommendation.objects.filter(mac_address=mac)
	men_prod = SerfoProduct.objects.filter(super_category='M')
	women_prod = SerfoProduct.objects.filter(super_category='W')
	appliances_prod = SerfoProduct.objects.filter(super_category='A')
	home_prod = SerfoProduct.objects.filter(super_category='H')
	electronics_prod = SerfoProduct.objects.filter(super_category='E')

	context = {
				"category":category, 
				"subcategory":subcategory, 
				"products":products, 
				"sub_category":sub_category, 
				"data1" : men_prod,
				"data2" : women_prod,
				"data3" : appliances_prod,
				"data4" : home_prod,
				"data5" : electronics_prod, 
				"navbar_category" : navbar_category,
				"news" : news,
				"user" : request.user,
				"saleoffer" : saleoffer,
				"limitedoffer" : limitedoffer,
				"recoms" : recommended_products,
				}
	template = 'home.html'
	return render(request, template, context)

"""=================================="""
"""=====CATEGORY INDIVIDUAL PAGE====="""
"""=================================="""

def CategoryPage(request, slug):
	"""Category Detail Page"""
	limitedoffer = LimitedOffer.objects.all()
	prices = Price.objects.all().order_by('-id')
	navbar_category = Category.objects.all()
	brands = Brand.objects.all().order_by('?')
	category = Category.objects.get(category_slug=slug)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
	products_list = Product.objects.filter(category=category).order_by('?')

	paginator = Paginator(products_list, 25)
	productcount = products_list.count
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	x = products.number - 1
	y = products.number + 7
	sl = "%d:%d" % (x,y)

	news = New.objects.filter(category=category).order_by('-id')
	context = {"prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "category":category, "subcategory":subcategory, "products":products, "navbar_category":navbar_category,"user" : request.user, "brands":brands,  "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages)}
	template = 'categorydetail.html'
	return render(request, template, context)

"""============================="""
"""=====CATEGORY PRICE PAGE====="""
"""============================="""

def PriceFilterCategory(request, slug, pr_id):
	"""Price Filter Category Page"""
	limitedoffer = LimitedOffer.objects.all()
	selected_price = Price.objects.get(pk=pr_id)
	title = selected_price.title
	upper = selected_price.upper_limit
	lower = selected_price.lower_limit
	prices = Price.objects.all().order_by('-id')
	navbar_category = Category.objects.all()
	brands = Brand.objects.all().order_by('?')
	category = Category.objects.get(category_slug=slug)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
	products_list = Product.objects.filter(Q(category=category, offer_price__lte=upper, offer_price__gte=lower) | Q(category=category, sale_price__lte=upper, sale_price__gte=lower))
	paginator = Paginator(products_list, 25)
	productcount = products_list.count
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	x = products.number - 1
	y = products.number + 7
	sl = "%d:%d" % (x,y)

	news = New.objects.filter(category=category).order_by('-id')
	context = {"prodnum":prodnum, "selected_price":selected_price, "limitedoffer":limitedoffer, "count":productcount, "category":category, "subcategory":subcategory, "products":products,"user" : request.user, "navbar_category":navbar_category, "brands":brands,  "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages), "title":title, "upper":upper, "lower":lower}
	template = 'pricecatdetail.html'
	return render(request, template, context)

"""=================================="""
"""======BRANDS INDIVIDUAL PAGE======"""
"""=================================="""

def BrandsPage(request, b_id):
	"""Brands Detail Page"""
	limitedoffer = LimitedOffer.objects.all()
	prices = Price.objects.all().order_by('-id')
	navbar_category = Category.objects.all()
	brands = Brand.objects.all().order_by('?')
	prime_brand = Brand.objects.get(pk=b_id)
	category = Category.objects.all()
	products_list = Product.objects.filter(brand=prime_brand).order_by('id')
	paginator = Paginator(products_list, 25)
	productcount = products_list.count
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	x = products.number - 1
	y = products.number + 7
	sl = "%d:%d" % (x,y)

	news = New.objects.all().order_by('-id')
	context = {"prodnum":prodnum, "limitedoffer":limitedoffer, "count":productcount, "category":category, "products":products, "navbar_category":navbar_category,"user" : request.user, "brands":brands, "prime_brand":prime_brand, "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages)}
	template = 'brandetail.html'
	return render(request, template, context)

"""============================="""
"""======BRANDS PRICE PAGE======"""
"""============================="""

def PriceFilterBrands(request, b_id, pr_id):
	"""Brands Price Filter Page"""
	limitedoffer = LimitedOffer.objects.all()
	selected_price = Price.objects.get(pk=pr_id)
	title = selected_price.title
	upper = selected_price.upper_limit
	lower = selected_price.lower_limit
	prices = Price.objects.all().order_by('-id')
	navbar_category = Category.objects.all()
	brands = Brand.objects.all().order_by('?')
	prime_brand = Brand.objects.get(pk=b_id)
	category = Category.objects.all()
	products_list = Product.objects.filter(Q(brand=prime_brand, offer_price__lte=upper, offer_price__gte=lower) | Q(brand=prime_brand, sale_price__lte=upper, sale_price__gte=lower))
	paginator = Paginator(products_list, 25)
	productcount = products_list.count
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	x = products.number - 1
	y = products.number + 7
	sl = "%d:%d" % (x,y)

	news = New.objects.all().order_by('-id')
	context = {"prodnum":prodnum, "selected_price":selected_price, "limitedoffer":limitedoffer, "count":productcount, "upper":upper, "lower":lower, "category":category, "products":products,"user" : request.user, "navbar_category":navbar_category, "brands":brands, "prime_brand":prime_brand, "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages), "title":title}
	template = 'pricebranddetail.html'
	return render(request, template, context)

"""====================================="""
"""=====SUBCATEGORY INDIVIDUAL PAGE====="""
"""====================================="""

def SubCategoryPage(request, slug1, slug2):
	"""SubCategory Detail Page"""
	limitedoffer = LimitedOffer.objects.all()
	prices = Price.objects.all().order_by('-id')
	navbar_category = Category.objects.all()
	brands = Brand.objects.all().order_by('?')
	category = Category.objects.get(category_slug=slug1)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
	subcat = SubCategory.objects.get(subcategory_slug=slug2, category=category)
	products_list = Product.objects.filter(subcategory=subcat).order_by('id')
	paginator = Paginator(products_list, 25)
	productcount = products_list.count
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	x = products.number - 1
	y = products.number + 7
	sl = "%d:%d" % (x,y)

	news = New.objects.filter(category=category).order_by('-id')
	context = {"prodnum":prodnum, "limitedoffer":limitedoffer, "count":productcount, "category":category, "subcategory":subcategory, "products":products,"user" : request.user, "navbar_category":navbar_category,"subcat":subcat, "brands":brands,  "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages)}
	template = 'subcategorydetail.html'
	return render(request, template, context)

"""====================================="""
"""=====SUBCATEGORY INDIVIDUAL PAGE====="""
"""====================================="""

def PriceFilterSubCategory(request, slug1, slug2, pr_id):
	"""SubCategory Filter Page"""
	limitedoffer = LimitedOffer.objects.all()
	prices = Price.objects.all().order_by('-id')
	selected_price = Price.objects.get(pk=pr_id)
	title = selected_price.title
	upper = selected_price.upper_limit
	lower = selected_price.lower_limit
	navbar_category = Category.objects.all()
	brands = Brand.objects.all().order_by('?')
	category = Category.objects.get(category_slug=slug1)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
	subcat = SubCategory.objects.get(subcategory_slug=slug2, category=category)
	products_list = Product.objects.filter(Q(subcategory=subcat, offer_price__lte=upper, offer_price__gte=lower) | Q(subcategory=subcat, sale_price__lte=upper, sale_price__gte=lower))
	paginator = Paginator(products_list, 25)
	productcount = products_list.count
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	x = products.number - 1
	y = products.number + 7
	sl = "%d:%d" % (x,y)

	news = New.objects.filter(category=category).order_by('-id')
	context = {"prodnum":prodnum, "selected_price":selected_price, "limitedoffer":limitedoffer, "category":category, "subcategory":subcategory, "products":products,"user" : request.user, "navbar_category":navbar_category,"subcat":subcat, "count":productcount, "brands":brands,  "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages), "title":title, "upper":upper, "lower":lower}
	template = 'pricesubcatdetail.html'
	return render(request, template, context)

"""=============================="""
"""=====NEWS INDIVIDUAL PAGE====="""
"""=============================="""

def NewsPage(request, n_id):
	"""Product News Detail Page"""
	limitedoffer = LimitedOffer.objects.all()
	navbar_category = Category.objects.all()
	news = New.objects.get(pk=n_id)
	multi_news = New.objects.all().order_by('?')
	saleoffer = SaleOffer.objects.all()
	product1 = []
	product2 = []
	product3 = []
	product4 = []
	product5 = []
	product6 = []
	product7 = []
	product8 = []
	product9 = []
	product10 = []

	if news.product_link1:
		link1 = str(news.product_link1)
		id1 = int(link1.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product1 = Product.objects.get(pk=id1)
	if news.product_link2:
		link2 = news.product_link2
		id2 = int(link2.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product2 = Product.objects.get(pk=id2)
	if news.product_link3:
		link3 = news.product_link3
		id3 = int(link3.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product3 = Product.objects.get(pk=id3)
	if news.product_link4:
		link4 = news.product_link4
		id4 = int(link4.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product4 = Product.objects.get(pk=id4)
	if news.product_link5:
		link5 = news.product_link5
		id5 = int(link5.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product5 = Product.objects.get(pk=id5)
	if news.product_link6:
		link6 = news.product_link6
		id6 = int(link6.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product6 = Product.objects.get(pk=id6)
	if news.product_link7:
		link7 = news.product_link7
		id7 = int(link7.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product7 = Product.objects.get(pk=id7)
	if news.product_link8:
		link8 = news.product_link8
		id8 = int(link8.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product8 = Product.objects.get(pk=id8)
	if news.product_link9:
		link9 = news.product_link9
		id9 = int(link9.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product9 = Product.objects.get(pk=id9)
	if news.product_link10:
		link10 = news.product_link10
		id10 = int(link10.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product10 = Product.objects.get(pk=id10)

	men_prod = SerfoProduct.objects.filter(super_category='M')
	women_prod = SerfoProduct.objects.filter(super_category='W')
	appliances_prod = SerfoProduct.objects.filter(super_category='A')
	home_prod = SerfoProduct.objects.filter(super_category='H')
	electronics_prod = SerfoProduct.objects.filter(super_category='E')
	
	context = {
				"news":news, 
				"navbar_category":navbar_category,
				"data1" : men_prod,
				"data2" : women_prod,
				"data3" : appliances_prod,
				"data4" : home_prod,
				"data5" : electronics_prod,
				"product1" : product1,
				"product2" : product2,
				"product3" : product3,
				"product4" : product4,
				"product5" : product5,
				"product6" : product6,
				"product7" : product7,
				"product8" : product8,
				"product9" : product9,
				"product10" : product10,
				"multi_news" : multi_news,
				"user" : request.user,
				"limitedoffer":limitedoffer,
				"saleoffer":saleoffer,
				}
	template = 'newsdetail.html'
	return render(request, template, context)

"""============================="""
"""=====PRODUCT DETAIL PAGE====="""
"""============================="""

def ProductPage(request, p_id):
	"""Product detail page"""
	mac = str(get_client_ip(request))
	limitedoffer = LimitedOffer.objects.all()
	navbar_category = Category.objects.all()
	category = Category.objects.all()
	subcategory = SubCategory.objects.all()
	product = Product.objects.get(pk=p_id)
	image = ProductImage.objects.filter(product_name=product)
	comments = Comment.objects.filter(product=product)
	subcomments = SubComment.objects.filter(comment=comments)
	form = CommentForm()
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = CommentForm(data=request.POST)
			if form.is_valid():
				content=form.cleaned_data.get('content')
				comment = Comment(user=request.user, content=content, product=product)
				comment.save()
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else :
			form = CommentForm()

	similar_products = Product.objects.filter(subcategory=product.subcategory).order_by('?')

	recom_temp1 = Recommendation.objects.filter(mac_address=mac, rectype="P")
	count_temp1 = recom_temp1.count()
	simi =  similar_products.first()

	if count_temp1 < 5:
		recom1_type = Recommendation(product=simi, mac_address=mac, rectype="P")
		recom1_type.save()
	else : 
		recom_x1 = Recommendation.objects.filter(mac_address=mac, rectype="P").first()
		recom_x1.delete()
		recom1_type = Recommendation(product=simi, mac_address=mac, rectype="P")
		recom1_type.save()

	recommended_products = Recommendation.objects.filter(mac_address=mac)

	if product.offer_price != None:
		cheapers = Product.objects.filter(subcategory=product.subcategory, offer_price__lt=product.offer_price)
	else:
		cheapers = Product.objects.filter(subcategory=product.subcategory, sale_price__lt=product.sale_price)

	context = {
				"category":category,
				"subcategory":subcategory, 
				"product":product, 
				"navbar_category":navbar_category,
				"image" : image,
				"limitedoffer":limitedoffer,
				"comments" : comments,
				"subcomments" : subcomments,
				"similars" : similar_products,
				"user" : request.user,
				"cheapers" : cheapers,
				"form" : form,
				"recoms" : recommended_products,
				}
	template = 'productpage.html'
	return render(request, template, context)

"""========================"""
"""=====SERFO PRODUCTS====="""
"""========================"""

@api_view(['GET','POST'])
def getmenproducts(request):
	"""Products to be sent to Serfo"""
	now = datetime.datetime.now().replace(tzinfo=None)
	current = SerfoProduct.objects.filter(super_category='M')

	for i in current:
		n = i.date_modified.replace(tzinfo=None)
		diff = now-n

		if diff > datetime.timedelta(hours=24):
			SerfoProduct.objects.filter(super_category='M').delete()
			list1 = Product.objects.filter(subcategory__subcategory_name="Men").order_by('?')[:3]
			list2 = Product.objects.filter(subcategory__subcategory_name="Men's Watches").order_by('?')[:2]
			list3 = Product.objects.filter(subcategory__subcategory_name="Formals & Lace-ups").order_by('?')[:1]
			list4 = Product.objects.filter(subcategory__subcategory_name="Men's Grooming").order_by('?')[:1]
			result_list = list(chain(list1, list2, list3, list4))

			for x in result_list:
				serfoproducts = SerfoProduct(super_category='M', product=x)
				serfoproducts.save()

	item = []
	men_prod = SerfoProduct.objects.filter(super_category='M')

	"""Men"""
	for i in men_prod:
		response1 = {}
		response1['super_category'] = i.super_category
		response1['id'] = i.product.id
		response1['title'] = i.product.title
		if i.product.offer_price != None:
			response1['price'] = i.product.offer_price
		else:
			response1['price'] = i.product.sale_price
		response1['link'] = i.product.link
		temp_image = i.product.mainimage
		response1['mainimage'] = temp_image
		item.append(response1)

	data=item
	return Response({"data":data, 'status':200})

@api_view(['GET','POST'])
def getwomenproducts(request):
	"""Products to be sent to Serfo"""
	now = datetime.datetime.now().replace(tzinfo=None)
	current = SerfoProduct.objects.filter(super_category='W')

	for i in current:
		n = i.date_modified.replace(tzinfo=None)
		diff = now-n

		if diff > datetime.timedelta(hours=24):
			SerfoProduct.objects.filter(super_category='W').delete()
			list1 = Product.objects.filter(subcategory__subcategory_name="Women").order_by('?')[:3]
			list2 = Product.objects.filter(subcategory__subcategory_name="Women's Watches").order_by('?')[:2]
			list3 = Product.objects.filter(subcategory__subcategory_name="Women's Jewellery").order_by('?')[:1]
			list4 = Product.objects.filter(subcategory__subcategory_name="Ballerinas").order_by('?')[:1]
			result_list = list(chain(list1, list2, list3, list4))

			for x in result_list:
				serfoproducts = SerfoProduct(super_category='W', product=x)
				serfoproducts.save()

	item = []
	women_prod = SerfoProduct.objects.filter(super_category='W')

	"""Women"""
	for j in women_prod:
		response2 = {}
		response2['super_category'] = j.super_category
		response2['id'] = j.product.id
		response2['title'] = j.product.title
		if j.product.offer_price != None:
			response2['price'] = j.product.offer_price
		else:
			response2['price'] = j.product.sale_price
		response2['link'] = j.product.link
		temp_image = j.product.mainimage
		response2['mainimage'] = temp_image
		item.append(response2)

	data=item
	return Response({"data":data, 'status':200})

@api_view(['GET','POST'])
def getappliancesproducts(request):
	"""Products to be sent to Serfo"""
	now = datetime.datetime.now().replace(tzinfo=None)
	current = SerfoProduct.objects.filter(super_category='A')

	for i in current:
		n = i.date_modified.replace(tzinfo=None)
		diff = now-n

		if diff > datetime.timedelta(hours=24):
			SerfoProduct.objects.filter(super_category='A').delete()
			list1 = Product.objects.filter(subcategory__subcategory_name="Kitchen & Home Appliances").order_by('?')[:3]
			list2 = Product.objects.filter(subcategory__subcategory_name="Large Appliances").order_by('?')[:4]
			result_list = list(chain(list1, list2))

			for x in result_list:
				serfoproducts = SerfoProduct(super_category='A', product=x)
				serfoproducts.save()

	item = []
	appliances_prod = SerfoProduct.objects.filter(super_category='A')

	"""Appliances"""
	for x in appliances_prod:
		response3 = {}
		response3['super_category'] = x.super_category
		response3['id'] = x.product.id
		response3['title'] = x.product.title
		if x.product.offer_price != None:
			response3['price'] = x.product.offer_price
		else:
			response3['price'] = x.product.sale_price
		response3['link'] = x.product.link
		response3['mainimage'] = x.product.mainimage
		item.append(response3)

	data=item
	return Response({"data":data, 'status':200})

@api_view(['GET','POST'])
def gethomeproducts(request):
	"""Products to be sent to Serfo"""
	now = datetime.datetime.now().replace(tzinfo=None)
	current = SerfoProduct.objects.filter(super_category='H')

	for i in current:
		n = i.date_modified.replace(tzinfo=None)
		diff = now-n

		if diff > datetime.timedelta(hours=24):
			SerfoProduct.objects.filter(super_category='H').delete()
			list1 = Product.objects.filter(subcategory__subcategory_name="Decor & Lighting").order_by('?')[:3]
			list2 = Product.objects.filter(subcategory__subcategory_name="Kitchen & Dining").order_by('?')[:2]
			list3 = Product.objects.filter(subcategory__subcategory_name="Home Improvement").order_by('?')[:2]
			result_list = list(chain(list1, list2, list3))

			for x in result_list:
				serfoproducts = SerfoProduct(super_category='H', product=x)
				serfoproducts.save()

	item = []
	home_prod = SerfoProduct.objects.filter(super_category='H')

	"""Home"""
	for y in home_prod:
		response4 = {}
		response4['super_category'] = y.super_category
		response4['id'] = y.product.id
		response4['title'] = y.product.title
		if y.product.offer_price != None:
			response4['price'] = y.product.offer_price
		else:
			response4['price'] = y.product.sale_price
		response4['link'] = y.product.link
		response4['mainimage'] = y.product.mainimage
		item.append(response4)

	data=item
	return Response({"data":data, 'status':200})

@api_view(['GET','POST'])
def getelectronicproducts(request):
	"""Products to be sent to Serfo"""
	now = datetime.datetime.now().replace(tzinfo=None)
	current = SerfoProduct.objects.filter(super_category='E')

	for i in current:
		n = i.date_modified.replace(tzinfo=None)
		diff = now-n

		if diff > datetime.timedelta(hours=24):
			SerfoProduct.objects.filter(super_category='E').delete()
			list1 = Product.objects.filter(subcategory__subcategory_name="Android Mobiles").order_by('?')[:3]
			list2 = Product.objects.filter(subcategory__subcategory_name="Tablets").order_by('?')[:2]
			list3 = Product.objects.filter(subcategory__subcategory_name="Laptops").order_by('?')[:1]
			list4 = Product.objects.filter(subcategory__subcategory_name="Digital SLRs").order_by('?')[:1]
			result_list = list(chain(list1, list2, list3, list4))

			for x in result_list:
				serfoproducts = SerfoProduct(super_category='E', product=x)
				serfoproducts.save()
	item = []
	electronics_prod = SerfoProduct.objects.filter(super_category='E')

	"""Electronics"""
	for z in electronics_prod:
		response5 = {}
		response5['super_category'] = z.super_category
		response5['id'] = z.product.id
		response5['title'] = z.product.title
		if z.product.offer_price != None:
			response5['price'] = z.product.offer_price
		else:
			response5['price'] = z.product.sale_price
		response5['link'] = z.product.link
		response5['mainimage'] = z.product.mainimage
		item.append(response5)

	data=item
	return Response({"data":data, 'status':200})

"""============================"""
"""=====EXCEPTION HANDLING====="""
"""============================"""

# HTTP Error 400
def bad_request(request):
	return render_to_response('400.html')

# HTTP Error 403
def permission_denied(request):
	return render_to_response('403.html')

# HTTP Error 404
def page_not_found(request):
	return render_to_response('404.html')

# HTTP Error 500
def server_error(request):
	return render_to_response('500.html')	

"""================================="""
"""=====SOCIAL ACCOUNT REDIRECT====="""
"""================================="""

@api_view(['GET','POST'])
def getproducts(request):
	"""Products to be sent to Serfo"""
	now = datetime.datetime.now().replace(tzinfo=None)
	current1 = SerfoProduct.objects.filter(super_category='M')
	current2 = SerfoProduct.objects.filter(super_category='W')
	current3 = SerfoProduct.objects.filter(super_category='A')
	current4 = SerfoProduct.objects.filter(super_category='H')
	current5 = SerfoProduct.objects.filter(super_category='E')

	for c in current1:
		n = c.date_modified.replace(tzinfo=None)
		diff = now-n

		if diff > datetime.timedelta(hours=24):
			SerfoProduct.objects.filter(super_category='M').delete()
			list1 = Product.objects.filter(subcategory__subcategory_name="Men").exclude(offer_price=None, sale_price=None).order_by('?')[:3]
			list2 = Product.objects.filter(subcategory__subcategory_name="Men's Watches").exclude(offer_price=None, sale_price=None).order_by('?')[:2]
			list3 = Product.objects.filter(subcategory__subcategory_name="Formals & Lace-ups").exclude(offer_price=None, sale_price=None).order_by('?')[:1]
			list4 = Product.objects.filter(subcategory__subcategory_name="Men's Grooming").exclude(offer_price=None, sale_price=None).order_by('?')[:1]
			result_list = list(chain(list1, list2, list3, list4))

			for p in result_list:
				serfoproducts = SerfoProduct(super_category='M', product=p)
				serfoproducts.save()

	for c in current2:
		n = c.date_modified.replace(tzinfo=None)
		diff = now-n

		if diff > datetime.timedelta(hours=24):
			SerfoProduct.objects.filter(super_category='W').delete()
			list1 = Product.objects.filter(subcategory__subcategory_name="Women").exclude(offer_price=None, sale_price=None).order_by('?')[:3]
			list2 = Product.objects.filter(subcategory__subcategory_name="Women's Watches").exclude(offer_price=None, sale_price=None).order_by('?')[:2]
			list3 = Product.objects.filter(subcategory__subcategory_name="Women's Jewellery").exclude(offer_price=None, sale_price=None).order_by('?')[:1]
			list4 = Product.objects.filter(subcategory__subcategory_name="Ballerinas").exclude(offer_price=None, sale_price=None).order_by('?')[:1]
			result_list = list(chain(list1, list2, list3, list4))

			for p in result_list:
				serfoproducts = SerfoProduct(super_category='W', product=p)
				serfoproducts.save()

	for c in current3:
		n = c.date_modified.replace(tzinfo=None)
		diff = now-n

		if diff > datetime.timedelta(hours=24):
			SerfoProduct.objects.filter(super_category='A').delete()
			list1 = Product.objects.filter(subcategory__subcategory_name="Kitchen & Home Appliances").exclude(offer_price=None, sale_price=None).order_by('?')[:3]
			list2 = Product.objects.filter(subcategory__subcategory_name="Large Appliances").exclude(offer_price=None, sale_price=None).order_by('?')[:4]
			result_list = list(chain(list1, list2))

			for p in result_list:
				serfoproducts = SerfoProduct(super_category='A', product=p)
				serfoproducts.save()

	for c in current4:
		n = c.date_modified.replace(tzinfo=None)
		diff = now-n

		if diff > datetime.timedelta(hours=24):
			SerfoProduct.objects.filter(super_category='H').delete()
			list1 = Product.objects.filter(subcategory__subcategory_name="Decor & Lighting").exclude(offer_price=None, sale_price=None).order_by('?')[:3]
			list2 = Product.objects.filter(subcategory__subcategory_name="Kitchen & Dining").exclude(offer_price=None, sale_price=None).order_by('?')[:2]
			list3 = Product.objects.filter(subcategory__subcategory_name="Home Improvement").exclude(offer_price=None, sale_price=None).order_by('?')[:2]
			result_list = list(chain(list1, list2, list3))

			for p in result_list:
				serfoproducts = SerfoProduct(super_category='H', product=p)
				serfoproducts.save()

	for c in current5:
		n = c.date_modified.replace(tzinfo=None)
		diff = now-n

		if diff > datetime.timedelta(hours=24):
			SerfoProduct.objects.filter(super_category='E').delete()
			list1 = Product.objects.filter(subcategory__subcategory_name="Android Mobiles").exclude(offer_price=None, sale_price=None).order_by('?')[:3]
			list2 = Product.objects.filter(subcategory__subcategory_name="Tablets").exclude(offer_price=None, sale_price=None).order_by('?')[:2]
			list3 = Product.objects.filter(subcategory__subcategory_name="Laptops").exclude(offer_price=None, sale_price=None).order_by('?')[:1]
			list4 = Product.objects.filter(subcategory__subcategory_name="Digital SLRs").exclude(offer_price=None, sale_price=None).order_by('?')[:1]
			result_list = list(chain(list1, list2, list3, list4))

			for p in result_list:
				serfoproducts = SerfoProduct(super_category='E', product=p)
				serfoproducts.save()

	item = []
	men_prod = SerfoProduct.objects.filter(super_category='M')
	women_prod = SerfoProduct.objects.filter(super_category='W')
	appliances_prod = SerfoProduct.objects.filter(super_category='A')
	home_prod = SerfoProduct.objects.filter(super_category='H')
	electronics_prod = SerfoProduct.objects.filter(super_category='E')

	"""Men"""
	for i in men_prod:
		response1 = {}
		response1['super_category'] = i.super_category
		response1['id'] = i.product.id
		response1['title'] = i.product.title
		if i.product.offer_price != None:
			response1['price'] = i.product.offer_price
		else:
			response1['price'] = i.product.sale_price
		response1['link'] = i.product.link
		temp_image = i.product.mainimage
		response1['mainimage'] = temp_image
		item.append(response1)

	"""Women"""
	for j in women_prod:
		response2 = {}
		response2['super_category'] = j.super_category
		response2['id'] = j.product.id
		response2['title'] = j.product.title
		if j.product.offer_price != None:
			response2['price'] = j.product.offer_price
		else:
			response2['price'] = j.product.sale_price
		response2['link'] = j.product.link
		temp_image = j.product.mainimage
		response2['mainimage'] = temp_image
		item.append(response2)

	"""Appliances"""
	for x in appliances_prod:
		response3 = {}
		response3['super_category'] = x.super_category
		response3['id'] = x.product.id
		response3['title'] = x.product.title
		if x.product.offer_price != None:
			response3['price'] = x.product.offer_price
		else:
			response3['price'] = x.product.sale_price
		response3['link'] = x.product.link
		response3['mainimage'] = x.product.mainimage
		item.append(response3)

	"""Home"""
	for y in home_prod:
		response4 = {}
		response4['super_category'] = y.super_category
		response4['id'] = y.product.id
		response4['title'] = y.product.title
		if y.product.offer_price != None:
			response4['price'] = y.product.offer_price
		else:
			response4['price'] = y.product.sale_price
		response4['link'] = y.product.link
		response4['mainimage'] = y.product.mainimage
		item.append(response4)

	"""Electronics"""
	for z in electronics_prod:
		response5 = {}
		response5['super_category'] = z.super_category
		response5['id'] = z.product.id
		response5['title'] = z.product.title
		if z.product.offer_price != None:
			response5['price'] = z.product.offer_price
		else:
			response5['price'] = z.product.sale_price
		response5['link'] = z.product.link
		response5['mainimage'] = z.product.mainimage
		item.append(response5)

	data=item
	return Response({"data":data, 'status':200})







	