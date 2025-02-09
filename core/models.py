from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# ---------------------------
# Modèle pour les Types d'Entreprises (SDN ou UAC)
# ---------------------------
class CompanyType(models.TextChoices):
    SDN = "SDN", "Société Diarra Négoce"
    UAC = "UAC", "UAC"

# ---------------------------
# Modèle pour les Sociétés/Entreprises
# ---------------------------
class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='companies/logos/', blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    company_type = models.CharField(max_length=3, choices=CompanyType.choices, default=CompanyType.SDN)  # Identification SDN/UAC
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_company_type_display()})"

# ---------------------------
# Modèle pour les Catégories de Produits
# ---------------------------
class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# ---------------------------
# Modèle pour les Produits
# ---------------------------
class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_flagship = models.BooleanField(default=False)  # ✅ Nouveau champ pour les produits phares

    def __str__(self):
        return f"{self.name} ({self.company.name})"

    @property
    def is_in_stock(self):
        return self.stock_quantity > 0

# ---------------------------
# Modèle pour les Commandes
# ---------------------------
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    quantity = models.PositiveIntegerField()
    proforma_invoice = models.FileField(upload_to='invoices/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'En attente'),
        ('processed', 'Traitée'),
        ('shipped', 'Expédiée'),
        ('completed', 'Terminée'),
    ], default='pending')

    def __str__(self):
        return f"Commande de {self.customer_name} pour {self.product.name}"

# ---------------------------
# Modèle pour les Contacts
# ---------------------------
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.name}"

# ---------------------------
# Modèle pour les Documents Utiles
# ---------------------------
class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ---------------------------
# Modèle pour les Partenaires
# ---------------------------
class Partner(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='partners/logos/')
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# ---------------------------
# Modèle pour les Membres du Staff
# ---------------------------
class StaffMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='staff/')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# ---------------------------
# Modèle pour les bannières de la page d'accueil
# ---------------------------
class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ---------------------------
# Modèle pour les Actualités (News)
# ---------------------------
class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)  # Vérifie que ce champ est bien présent
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.IntegerField(default=0)
    class Meta:
        ordering = ['-published_at']
        verbose_name = "Actualité"
        verbose_name_plural = "Actualités"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# ---------------------------
# Modèle pour la Médiathèque (Images & Vidéos)
# ---------------------------
class Media(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Vidéo'),
    )

    title = models.CharField(max_length=255)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='media_files/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = "Média"
        verbose_name_plural = "Médiathèque"

    def __str__(self):
        return f"{self.title} ({self.media_type})"






class Testimonial(models.Model):
    client_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)
    feedback = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.client_name
