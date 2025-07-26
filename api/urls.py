from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name='home'),
    
    # HTML page views
    # path('otp/', views.otp_view, name='otp'),
    path('', views.index, name='index'),
    path('request-otp/', views.request_otp_page, name='request_otp'),
    path('verify-otp/', views.verify_otp_page, name='verify_otp'),
    

    path('citizen-dashboard/', views.citizen_dashboard, name='citizen_dashboard'),
    path('logout/', views.logout_view, name='logout'),

    path('corporator-login/', views.corporator_login_view, name='corporator-login'),
    path('mnc-login/', views.mnc_login_view, name='mnc-login'),
    
    path('corporator-dashboard/', views.corporator_dashboard, name='corporator-dashboard'),
    path('mnc-dashboard/', views.mnc_dashboard, name='mnc-dashboard'),

    path('submit-report/', views.submit_report, name='submit_report'),
    

]








