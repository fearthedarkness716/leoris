import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from shop.models import Product

def update_l_product():
    try:
        # Find the product by its old name
        product = Product.objects.get(name='L Detective Figure')
        
        # Update the product details
        product.name = 'L Trinket'
        product.slug = slugify('L Trinket')
        product.description = 'Elegant trinket featuring L\'s iconic symbol from Death Note. Perfect for fans of the mysterious detective.'
        
        # Save the changes
        product.save()
        print("Product updated successfully!")
        
    except Product.DoesNotExist:
        print("Product not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_tanjiro_product():
    try:
        # Find the product by its old name
        product = Product.objects.get(name='Tanjiro Kamado Figure')
        
        # Update the product details
        product.name = 'Tanjiro Kamado Earrings'
        product.slug = slugify('Tanjiro Kamado Earrings')
        product.description = 'Authentic replica of Tanjiro\'s Hanafuda earrings from Demon Slayer. These meticulously crafted accessories feature the iconic design that represents his family\'s heritage.'
        
        # Save the changes
        product.save()
        print("Product updated successfully!")
        
    except Product.DoesNotExist:
        print("Product not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    update_l_product()
    update_tanjiro_product() 