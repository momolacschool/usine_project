from django.contrib import admin
from .models import (
    Company, ProductCategory, Product, Order, Contact, Document,
    Partner, StaffMember, Banner
)

# ---------------------------
# Configuration de l'Admin pour Company
# ---------------------------
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('company_type', 'created_at')

# ---------------------------
# Configuration de l'Admin pour les Catégories de Produits
# ---------------------------
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

# ---------------------------
# Configuration de l'Admin pour les Produits
# ---------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'category', 'price', 'stock_quantity', 'available', 'created_at')
    search_fields = ('name', 'company__name', 'category__name')
    list_filter = ('available', 'category', 'company')

# ---------------------------
# Configuration de l'Admin pour les Commandes
# ---------------------------
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer_name', 'status', 'created_at')
    search_fields = ('customer_name', 'product__name')
    list_filter = ('status', 'created_at')

# ---------------------------
# Configuration de l'Admin pour les Contacts
# ---------------------------
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')
    list_filter = ('submitted_at',)

# ---------------------------
# Configuration de l'Admin pour les Partenaires
# ---------------------------
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# ---------------------------
# Configuration de l'Admin pour les Membres du Staff
# ---------------------------
@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name', 'position')

# ---------------------------
# Configuration de l'Admin pour les Bannières
# ---------------------------
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)


from django.contrib import admin
from .models import News, Media

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'author', 'views')
    search_fields = ('title', 'content')
    list_filter = ('published_at',)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'uploaded_at')
    search_fields = ('title',)
    list_filter = ('media_type',)
