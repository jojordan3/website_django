from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from wagtail.images.views.serve import ServeView
from wagtail.contrib.sitemaps.views import sitemap

from search import views as search_views

from wagtail_feeds.feeds import BasicFeed, ExtendedFeed

admin.autodiscover()


urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path(settings.ADMIN_URL, admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),

    # User management
    path("users/", include("website_django.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),

    path('search/', search_views.search, name='search'),
    path('documents/', include(wagtaildocs_urls)),

    path('sitemap.xml', sitemap),
    path('blog/feed/basic/', BasicFeed(), name='basic_feed'),
    path('blog/feed/extended/', ExtendedFeed(), name='extended_feed'),

    path('privacy-policy/', TemplateView.as_view(template_name='pages/privacy.html'), name='privacy'),
    path('terms-of-service/', TemplateView.as_view(template_name='pages/terms.html'), name='terms'),

    path(
        r'^images/([^/]*)/(\d*)/([^/]*)/[^/]*$',
        ServeView.as_view(), name='wagtailimages_serve'
    ),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    path('', include(wagtail_urls)),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url('favicon.ico',
            RedirectView.as_view(
                url=settings.STATIC_URL + 'favicon.ico', permanent=True)
            ),
    ]

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
