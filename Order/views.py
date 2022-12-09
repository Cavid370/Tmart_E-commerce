from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  ListView
from django.db.models import Q
from .models import WishlistModel, CartModel,Cart_item
from django.views.generic import CreateView
from .forms import BillingAddressModelForm, PaymentDetailModelForm
from .models import CheckoutModel
from django.contrib import messages
# Create your views here.
class WishlistView(LoginRequiredMixin,ListView):
    model = WishlistModel
    template_name = 'wishlist.html'
    
    def get_context_data(self, **kwargs):
        context = super(WishlistView, self).get_context_data(**kwargs)
        user_wishlist =  WishlistModel.objects.filter(user_id = self.request.user).all()
        if user_wishlist:
            all_products = user_wishlist
            context['items'] = all_products
        return context

class CartView(LoginRequiredMixin, ListView):
    model = CartModel
    template_name = 'cart.html'
    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        user_card =  CartModel.objects.filter(user_id = self.request.user, is_active = True).all()
        if user_card:
            all_products = user_card
            context['cart_elements'] = all_products
        grand_total = 0
        products = Cart_item.objects.filter(user_id = self.request.user)
        for product in products:
            grand_total += product.total
        context['grand_total'] = grand_total
        return context

class CheckoutView(LoginRequiredMixin, CreateView):
    model = CheckoutModel
    form_class = BillingAddressModelForm
    template_name = 'checkout.html'
    context_object_name = 'check'

    def get(self, request, *args, **kwargs):
        context = {
            'billing': BillingAddressModelForm(),
            'payment': PaymentDetailModelForm()
        }
        return render(request, 'checkout.html', context=context)

    def post(self, request, *args, **kwargs):
        new_billing = BillingAddressModelForm(request.POST)
        new_payment = PaymentDetailModelForm(request.POST)
        if new_billing.is_valid() and new_payment.is_valid():
            new_billing.instance.user_id = request.user
            new_billing.save()
            new_payment.save()
            messages.success(request, 'Thank you for your payment. Your invoice has been sent to your mail.')
            return redirect('checkout')
        context = {
            'billing': new_billing,
            'payment': new_payment,
        }
        return render(request, 'checkout.html', context = context)




