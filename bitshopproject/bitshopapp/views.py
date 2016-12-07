from django.shortcuts import render, HttpResponse, Http404, render_to_response, get_object_or_404
from django.template.loader import get_template
from django.template import Context, RequestContext, loader
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.forms.models import model_to_dict
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
import ast

# def set_cookie(response, key, value, days_expire = 7):
# 	if days_expire is None:
# 		max_age = 365 * 24 * 60 * 60  #one year
# 	else:
# 		max_age = days_expire * 24 * 60 * 60 
# 	expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
# 	response.set_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)


def serfoproductcoverter(prod_query):
	xlist = []
	for i in prod_query:
		prod_dict = {}
		prod_dict['id'] = i.product.id
		prod_dict['title'] = i.product.title
		prod_dict['offer_price'] = str(i.product.offer_price)
		prod_dict['sale_price'] = str(i.product.sale_price)
		prod_dict['mainimage'] = str(i.product.mainimage)
		xlist.append(prod_dict)
	return xlist

def productcoverter(prod_query):
	xlist = []
	for i in prod_query:
		prod_dict = {}
		prod_dict['id'] = i.id
		prod_dict['title'] = i.title
		prod_dict['offer_price'] = str(i.offer_price)
		prod_dict['sale_price'] = str(i.sale_price)
		prod_dict['mainimage'] = str(i.mainimage)
		xlist.append(prod_dict)
	return xlist

def limitedconverter(prod_query):
	limlist = []
	for lim in prod_query:
		limdict = {}
		limdict['image'] = lim.image
		limdict['link'] = lim.link
		limlist.append(limdict)
	return limlist

def newsconverter(prod_query):
	newslist = []
	for new in prod_query:
		newsdict = {}
		newsdict['id'] = new.id
		newsdict['title'] = new.title
		newsdict['image_url'] = new.image_url
		newslist.append(newsdict)
	return newslist

def categoryconverter(prod_query):
	catlist = []
	for cat in prod_query:
		catdict = {}
		catdict['id'] = cat.id
		catdict['category_name'] = cat.category_name
		catdict['category_slug'] = str(cat.category_slug)
		catlist.append(catdict)
	return catlist

def priceconverter(prod_query):
	pricelist = []
	for price in prod_query:
		pricedict = {}
		pricedict['id'] = price.id
		pricedict['title'] = price.title
		pricedict['upper_limit'] = str(price.upper_limit)
		pricedict['lower_limit'] = str(price.lower_limit)
		pricelist.append(pricedict)
	return pricelist

"""=============================="""
"""=========SEARCH SERFO========="""
"""=============================="""

def Search(request):
	"""Search."""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass

	limitedoffer = LimitedOffer.objects.all()
	limlist = []
	for lim in limitedoffer:
		limdict = {}
		limdict['image'] = lim.image
		limdict['link'] = lim.link
		limlist.append(limdict)
	limitedoffer = limlist

	navbar_category = Category.objects.all()
	catlist = []
	for cat in navbar_category:
		catdict = {}
		catdict['id'] = cat.id
		catdict['category_name'] = cat.category_name
		catdict['category_slug'] = str(cat.category_slug)
		catlist.append(catdict)
	navbar_category = catlist

	try:
		q = request.GET.get('q')
	except:
		q = None

	if q:
		products_list = Product.objects.filter(title__icontains=q).order_by('?')
		productcount = str(len(products_list))
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
		
		if prodnum == 1:
			x = products.number - 1
			y = products.number + 7
		elif prodnum == 2:
			x = products.number - 2
			y = products.number + 6
		elif prodnum == 3:
			x = products.number - 3
			y = products.number + 5
		else:
			x = products.number - 4
			y = products.number + 4

		ibool = False
		jbool = False
		if products.has_previous():
			ibool = True
		else:
			ibool = False

		if products.has_next():
			jbool = True
		else:
			jbool = False

		prev_bool = ibool
		next_bool = jbool

		sl = "%d:%d" % (x,y)
		prod_list = productcoverter(products)
		products = prod_list

		Xbool = False
		if len(products_list) > 25:
			Xbool = True
		else:
			Xbool = False

		Ybool = str(Xbool)

		context = {
					"query": q, 
					"count": productcount,
					"products": products,
					"nbool" : prev_bool,
					"mbool" : next_bool,
					"limitedoffer":limitedoffer,
					"navbar_category" : navbar_category,
					"sl":sl,
					"Ybool":Ybool,
					"prodnum":prodnum,
					'range': range(1,total_pages),
					}
		template = 'results.html'
	else:
		template = 'home.html'
		context = {"navbar_category" : navbar_category,}
	return HttpResponse(json.dumps(context), content_type = 'application/json')

"""====================================="""
"""===========HOME PAGE SERFO==========="""
"""====================================="""

def HomePage(request):
	"""Home Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass

	navbar_category = Category.objects.all()
	catlist = categoryconverter(navbar_category)
	navbar_category = catlist

	saleoffer = SaleOffer.objects.all()
	salelist = []
	for sale in saleoffer:
		saledict = {}
		saledict['image'] = sale.image
		saledict['link'] = sale.link
		salelist.append(saledict)
	saleoffer = salelist

	limitedoffer = LimitedOffer.objects.all()
	limlist = limitedconverter(limitedoffer)
	limitedoffer = limlist

	news = New.objects.all().order_by('-id')
	newslist = newsconverter(news)
	news = newslist

	men_prod = SerfoProduct.objects.filter(super_category='M')
	women_prod = SerfoProduct.objects.filter(super_category='W')
	appliances_prod = SerfoProduct.objects.filter(super_category='A')
	home_prod = SerfoProduct.objects.filter(super_category='H')
	electronics_prod = SerfoProduct.objects.filter(super_category='E')

	men_prod_list = serfoproductcoverter(men_prod)
	women_prod_list = serfoproductcoverter(women_prod)
	appliances_prod_list = serfoproductcoverter(appliances_prod)
	home_prod_list = serfoproductcoverter(home_prod)
	electronics_prod_list = serfoproductcoverter(electronics_prod)

	men_prod = men_prod_list
	women_prod = women_prod_list
	appliances_prod = appliances_prod_list
	home_prod = home_prod_list
	electronics_prod = electronics_prod_list


	context = { 
				"data1" : men_prod,
				"data2" : women_prod,
				"data3" : appliances_prod,
				"data4" : home_prod,
				"data5" : electronics_prod, 
				"navbar_category" : navbar_category,
				"news" : news,
				"saleoffer" : saleoffer,
				"limitedoffer" : limitedoffer,
				}
	template = 'home.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

"""============================="""
"""=====CATEGORY SERFO PAGE====="""
"""============================="""

def CategoryPage(request, slug):
	"""Category Detail Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	prices = Price.objects.all().order_by('-id')
	navbar_category = Category.objects.all()
	category = Category.objects.get(category_slug=slug)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
	products_list = Product.objects.filter(category=category).order_by('?')
	news = New.objects.filter(category=category).order_by('-id')

	items = []
	for i in products_list:
		brands_dict = {}
		brands_dict['id'] = i.brand.id
		brands_dict['brand_name'] = i.brand.brand_name
		items.append(brands_dict)
	brands = [ast.literal_eval(el1) for el1 in set([str(el2) for el2 in items])]
	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)

	paginator = Paginator(products_list, 25)
	productcount = str(len(products_list))
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	
	if prodnum == 1:
		x = products.number - 1
		y = products.number + 7
	elif prodnum == 2:
		x = products.number - 2
		y = products.number + 6
	elif prodnum == 3:
		x = products.number - 3
		y = products.number + 5
	else:
		x = products.number - 4
		y = products.number + 4

	sl = "%d:%d" % (x,y)

	ibool = False
	jbool = False
	if products.has_previous():
		ibool = True
	else:
		ibool = False

	if products.has_next():
		jbool = True
	else:
		jbool = False

	prev_bool = ibool
	next_bool = jbool

	limlist = limitedconverter(limitedoffer)
	pricelist = priceconverter(prices)
	catlist = categoryconverter(navbar_category)
	newslist = newsconverter(news)
	prod_list = productcoverter(products)
	news = newslist
	limitedoffer = limlist
	prices = pricelist
	navbar_category = catlist
	products = prod_list

	catdict2 = {}
	catdict2['category_slug'] = str(category.category_slug)
	catdict2['category_name'] = category.category_name
	category = catdict2
	
	subcatlist = []
	for sub in subcategory:
		subcatdict = {}
		subcatdict['subcategory_name'] = sub.subcategory_name
		subcatdict['subcategory_slug'] = sub.subcategory_slug
		subcatdict['category'] = sub.category.category_name
		subcatlist.append(subcatdict)
	subcategory = subcatlist

	Xbool = False
	if len(products_list) > 25:
		Xbool = True
	else:
		Xbool = False

	Ybool = str(Xbool)

	context = {"nbool" : prev_bool, "mbool" : next_bool, "Ybool":Ybool, "l1":l1,"l2":l2,"l3":l3,"l4":l4, "prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "category":category, "subcategory":subcategory, "products":products, "navbar_category":navbar_category, "brands":brands,  "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages)}
	template = 'categorydetail.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

"""==================================="""
"""=====CATEGORY PRICE PAGE SERFO====="""
"""==================================="""

def PriceFilterCategory(request, slug, pr_id):
	"""Price Filter Category Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	selected_price = Price.objects.get(pk=pr_id)
	title = selected_price.title
	upper = selected_price.upper_limit
	lower = selected_price.lower_limit
	prices = Price.objects.all().order_by('-id')
	navbar_category = Category.objects.all()
	category = Category.objects.get(category_slug=slug)
	news = New.objects.filter(category=category).order_by('-id')
	subcategory = SubCategory.objects.filter(category=category).order_by('id')

	subcatlist = []
	for sub in subcategory:
		subcatdict = {}
		subcatdict['subcategory_name'] = sub.subcategory_name
		subcatdict['subcategory_slug'] = sub.subcategory_slug
		subcatdict['category'] = sub.category.category_name
		subcatlist.append(subcatdict)
	subcategory = subcatlist

	products_list = Product.objects.filter(Q(category=category, offer_price__lte=upper, offer_price__gte=lower) | Q(category=category, sale_price__lte=upper, sale_price__gte=lower))

	items = []
	for i in products_list:
		brands_dict = {}
		brands_dict['id'] = i.brand.id
		brands_dict['brand_name'] = i.brand.brand_name
		items.append(brands_dict)
	brands = [ast.literal_eval(el1) for el1 in set([str(el2) for el2 in items])]
	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)

	paginator = Paginator(products_list, 25)
	productcount = str(len(products_list))
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	
	if prodnum == 1:
		x = products.number - 1
		y = products.number + 7
	elif prodnum == 2:
		x = products.number - 2
		y = products.number + 6
	elif prodnum == 3:
		x = products.number - 3
		y = products.number + 5
	else:
		x = products.number - 4
		y = products.number + 4

	sl = "%d:%d" % (x,y)

	ibool = False
	jbool = False
	if products.has_previous():
		ibool = True
	else:
		ibool = False

	if products.has_next():
		jbool = True
	else:
		jbool = False

	prev_bool = ibool
	next_bool = jbool

	catdict2 = {}
	catdict2['category_slug'] = str(category.category_slug)
	catdict2['category_name'] = category.category_name
	category = catdict2

	selected_price_dict = {}
	selected_price_dict['id'] = selected_price.id
	selected_price_dict['title'] = selected_price.title
	selected_price_dict['upper_limit'] = str(selected_price.upper_limit)
	selected_price_dict['lower_limit'] = str(selected_price.lower_limit)
	selected_price = selected_price_dict
	
	limlist = limitedconverter(limitedoffer)
	pricelist = priceconverter(prices)
	catlist = categoryconverter(navbar_category)
	newslist = newsconverter(news)
	prod_list = productcoverter(products)
	news = newslist
	limitedoffer = limlist
	prices = pricelist
	navbar_category = catlist
	products = prod_list

	Xbool = False
	if len(products_list) > 25:
		Xbool = True
	else:
		Xbool = False

	Ybool = str(Xbool)

	context = {"nbool" : prev_bool, "mbool" : next_bool, "Ybool":Ybool,"l1":l1,"l2":l2,"l3":l3,"l4":l4,"prodnum":prodnum, "selected_price":selected_price, "limitedoffer":limitedoffer, "count":productcount, "category":category, "subcategory":subcategory, "products":products, "navbar_category":navbar_category, "brands":brands,  "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages)}
	template = 'pricecatdetail.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

"""============================="""
"""======BRANDS SERFO PAGE======"""
"""============================="""

def BrandsPage(request, b_id):
	"""Brands Detail Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	prices = Price.objects.all().order_by('-id')
	navbar_category = Category.objects.all()
	brands = Brand.objects.all().order_by('?')
	prime_brand = Brand.objects.get(pk=b_id)
	news = New.objects.all().order_by('-id')
	products_list = Product.objects.filter(brand=prime_brand).order_by('id')

	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)

	paginator = Paginator(products_list, 25)
	productcount = str(len(products_list))
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	if prodnum == 1:
		x = products.number - 1
		y = products.number + 7
	elif prodnum == 2:
		x = products.number - 2
		y = products.number + 6
	elif prodnum == 3:
		x = products.number - 3
		y = products.number + 5
	else:
		x = products.number - 4
		y = products.number + 4
	sl = "%d:%d" % (x,y)

	ibool = False
	jbool = False
	if products.has_previous():
		ibool = True
	else:
		ibool = False

	if products.has_next():
		jbool = True
	else:
		jbool = False

	prev_bool = ibool
	next_bool = jbool

	prod_list = productcoverter(products)
	limlist = limitedconverter(limitedoffer)
	pricelist = priceconverter(prices)
	catlist = categoryconverter(navbar_category)
	newslist = newsconverter(news)

	news = newslist
	limitedoffer = limlist
	prices = pricelist
	navbar_category = catlist
	products = prod_list

	brandslist = []
	for i in brands:
		brands_dict = {}
		brands_dict['id'] = i.id
		brands_dict['brand_name'] = i.brand_name
		brandslist.append(brands_dict)
	brands = brandslist

	prime_brand_dict = {}
	prime_brand_dict['id'] = prime_brand.id
	prime_brand_dict['brand_name'] = prime_brand.brand_name
	prime_brand = prime_brand_dict

	Xbool = False
	if len(products_list) > 25:
		Xbool = True
	else:
		Xbool = False

	Ybool = str(Xbool)

	context = {"nbool" : prev_bool, "mbool" : next_bool, "Ybool":Ybool, "l1":l1,"l2":l2,"l3":l3,"l4":l4,"prodnum":prodnum, "limitedoffer":limitedoffer, "count":productcount, "products":products, "navbar_category":navbar_category,"brands":brands, "prime_brand":prime_brand, "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages)}
	template = 'brandetail.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

"""=============================="""
"""======BRANDS PRICE SERFO======"""
"""=============================="""

def PriceFilterBrands(request, b_id, pr_id):
	"""Brands Price Filter Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	selected_price = Price.objects.get(pk=pr_id)
	title = selected_price.title
	upper = selected_price.upper_limit
	lower = selected_price.lower_limit
	prices = Price.objects.all().order_by('-id')
	navbar_category = Category.objects.all()
	brands = Brand.objects.all().order_by('?')
	news = New.objects.all().order_by('-id')

	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)
	prime_brand = Brand.objects.get(pk=b_id)
	products_list = Product.objects.filter(Q(brand=prime_brand, offer_price__lte=upper, offer_price__gte=lower) | Q(brand=prime_brand, sale_price__lte=upper, sale_price__gte=lower))
	paginator = Paginator(products_list, 25)
	productcount = str(len(products_list))
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	if prodnum == 1:
		x = products.number - 1
		y = products.number + 7
	elif prodnum == 2:
		x = products.number - 2
		y = products.number + 6
	elif prodnum == 3:
		x = products.number - 3
		y = products.number + 5
	else:
		x = products.number - 4
		y = products.number + 4
	sl = "%d:%d" % (x,y)

	ibool = False
	jbool = False
	if products.has_previous():
		ibool = True
	else:
		ibool = False

	if products.has_next():
		jbool = True
	else:
		jbool = False

	prev_bool = ibool
	next_bool = jbool

	limlist = limitedconverter(limitedoffer)
	pricelist = priceconverter(prices)
	catlist = categoryconverter(navbar_category)
	newslist = newsconverter(news)
	prod_list = productcoverter(products)
	news = newslist
	limitedoffer = limlist
	prices = pricelist
	navbar_category = catlist
	products = prod_list

	selected_price_dict = {}
	selected_price_dict['id'] = selected_price.id
	selected_price_dict['title'] = selected_price.title
	selected_price_dict['upper_limit'] = str(selected_price.upper_limit)
	selected_price_dict['lower_limit'] = str(selected_price.lower_limit)
	selected_price = selected_price_dict

	brandslist = []
	for i in brands:
		brands_dict = {}
		brands_dict['id'] = i.id
		brands_dict['brand_name'] = i.brand_name
		brandslist.append(brands_dict)
	brands = brandslist

	prime_brand_dict = {}
	prime_brand_dict['id'] = prime_brand.id
	prime_brand_dict['brand_name'] = prime_brand.brand_name
	prime_brand = prime_brand_dict

	Xbool = False
	if len(products_list) > 25:
		Xbool = True
	else:
		Xbool = False

	Ybool = str(Xbool)

	context = {"nbool" : prev_bool, "mbool" : next_bool, "Ybool":Ybool,"l1":l1,"l2":l2,"l3":l3,"l4":l4,"prodnum":prodnum, "selected_price":selected_price, "limitedoffer":limitedoffer, "count":productcount, "products":products, "navbar_category":navbar_category, "brands":brands, "prime_brand":prime_brand, "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages),}
	template = 'pricebranddetail.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

"""====================================="""
"""=====SUBCATEGORY INDIVIDUAL PAGE====="""
"""====================================="""

def SubCategoryPage(request, slug1, slug2):
	"""SubCategory Detail Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	prices = Price.objects.all().order_by('-id')
	navbar_category = Category.objects.all()
	category = Category.objects.get(category_slug=slug1)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
	subcat = SubCategory.objects.get(subcategory_slug=slug2, category=category)
	products_list = Product.objects.filter(subcategory=subcat).order_by('id')
	news = New.objects.filter(category=category).order_by('-id')

	items = []
	for i in products_list:
		brands_dict = {}
		brands_dict['id'] = i.brand.id
		brands_dict['brand_name'] = i.brand.brand_name
		items.append(brands_dict)
	brands = [ast.literal_eval(el1) for el1 in set([str(el2) for el2 in items])]

	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)

	paginator = Paginator(products_list, 25)
	productcount = str(len(products_list))
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	if prodnum == 1:
		x = products.number - 1
		y = products.number + 7
	elif prodnum == 2:
		x = products.number - 2
		y = products.number + 6
	elif prodnum == 3:
		x = products.number - 3
		y = products.number + 5
	else:
		x = products.number - 4
		y = products.number + 4
	sl = "%d:%d" % (x,y)

	ibool = False
	jbool = False
	if products.has_previous():
		ibool = True
	else:
		ibool = False

	if products.has_next():
		jbool = True
	else:
		jbool = False

	prev_bool = ibool
	next_bool = jbool

	limlist = limitedconverter(limitedoffer)
	pricelist = priceconverter(prices)
	catlist = categoryconverter(navbar_category)
	newslist = newsconverter(news)
	prod_list = productcoverter(products)
	news = newslist
	limitedoffer = limlist
	prices = pricelist
	navbar_category = catlist
	products = prod_list

	catdict = {}
	catdict['category_name'] = category.category_name
	catdict['category_slug'] = category.category_slug
	category = catdict

	subcatlist = []
	for sub in subcategory:
		subcatdictx = {}
		subcatdictx['subcategory_name'] = sub.subcategory_name
		subcatdictx['subcategory_slug'] = sub.subcategory_slug
		subcatdictx['category'] = sub.category.category_name
		subcatlist.append(subcatdictx)
	subcategory = subcatlist

	subcatdict = {}
	subcatdict['subcategory_name'] = subcat.subcategory_name
	subcatdict['subcategory_slug'] = subcat.subcategory_slug
	subcatdict['category'] = subcat.category.category_name
	subcat = subcatdict

	Xbool = False
	if len(products_list) > 25:
		Xbool = True
	else:
		Xbool = False

	Ybool = str(Xbool)
	
	context = {"nbool" : prev_bool, "mbool" : next_bool, "Ybool":Ybool,"l1":l1,"l2":l2,"l3":l3,"l4":l4,"prodnum":prodnum, "category":category, "limitedoffer":limitedoffer, "count":productcount, "subcategory":subcategory, "products":products, "navbar_category":navbar_category,"subcat":subcat, "brands":brands,  "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages)}
	template = 'subcategorydetail.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

"""======================================"""
"""=====SUBCATEGORY PRICE SERFO PAGE====="""
"""======================================"""

def PriceFilterSubCategory(request, slug1, slug2, pr_id):
	"""SubCategory Filter Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	prices = Price.objects.all().order_by('-id')
	selected_price = Price.objects.get(pk=pr_id)
	title = selected_price.title
	upper = selected_price.upper_limit
	lower = selected_price.lower_limit
	navbar_category = Category.objects.all()
	category = Category.objects.get(category_slug=slug1)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
	subcat = SubCategory.objects.get(subcategory_slug=slug2, category=category)
	products_list = Product.objects.filter(Q(subcategory=subcat, offer_price__lte=upper, offer_price__gte=lower) | Q(subcategory=subcat, sale_price__lte=upper, sale_price__gte=lower))
	news = New.objects.filter(category=category).order_by('-id')
	items = []
	for i in products_list:
		brands_dict = {}
		brands_dict['id'] = i.brand.id
		brands_dict['brand_name'] = i.brand.brand_name
		items.append(brands_dict)
	brands = [ast.literal_eval(el1) for el1 in set([str(el2) for el2 in items])]

	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)

	paginator = Paginator(products_list, 25)
	productcount = str(len(products_list))
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	if prodnum == 1:
		x = products.number - 1
		y = products.number + 7
	elif prodnum == 2:
		x = products.number - 2
		y = products.number + 6
	elif prodnum == 3:
		x = products.number - 3
		y = products.number + 5
	else:
		x = products.number - 4
		y = products.number + 4
	sl = "%d:%d" % (x,y)

	ibool = False
	jbool = False
	if products.has_previous():
		ibool = True
	else:
		ibool = False

	if products.has_next():
		jbool = True
	else:
		jbool = False

	prev_bool = ibool
	next_bool = jbool

	limlist = limitedconverter(limitedoffer)
	pricelist = priceconverter(prices)
	catlist = categoryconverter(navbar_category)
	newslist = newsconverter(news)
	prod_list = productcoverter(products)
	news = newslist
	limitedoffer = limlist
	prices = pricelist
	navbar_category = catlist
	products = prod_list

	catdict = {}
	catdict['category_name'] = category.category_name
	catdict['category_slug'] = category.category_slug
	category = catdict

	subcatlist = []
	for sub in subcategory:
		subcatdictx = {}
		subcatdictx['subcategory_name'] = sub.subcategory_name
		subcatdictx['subcategory_slug'] = sub.subcategory_slug
		subcatdictx['category'] = sub.category.category_name
		subcatlist.append(subcatdictx)
	subcategory = subcatlist

	subcatdict = {}
	subcatdict['subcategory_name'] = subcat.subcategory_name
	subcatdict['subcategory_slug'] = subcat.subcategory_slug
	subcatdict['category'] = subcat.category.category_name
	subcat = subcatdict

	selected_price_dict = {}
	selected_price_dict['id'] = selected_price.id
	selected_price_dict['title'] = selected_price.title
	selected_price_dict['upper_limit'] = str(selected_price.upper_limit)
	selected_price_dict['lower_limit'] = str(selected_price.lower_limit)
	selected_price = selected_price_dict

	Xbool = False
	if len(products_list) > 25:
		Xbool = True
	else:
		Xbool = False

	Ybool = str(Xbool)
	
	context = {"nbool" : prev_bool, "mbool" : next_bool, "Ybool":Ybool,"l1":l1,"l2":l2,"l3":l3,"l4":l4,"prodnum":prodnum, "selected_price":selected_price, "limitedoffer":limitedoffer, "category":category, "subcategory":subcategory, "products":products, "navbar_category":navbar_category,"subcat":subcat, "count":productcount, "brands":brands,  "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages)}
	template = 'pricesubcatdetail.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

"""=============================="""
"""=====NEWS INDIVIDUAL PAGE====="""
"""=============================="""

def NewsPage(request, n_id):
	"""Product News Detail Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	navbar_category = Category.objects.all()
	news = New.objects.get(pk=n_id)
	multi_news = New.objects.all().order_by('?')
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
		id1 = int(link1.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://serfo.com/shop/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product1 = Product.objects.get(pk=id1)
		dict1 = {}
		dict1['id'] = str(product1.id)
		dict1['title'] = product1.title
		dict1['mainimage'] = product1.mainimage
		dict1['brand'] = product1.brand.brand_name
		dict1['offer_price'] = str(product1.offer_price)
		dict1['sale_price'] = str(product1.sale_price)
		dict1['link'] = str(product1.link)
		dict1['id'] = str(product1.id)
		dict1['seller'] = product1.seller
		product1 = dict1

	if news.product_link2:
		link2 = news.product_link2
		id2 = int(link2.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://serfo.com/shop/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product2 = Product.objects.get(pk=id2)
		dict2 = {}
		dict2['id'] = str(product2.id)
		dict2['title'] = product2.title
		dict2['mainimage'] = product2.mainimage
		dict2['brand'] = product2.brand.brand_name
		dict2['offer_price'] = str(product2.offer_price)
		dict2['sale_price'] = str(product2.sale_price)
		dict2['link'] = str(product2.link)
		dict2['id'] = str(product2.id)
		dict2['seller'] = product2.seller
		product2 = dict2

	if news.product_link3:
		link3 = news.product_link3
		id3 = int(link3.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://serfo.com/shop/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product3 = Product.objects.get(pk=id3)
		dict3 = {}
		dict3['id'] = str(product3.id)
		dict3['title'] = product3.title
		dict3['mainimage'] = product3.mainimage
		dict3['brand'] = product3.brand.brand_name
		dict3['offer_price'] = str(product3.offer_price)
		dict3['sale_price'] = str(product3.sale_price)
		dict3['link'] = str(product3.link)
		dict3['id'] = str(product3.id)
		dict3['seller'] = product3.seller
		product3 = dict3

	if news.product_link4:
		link4 = news.product_link4
		id4 = int(link4.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://serfo.com/shop/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product4 = Product.objects.get(pk=id4)
		dict4 = {}
		dict4['id'] = str(product4.id)
		dict4['title'] = product4.title
		dict4['mainimage'] = product4.mainimage
		dict4['brand'] = product4.brand.brand_name
		dict4['offer_price'] = str(product4.offer_price)
		dict4['sale_price'] = str(product4.sale_price)
		dict4['link'] = str(product4.link)
		dict4['id'] = str(product4.id)
		dict4['seller'] = product4.seller
		product4 = dict4

	if news.product_link5:
		link5 = news.product_link5
		id5 = int(link5.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://serfo.com/shop/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product5 = Product.objects.get(pk=id5)
		dict5 = {}
		dict5['title'] = product5.title
		dict5['id'] = str(product5.id)
		dict5['mainimage'] = product5.mainimage
		dict5['brand'] = product5.brand.brand_name
		dict5['offer_price'] = str(product5.offer_price)
		dict5['sale_price'] = str(product5.sale_price)
		dict5['link'] = str(product5.link)
		dict5['id'] = str(product5.id)
		dict5['seller'] = product5.seller
		product5 = dict5

	if news.product_link6:
		link6 = news.product_link6
		id6 = int(link6.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://serfo.com/shop/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product6 = Product.objects.get(pk=id6)
		dict6 = {}
		dict6['title'] = product6.title
		dict6['id'] = str(product6.id)
		dict6['mainimage'] = product6.mainimage
		dict6['brand'] = product6.brand.brand_name
		dict6['offer_price'] = str(product6.offer_price)
		dict6['sale_price'] = str(product6.sale_price)
		dict6['link'] = str(product6.link)
		dict6['id'] = str(product6.id)
		dict6['seller'] = product6.seller
		product6 = dict6

	if news.product_link7:
		link7 = news.product_link7
		id7 = int(link7.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://serfo.com/shop/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product7 = Product.objects.get(pk=id7)
		dict7 = {}
		dict7['title'] = product7.title
		dict7['id'] = str(product7.id)
		dict7['mainimage'] = product7.mainimage
		dict7['brand'] = product7.brand.brand_name
		dict7['offer_price'] = str(product7.offer_price)
		dict7['sale_price'] = str(product7.sale_price)
		dict7['link'] = str(product7.link)
		dict7['id'] = str(product7.id)
		dict7['seller'] = product7.seller
		product7 = dict7

	if news.product_link8:
		link8 = news.product_link8
		id8 = int(link8.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://serfo.com/shop/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product8 = Product.objects.get(pk=id8)
		dict8 = {}
		dict8['title'] = product8.title
		dict8['id'] = str(product8.id)
		dict8['mainimage'] = product8.mainimage
		dict8['brand'] = product8.brand.brand_name
		dict8['offer_price'] = str(product8.offer_price)
		dict8['sale_price'] = str(product8.sale_price)
		dict8['link'] = str(product8.link)
		dict8['id'] = str(product8.id)
		dict8['seller'] = product8.seller
		product8 = dict8

	if news.product_link9:
		link9 = news.product_link9
		id9 = int(link9.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://serfo.com/shop/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product9 = Product.objects.get(pk=id9)
		dict9 = {}
		dict9['title'] = product9.title
		dict9['id'] = str(product9.id)
		dict9['mainimage'] = product9.mainimage
		dict9['brand'] = product9.brand.brand_name
		dict9['offer_price'] = str(product9.offer_price)
		dict9['sale_price'] = str(product9.sale_price)
		dict9['link'] = str(product9.link)
		dict9['id'] = str(product9.id)
		dict9['seller'] = product9.seller
		product9 = dict9

	if news.product_link10:
		link10 = news.product_link10
		id10 = int(link10.replace("http://54.191.242.230:8000/productdetails/","").replace("http://shop.serfo.com/productdetails/","").replace("http://serfo.com/shop/productdetails/","").replace("http://127.0.0.1:8000/productdetails/","").replace("/",""))
		product10 = Product.objects.get(pk=id10)
		dict10 = {}
		dict10['title'] = product10.title
		dict10['id'] = str(product10.id)
		dict10['mainimage'] = product10.mainimage
		dict10['brand'] = product10.brand.brand_name
		dict10['offer_price'] = str(product10.offer_price)
		dict10['sale_price'] = str(product10.sale_price)
		dict10['link'] = str(product10.link)
		dict10['id'] = str(product10.id)
		dict10['seller'] = product10.seller
		product10 = dict10

	limlist = limitedconverter(limitedoffer)
	catlist = categoryconverter(navbar_category)
	newslist = newsconverter(multi_news)
	multi_news = newslist
	limitedoffer = limlist
	navbar_category = catlist

	newdict = {}
	newdict['id'] = news.id
	newdict['title'] = news.title
	newdict['main_content'] = news.main_content
	newdict['timestamp'] = str(news.timestamp)
	newdict['image_url'] = news.image_url
	newdict['category'] = news.category.category_name
	newdict['subcategory'] = news.subcategory.subcategory_name
	news = newdict
	
	context = {
				"news":news, 
				"navbar_category":navbar_category,
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
				"limitedoffer":limitedoffer,
				}
	template = 'newsdetail.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

"""==================================="""
"""=====AMALGAMATED CATEGORY PAGE====="""
"""==================================="""

def Men(request):
	"""Men's Detail Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	navbar_category = Category.objects.all()
	list1 = Product.objects.filter(subcategory__subcategory_name="Men").order_by('?')
	list2 = Product.objects.filter(subcategory__subcategory_name="Men's Watches").order_by('?')
	list3 = Product.objects.filter(subcategory__subcategory_name="Formals & Lace-ups").order_by('?')
	list4 = Product.objects.filter(subcategory__subcategory_name="Men's Grooming").order_by('?')
	count1 = list1.count()
	count2 = list2.count()
	count3 = list3.count()
	count4 = list4.count()

	sub1 = SubCategory.objects.get(subcategory_name="Men")
	sub2 = SubCategory.objects.get(subcategory_name="Men's Watches")
	sub3 = SubCategory.objects.get(subcategory_name="Formals & Lace-ups")
	sub4 = SubCategory.objects.get(subcategory_name="Men's Grooming")
	products_list = list(chain(list1, list2, list3, list4))

	items = []
	for i in products_list:
		brands_dict = {}
		brands_dict['id'] = i.brand.id
		brands_dict['brand_name'] = i.brand.brand_name
		if brands_dict['brand_name'] not in items:
			items.append(brands_dict)
	brands = [ast.literal_eval(el1) for el1 in set([str(el2) for el2 in items])]

	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)

	paginator = Paginator(products_list, 25)
	productcount = str(count1 + count2 + count3 + count4) 
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	if prodnum == 1:
		x = products.number - 1
		y = products.number + 7
	elif prodnum == 2:
		x = products.number - 2
		y = products.number + 6
	elif prodnum == 3:
		x = products.number - 3
		y = products.number + 5
	else:
		x = products.number - 4
		y = products.number + 4
	sl = "%d:%d" % (x,y)

	ibool = False
	jbool = False
	if products.has_previous():
		ibool = True
	else:
		ibool = False

	if products.has_next():
		jbool = True
	else:
		jbool = False

	prev_bool = ibool
	next_bool = jbool

	limlist = limitedconverter(limitedoffer)
	catlist = categoryconverter(navbar_category)
	prod_list = productcoverter(products)
	limitedoffer = limlist
	navbar_category = catlist
	products = prod_list

	subcatdict1 = {}
	subcatdict1['subcategory_name'] = sub1.subcategory_name
	subcatdict1['subcategory_slug'] = sub1.subcategory_slug
	subcatdict1['category'] = sub1.category.category_name
	subcatdict1['category_slug'] = str(sub1.category.category_slug)
	sub1 = subcatdict1

	subcatdict2 = {}
	subcatdict2['subcategory_name'] = sub2.subcategory_name
	subcatdict2['subcategory_slug'] = sub2.subcategory_slug
	subcatdict2['category'] = sub2.category.category_name
	subcatdict2['category_slug'] = str(sub2.category.category_slug)
	sub2 = subcatdict2

	subcatdict3 = {}
	subcatdict3['subcategory_name'] = sub3.subcategory_name
	subcatdict3['subcategory_slug'] = sub3.subcategory_slug
	subcatdict3['category'] = sub3.category.category_name
	subcatdict3['category_slug'] = str(sub3.category.category_slug)
	sub3 = subcatdict3

	subcatdict4 = {}
	subcatdict4['subcategory_name'] = sub4.subcategory_name
	subcatdict4['subcategory_slug'] = sub4.subcategory_slug
	subcatdict4['category'] = sub4.category.category_name
	subcatdict4['category_slug'] = str(sub4.category.category_slug)
	sub4 = subcatdict4

	Xbool = False
	if len(products_list) > 25:
		Xbool = True
	else:
		Xbool = False

	Ybool = str(Xbool)

	context = {"nbool" : prev_bool, "mbool" : next_bool, "Ybool":Ybool,"l1":l1,"l2":l2,"l3":l3,"l4":l4,"brands":brands, "prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "products":products, "navbar_category":navbar_category, "sl":sl, 'range': range(1,total_pages), "sub1":sub1,"sub2":sub2,"sub3":sub3,"sub4":sub4}
	template = 'men.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

def Women(request):
	"""Women's Detail Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	navbar_category = Category.objects.all()
	list1 = Product.objects.filter(subcategory__subcategory_name="Women").order_by('?')
	list2 = Product.objects.filter(subcategory__subcategory_name="Women's Watches").order_by('?')
	list3 = Product.objects.filter(subcategory__subcategory_name="Women's Jewellery").order_by('?')
	list4 = Product.objects.filter(subcategory__subcategory_name="Ballerinas").order_by('?')
	count1 = list1.count()
	count2 = list2.count()
	count3 = list3.count()
	count4 = list4.count()

	sub1 = SubCategory.objects.get(subcategory_name="Women")
	sub2 = SubCategory.objects.get(subcategory_name="Women's Watches")
	sub3 = SubCategory.objects.get(subcategory_name="Women's Jewellery")
	sub4 = SubCategory.objects.get(subcategory_name="Ballerinas")

	products_list = list(chain(list1, list2, list3, list4))

	items = []
	for i in products_list:
		brands_dict = {}
		brands_dict['id'] = i.brand.id
		brands_dict['brand_name'] = i.brand.brand_name
		items.append(brands_dict)
	brands = [ast.literal_eval(el1) for el1 in set([str(el2) for el2 in items])]

	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)

	paginator = Paginator(products_list, 25)
	productcount = str(count1 + count2 + count3 + count4) 
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	if prodnum == 1:
		x = products.number - 1
		y = products.number + 7
	elif prodnum == 2:
		x = products.number - 2
		y = products.number + 6
	elif prodnum == 3:
		x = products.number - 3
		y = products.number + 5
	else:
		x = products.number - 4
		y = products.number + 4
	sl = "%d:%d" % (x,y)

	ibool = False
	jbool = False
	if products.has_previous():
		ibool = True
	else:
		ibool = False

	if products.has_next():
		jbool = True
	else:
		jbool = False

	prev_bool = ibool
	next_bool = jbool

	limlist = limitedconverter(limitedoffer)
	catlist = categoryconverter(navbar_category)
	prod_list = productcoverter(products)
	limitedoffer = limlist
	navbar_category = catlist
	products = prod_list

	subcatdict1 = {}
	subcatdict1['subcategory_name'] = sub1.subcategory_name
	subcatdict1['subcategory_slug'] = sub1.subcategory_slug
	subcatdict1['category'] = sub1.category.category_name
	subcatdict1['category_slug'] = str(sub1.category.category_slug)
	sub1 = subcatdict1

	subcatdict2 = {}
	subcatdict2['subcategory_name'] = sub2.subcategory_name
	subcatdict2['subcategory_slug'] = sub2.subcategory_slug
	subcatdict2['category'] = sub2.category.category_name
	subcatdict2['category_slug'] = str(sub2.category.category_slug)
	sub2 = subcatdict2

	subcatdict3 = {}
	subcatdict3['subcategory_name'] = sub3.subcategory_name
	subcatdict3['subcategory_slug'] = sub3.subcategory_slug
	subcatdict3['category'] = sub3.category.category_name
	subcatdict3['category_slug'] = str(sub3.category.category_slug)
	sub3 = subcatdict3

	subcatdict4 = {}
	subcatdict4['subcategory_name'] = sub4.subcategory_name
	subcatdict4['subcategory_slug'] = sub4.subcategory_slug
	subcatdict4['category'] = sub4.category.category_name
	subcatdict4['category_slug'] = str(sub4.category.category_slug)
	sub4 = subcatdict4

	Xbool = False
	if len(products_list) > 25:
		Xbool = True
	else:
		Xbool = False

	Ybool = str(Xbool)

	context = {"nbool" : prev_bool, "mbool" : next_bool, "Ybool":Ybool,"l1":l1,"l2":l2,"l3":l3,"l4":l4,"brands":brands, "prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "products":products, "navbar_category":navbar_category, "sl":sl, 'range': range(1,total_pages), "sub1":sub1,"sub2":sub2,"sub3":sub3,"sub4":sub4}
	template = 'women.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

def Appliances(request):
	"""Appliances Detail Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	navbar_category = Category.objects.all()
	list1 = Product.objects.filter(subcategory__subcategory_name="Kitchen & Home Appliances").order_by('?')
	list2 = Product.objects.filter(subcategory__subcategory_name="Large Appliances").order_by('?')
	count1 = list1.count()
	count2 = list2.count()

	sub1 = SubCategory.objects.get(subcategory_name="Kitchen & Home Appliances")
	sub2 = SubCategory.objects.get(subcategory_name="Large Appliances")

	products_list = list(chain(list1, list2))

	items = []
	for i in products_list:
		brands_dict = {}
		brands_dict['id'] = i.brand.id
		brands_dict['brand_name'] = i.brand.brand_name
		items.append(brands_dict)
	brands = [ast.literal_eval(el1) for el1 in set([str(el2) for el2 in items])]

	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)

	paginator = Paginator(products_list, 25)
	productcount = str(count1 + count2)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	if prodnum == 1:
		x = products.number - 1
		y = products.number + 7
	elif prodnum == 2:
		x = products.number - 2
		y = products.number + 6
	elif prodnum == 3:
		x = products.number - 3
		y = products.number + 5
	else:
		x = products.number - 4
		y = products.number + 4
	sl = "%d:%d" % (x,y)

	ibool = False
	jbool = False
	if products.has_previous():
		ibool = True
	else:
		ibool = False

	if products.has_next():
		jbool = True
	else:
		jbool = False

	prev_bool = ibool
	next_bool = jbool

	limlist = limitedconverter(limitedoffer)
	catlist = categoryconverter(navbar_category)
	prod_list = productcoverter(products)
	limitedoffer = limlist
	navbar_category = catlist
	products = prod_list

	subcatdict1 = {}
	subcatdict1['subcategory_name'] = sub1.subcategory_name
	subcatdict1['subcategory_slug'] = sub1.subcategory_slug
	subcatdict1['category'] = sub1.category.category_name
	subcatdict1['category_slug'] = str(sub1.category.category_slug)
	sub1 = subcatdict1

	subcatdict2 = {}
	subcatdict2['subcategory_name'] = sub2.subcategory_name
	subcatdict2['subcategory_slug'] = sub2.subcategory_slug
	subcatdict2['category'] = sub2.category.category_name
	subcatdict2['category_slug'] = str(sub2.category.category_slug)
	sub2 = subcatdict2

	Xbool = False
	if len(products_list) > 25:
		Xbool = True
	else:
		Xbool = False

	Ybool = str(Xbool)

	context = {"nbool" : prev_bool, "mbool" : next_bool, "Ybool":Ybool,"l1":l1,"l2":l2,"l3":l3,"l4":l4,"brands":brands, "prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "products":products, "navbar_category":navbar_category, "sl":sl, 'range': range(1,total_pages), "sub1":sub1, "sub2":sub2}
	template = 'appliances.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

def Home2(request):
	"""Home Detail Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	navbar_category = Category.objects.all()
	list1 = Product.objects.filter(subcategory__subcategory_name="Decor & Lighting").order_by('?')
	list2 = Product.objects.filter(subcategory__subcategory_name="Kitchen & Dining").order_by('?')
	list3 = Product.objects.filter(subcategory__subcategory_name="Home Improvement").order_by('?')
	count1 = list1.count()
	count2 = list2.count()
	count3 = list3.count()

	sub1 = SubCategory.objects.get(subcategory_name="Decor & Lighting")
	sub2 = SubCategory.objects.get(subcategory_name="Kitchen & Dining")
	sub3 = SubCategory.objects.get(subcategory_name="Home Improvement")

	products_list = list(chain(list1, list2, list3))

	items = []
	for i in products_list:
		brands_dict = {}
		brands_dict['id'] = i.brand.id
		brands_dict['brand_name'] = i.brand.brand_name
		items.append(brands_dict)
	brands = [ast.literal_eval(el1) for el1 in set([str(el2) for el2 in items])]
	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)

	paginator = Paginator(products_list, 25)
	productcount = str(count1 + count2 + count3)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	if prodnum == 1:
		x = products.number - 1
		y = products.number + 7
	elif prodnum == 2:
		x = products.number - 2
		y = products.number + 6
	elif prodnum == 3:
		x = products.number - 3
		y = products.number + 5
	else:
		x = products.number - 4
		y = products.number + 4
	sl = "%d:%d" % (x,y)

	ibool = False
	jbool = False
	if products.has_previous():
		ibool = True
	else:
		ibool = False

	if products.has_next():
		jbool = True
	else:
		jbool = False

	prev_bool = ibool
	next_bool = jbool

	limlist = limitedconverter(limitedoffer)
	catlist = categoryconverter(navbar_category)
	prod_list = productcoverter(products)
	limitedoffer = limlist
	navbar_category = catlist
	products = prod_list

	subcatdict1 = {}
	subcatdict1['subcategory_name'] = sub1.subcategory_name
	subcatdict1['subcategory_slug'] = sub1.subcategory_slug
	subcatdict1['category'] = sub1.category.category_name
	subcatdict1['category_slug'] = str(sub1.category.category_slug)
	sub1 = subcatdict1

	subcatdict2 = {}
	subcatdict2['subcategory_name'] = sub2.subcategory_name
	subcatdict2['subcategory_slug'] = sub2.subcategory_slug
	subcatdict2['category'] = sub2.category.category_name
	subcatdict2['category_slug'] = str(sub2.category.category_slug)
	sub2 = subcatdict2

	subcatdict3 = {}
	subcatdict3['subcategory_name'] = sub3.subcategory_name
	subcatdict3['subcategory_slug'] = sub3.subcategory_slug
	subcatdict3['category'] = sub3.category.category_name
	subcatdict3['category_slug'] = str(sub3.category.category_slug)
	sub3 = subcatdict3

	Xbool = False
	if len(products_list) > 25:
		Xbool = True
	else:
		Xbool = False

	Ybool = str(Xbool)

	context = {"nbool" : prev_bool, "mbool" : next_bool, "Ybool":Ybool,"l1":l1,"l2":l2,"l3":l3,"l4":l4,"brands":brands, "prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "products":products, "navbar_category":navbar_category, "sl":sl, 'range': range(1,total_pages), "sub1":sub1, "sub2":sub2, "sub3":sub3}
	template = 'home2.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

def Electronics(request):
	"""Home Detail Page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	navbar_category = Category.objects.all()
	list1 = Product.objects.filter(subcategory__subcategory_name="Android Mobiles").order_by('?')
	list2 = Product.objects.filter(subcategory__subcategory_name="Tablets").order_by('?')
	list3 = Product.objects.filter(subcategory__subcategory_name="Laptops").order_by('?')
	list4 = Product.objects.filter(subcategory__subcategory_name="Digital SLRs").order_by('?')
	count1 = list1.count()
	count2 = list2.count()
	count3 = list3.count()
	count4 = list4.count()

	sub1 = SubCategory.objects.get(subcategory_name="Android Mobiles")
	sub2 = SubCategory.objects.get(subcategory_name="Tablets")
	sub3 = SubCategory.objects.get(subcategory_name="Laptops")
	sub4 = SubCategory.objects.get(subcategory_name="Digital SLRs")

	products_list = list(chain(list1, list2, list3, list4))

	items = []
	for i in products_list:
		brands_dict = {}
		brands_dict['id'] = i.brand.id
		brands_dict['brand_name'] = i.brand.brand_name
		items.append(brands_dict)
	brands = [ast.literal_eval(el1) for el1 in set([str(el2) for el2 in items])]

	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)

	paginator = Paginator(products_list, 25)
	productcount = str(count1 + count2 + count3 + count4)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1

	prodnum = products.number
	if prodnum == 1:
		x = products.number - 1
		y = products.number + 7
	elif prodnum == 2:
		x = products.number - 2
		y = products.number + 6
	elif prodnum == 3:
		x = products.number - 3
		y = products.number + 5
	else:
		x = products.number - 4
		y = products.number + 4
	sl = "%d:%d" % (x,y)

	ibool = False
	jbool = False
	if products.has_previous():
		ibool = True
	else:
		ibool = False

	if products.has_next():
		jbool = True
	else:
		jbool = False

	prev_bool = ibool
	next_bool = jbool

	limlist = limitedconverter(limitedoffer)
	catlist = categoryconverter(navbar_category)
	prod_list = productcoverter(products)
	limitedoffer = limlist
	navbar_category = catlist
	products = prod_list

	subcatdict1 = {}
	subcatdict1['subcategory_name'] = sub1.subcategory_name
	subcatdict1['subcategory_slug'] = sub1.subcategory_slug
	subcatdict1['category'] = sub1.category.category_name
	subcatdict1['category_slug'] = str(sub1.category.category_slug)
	sub1 = subcatdict1

	subcatdict2 = {}
	subcatdict2['subcategory_name'] = sub2.subcategory_name
	subcatdict2['subcategory_slug'] = sub2.subcategory_slug
	subcatdict2['category'] = sub2.category.category_name
	subcatdict2['category_slug'] = str(sub2.category.category_slug)
	sub2 = subcatdict2

	subcatdict3 = {}
	subcatdict3['subcategory_name'] = sub3.subcategory_name
	subcatdict3['subcategory_slug'] = sub3.subcategory_slug
	subcatdict3['category'] = sub3.category.category_name
	subcatdict3['category_slug'] = str(sub3.category.category_slug)
	sub3 = subcatdict3

	subcatdict4 = {}
	subcatdict4['subcategory_name'] = sub4.subcategory_name
	subcatdict4['subcategory_slug'] = sub4.subcategory_slug
	subcatdict4['category'] = sub4.category.category_name
	subcatdict4['category_slug'] = str(sub4.category.category_slug)
	sub4 = subcatdict4

	Xbool = False
	if len(products_list) > 25:
		Xbool = True
	else:
		Xbool = False

	Ybool = str(Xbool)

	context = {"nbool" : prev_bool, "mbool" : next_bool, "Ybool":Ybool, "l1":l1,"l2":l2,"l3":l3,"l4":l4,"brands":brands, "prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "products":products, "navbar_category":navbar_category, "sl":sl, 'range': range(1,total_pages),  "sub1":sub1,"sub2":sub2,"sub3":sub3,"sub4":sub4}
	template = 'electronics.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

"""============================="""
"""=====PRODUCT DETAIL PAGE====="""
"""============================="""

def ProductPage(request, p_id):
	"""Product detail page"""
	user = None
	try:
		username = request.GET.get('username')
		email  = request.GET.get('email')
		user, s = User.objects.get_or_create(username = username, email = email)
	except Exception as e:
		pass
	
	limitedoffer = LimitedOffer.objects.all()
	navbar_category = Category.objects.all()
	product = Product.objects.get(pk=p_id)
	image = ProductImage.objects.filter(product_name=product)
	variants = Product.objects.filter(title=product.title).order_by('?')[1:]

	product_title = str(product.title)
	request.session['product_title'] = product_title
	print request.session['product_title'], request.session

	similar_products = Product.objects.filter(subcategory=product.subcategory).exclude(title=product.title).order_by('?')
	
	if product.offer_price != None:
		cheapers = Product.objects.filter(subcategory=product.subcategory, offer_price__lt=product.offer_price)
	else:
		cheapers = Product.objects.filter(subcategory=product.subcategory, sale_price__lt=product.sale_price)

	xlist = productcoverter(similar_products)
	similar_products = xlist
	ylist = productcoverter(cheapers)
	cheapers = ylist
	zlist = productcoverter(variants)
	varints = zlist

	limlist = limitedconverter(limitedoffer)
	catlist = categoryconverter(navbar_category)
	limitedoffer = limlist
	navbar_category = catlist

	prod_dict = {}
	prod_dict['id'] = product.id
	prod_dict['title'] = product.title
	prod_dict['brand'] = product.brand.brand_name
	prod_dict['offer_price'] = str(product.offer_price)
	prod_dict['sale_price'] = str(product.sale_price)
	prod_dict['description'] = product.description
	prod_dict['feature'] = product.feature
	prod_dict['link'] = product.link
	prod_dict['seller'] = product.seller
	prod_dict['seller_rating'] = str(product.seller_rating)
	prod_dict['star_rating'] = str(product.star_rating)
	prod_dict['COD'] = product.COD
	prod_dict['mainimage'] = product.mainimage
	prod_dict['category_name'] = product.category.category_name
	prod_dict['subcategory_name'] = product.subcategory.subcategory_name
	prod_dict['category_slug'] = product.category.category_slug
	prod_dict['subcategory_slug'] = product.subcategory.subcategory_slug
	product = prod_dict

	image_list = []
	for i in image:
		image_dict = {}
		image_dict['image_url'] = i.image_url
		image_list.append(image_dict)
	image = image_list

	context = { 
				"product":product, 
				"navbar_category":navbar_category,
				"image" : image,
				"limitedoffer":limitedoffer,
				"similars" : similar_products,
				"cheapers" : cheapers,
				"varints" : varints,
				}
	template = 'productpage.html'
	return HttpResponse(json.dumps(context), content_type = 'application/json')

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

"""========================"""
"""=====SERFO PRODUCTS====="""
"""========================"""

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







	