from dal import autocomplete

from django.urls import re_path as url

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path

import authentication.views
import blog.views
import dbmanagement.views
from profiles import views as profiles_views
import archives.views
import travel.views
from archives.views import CountryAutocomplete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('profile-photo/upload', authentication.views.upload_profile_photo,
         name='upload_profile_photo'),
    path('home/', blog.views.home, name='home'),
    path('photo/upload/', blog.views.photo_upload, name='photo_upload'),
    path('blog/create', blog.views.blog_and_photo_upload, name='blog_create'),
    path('blog/<int:blog_id>', blog.views.view_blog, name='view_blog'),
    path('home2/', dbmanagement.views.home2, name='home2'),
    path('db/upload/', dbmanagement.views.db_upload, name='db_upload'),
    path('characters/', profiles_views.character_list, name='character-list'),
    path('characters/<int:character_id>/', profiles_views.character_detail, name='character-detail'),
    path('inventaire/', archives.views.inventaire, name='inventaire'),
    path('press/', archives.views.newspaper_list, name='press'),
    path('archive_registration/', archives.views.archive_registration, name='archive_registration'),
    path('documents/<int:document_id>/', archives.views.document_detail, name='document-detail'),
    path('travels/', travel.views.travel_list, name='travel-list'),
    path('travel/<int:travel_id>/', travel.views.travel_detail, name='travel-detail'),
    path('place/<int:place_id>/', travel.views.place_detail, name='place-detail'),
    url(
        r'^country-autocomplete/$',
        CountryAutocomplete.as_view(),
        name='country-autocomplete',
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)