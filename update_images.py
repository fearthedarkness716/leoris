import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from shop.models import Product

def update_product_image(product_name, new_image_path):
    try:
        product = Product.objects.get(name__icontains=product_name)
        with open(new_image_path, 'rb') as f:
            product.image.save(os.path.basename(new_image_path), File(f), save=True)
        print(f"Successfully updated image for {product.name}")
    except Product.DoesNotExist:
        print(f"Product with name containing '{product_name}' not found")
    except Exception as e:
        print(f"Error updating image: {str(e)}")

# Update Isaac Netero's image
update_product_image('Netero', 'media/isaac_netero_2.png')

# Update Ainz's image
update_product_image('Ainz', 'media/ainz_ooal_gown_2.png')

print("Image update process completed") 