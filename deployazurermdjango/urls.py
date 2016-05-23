from django.views.generic import TemplateView, RedirectView
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'azure_deploy.views.index', name='home'),

    # authentication url
    url(r'^login/complete/$', 'azure_ad_auth.views.complete', name='complete'),
    # url(r'^login/complete/success/$',
    #     TemplateView.as_view(template_name='registration/login_success.html'),
    #     name='success'),
    url(r'^login/$', 'azure_ad_auth.views.auth', name="login"),
    url(r'^logout/$', 'azure_deploy.views.logout_view', name="logout"),
    url(r'^login/complete/success/$',
        RedirectView.as_view(pattern_name='subs', permanent=False), name="success"),
    url(r'^login/complete/failure/$',
        TemplateView.as_view(template_name='registration/login_failure.html'),
        name='failure'),
    url(r'^logout/complete$',
        TemplateView.as_view(template_name='registration/logged_out.html'),
        name='logout_complete'),

    # azure urls
    url(r'^subscriptions/$', 'azure_deploy.views.subs', name='subs'),

    url(r'^admin/', include(admin.site.urls)),
)
