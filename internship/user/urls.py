from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register-patient/', views.registerPatient, name='register-patient'),
    path('register-doctor/', views.registerDoctor, name='register-doctor'),

    path('dashboard-patient/', views.dashboardPatient, name='dashboard-patinet'),
    path('dashboard-doctor/', views.dashboardDoctor, name='dashboard-doctor'),
    path('login/', views.login_view, name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
