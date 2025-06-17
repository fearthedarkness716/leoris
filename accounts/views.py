from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm, UserUpdateForm
from orders.models import Order

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    next_page = 'shop:product_list'  # Перенаправление на главную страницу после входа

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def profile_view(request):
    orders = Order.objects.all().order_by('-created')
    return render(request, 'accounts/profile.html', {
        'orders': orders
    }) 