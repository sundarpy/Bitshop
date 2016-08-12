from __future__ import unicode_literals
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import utc
import datetime
from django.utils import timezone
from django.dispatch import receiver

_APP_NAME = 'bitshopapp'
# Create your models here.
"""=================================="""
"""============USER MODELS==========="""
"""=================================="""

class UserProfile(models.Model):
	"""User Profile Class"""
	user = models.OneToOneField(User, primary_key=True, related_name='bitshopapp_users')
	user_image = models.ImageField()
	img_url = models.CharField(null=True, blank=True, max_length=255)

	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
		('X', 'Other'),
	)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True, null=True)

	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(UserProfile, self).dispatch(*args, **kwargs)

	def create_user(self, user):
		userProfile = self.create(user= user)
		userProfile.save()
		return userProfile

	def create_user(self, user, profile_pic):
		userProfile = self.create(user= user)
		userProfile.save()
		userProfile.profile_pic = profile_pic
		userProfile.profile_pic(upload_to = 'media/'+userProfile.user.name)
		return userProfile

	class Meta:
		db_table = "bitshopapp_User"
		verbose_name_plural = "User Profile"
		abstract = True

	def __unicode__(self):
		return unicode(self.user)

	class Meta:
		app_label = _APP_NAME
		
"""=================================="""
"""==========PRODUCT MODELS=========="""
"""=================================="""

class Category(models.Model):
	"""Product Categories Class"""
	category_name = models.CharField(max_length=100, null=True)
	category_slug = AutoSlugField(populate_from='category_name', null=True)
	icon = models.ImageField(upload_to='icons/', null=True, blank=True, default="http://images.all-free-download.com/images/graphicthumb/abstract_led_tv_blank_screen_realistic_reflection_blue_wave_stylish_colorful_vector_6818232.jpg")

	def __unicode__(self):
		"""Unicode class."""
		return str(self.category_name)

	def get_subs(self):
		return SubCategory.objects.filter(category=self)


class SubCategory(models.Model):
	"""Product SubCategories Class"""
	subcategory_name = models.CharField(max_length=100, null=True)
	category = models.ForeignKey(Category, blank=True, null=True)
	subcategory_slug = AutoSlugField(populate_from='subcategory_name', null=True)

	def __unicode__(self):
		"""Unicode class."""
		return str(self.subcategory_name)

	def get_prods(self):
		return Product.objects.filter(subcategory=self)

class Product(models.Model):
	"""Product Class"""
	title = models.CharField(max_length=255, null=True)
	# selling_price = models.DecimalField(max_digits=10, decimal_places=0, null=True)
	# offer_price = models.DecimalField(max_digits=10, decimal_places=0, null=True)
	# sale_price = models.DecimalField(max_digits=10, decimal_places=0, null=True)  
	selling_price = models.CharField(max_length=255, null=True)
	offer_price = models.CharField(max_length=255, null=True)
	sale_price = models.CharField(max_length=255, null=True)								
	description = models.TextField(null=True)		
	link = models.TextField(null=True)    									
	seller = models.CharField(max_length=50, null=True)									
	seller_rating = models.CharField(max_length=10, null=True)	
	star_rating = models.CharField(max_length=20, null=True)	
	COD = models.CharField(max_length=50, null=True)	
	mainimage = models.TextField(null=True)
	category = models.ForeignKey(Category, default="")
	subcategory = models.ForeignKey(SubCategory, default="")

	def __str__(self):
		return self.title

class ProductImage(models.Model):
	"""Product Image Class"""
	image_url = models.CharField(max_length=200)
	product_name = models.ForeignKey(Product)

	def __str__(self):
		return self.product_name.title

"""=================================="""
"""==========REVIEWS MODELS=========="""
"""=================================="""

class Review(models.Model):
	"""Reviews Class"""
	user = models.ForeignKey(User)
	title = models.CharField(max_length=255, null=True)
	content = models.TextField(null=True)
	timestamp = models.DateTimeField(auto_now_add=True, blank=True)
	product = models.ForeignKey(Product)

	def __str__(self):
		return self.title

"""=================================="""
"""===========FORUMS MODELS=========="""
"""=================================="""

class Post(models.Model):
	"""Post Class"""
	popularity = models.FloatField(default=0.0)
	timestamp = models.DateTimeField(auto_now_add=True, blank=True)
	title = models.CharField(max_length = 200)
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)
	upvoted_by = models.ManyToManyField(User,  related_name='%(class)s_requests_created', blank = True)
	downvoted_by = models.ManyToManyField(User,  related_name='downvotes_request', blank = True)
	user = models.ForeignKey(User)
	width = models.IntegerField(default=0,blank = True)
	height = models.IntegerField(default=0,blank = True)
	img_url = models.ImageField(upload_to = 'post/')
	last_mod = models.DateTimeField(auto_now_add=True, blank = True)

	class Meta:
		ordering = ('-popularity','id')

	def __unicode__(self):
		return " " + str(self.id) + " " + self.title

	def set_popularity(self):
		now = datetime.datetime.utcnow().replace(tzinfo=utc)
		activ_period = abs((self.last_mod - self.timestamp).seconds)
		inactiv_period = abs((now - self.last_mod).seconds)
		#  = (Comments.objects.filter(post = self).count() * 0.5 + self.upvotes * 0.5 - self.downvotes * 0.5 * 
		self.popularity = float(pow(activ_period,2) / (pow(inactiv_period, 1)))
		self.save()

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	upvotes = models.IntegerField(default = 0)
	downvotes = models.IntegerField(default = 0)
	post = models.ForeignKey(Post)
	upvoted_by = models.ManyToManyField(User,  related_name='%(class)s_requests_created_comment', blank = True)
	downvoted_by = models.ManyToManyField(User,  related_name='downvotes_request_comment', blank = True)
	timestamp = models.DateTimeField(auto_now_add=True, blank=True)
	content = models.TextField()

	def __unicode__(self):
		return self.content

class SubComment(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	receiver = models.ForeignKey(User, related_name='%(class)s_requests_created')
	timestamp = models.DateTimeField(auto_now_add=True, blank=True)
	comment = models.ForeignKey(Comment)
	upvoted_by = models.ManyToManyField(User,  related_name='%(class)s_requests_created_sub_comment', blank = True)
	downvoted_by = models.ManyToManyField(User,  related_name='downvotes_request_sub_comment', blank = True)
	upvotes = models.IntegerField(default = 0)
	downvotes = models.IntegerField(default = 0)
	content = models.TextField()

	def __unicode__(self):
		return self.content

class UserActivity(models.Model):
	upvoted = models.IntegerField(default = 0)	
	downvoted = models.IntegerField(default = 0)	
	uploaded = models.IntegerField(default = 0)	
	comment = models.IntegerField(default = 0)	
	subcomment = models.IntegerField(default = 0)
	post = models.ForeignKey(Post)
	timestamp = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

"""==================================="""
"""===========SERFO PRODUCTS=========="""
"""==================================="""

class SerfoProduct(models.Model):
	"""Products to be sent to Serfo"""
	product = models.ForeignKey(Product, null=True, blank=True)
	PRODUCT_CATEGORY = (
		('M', 'Men'),
		('W', 'Women'),
		('A', 'Appliances'),
		('H', 'Home & Furniture'),
		('E', 'Electronics'),
	)
	super_category = models.CharField(max_length=2, choices=PRODUCT_CATEGORY, blank=True, null=True)

	def __str__(self):
		return str(self.product.title)

"""======================================"""
"""===========NEWS FOR PRODUCTS=========="""
"""======================================"""

class New(models.Model):
	"""News related to Products"""
	title = models.CharField(max_length=255, null=True)
	subtitle = models.TextField(null=True, blank=True)
	main_content = models.TextField(null=True, blank=True)
	product = models.ManyToManyField(Product, blank=True)

	def __str__(self):
		return str(self.title)














