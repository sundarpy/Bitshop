from django.contrib import admin
from .models import SerfoProduct, Product, ProductImage, Category, SubCategory, UserProfile, Review, Post, Comment, SubComment, UserActivity, New

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'offer_price', 'seller', 'category')
	search_fields = ('title',)

class ProductImageAdmin(admin.ModelAdmin):
	list_display = ('product_name',)
	search_fields = ('product_name__title',)

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

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Review)
admin.site.register(Post)
admin.site.register(New, NewAdmin)
admin.site.register(SerfoProduct, SerfoProductAdmin)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(UserActivity)