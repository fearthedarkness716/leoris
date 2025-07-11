from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import OrderItem, Order
from .forms import OrderForm, OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            if len(cart) == 0:
                form.add_error(None, 'Ваша корзина пуста. Добавьте товары для оформления заказа.')
            else:
                order = form.save(commit=False)
                if request.user.is_authenticated:
                    order.user = request.user
                order.save()
                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity']
                    )
                cart.clear()
                return redirect('accounts:profile')
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


def order_completed(request):
    order_id = request.session.get('order_id')
    if not order_id:
        return redirect('shop:product_list')
    
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/created.html', {'order': order})


def profile_view(request):
    # Get all orders for the current user, только с товарами
    orders = Order.objects.filter(user=request.user).order_by('-created')
    orders = [order for order in orders if order.items.exists()]
    return render(request, 'orders/profile.html', {
        'user': request.user,
        'orders': orders
    })

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})

# Временно удаляем функцию admin_order_pdf
# @staff_member_required
# def admin_order_pdf(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     html = render_to_string('orders/order/pdf.html', {'order': order})
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
#     weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')])
#     return response

def order_pay(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.paid = True
        order.save()
        return redirect('orders:order_detail', order_id=order.id)
    return render(request, 'orders/order/pay.html', {'order': order})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order/detail.html', {'order': order})
