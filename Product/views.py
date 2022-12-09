from django.contrib import messages
from django.shortcuts import render , redirect
from django.urls import reverse
from requests import request
from django.contrib.auth.decorators import login_required
from Order.models import WishlistModel
from .forms import ReviewModelForm
from .models import ProductModel, ProductStatistic, ReviewsModel, Tag,ProductVersionModel
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.

class ProductDetailView(DetailView, CreateView):
    model = ProductModel
    form_class = ReviewModelForm
    template_name = 'product-details.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        product_stats = ProductStatistic.objects.get(product_id=self.object)
        product_stats.read_count += 1
        product_stats.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = ProductModel.objects.get(slug = self.kwargs.get('slug'))
        context['product_version'] = ProductVersionModel.objects.get(product_id__slug = self.kwargs.get('slug'))
        print(context['product_version'].quantity)
        context['reviews'] = ReviewsModel.objects.filter(product_id__slug = self.kwargs.get('slug')).all()[:3]
        context['review_form'] = ReviewModelForm()
        # ProductModel.objects.filter(tags__id__in=context["product"].tags.values_list("id", flat=True))
        context['related'] = ProductModel.objects.filter(tags__id__in=context["product"].tags.values_list("id", flat=True)).exclude(slug = self.kwargs.get('slug')).all()[:3]
        return context
    def post(self, request, *args, **kwargs):
        new_review = ReviewModelForm(request.POST, request.FILES)
        product = ProductModel.objects.get(slug = kwargs['slug'])
        if new_review.is_valid():
            new_review.instance.product_id = product
            new_review.instance.save()
            messages.success(request, 'Your review added.')
            return redirect(reverse('product_detail', kwargs={'slug': kwargs['slug']}))
        context = {
            'review_form': new_review
        }
        return render(request, 'product-details.html', context = context)
    def form_valid(self, form, *args, **kwargs):
        form.instance.product_id = ProductModel.objects.get(slug = self.kwargs.get('slug'))
        form.instance.save()
        self.object = self.get_object()
        product = ProductStatistic.objects.get(product_id=self.object)
        product.review_count += 1
        product.save()
        return redirect("product_detail", slug = self.kwargs.get('slug'))




# def product(requests):
#     tags = Tag.objects.all()
#     products = ProductModel.objects.all()
#     context = {
#         'products': products,
#         'tags':tags

#     }
#     return render(requests, 'shop.html', context=context)

# def product_detail(requests,slug):
#     product = ProductModel.objects.filter(slug = slug)
#     form = Review_form()
#     if requests.method == "POST":
#         form = Review_form(requests.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(requests,messages.INFO, "Məhsul haqqında rəyiniz qeydə alındı")
#             return redirect("/product/product_detail")
#     return render(requests, 'product-details.html', {"form": form})
def customer_review(requests):
    return render(requests, 'customer-review.html')

class TagPageView(ListView):
    model = ProductModel
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 8
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    def get_queryset(self):
        tag = self.request.GET.get('tag')
        category = self.request.GET.get('category')
        if tag:
            self.queryset = ProductModel.objects.filter(tags__name=tag).all()
        elif category:
            self.queryset = ProductModel.objects.filter(category__category_name=category).all()
        else:
            self.queryset = ProductModel.objects.all()

        return self.queryset

