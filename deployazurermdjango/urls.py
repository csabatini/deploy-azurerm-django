from django.views.generic import TemplateView, RedirectView
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'azure_deploy.views.index', name='home'),

    # authentication url
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^login/complete/$', 'azure_ad_auth.views.complete', name='azure_complete'),
    # url(r'^login/complete/success/$',
    #     TemplateView.as_view(template_name='registration/login_success.html'),
    #     name='success'),
    url(r'^login/complete/success/$', 'azure_deploy.views.success', name="success"),
    url(r'^login/complete/failure/$',
        TemplateView.as_view(template_name='auth/login_failure.html'),
        name='failure'),

    # azure urls
    url(r'^subscriptions/$', 'azure_deploy.views.subs', name='subs'),

    url(r'^admin/', include(admin.site.urls)),
)
