#!/usr/bin/python
import os, sys
import json
from bitshopapp.models import Product, ProductImage, Category, SubCategory
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib2
import unicodedata

"""================================"""
"""=====#API for Amazon Items#====="""
"""================================"""

@api_view(['GET','POST'])
def read_file12(request):

	urls = [
		# 'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags1.json',
		# 'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags2.json',
		# 'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags3.json',
		# 'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags4.json',
		# 'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags5.json',
		# 'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags6.json',
		# 'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags7.json',
		# 'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags8.json',
		# 'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags9.json',
		# 'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags10.json',
		# 'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags11.json',
		# 'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags12.json',
		'https://s3.ap-south-1.amazonaws.com/bitshopping/json+files/bags/bags14.json',
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
				elif key=='sellingprice':
					sellingprice_temp = str(item[key])
					sellingprice_temp2 = sellingprice_temp.replace("[u'","").replace("']","").replace('[u"','').replace('"]','')
					if sellingprice_temp2 == "[]":
						product_sellingprice = ""
					else:
						product_sellingprice = sellingprice_temp2[1:]
				elif key=='offerprice':
					offerprice_temp = str(item[key])
					offerprice_temp2 = offerprice_temp.replace("[u'","").replace("']","").replace('[u"','').replace('"]','')
					if offerprice_temp2 == "[]":
						product_offerprice = ""
					else:
						product_offerprice = offerprice_temp2[1:]
				elif key=='saleprice':
					saleprice_temp = str(item[key])
					saleprice_temp2 = saleprice_temp.replace("[u'","").replace("']","").replace('[u"','').replace('"]','')
					if saleprice_temp2 == "[]":
						product_saleprice = ""
					else:
						product_saleprice = saleprice_temp2[1:]
				elif key=='description':
					xlist = []
					description_temp = item[key]
					for n in description_temp:
						description_temp2 = unicodedata.normalize('NFKD', n).encode('ascii', 'ignore')
						xlist.append(description_temp2)
					description_temp3 = str(xlist)
					description_temp4 = description_temp3.replace("\\n","").replace("\\t","").replace("\\r","").replace("['","").replace("']","").replace("'","").replace(",","").replace('"','').replace("Review","").replace("About the Author","").replace("Book Description","").replace("See all Product Description","").replace("Product Description","")
					description_temp5 = description_temp4.lstrip().rstrip()
					product_desc = description_temp5
				elif key=='image':
					imagelist = []
					image_urls = item[key]
					for i in image_urls:
						temp = i.replace("[u'","").replace("']","").replace('[u"','').replace('"]','').replace("SS40","SS256")
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
					product_cod = "Available"


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

			if product_title != "[]":
				prod_obj=Product(
						title = product_title,
						selling_price = product_sellingprice,
						offer_price = product_offerprice, 
						sale_price = product_saleprice,
						description = product_desc, 
						link = product_link,
						seller = product_seller, 
						seller_rating = product_sellrating,
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


