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
import ast

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
	navbar_category = Category.objects.all()
	saleoffer = SaleOffer.objects.all()
	limitedoffer = LimitedOffer.objects.all()
	news = New.objects.all().order_by('-id')

	men_prod = SerfoProduct.objects.filter(super_category='M')
	women_prod = SerfoProduct.objects.filter(super_category='W')
	appliances_prod = SerfoProduct.objects.filter(super_category='A')
	home_prod = SerfoProduct.objects.filter(super_category='H')
	electronics_prod = SerfoProduct.objects.filter(super_category='E')

	context = {
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
				}
	template = 'home.html'
	return render(request, template, context)

# def serfoproductcoverter(prod_query):
# 	xlist = []
# 	for i in prod_query:
# 		prod_dict = {}
# 		prod_dict['id'] = str(i.product.id)
# 		prod_dict['title'] = i.product.title
# 		prod_dict['offer_price'] = str(i.product.offer_price)
# 		prod_dict['sale_price'] = str(i.product.sale_price)
# 		prod_dict['mainimage'] = i.product.mainimage
# 		xlist.append(prod_dict)
# 	return xlist

# def productcoverter(prod_query):
# 	xlist = []
# 	for i in prod_query:
# 		prod_dict = {}
# 		prod_dict['id'] = str(i.id)
# 		prod_dict['title'] = i.title
# 		prod_dict['offer_price'] = str(i.offer_price)
# 		prod_dict['sale_price'] = str(i.sale_price)
# 		prod_dict['mainimage'] = i.mainimage
# 		xlist.append(prod_dict)
# 	return xlist


# def HomePage(request):
# 	"""Home Page"""
# 	navbar_category = Category.objects.all()
# 	catlist = []
# 	for cat in navbar_category:
# 		catdict = {}
# 		catdict['id'] = str(cat.id)
# 		catdict['category_name'] = cat.category_name
# 		catdict['category_slug'] = str(cat.category_slug)
# 		catlist.append(catdict)
# 	navbar_category = catlist

# 	saleoffer = SaleOffer.objects.all()
# 	salelist = []
# 	for sale in saleoffer:
# 		saledict = {}
# 		saledict['image'] = sale.image
# 		saledict['link'] = sale.link
# 		salelist.append(saledict)
# 	saleoffer = salelist

# 	limitedoffer = LimitedOffer.objects.all()
# 	limlist = []
# 	for lim in limitedoffer:
# 		limdict = {}
# 		limdict['image'] = lim.image
# 		limdict['link'] = lim.link
# 		limlist.append(limdict)
# 	limitedoffer = limlist

# 	news = New.objects.all().order_by('-id')
# 	newslist = []
# 	for new in news:
# 		newsdict = {}
# 		newsdict['id'] = str(new.id)
# 		newsdict['title'] = new.title
# 		newsdict['image_url'] = new.image_url
# 		newslist.append(newsdict)
# 	news = newslist

# 	men_prod = SerfoProduct.objects.filter(super_category='M')
# 	women_prod = SerfoProduct.objects.filter(super_category='W')
# 	appliances_prod = SerfoProduct.objects.filter(super_category='A')
# 	home_prod = SerfoProduct.objects.filter(super_category='H')
# 	electronics_prod = SerfoProduct.objects.filter(super_category='E')

# 	men_prod_list = serfoproductcoverter(men_prod)
# 	women_prod_list = serfoproductcoverter(women_prod)
# 	appliances_prod_list = serfoproductcoverter(appliances_prod)
# 	home_prod_list = serfoproductcoverter(home_prod)
# 	electronics_prod_list = serfoproductcoverter(electronics_prod)

# 	men_prod = men_prod_list
# 	women_prod = women_prod_list
# 	appliances_prod = appliances_prod_list
# 	home_prod = home_prod_list
# 	electronics_prod = electronics_prod_list


# 	context = { 
# 				"data1" : men_prod,
# 				"data2" : women_prod,
# 				"data3" : appliances_prod,
# 				"data4" : home_prod,
# 				"data5" : electronics_prod, 
# 				"navbar_category" : navbar_category,
# 				"news" : news,
# 				"saleoffer" : saleoffer,
# 				"limitedoffer" : limitedoffer,
# 				}
# 	template = 'home.html'
# 	return HttpResponse(json.dumps(context), content_type = 'application/json')

"""=================================="""
"""=====CATEGORY INDIVIDUAL PAGE====="""
"""=================================="""

def CategoryPage(request, slug):
	"""Category Detail Page"""
	limitedoffer = LimitedOffer.objects.all()
	prices = Price.objects.all().order_by('-id')
	navbar_category = Category.objects.all()
	category = Category.objects.get(category_slug=slug)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
	products_list = Product.objects.filter(category=category).order_by('?')

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

	news = New.objects.filter(category=category).order_by('-id')
	context = {"l1":l1,"l2":l2,"l3":l3,"l4":l4, "prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "category":category, "subcategory":subcategory, "products":products, "navbar_category":navbar_category,"user" : request.user, "brands":brands,  "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages)}
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
	
	category = Category.objects.get(category_slug=slug)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
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

	news = New.objects.filter(category=category).order_by('-id')
	context = {"l1":l1,"l2":l2,"l3":l3,"l4":l4,"prodnum":prodnum, "selected_price":selected_price, "limitedoffer":limitedoffer, "count":productcount, "category":category, "subcategory":subcategory, "products":products,"user" : request.user, "navbar_category":navbar_category, "brands":brands,  "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages), "title":title, "upper":upper, "lower":lower}
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
	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)

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

	news = New.objects.all().order_by('-id')
	context = {"l1":l1,"l2":l2,"l3":l3,"l4":l4,"prodnum":prodnum, "limitedoffer":limitedoffer, "count":productcount, "category":category, "products":products, "navbar_category":navbar_category,"user" : request.user, "brands":brands, "prime_brand":prime_brand, "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages)}
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
	column_count1 = len(brands)/4
	column_count2 = column_count1 * 2
	column_count3 = column_count1 * 3
	column_count4 = column_count1 * 4

	l1 = "%d:%d" % (0,column_count1)
	l2 = "%d:%d" % (column_count1,column_count2)
	l3 = "%d:%d" % (column_count2,column_count3)
	l4 = "%d:%d" % (column_count3,column_count4)
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

	news = New.objects.all().order_by('-id')
	context = {"l1":l1,"l2":l2,"l3":l3,"l4":l4,"prodnum":prodnum, "selected_price":selected_price, "limitedoffer":limitedoffer, "count":productcount, "upper":upper, "lower":lower, "category":category, "products":products,"user" : request.user, "navbar_category":navbar_category, "brands":brands, "prime_brand":prime_brand, "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages), "title":title}
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
	category = Category.objects.get(category_slug=slug1)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
	subcat = SubCategory.objects.get(subcategory_slug=slug2, category=category)
	products_list = Product.objects.filter(subcategory=subcat).order_by('id')

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

	news = New.objects.filter(category=category).order_by('-id')
	context = {"l1":l1,"l2":l2,"l3":l3,"l4":l4,"prodnum":prodnum, "limitedoffer":limitedoffer, "count":productcount, "category":category, "subcategory":subcategory, "products":products,"user" : request.user, "navbar_category":navbar_category,"subcat":subcat, "brands":brands,  "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages)}
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
	category = Category.objects.get(category_slug=slug1)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
	subcat = SubCategory.objects.get(subcategory_slug=slug2, category=category)
	products_list = Product.objects.filter(Q(subcategory=subcat, offer_price__lte=upper, offer_price__gte=lower) | Q(subcategory=subcat, sale_price__lte=upper, sale_price__gte=lower))

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

	news = New.objects.filter(category=category).order_by('-id')
	context = {"l1":l1,"l2":l2,"l3":l3,"l4":l4,"prodnum":prodnum, "selected_price":selected_price, "limitedoffer":limitedoffer, "category":category, "subcategory":subcategory, "products":products,"user" : request.user, "navbar_category":navbar_category,"subcat":subcat, "count":productcount, "brands":brands,  "news" : news, "prices":prices, "sl":sl, 'range': range(1,total_pages), "title":title, "upper":upper, "lower":lower}
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

"""==================================="""
"""=====AMALGAMATED CATEGORY PAGE====="""
"""==================================="""

def Men(request):
	"""Men's Detail Page"""
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
	productcount = count1 + count2 + count3 + count4 
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
	context = {"l1":l1,"l2":l2,"l3":l3,"l4":l4,"brands":brands, "prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "products":products, "navbar_category":navbar_category,"user" : request.user, "sl":sl, 'range': range(1,total_pages), "sub1":sub1,"sub2":sub2,"sub3":sub3,"sub4":sub4}
	template = 'men.html'
	return render(request, template, context)

def Women(request):
	"""Women's Detail Page"""
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
	productcount = count1 + count2 + count3 + count4 
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
	context = {"l1":l1,"l2":l2,"l3":l3,"l4":l4,"brands":brands, "prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "products":products, "navbar_category":navbar_category,"user" : request.user, "sl":sl, 'range': range(1,total_pages), "sub1":sub1,"sub2":sub2,"sub3":sub3,"sub4":sub4}
	template = 'women.html'
	return render(request, template, context)

def Appliances(request):
	"""Appliances Detail Page"""
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
	productcount = count1 + count2
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
	context = {"l1":l1,"l2":l2,"l3":l3,"l4":l4,"brands":brands, "prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "products":products, "navbar_category":navbar_category,"user" : request.user, "sl":sl, 'range': range(1,total_pages), "sub1":sub1, "sub2":sub2}
	template = 'appliances.html'
	return render(request, template, context)

def Home2(request):
	"""Home Detail Page"""
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
	productcount = count1 + count2 + count3
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
	context = {"l1":l1,"l2":l2,"l3":l3,"l4":l4,"brands":brands, "prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "products":products, "navbar_category":navbar_category,"user" : request.user, "sl":sl, 'range': range(1,total_pages), "sub1":sub1, "sub2":sub2, "sub3":sub3}
	template = 'home2.html'
	return render(request, template, context)

def Electronics(request):
	"""Home Detail Page"""
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
	productcount = count1 + count2 + count3 + count4
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
	context = {"l1":l1,"l2":l2,"l3":l3,"l4":l4,"brands":brands, "prodnum":prodnum, "count":productcount, "limitedoffer" : limitedoffer, "products":products, "navbar_category":navbar_category,"user" : request.user, "sl":sl, 'range': range(1,total_pages),  "sub1":sub1,"sub2":sub2,"sub3":sub3,"sub4":sub4}
	template = 'electronics.html'
	return render(request, template, context)

"""============================="""
"""=====PRODUCT DETAIL PAGE====="""
"""============================="""

def ProductPage(request, p_id):
	"""Product detail page"""
	limitedoffer = LimitedOffer.objects.all()
	navbar_category = Category.objects.all()
	category = Category.objects.all()
	subcategory = SubCategory.objects.all()
	product = Product.objects.get(pk=p_id)
	image = ProductImage.objects.filter(product_name=product)
	# comments = Comment.objects.filter(product=product)
	# subcomments = SubComment.objects.filter(comment=comments)
	# form = CommentForm()
	# if request.user.is_authenticated():
	# 	if request.method == 'POST':
	# 		form = CommentForm(data=request.POST)
	# 		if form.is_valid():
	# 			content=form.cleaned_data.get('content')
	# 			comment = Comment(user=request.user, content=content, product=product)
	# 			comment.save()
	# 			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	# 	else :
	# 		form = CommentForm()

	similar_products = Product.objects.filter(subcategory=product.subcategory).exclude(title=product.title).order_by('?')
	
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
				"similars" : similar_products,
				"cheapers" : cheapers,
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







	