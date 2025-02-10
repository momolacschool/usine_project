from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Company, Product, Partner, StaffMember, News, Order, Contact, Media, Document, Banner

# ---------------------------
# core/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Company, Product, Partner, StaffMember, News, Order, Contact, Media, Document, Banner

# ---------------------------
# Vue d'accueil
# ---------------------------
def home(request):
    sdn_company = Company.objects.filter(company_type="SDN").first()
    uac_company = Company.objects.filter(company_type="UAC").first()

    context = {
        'banners': Banner.objects.all(),
        'products': Product.objects.filter(available=True),
        'partners': Partner.objects.all(),
        'staff_members': StaffMember.objects.all(),
        'news': News.objects.order_by('-published_at')[:5],
        "products_sdn": Product.objects.filter(company=sdn_company) if sdn_company else [],
        "products_uac": Product.objects.filter(company=uac_company) if uac_company else [],
    }
    return render(request, 'core/home.html', context)

# ---------------------------
# Vue "À propos de nous"
# ---------------------------
# core/views.py

from django.shortcuts import render
from .models import Product, StaffMember, Testimonial


def about_view(request):
    # Produits phares
    flagship_products = Product.objects.filter(is_flagship=True)[:2]

    # Membres de l'équipe
    staff_members = StaffMember.objects.all()
    print(staff_members.values('name', 'position', 'bio'))
    # Témoignages des clients
    testimonials = Testimonial.objects.all()

    context = {
        'flagship_products': flagship_products,
        'staff_members': staff_members,
        'testimonials': testimonials,
    }
    return render(request, "core/about.html", context)


# ---------------------------
# Vue de Contact
# ---------------------------
def contact_view(request):
    return render(request, "core/contact.html")

def legal_mentions_view(request):
    return render(request, "core/mentions_legales.html")


# ---------------------------
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News

# ---------------------------
# Vues pour les Actualités
# ---------------------------
class NewsListView(ListView):
    model = News
    template_name = "core/news_list.html"
    context_object_name = "news"

class NewsDetailView(DetailView):
    model = News
    template_name = "core/news_detail.html"
    context_object_name = "news_item"



# ---------------------------
# Vues pour les Sociétés
# ---------------------------
class CompanyListView(ListView):
    model = Company
    template_name = "core/company_list.html"
    context_object_name = "companies"

class CompanyDetailView(DetailView):
    model = Company
    template_name = "core/company_detail.html"
    context_object_name = "company"

# ---------------------------
# Vues pour les Produits
# ---------------------------
class ProductListView(ListView):
    model = Product
    template_name = "core/products.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "core/product_detail.html"
    context_object_name = "product"

# ---------------------------
# Vues pour les Actualités
# ---------------------------

# ---------------------------
# Vue pour la création d'une commande
# ---------------------------
class OrderCreateView(CreateView):
    model = Order
    template_name = "core/order_form.html"
    fields = ["product", "customer_name", "customer_email", "quantity"]
    success_url = reverse_lazy("order_success")

# ---------------------------
# Vue pour le formulaire de contact
# ---------------------------
class ContactCreateView(CreateView):
    model = Contact
    template_name = "core/contact.html"
    fields = ["name", "email", "phone", "message"]
    success_url = reverse_lazy("contact_success")

# ---------------------------
# Vues pour les Médias et Documents
# ---------------------------

class MediaListView(ListView):
    model = Media
    template_name = "core/media_list.html"
    context_object_name = "media"

class DocumentListView(ListView):
    model = Document
    template_name = "core/document_list.html"
    context_object_name = "documents"
