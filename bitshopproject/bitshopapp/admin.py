from django.contrib import admin
from .models import Price, Brand, SerfoProduct, Product, ProductImage, Category, SubCategory, UserProfile, Review, Comment, SubComment, New

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'offer_price', 'sale_price', 'seller', 'category')
	search_fields = ('title',)

class ProductImageAdmin(admin.ModelAdmin):
	list_display = ('product_name',)
	search_fields = ('product_name__title',)

class BrandAdmin(admin.ModelAdmin):
	list_display = ('brand_name',)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_name',)

class SubCategoryAdmin(admin.ModelAdmin):
	list_display = ('subcategory_name',)

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)

class SerfoProductAdmin(admin.ModelAdmin):
	list_display = ('product','super_category',)

class NewAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ('title',)

class PriceAdmin(admin.ModelAdmin):
	list_display = ('title', 'lower_limit', 'upper_limit',)
	search_fields = ('title',)

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Review)
admin.site.register(New, NewAdmin)
admin.site.register(SerfoProduct, SerfoProductAdmin)
admin.site.register(Comment)
admin.site.register(SubComment)
