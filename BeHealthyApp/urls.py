from django.urls import re_path
from BeHealthyApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^package/$', views.packageApi),
    re_path(r'^package/([0-9]+)$', views.packageApi),

    re_path(r'^user/$', views.userApi),
    re_path(r'^user/([0-9]+)$', views.userApi),

    re_path(r'^recipe/$', views.recipeApi),
    re_path(r'^recipe/([0-9]+)$', views.recipeApi),

    re_path(r'^feedback/$', views.feedbackApi),
    re_path(r'^feedback/([0-9]+)$', views.feedbackApi),

    re_path(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)