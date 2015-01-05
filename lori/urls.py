from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin

# urlpatterns = i18n_patterns('', # prepends with /en-us/
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),

    url(r'^', include('cms.urls')),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
