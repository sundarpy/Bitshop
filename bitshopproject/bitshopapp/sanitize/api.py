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
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags8.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags9.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags10.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags11.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags12.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags13.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/beauty1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/beauty2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/beauty3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/beauty4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/beauty5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/beauty6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/beauty7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/beauty8.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/books1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/books2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/books3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/books4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/books5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/books6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/books7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/books8.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/books9.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cameras1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cameras2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cameras3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cameras4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cameras5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cameras6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cameras7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cameras8.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cameras9.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cameras10.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cameras11.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cameras12.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cars1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cars2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cars3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cars4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cars5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cars6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/cars7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/clothing1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/clothing2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/clothing3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/clothing4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/clothing5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/computers1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/computers2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/computers3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/computers4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/computers5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/computers6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/computers7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/home1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/home2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/home3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/home4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/home5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/home6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/home7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/home8.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/home9.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/home10.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/home11.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/home12.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel8.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel9.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel10.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel11.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel12.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel13.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/jewel14.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/mobiles1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/mobiles2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/mobiles3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/mobiles4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/mobiles5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/mobiles6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/mobiles7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes8.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes9.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes10.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes11.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes12.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/shoes13.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/sports1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/sports2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/sports3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/sports4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/sports5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/sports6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/sports7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/sports8.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/sports9.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/sports10.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/sports11.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/toys1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/toys2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/toys3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/toys4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/toys5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/toys6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/toys7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/toys8.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/movies1.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/movies2.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/movies3.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/movies4.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/movies5.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/movies6.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/movies7.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/movies8.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/movies9.json',
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
