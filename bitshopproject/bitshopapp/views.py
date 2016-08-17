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

"""==============================="""
"""=========SEARCH METHOD========="""
"""==============================="""

def Search(request):
	"""Search."""
	item1 = []
	item2 = []
	item3 = []
	item4 = []
	item5 = []

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
		if i.product.offer_price != "":
			response1['price'] = i.product.offer_price
		else:
			response1['price'] = i.product.sale_price
		response1['link'] = i.product.link
		temp_image = i.product.mainimage
		response1['mainimage'] = temp_image
		item1.append(response1)

	"""Women"""
	for j in women_prod:
		response2 = {}
		response2['super_category'] = j.super_category
		response2['id'] = j.product.id
		response2['title'] = j.product.title
		if j.product.offer_price != "":
			response2['price'] = j.product.offer_price
		else:
			response2['price'] = j.product.sale_price
		response2['link'] = j.product.link
		temp_image = j.product.mainimage
		response2['mainimage'] = temp_image
		item2.append(response2)

	"""Appliances"""
	for x in appliances_prod:
		response3 = {}
		response3['super_category'] = x.super_category
		response3['id'] = x.product.id
		response3['title'] = x.product.title
		if x.product.offer_price != "":
			response3['price'] = x.product.offer_price
		else:
			response3['price'] = x.product.sale_price
		response3['link'] = x.product.link
		response3['mainimage'] = x.product.mainimage
		item3.append(response3)

	"""Home"""
	for y in home_prod:
		response4 = {}
		response4['super_category'] = y.super_category
		response4['id'] = y.product.id
		response4['title'] = y.product.title
		if y.product.offer_price != "":
			response4['price'] = y.product.offer_price
		else:
			response4['price'] = y.product.sale_price
		response4['link'] = y.product.link
		response4['mainimage'] = y.product.mainimage
		item4.append(response4)

	"""Electronics"""
	for z in electronics_prod:
		response5 = {}
		response5['super_category'] = z.super_category
		response5['id'] = z.product.id
		response5['title'] = z.product.title
		if z.product.offer_price != "":
			response5['price'] = z.product.offer_price
		else:
			response5['price'] = z.product.sale_price
		response5['link'] = z.product.link
		response5['mainimage'] = z.product.mainimage
		item5.append(response5)
	navbar_category = Category.objects.all().order_by('?')
	data1 = item1
	data2 = item2
	data3 = item3
	data4 = item4
	data5 = item5
	cat = Category.objects.all()
	subcat = SubCategory.objects.all()
	try:
		q = request.GET.get('q')
	except:
		q = None

	if q:
		products = Product.objects.filter(title__icontains=q)
		context = {
					"query": q, 
					"products": products,
					"subcats":subcat, 
					"cats":cat,
					"data1" : data1,
					"data2" : data2,
					"data3" : data3,
					"data4" : data4,
					"data5" : data5, 
					"navbar_category" : navbar_category,
					}
		template = 'results.html'
	else:
		template = 'home.html'
		context = {"subcats":subcat, "cat":cat, "navbar_category" : navbar_category,}
	return render(request, template, context)

"""==============================="""
"""===========HOME PAGE==========="""
"""==============================="""

def HomePage(request):
	"""Home Page"""
	navbar_category = Category.objects.all().order_by('?')
	category = Category.objects.all()
	sub_category = SubCategory.objects.all()
	subcategory = SubCategory.objects.filter(category=category)
	products = Product.objects.filter(subcategory=subcategory)
	news = New.objects.all()
	
	item1 = []
	item2 = []
	item3 = []
	item4 = []
	item5 = []

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
		if i.product.offer_price != "":
			response1['price'] = i.product.offer_price
		else:
			response1['price'] = i.product.sale_price
		response1['link'] = i.product.link
		temp_image = i.product.mainimage
		response1['mainimage'] = temp_image
		item1.append(response1)

	"""Women"""
	for j in women_prod:
		response2 = {}
		response2['super_category'] = j.super_category
		response2['id'] = j.product.id
		response2['title'] = j.product.title
		if j.product.offer_price != "":
			response2['price'] = j.product.offer_price
		else:
			response2['price'] = j.product.sale_price
		response2['link'] = j.product.link
		temp_image = j.product.mainimage
		response2['mainimage'] = temp_image
		item2.append(response2)

	"""Appliances"""
	for x in appliances_prod:
		response3 = {}
		response3['super_category'] = x.super_category
		response3['id'] = x.product.id
		response3['title'] = x.product.title
		if x.product.offer_price != "":
			response3['price'] = x.product.offer_price
		else:
			response3['price'] = x.product.sale_price
		response3['link'] = x.product.link
		response3['mainimage'] = x.product.mainimage
		item3.append(response3)

	"""Home"""
	for y in home_prod:
		response4 = {}
		response4['super_category'] = y.super_category
		response4['id'] = y.product.id
		response4['title'] = y.product.title
		if y.product.offer_price != "":
			response4['price'] = y.product.offer_price
		else:
			response4['price'] = y.product.sale_price
		response4['link'] = y.product.link
		response4['mainimage'] = y.product.mainimage
		item4.append(response4)

	"""Electronics"""
	for z in electronics_prod:
		response5 = {}
		response5['super_category'] = z.super_category
		response5['id'] = z.product.id
		response5['title'] = z.product.title
		if z.product.offer_price != "":
			response5['price'] = z.product.offer_price
		else:
			response5['price'] = z.product.sale_price
		response5['link'] = z.product.link
		response5['mainimage'] = z.product.mainimage
		item5.append(response5)

	data1 = item1
	data2 = item2
	data3 = item3
	data4 = item4
	data5 = item5

	context = {
				"category":category, 
				"subcategory":subcategory, 
				"products":products, 
				"sub_category":sub_category, 
				"data1" : data1,
				"data2" : data2,
				"data3" : data3,
				"data4" : data4,
				"data5" : data5, 
				"navbar_category" : navbar_category,
				}
	template = 'home.html'
	return render(request, template, context)

"""=================================="""
"""=====CATEGORY INDIVIDUAL PAGE====="""
"""=================================="""

def CategoryPage(request, c_id):
	"""Category Detail Page"""
	navbar_category = Category.objects.all().order_by('?')
	brands = Brand.objects.all().order_by('?')
	category = Category.objects.get(pk=c_id)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
	products_list = Product.objects.filter(category=category).exclude(offer_price="", sale_price="").order_by('id')
	paginator = Paginator(products_list, 18)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1
	context = {"category":category, "subcategory":subcategory, "products":products, "navbar_category":navbar_category, "brands":brands}
	template = 'categorydetail.html'
	return render(request, template, context)

"""=================================="""
"""======BRANDS INDIVIDUAL PAGE======"""
"""=================================="""

def BrandsPage(request, b_id):
	"""Brands Detail Page"""
	navbar_category = Category.objects.all().order_by('?')
	brands = Brand.objects.all().order_by('?')
	prime_brand = Brand.objects.get(pk=b_id)
	category = Category.objects.all()
	products_list = Product.objects.filter(brand=prime_brand).exclude(offer_price="", sale_price="").order_by('id')
	paginator = Paginator(products_list, 18)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1
	context = {"category":category, "products":products, "navbar_category":navbar_category, "brands":brands, "prime_brand":prime_brand}
	template = 'brandetail.html'
	return render(request, template, context)

"""====================================="""
"""=====SUBCATEGORY INDIVIDUAL PAGE====="""
"""====================================="""

def SubCategoryPage(request, c_id, s_id):
	"""SubCategory Detail Page"""
	navbar_category = Category.objects.all().order_by('?')
	brands = Brand.objects.all().order_by('?')
	category = Category.objects.get(pk=c_id)
	subcategory = SubCategory.objects.filter(category=category).order_by('id')
	subcat = SubCategory.objects.get(pk=s_id, category=category)
	products_list = Product.objects.filter(subcategory=subcat).exclude(offer_price="", sale_price="").order_by('id')
	paginator = Paginator(products_list, 18)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	total_pages = products.paginator.num_pages+1
	context = {"category":category, "subcategory":subcategory, "products":products, "navbar_category":navbar_category,"subcat":subcat, "brands":brands}
	template = 'subcategorydetail.html'
	return render(request, template, context)

"""=============================="""
"""=====NEWS INDIVIDUAL PAGE====="""
"""=============================="""

def NewsPage(request, n_id):
	"""Product News Detail Page"""
	navbar_category = Category.objects.all().order_by('?')
	news = New.objects.get(pk=n_id)
	item1 = []
	item2 = []
	item3 = []
	item4 = []
	item5 = []

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
		if i.product.offer_price != "":
			response1['price'] = i.product.offer_price
		else:
			response1['price'] = i.product.sale_price
		response1['link'] = i.product.link
		temp_image = i.product.mainimage
		response1['mainimage'] = temp_image
		item1.append(response1)

	"""Women"""
	for j in women_prod:
		response2 = {}
		response2['super_category'] = j.super_category
		response2['id'] = j.product.id
		response2['title'] = j.product.title
		if j.product.offer_price != "":
			response2['price'] = j.product.offer_price
		else:
			response2['price'] = j.product.sale_price
		response2['link'] = j.product.link
		temp_image = j.product.mainimage
		response2['mainimage'] = temp_image
		item2.append(response2)

	"""Appliances"""
	for x in appliances_prod:
		response3 = {}
		response3['super_category'] = x.super_category
		response3['id'] = x.product.id
		response3['title'] = x.product.title
		if x.product.offer_price != "":
			response3['price'] = x.product.offer_price
		else:
			response3['price'] = x.product.sale_price
		response3['link'] = x.product.link
		response3['mainimage'] = x.product.mainimage
		item3.append(response3)

	"""Home"""
	for y in home_prod:
		response4 = {}
		response4['super_category'] = y.super_category
		response4['id'] = y.product.id
		response4['title'] = y.product.title
		if y.product.offer_price != "":
			response4['price'] = y.product.offer_price
		else:
			response4['price'] = y.product.sale_price
		response4['link'] = y.product.link
		response4['mainimage'] = y.product.mainimage
		item4.append(response4)

	"""Electronics"""
	for z in electronics_prod:
		response5 = {}
		response5['super_category'] = z.super_category
		response5['id'] = z.product.id
		response5['title'] = z.product.title
		if z.product.offer_price != "":
			response5['price'] = z.product.offer_price
		else:
			response5['price'] = z.product.sale_price
		response5['link'] = z.product.link
		response5['mainimage'] = z.product.mainimage
		item5.append(response5)

	data1 = item1
	data2 = item2
	data3 = item3
	data4 = item4
	data5 = item5
	context = {
				"news":news, 
				"navbar_category":navbar_category,
				"data1" : data1,
				"data2" : data2,
				"data3" : data3,
				"data4" : data4,
				"data5" : data5,
				}
	template = 'newsdetail.html'
	return render(request, template, context)

"""========================="""
"""=====NEWS TOTAL PAGE====="""
"""========================="""

def News(request):
	"""Product News Detail Page"""
	navbar_category = Category.objects.all().order_by('?')
	news = New.objects.all()
	item1 = []
	item2 = []
	item3 = []
	item4 = []
	item5 = []

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
		if i.product.offer_price != "":
			response1['price'] = i.product.offer_price
		else:
			response1['price'] = i.product.sale_price
		response1['link'] = i.product.link
		temp_image = i.product.mainimage
		response1['mainimage'] = temp_image
		item1.append(response1)

	"""Women"""
	for j in women_prod:
		response2 = {}
		response2['super_category'] = j.super_category
		response2['id'] = j.product.id
		response2['title'] = j.product.title
		if j.product.offer_price != "":
			response2['price'] = j.product.offer_price
		else:
			response2['price'] = j.product.sale_price
		response2['link'] = j.product.link
		temp_image = j.product.mainimage
		response2['mainimage'] = temp_image
		item2.append(response2)

	"""Appliances"""
	for x in appliances_prod:
		response3 = {}
		response3['super_category'] = x.super_category
		response3['id'] = x.product.id
		response3['title'] = x.product.title
		if x.product.offer_price != "":
			response3['price'] = x.product.offer_price
		else:
			response3['price'] = x.product.sale_price
		response3['link'] = x.product.link
		response3['mainimage'] = x.product.mainimage
		item3.append(response3)

	"""Home"""
	for y in home_prod:
		response4 = {}
		response4['super_category'] = y.super_category
		response4['id'] = y.product.id
		response4['title'] = y.product.title
		if y.product.offer_price != "":
			response4['price'] = y.product.offer_price
		else:
			response4['price'] = y.product.sale_price
		response4['link'] = y.product.link
		response4['mainimage'] = y.product.mainimage
		item4.append(response4)

	"""Electronics"""
	for z in electronics_prod:
		response5 = {}
		response5['super_category'] = z.super_category
		response5['id'] = z.product.id
		response5['title'] = z.product.title
		if z.product.offer_price != "":
			response5['price'] = z.product.offer_price
		else:
			response5['price'] = z.product.sale_price
		response5['link'] = z.product.link
		response5['mainimage'] = z.product.mainimage
		item5.append(response5)

	data1 = item1
	data2 = item2
	data3 = item3
	data4 = item4
	data5 = item5

	context = {
				"news":news, 
				"navbar_category":navbar_category,
				"data1" : data1,
				"data2" : data2,
				"data3" : data3,
				"data4" : data4,
				"data5" : data5, 
				}
	template = 'news.html'
	return render(request, template, context)

"""========================="""
"""=====NEWS API METHOD====="""
"""========================="""

# def EmbedNews(request, n_id):

"""==========================="""
"""=====ALL BRANDS METHOD====="""
"""==========================="""

def AllBrands(request):
	"""All brands page"""
	brands = Brand.objects.all().order_by('brand_name')
	navbar_category = Category.objects.all().order_by('?')
	context = {"navbar_category":navbar_category, "brands":brands}
	template = 'brand.html'
	return render(request, template, context)

"""============================="""
"""=====PRODUCT DETAIL PAGE====="""
"""============================="""

def ProductPage(request, p_id):
	"""Product detail page"""
	navbar_category = Category.objects.all().order_by('?')
	category = Category.objects.all()
	subcategory = SubCategory.objects.all()
	product = Product.objects.get(pk=p_id)
	image = ProductImage.objects.filter(product_name=product)
	comments = Comment.objects.filter(product=product)
	subcomments = SubComment.objects.filter(comment=comments)
	similar_products = Product.objects.filter(subcategory=product.subcategory).order_by('?')

	context = {
				"category":category,
				"subcategory":subcategory, 
				"product":product, 
				"navbar_category":navbar_category,
				"image" : image,
				"comments" : comments,
				"subcomments" : subcomments,
				"similars" : similar_products,
				}
	template = 'productpage.html'
	return render(request, template, context)

"""============================="""
"""=====USER AUTHENTICATION====="""
"""============================="""

@csrf_protect
def login_view(request):
	"""Sign In Method"""
	next = request.GET.get('next')
	title = "LOG IN"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		messages.info(request, 'Logged in as '+request.user.username+'.',fail_silently=True)
		if next:
			return HttpResponseRedirect(next)
		return HttpResponseRedirect('/')
	context = {"form":form, "title":title}
	template = 'login.html'
	return render(request, template, context)

@csrf_protect
def register_view(request):
	"""Sign Up Method"""
	next = request.GET.get('next')
	title = "SIGN UP"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		user_details = UserProfile(user_id=user.id)
		user_details.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		messages.info(request, 'Logged in as '+request.user.username+'.',fail_silently=True)
		if next:
			return HttpResponseRedirect(next)
		return HttpResponseRedirect('/')
	context = {"form":form, "title":title}
	template = 'signup.html'
	return render(request, template, context)

def logout_view(request):
	logout(request)
	messages.info(request, 'Successfully logged out.',fail_silently=True)
	return HttpResponseRedirect('/')

"""========================"""
"""=====SERFO PRODUCTS====="""
"""========================"""

@api_view(['GET','POST'])
def getproducts(request):
	"""Products to be sent to Serfo"""
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
		if i.product.offer_price != "":
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
		if j.product.offer_price != "":
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
		if x.product.offer_price != "":
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
		if y.product.offer_price != "":
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
		if z.product.offer_price != "":
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
	