import os
import django
from django.core.files import File
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from shop.models import Category, Product

def create_category(name, description):
    slug = slugify(name)
    category, created = Category.objects.get_or_create(
        name=name,
        slug=slug,
        defaults={'description': description}
    )
    return category

def create_product(name, category, price, stock, description, image_path):
    slug = slugify(name)
    product, created = Product.objects.get_or_create(
        name=name,
        slug=slug,
        defaults={
            'category': category,
            'price': price,
            'stock': stock,
            'description': description,
        }
    )
    
    if created and image_path:
        with open(image_path, 'rb') as f:
            product.image.save(os.path.basename(image_path), File(f), save=True)
    
    return product

# Create categories
anime_series = {
    'Demon Slayer': 'Experience the epic world of demon slaying with our collection of Demon Slayer merchandise.',
    'Death Note': 'Dive into the psychological thriller with our Death Note collection.',
    'JoJo\'s Bizarre Adventure': 'Stand proud with our collection from JoJo\'s Bizarre Adventure.',
    'Hunter x Hunter': 'Discover the world of Hunters with our Hunter x Hunter merchandise.',
    'Overlord': 'Rule the world with our collection from Overlord.'
}

for series, desc in anime_series.items():
    create_category(series, desc)

# Create products
products = [
    {
        'name': 'Tanjiro Kamado Earrings',
        'category': 'Demon Slayer',
        'price': 59.99,
        'stock': 10,
        'description': 'Authentic replica of Tanjiro\'s Hanafuda earrings from Demon Slayer. These meticulously crafted accessories feature the iconic design that represents his family\'s heritage.',
        'image': 'media/tanjiro.png'
    },
    {
        'name': 'L Trinket',
        'category': 'Death Note',
        'price': 49.99,
        'stock': 8,
        'description': 'Elegant trinket featuring L\'s iconic symbol from Death Note. Perfect for fans of the mysterious detective.',
        'image': 'media/l.png'
    },
    {
        'name': 'Jotaro Kujo Cap',
        'category': 'JoJo\'s Bizarre Adventure',
        'price': 29.99,
        'stock': 15,
        'description': 'Replica of Jotaro Kujo\'s iconic cap from JoJo\'s Bizarre Adventure. Perfect for cosplay or daily wear.',
        'image': 'media/jotaro_cap.png'
    },
    {
        'name': 'Isaac Netero Figure',
        'category': 'Hunter x Hunter',
        'price': 69.99,
        'stock': 5,
        'description': 'Premium figure of Chairman Netero from Hunter x Hunter. Showcases his powerful stance and incredible detail.',
        'image': 'media/isaac_netero.png'
    },
    {
        'name': 'Ainz Ooal Gown Statue',
        'category': 'Overlord',
        'price': 79.99,
        'stock': 7,
        'description': 'Impressive statue of the Supreme Being Ainz Ooal Gown from Overlord. Features intricate details and magical effects.',
        'image': 'media/ainz_ooal_gown.png'
    }
]

for product in products:
    category = Category.objects.get(name=product['category'])
    create_product(
        name=product['name'],
        category=category,
        price=product['price'],
        stock=product['stock'],
        description=product['description'],
        image_path=product['image']
    )

print("Categories and products have been created successfully!") 