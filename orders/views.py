from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItem
from .tasks import order_created
from django.db import transaction

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    order = form.save(commit=False)
                    if cart.coupon:
                        order.coupon = cart.coupon
                        order.discount = cart.coupon.discount
                    order.save()
                    for item in cart:
                        OrderItem.objects.create(
                            order=order,
                            product=item['product'],
                            price=item['price'],
                            quantity=item['quantity'],
                        )
                    cart.clear()
                    request.session['order_id'] = order.id
                    order_created(order.id)
                return redirect('payment:process')
            except Exception as e:
                # Handle any errors that occur during order creation
                print(f"Error creating order: {e}")
                return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
        else:
            return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
    else:
        form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})
