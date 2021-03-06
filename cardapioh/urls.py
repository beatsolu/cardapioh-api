"""cardapioh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.debug import default_urlconf
from django.views.generic import TemplateView

from rest_framework.routers import SimpleRouter
from rest_framework.schemas import get_schema_view

from . import __version__
from .apps.accounts import views as accounts
from .apps.places   import views as places

routes = SimpleRouter(trailing_slash=True)

routes.register('users', accounts.UserModelViewSet)
routes.register('items', places.ItemListAPIView)
routes.register('places', places.PlaceListAPIView)
routes.register('sessions', places.SessionListAPIView)

api_patterns = [
    path('api/', include(routes.urls)),
]

admin.site.site_title = 'Cardapioh'
admin.site.site_header = 'Cardapioh'
admin.site.index_title = 'Administração'
admin.site.site_url = 'http://cardapioh.com.br'

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
]

urlpatterns += api_patterns

if settings.DEBUG:
    urlpatterns += [
        path('', default_urlconf),
        path('docs/', TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url': 'open-api-schema'}
        ), name='docs'),
        path('schema/', get_schema_view(
            title="Cardapioh API",
            description="Reference documentation for the Cardapioh API.",
            version=__version__,
            patterns=api_patterns,
        ), name='open-api-schema'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
