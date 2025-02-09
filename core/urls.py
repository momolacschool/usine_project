from django.urls import path
from .views import *
urlpatterns = [
    # Pages statiques
    path("", home, name="home"),
    path("about/", about_view, name="about"),
    path("contact/", contact_view, name="contact"),
    path("legal-mentions/", legal_mentions_view, name="legal_mentions"),

    # Sociétés
    path("companies/", CompanyListView.as_view(), name="company_list"),
    path("companies/<int:pk>/", CompanyDetailView.as_view(), name="company_detail"),

    # Produits
    path("products/", ProductListView.as_view(), name="products"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),

    # Actualités
    path("actualites/", NewsListView.as_view(), name="news_list"),
    path("actualites/<int:pk>/", NewsDetailView.as_view(), name="news_detail"),

    # Commandes
    path("order/new/", OrderCreateView.as_view(), name="order_create"),

    # Formulaire de contact
    path("contact-form/", ContactCreateView.as_view(), name="contact_form"),

    # Médias et Documents
    path('media/', MediaListView.as_view(), name='media_list'),
    path("documents/", DocumentListView.as_view(), name="document_list"),

]
