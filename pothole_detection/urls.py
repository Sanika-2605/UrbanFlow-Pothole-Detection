from django.contrib import admin
from django.urls import path, include
# from api.views import home
from django.conf import settings
from django.conf.urls.static import static
from api import views 
# from api.views import officer_dashboard, detect


urlpatterns = [
    # path('', home),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('api/', include('api.urls')),
    # path('',views.citizen_dashboard, name='citizen_dashboard'), 
    
    # path('', views.corporator_login_view, name='corporator_login'),
    # path('',views.mnc_login_view, name='mnc_login'),

    # path('',views.corporator_dashboard, name='corporator_dashboard'),
    # path('',views.mnc_dashboard, name='mnc_dashboard'),

    # path('submit-report/', views.submit_report, name='submit_report'),
    # path('upload/', api_views.upload_view, name='upload'),
    # path('dashboard/', officer_dashboard, name='officer_dashboard'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









