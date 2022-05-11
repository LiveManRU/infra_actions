from django import urls
from django.contrib import admin

urlpatterns = [
    urls.path('', urls.include('infra_app.urls', namespace='infra_app')),
    urls.path('admin/', admin.site.urls),
]
