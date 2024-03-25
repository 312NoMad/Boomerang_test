from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


from utils.swagger import schema_view

from djangoProject import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include([
        path('v1/', include([
            path('product/', include('apps.product.urls')),
            path('user/', include('apps.user.urls')),
            path('order/', include('apps.order.urls'))
        ]))
    ]))
]

if settings.DEBUG:
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')

    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
