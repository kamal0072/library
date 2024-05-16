from django.contrib import admin
from django.urls import path
from book import views
from django.conf.urls.static import static
from django.conf import settings
from library.settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_ROOT,MEDIA_URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', views.show_book, name='books'),
    path('delete/<int:pk>', views.delete_book, name="deletebook"),
    path('upload/', views.upload, name="uploadbook"),
    path('update/<int:id>', views.update_book, name="updatebook"),
]
if settings.DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
