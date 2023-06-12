from django.db import models

# Create your models here.

class Products(models.Model):
    GENDER_CHOICES = [
            ('Men','Men'),
            ('Women','Women'), 
        ]

    product_name              = models.CharField(max_length=100)
    # product_description       = models.TextField(max_length=300)
    product_brand             = models.ForeignKey("Brand", on_delete=models.CASCADE, default=False , null=False)
    product_category          = models.ForeignKey("Category", on_delete=models.CASCADE, default=False , null=False)
    product_gender            = models.CharField(max_length=10,choices=GENDER_CHOICES,default='Men')
    product_sport             = models.ForeignKey("Sport", on_delete=models.CASCADE, default=False , null=False)
    product_type              = models.CharField(max_length=30, null=False)
    product_price             = models.DecimalField(max_digits=8, decimal_places=2, null=False)

    def __str__(self):
        return str(self.product_name)
    
class Category(models.Model):
    category_name             = models.CharField(max_length=50)
    # thumbnail                  = models.ImageField(upload_to='photos/',null=False,blank=False)
    
    def __str__(self):
        return str(self.category_name)
    
    
class Brand(models.Model):
    brand_name                = models.CharField(max_length=50)
    # logo                       = models.ImageField(upload_to='Logos/',null=False,blank=False)
    
    def __str__(self):
        return str(self.brand_name)
    
class Sport(models.Model):
    sport_name                = models.CharField(max_length=30)

    def __str__(self):
        return str(self.sport_name)

class Color(models.Model):
    color_name                = models.CharField(max_length=30)

    def __str__(self):
        return str(self.color_name)

class Size(models.Model):
    size                      = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.size)
# class VariantImages(models.Model):
#     variant_id = 

class Variants(models.Model):
    variant_product           = models.ForeignKey(Products,related_name= 'variants',on_delete=models.CASCADE)
    variant_name              = models.CharField(max_length=100, blank=True)
    size                      = models.ForeignKey(Size, on_delete=models.RESTRICT, default=False, null=False)
    color                     = models.ForeignKey(Color, on_delete=models.RESTRICT, default=False, null=False)
    stock                     = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Concatenate product name, size, and color names
        color_name = self.color.color_name
        print(color_name)
        variant_name = f"{self.variant_product.product_name} {self.size} {color_name}"

        # Assign the concatenated name to the variant_name field
        self.variant_name = variant_name

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.variant_name)