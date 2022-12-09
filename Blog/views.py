from .models import BlogModel, CommentModel
from django.views.generic import ListView, DetailView
# Create your views here.
class BlogView(ListView):
    model = BlogModel
    template_name = 'blog.html'
    context_object_name = 'blogs'
    paginate_by = 1

class BlogDetailsView(DetailView):
    model = BlogModel
    template_name = 'blog-details.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        return context