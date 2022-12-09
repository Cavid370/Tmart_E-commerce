from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('Core.urls')),
    path('account/', include('User.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/', include('Blog.urls')),
    path('order/', include('Order.urls')),
    path('product/', include('Product.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
)
urlpatterns +=[
    path('api/', include('Product.api.urls')),
    path('api/', include('Order.api.urls')),
    path('api/', include('User.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

urlpatterns += [
    # ... previously added endpoints
    path('openapi/', get_schema_view(
        title="School Service",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




