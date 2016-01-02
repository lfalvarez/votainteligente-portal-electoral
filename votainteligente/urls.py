from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns


admin.autodiscover()
admin.site.site_header = getattr(settings, 'ADMIN_HEADER', 'Vota Inteligente')

urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'votainteligente.views.home', name='home'),
    # url(r'^votainteligente/', include('votainteligente.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('elections.urls')),
    ('^pages/', include('django.contrib.flatpages.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^newsletter/', include('newsletter.urls')),
)


from django.conf import settings
if settings.THEME:
    urlpatterns += patterns('',
        ('^theme/', include('%s.urls' % (settings.THEME)))
        )
