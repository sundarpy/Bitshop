#!/usr/bin/python
import os, sys
import json
from bitshopapp.models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib2
import unicodedata
import string

"""================================"""
"""=====#API for Amazon Items#====="""
"""================================"""

@api_view(['GET','POST'])
def read_file(request):

	urls = [
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags8.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags9.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags10.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags11.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags12.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/bags13.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/beauty1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/beauty2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/beauty3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/beauty4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/beauty5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/beauty6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/beauty7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/beauty8.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/books1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/books2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/books3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/books4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/books5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/books6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/books7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/books8.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/books9.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cameras1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cameras2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cameras3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cameras4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cameras5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cameras6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cameras7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cameras8.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cameras9.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cameras10.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cameras11.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cameras12.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cars1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cars2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cars3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cars4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cars5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cars6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/cars7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/clothing1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/clothing2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/clothing3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/clothing4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/clothing5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/computers1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/computers2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/computers3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/computers4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/computers5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/computers6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/computers7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/home1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/home2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/home3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/home4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/home5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/home6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/home7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/home8.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/home9.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/home10.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/home11.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/home12.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel8.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel9.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel10.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel11.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel12.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel13.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/jewel14.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/mobiles1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/mobiles2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/mobiles3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/mobiles4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/mobiles5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/mobiles6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/mobiles7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes8.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes9.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes10.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes11.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes12.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/shoes13.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/sports1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/sports2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/sports3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/sports4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/sports5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/sports6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/sports7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/sports8.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/sports9.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/sports10.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/sports11.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/toys1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/toys2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/toys3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/toys4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/toys5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/toys6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/toys7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/toys8.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/movies1.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/movies2.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/movies3.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/movies4.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/movies5.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/movies6.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/movies7.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/movies8.json',
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/movies9.json',
	]

	for url in urls:					
		json_string = urllib2.urlopen(url).read()																
		data = json.loads(json_string)												
		for item in data:															
			for key in item:
				if key=='category':
					product_category = str(item[key])
				elif key=='subcategory':
					product_subcategory = str(item[key])
				elif key=='title':
					ylist = []
					title_temp = item[key]
					for i in title_temp:
						title_temp2 = unicodedata.normalize('NFKD', i).encode('ascii', 'ignore')
						ylist.append(title_temp2)
					title_temp3 = str(ylist)
					title_temp4 = title_temp3.replace("['","").replace("']","").replace('["','').replace('"]','').replace("\\n","").replace("\\t","").replace("\\r","")
					product_title = title_temp4.lstrip().rstrip()
				elif key=='brand':
					blist = []
					brand_temp = item[key]
					for i in brand_temp:
						brand_temp2 = unicodedata.normalize('NFKD', i).encode('ascii', 'ignore')
						blist.append(brand_temp2)
					brand_temp3 = str(blist)
					brand_temp4 = brand_temp3.replace("['","").replace("']","").replace('["','').replace('"]','').replace("\\n","").replace("\\t","").replace("\\r","")
					product_brand = brand_temp4.lstrip().rstrip()
				elif key=='offerprice':
					sep = "-"
					offerprice_temp = str(item[key])
					offerprice_temp2 = offerprice_temp.replace("[u'","").replace("']","").replace('[u"','').replace('"]','').replace(" ', u'","").replace("Lower price available on selected options","")
					print "==========",offerprice_temp2
					if offerprice_temp2 == "[]" or offerprice_temp2 == "":
						product_offerprice = None
					else:
						offerprice = offerprice_temp2[1:]
						if sep in offerprice:
							offerprice_tempx = str(offerprice).replace(",","").replace(" ","").split(sep, 1)[0]
							product_offerprice = float(offerprice_tempx)
						else:
							offerprice_tempx = str(offerprice).replace(",","").replace(" ","")
							product_offerprice = float(offerprice_tempx)

				elif key=='saleprice':
					sep = "-"
					saleprice_temp = str(item[key])
					saleprice_temp2 = saleprice_temp.replace("[u'","").replace("']","").replace('[u"','').replace('"]','').replace(" ', u'","").replace("Lower price available on selected options","")
					print "==========",saleprice_temp2
					if saleprice_temp2 == "[]" or saleprice_temp2 == "":
						product_saleprice = None
					else:
						saleprice = saleprice_temp2[1:]
						if sep in saleprice:
							saleprice_tempx = str(saleprice).replace(",","").replace(" ","").split(sep, 1)[0]
							product_saleprice = float(saleprice_tempx)
						else:
							saleprice_tempx = str(saleprice).replace(",","").replace(" ","")
							product_saleprice = float(saleprice_tempx)

				elif key=='description':
					xlist = []
					description_temp = item[key]
					for n in description_temp:
						description_temp2 = unicodedata.normalize('NFKD', n).encode('ascii', 'ignore')
						xlist.append(description_temp2)
					description_temp3 = str(xlist)
					description_temp4 = description_temp3.replace("\\n","").replace("\\t","").replace("\\r","").replace("[","").replace("]","").replace("'","").replace(",","").replace('"','').replace("Review","").replace("About the Author","").replace("Book Description","").replace("See all Product Description","").replace("Product Description","")
					description_temp5 = description_temp4.lstrip().rstrip()
					if description_temp5 == "[]":
						product_desc = ""
					else:
						product_desc = description_temp5
				elif key=='image':
					imagelist = []
					image_urls = item[key]
					for i in image_urls:
						temp = i.replace("[u'","").replace("']","").replace('[u"','').replace('"]','').replace("SS40","SS256").replace("SR38,50","SR190,250").replace("US40","US256").replace("SX38_SY50_CR,0,0,38,50","SX190_SY250_CR,0,0,190,250")
						temp2 = str(temp)
						imagelist.append(temp)
				elif key=='link':
					product_link = str(item[key])
				elif key=='seller':
					seller_temp = str(item[key])
					seller_temp2 = seller_temp.replace("[u'","").replace("']","").replace('[u"','').replace('"]','')
					if seller_temp2 == "[]":
						product_seller = ""
					elif seller_temp2 == "Amazing Buy', u'Amazing Buy":
						product_seller = "Amazing Buy"
					elif seller_temp2 == "uRead-shop', u'uRead-shop":
						product_seller = "uRead-shop"
					elif seller_temp2 == "Wonder Buy', u'Wonder Buy":
						product_seller = "Wonder Buy"
					elif seller_temp2 == "UBSPD', u'UBSPD":
						product_seller = "UBSPD"
					else:
						product_seller = seller_temp2
				elif key=='sellrating':
					sellrating_temp = str(item[key])
					sellrating_temp2 = sellrating_temp.replace("n","").replace(")","").replace("(","").replace(" ","").replace("Soldby","").replace("u","").replace(",","").replace("'","").replace("[","")
					sellrating_temp3 = sellrating_temp2[14:17]
					product_sellrating = sellrating_temp3
				elif key=='COD':
					product_cod = str(item[key])
				elif key=='feature':
					zlist = []
					feature_temp = item[key]
					for m in feature_temp:
						feature_temp2 = unicodedata.normalize('NFKD', m).encode('ascii', 'ignore')
						zlist.append(feature_temp2)
					feature_temp3 = str(zlist)
					feature_temp4 = feature_temp3.replace("\\n","").replace("\\t","").replace("\\r","").replace("[","").replace("]","").replace("'","").replace(",","").replace('"','').replace("Review","").replace("About the Author","").replace("Book Description","").replace("See all Product Description","").replace("Product Description","")
					feature_temp5 = feature_temp4.lstrip().rstrip()
					if feature_temp5 == "[]":
						product_feature = ""
					else:
						product_feature = feature_temp5
				elif key=='starating':
					starating_temp = str(item[key])
					starating_temp2 = starating_temp.replace(" ","").replace(")","").replace("(","").replace("[u'","").replace("']","").replace('[u"','').replace('"]','')
					product_starating = starating_temp2[:3]


			try:
				prod_brand=Brand.objects.get(brand_name=product_brand)
			except:
				prod_brand=Brand(brand_name=product_brand)
				prod_brand.save()

			try:
				prod_category=Category.objects.get(category_name=product_category)
			except:
				prod_category=Category(category_name=product_category)
				prod_category.save()

			try:
				prod_subcategory=SubCategory.objects.get(subcategory_name=product_subcategory)
			except:
				prod_subcategory=SubCategory(subcategory_name=product_subcategory, category=prod_category)
				prod_subcategory.save()

			try:
				prod_obj=Product.objects.get_or_update(
						title = product_title,
						brand = prod_brand,
						offer_price = product_offerprice, 
						sale_price = product_saleprice,
						description = product_desc, 
						feature = product_feature,
						link = product_link,
						seller = product_seller, 
						seller_rating = product_sellrating,
						star_rating = product_starating,
						COD = product_cod,
						mainimage = imagelist[0],
						category = prod_category,
						subcategory = prod_subcategory,
						)
				prod_obj=Product.objects.get(
						title = product_title,
						brand = prod_brand,
						offer_price = product_offerprice, 
						sale_price = product_saleprice,
						description = product_desc, 
						feature = product_feature,
						link = product_link,
						seller = product_seller, 
						seller_rating = product_sellrating,
						star_rating = product_starating,
						COD = product_cod,
						mainimage = imagelist[0],
						category = prod_category,
						subcategory = prod_subcategory,
						)
			except:
				if product_title != "[]" and imagelist != [] and product_offerprice != None and product_saleprice != None:
					prod_obj=Product(
							title = product_title,
							brand = prod_brand,
							offer_price = product_offerprice, 
							sale_price = product_saleprice,
							description = product_desc, 
							feature = product_feature,
							link = product_link,
							seller = product_seller, 
							seller_rating = product_sellrating,
							star_rating = product_starating,
							COD = product_cod,
							mainimage = imagelist[0],
							category = prod_category,
							subcategory = prod_subcategory,
							)
					prod_obj.save()

				for i in imagelist:
					prod_im=ProductImage(
						image_url = i,
						product_name = prod_obj, 
						)
					prod_im.save()

	return Response({'message':'Products saved succesfully', 'status':200})


"""===========#API END#==========="""

"""================================="""
"""=====#API for Amazon Offers#====="""
"""================================="""

@api_view(['GET','POST'])
def read_file2(request):

	urls = [
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/offer1.json',
	]

	query_Set = SaleOffer.objects.all()
	query_Set.delete()
	for url in urls:					
		json_string = urllib2.urlopen(url).read()																
		data = json.loads(json_string)												
		for item in data:															
			for key in item:
				if key=='image':
					temp1 = str(item[key])
					temp2 = temp1.replace("[u'","").replace("']","")
					offer_image = temp2
				elif key=='link':
					temp3 = str(item[key])
					temp4 = 'http://www.amazon.in/' + temp3.replace("[u'","").replace("']","")
					offer_link = temp4

			try:
				prod_offer1=SaleOffer.objects.get(image=offer_image, link=offer_link)
			except:
				prod_offer1=SaleOffer(image=offer_image, link=offer_link)
				prod_offer1.save()

	return Response({'message':'Offers saved succesfully', 'status':200})


"""===========#API END#==========="""

"""================================="""
"""=====#API for Amazon Offers#====="""
"""================================="""

@api_view(['GET','POST'])
def read_file3(request):

	urls = [
		'https://s3-us-west-2.amazonaws.com/serfoshop/newjson/offer2.json',
	]

	query_Set = LimitedOffer.objects.all()
	query_Set.delete()
	for url in urls:					
		json_string = urllib2.urlopen(url).read()																
		data = json.loads(json_string)												
		for item in data:															
			for key in item:
				if key=='image':
					temp1 = str(item[key])
					temp2 = temp1.replace("[u'","").replace("']","")
					offer_image = temp2
				elif key=='link':
					temp3 = str(item[key])
					temp4 = 'http://www.amazon.in/' + temp3.replace("[u'","").replace("']","")
					offer_link = temp4

			try:
				prod_offer2=LimitedOffer.objects.get(image=offer_image, link=offer_link)
			except:
				prod_offer2=LimitedOffer(image=offer_image, link=offer_link)
				prod_offer2.save()

	return Response({'message':'Offers saved succesfully', 'status':200})


"""===========#API END#==========="""
