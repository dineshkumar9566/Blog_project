from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class MyModel(models.Model):
    # Choice field with three categories
    CATEGORY_CHOICES = [
        ('A', 'Category A'),
        ('B', 'Category B'),
        ('C', 'Category C'),
    ]
    
    # Basic fields
    name = models.CharField(
        max_length=100, 
        help_text="Enter the name of the item. E.g., 'Premium Coffee Beans'"
    )  # Example: 'Premium Coffee Beans'
    
    description = models.TextField(
        help_text="Enter a detailed description. E.g., 'High-quality Arabica beans from Colombia...'"
    )  # Example: 'High-quality Arabica beans from Colombia...'
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the item was created."
    )  # Example: '2024-06-15 12:34:56' (auto set)
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when the item was last updated."
    )  # Example: '2024-06-15 12:34:56' (auto set)
    
    is_active = models.BooleanField(
        default=True,
        help_text="Is the item currently active? E.g., True"
    )  # Example: True
    
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        help_text="Enter the price of the item. E.g., '19.99'"
    )  # Example: 19.99
    
    quantity = models.IntegerField(
        help_text="Enter the quantity in stock. E.g., '100'"
    )  # Example: 100
    
    category = models.CharField(
        max_length=1, choices=CATEGORY_CHOICES,
        help_text="Select a category for the item. E.g., 'A'"
    )  # Example: 'A'
    
    email = models.EmailField(
        help_text="Enter a contact email. E.g., 'info@example.com'"
    )  # Example: 'info@example.com'
    
    website = models.URLField(
        help_text="Enter the website URL. E.g., 'https://www.example.com'"
    )  # Example: 'https://www.example.com'
    
    image = models.ImageField(
        upload_to='images/',
        help_text="Upload an image of the item."
    )  # Example: 'images/item_image.jpg'
    
    # Fields with attributes
    slug = models.SlugField(
        unique=True,
        help_text="Enter a unique slug for the item. E.g., 'premium-coffee-beans'"
    )  # Example: 'premium-coffee-beans'
    
    ip_address = models.GenericIPAddressField(
        protocol='both', unpack_ipv4=False,
        help_text="Enter an IP address. E.g., '192.168.1.1' or '2001:0db8:85a3:0000:0000:8a2e:0370:7334'"
    )  # Example: '192.168.1.1' or '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
    
    rating = models.FloatField(
        validators=[
            MinValueValidator(0.0), 
            MaxValueValidator(5.0)
        ],
        help_text="Enter a rating between 0.0 and 5.0. E.g., '4.5'"
    )  # Example: 4.5
    
    tags = models.JSONField(
        default=list, blank=True,
        help_text="Enter a list of tags in JSON format. E.g., ['coffee', 'arabica', 'premium']"
    )  # Example: ['coffee', 'arabica', 'premium']
    
    notes = models.TextField(
        null=True, blank=True,
        help_text="Enter any additional notes. E.g., 'Limited edition product'"
    )  # Example: 'Limited edition product'
    
    def __str__(self):
        return self.name

class RelatedModel(models.Model):
    # ForeignKey field example
    my_model_fk = models.ForeignKey(
        MyModel, 
        on_delete=models.CASCADE,
        related_name='related_models',
        help_text="ForeignKey relationship to MyModel. Deletes related records if MyModel instance is deleted."
    )
    
    # OneToOneField example
    my_model_o2o = models.OneToOneField(
        MyModel,
        on_delete=models.CASCADE,
        related_name='related_model',
        help_text="OneToOne relationship to MyModel. Deletes related record if MyModel instance is deleted."
    )
    
    # ManyToManyField example
    my_model_m2m = models.ManyToManyField(
        MyModel,
        related_name='related_models_m2m',
        help_text="ManyToMany relationship to MyModel."
    )
    
    # Additional fields for RelatedModel
    title = models.CharField(
        max_length=200, 
        help_text="Enter the title of the related item. E.g., 'Related Item Title'"
    )  # Example: 'Related Item Title'
    
    description = models.TextField(
        help_text="Enter a description for the related item. E.g., 'Detailed description of the related item...'"
    )  # Example: 'Detailed description of the related item...'
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the related item was created."
    )  # Example: '2024-06-15 12:34:56' (auto set)
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when the related item was last updated."
    )  # Example: '2024-06-15 12:34:56' (auto set)
    
    def __str__(self):
        return self.title