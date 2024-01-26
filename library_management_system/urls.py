from django.contrib import admin
from django.urls import path,include
from core.views import HomeView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('home/<slug:category_slug>/', HomeView.as_view(), name='category_wise_post'),
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('transactions.urls')),
    path('books/', include('book.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
] 
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)