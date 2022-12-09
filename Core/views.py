from django.shortcuts import render,redirect

from Product.models import Category, ProductModel,ProductVersionModel, Tag,ProductStatistic
from django.views.generic import ListView
from .forms import Test_form
from django.db.models import Q

# Create your views here.
class IndexPageView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'
    paginate_by = 8
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['products_latest'] = ProductModel.objects.all().order_by('-id')[:3][::-1]
        
        
        context['jewelary_latest'] = ProductModel.objects.filter(Q(category=8)|Q(category__parent_category_name=8)).order_by('-created_at')[:3]
        context['bags_latest'] = ProductModel.objects.filter(category=3).order_by('-created_at')[:3]
        context['kids_latest'] = ProductModel.objects.filter(category=7).order_by('-created_at')[:3]
        
        context['best_sales_jw'] = ProductStatistic.objects.filter(Q(product_id__category=8)|Q(product_id__category__parent_category_name=8)).order_by('-read_count')[:3][::-1]
        context['best_sales_bg'] = ProductStatistic.objects.filter(product_id__category=3).order_by('-read_count')[:3][::-1]
        context['best_sales_kd'] = ProductStatistic.objects.filter(product_id__category=7).order_by('-read_count')[:3][::-1]
        
        context['top_rateds_jw'] = ProductModel.objects.filter(Q(category=8)|Q(category__parent_category_name=8)).order_by('-rating')[:3][::-1]
        context['top_rateds_bg'] = ProductModel.objects.filter(category=3).order_by('-rating')[:3]
        context['top_rateds_kd'] = ProductModel.objects.filter(category=7).order_by('-rating')[:3][::-1]
        
        context['categories'] = Category.objects.all()
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




def about(requests):
    return render(requests, 'about.html')

def contact(requests):
    form = Test_form()
    if requests.method == "POST":
        form = Test_form(requests.POST)
        if form.is_valid():
            form.save()
            return redirect("/contact/")
    return render(requests, 'contact.html', {"form": form})

def team(requests):
    return render(requests, 'team.html')