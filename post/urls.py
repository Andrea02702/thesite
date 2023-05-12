


from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import PostDetail ,foto


urlpatterns = [
    path('home',views.jhome, name='home'),
    path('post/<int:pk>/',PostDetail.as_view(), name='img'),
    path('atrezzatura/', views.atrezzatura, name='atrezzatura'),
    path('chi_sono/', views.chi_sono, name='chi_sono'),
    path('galleria/',views.galleria, name='galleria'),
    path('allpost/',views.allpost, name='allpost'),
    path('foto/<int:pk>/',foto.as_view(), name='image'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )