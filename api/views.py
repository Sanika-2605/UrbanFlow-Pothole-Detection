from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .notification import send_sms
from datetime import datetime
import random
import string
from .utils.twilio_utils import send_sms
from django.contrib.auth import logout
from mongoengine import connect
from .models import PotholeReport
from django.http import HttpResponse
from django.utils import timezone
from collections import Counter
 
connect(db='urbanflow', host='localhost', port=27017)

def index(request):
    return render(request, 'api/index.html')

def home(request):
    return render(request, 'api/home.html')

def logout_view(request):
    logout(request)  # This clears the session
    return render(request, 'api/index.html')  # 'index' should be the name of your index URL

def corporator_login_view(request):
    return render(request, 'api/corporator.html')

def mnc_login_view(request):
    return render(request, 'api/mnc.html')



def corporator_dashboard(request):
    reports = PotholeReport.objects.all().order_by('-submitted_at')
    return render(request, 'api/corporator2.html', {'reports': reports})

def mnc_dashboard(request):
    reports = PotholeReport.objects.all().order_by('-submitted_at')
    return render(request, 'api/mnc2.html', {'reports': reports})


@csrf_exempt
def request_otp_page(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        otp = ''.join(random.choices(string.digits, k=6))
        request.session[f'otp_{phone}'] = otp
        request.session['phone'] = phone
        print(f"OTP sent to {phone}: {otp}")
        send_sms(phone, f"Your OTP is {otp}")
        return render(request,'api/verify_otp.html', {'phone': phone})
    return render(request, 'api/request_otp.html')
    

@csrf_exempt
def verify_otp_page(request):    
    if request.method == 'POST':
        return redirect('/api/citizen-dashboard')
    return render(request, 'api/verify_otp.html')


def citizen_dashboard(request):
    # if not request.session.get('is_verified'):
    #     return redirect('/api/request-otp/')  # redirect back if not verified

    return render(request, 'api/citizen2.html')



def mnc_dashboard(request):
    reports = PotholeReport.objects()

    # Count total reports
    total_reports = reports.count()

    # Count unique users (by phone number)
    unique_users = len(set(r.phone for r in reports))

    # Count resolved ones (assuming you have a 'status' field)
    resolved_count = reports.filter(status="Resolved").count()

    # Resolution rate
    resolution_rate = f"{(resolved_count / total_reports * 100):.2f}%" if total_reports else "0%"
    
        # Chart: Severity counts
    severity_counter = Counter(r.severity for r in reports)
    severity_chart_data = [severity_counter.get(level, 0) for level in ["High", "Medium", "Low"]]

    # Chart: Area counts
    area_counter = Counter(r.location for r in reports)
    area_labels = list(area_counter.keys())
    area_values = list(area_counter.values())

    severity_filter = request.GET.get('severity')
    area_filter = request.GET.get('area')

    reports = PotholeReport.objects
    if severity_filter and severity_filter != 'All':
        reports = reports.filter(severity=severity_filter)
    if area_filter and area_filter != 'All':
        reports = reports.filter(area=area_filter)

    resolved_reports = reports.filter(resolved=True)
    pending_reports = reports.filter(resolved=False)

    context = {
        'reports': reports,
        'resolved_reports': resolved_reports,
        'pending_reports': pending_reports,
        'total_reports': total_reports,
        'unique_users': unique_users,   
        'resolved_count': resolved_count,
        'resolution_rate': resolution_rate, 
        'severity_chart_data': severity_chart_data,
        'area_labels': area_labels,
        'area_values': area_values,
    }
    return render(request, 'api/mnc2.html', context)



def corporator_dashboard(request):
    reports = PotholeReport.objects()
    total = reports.count()
    pending = reports.filter(status__in=['Detected', 'In Progress']).count()
    resolved = reports.filter(status='Resolved').count()

    context = {
        'reports': reports,
        'total': total,
        'pending': pending,
        'resolved': resolved,
    }
    return render(request, 'api/corporator2.html', context)


# @csrf_exempt
# def submit_report(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         location = request.POST.get('location')
#         severity = request.POST.get('severity')
#         landmark = request.POST.get('landmark')
#         image_file = request.FILES.get('image')

#         report = PotholeReport(
#             name=name,
#             phone=phone,
#             location=location,
#             severity=severity,
#             landmark=landmark,
#             submitted_at=timezone.now()
#         )

#         if image_file:
#             report.image.put(image_file, content_type=image_file.content_type)

#         report.save()
#         return render(request, 'api/citizen2.html', {'success_message': 'Report submitted ✅'})
    
#     return render(request, 'api/citizen2.html', {'error_message': 'Form not submitted'})


@csrf_exempt
def submit_report(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        severity = request.POST.get('severity')
        landmark = request.POST.get('landmark')
        image_file = request.FILES.get('image')

        print(f"Received: {name}, {phone}, {location}, {severity}, {landmark}")

        try:
            report = PotholeReport(
                name=name,
                phone=phone,
                location=location,
                severity=severity,
                landmark=landmark,
                submitted_at=timezone.now()
            )

            if image_file:
                report.image.put(image_file, content_type=image_file.content_type)

            report.save()
            print("✅ Report saved to MongoDB")
            return render(request, 'api/citizen2.html', {'success_message': '✅ Report submitted successfully'})
        except Exception as e:
            print("❌ Error saving report:", e)
            return render(request, 'api/citizen2.html', {'error_message': f'Error: {str(e)}'})

    return render(request, 'api/citizen2.html', {'error_message': 'Invalid form submission'})





# @api_view(['POST'])
# def submit_report(request):
#     phone = request.data.get('phone')
#     user = get_object_or_404(User, phone=phone, otp_verified=True)
#     image = request.FILES.get('image')
#     latitude = float(request.data.get('latitude'))
#     longitude = float(request.data.get('longitude'))
#     location = request.data.get('location', '')
#     saved_path = default_storage.save(f"pothole_images/{image.name}", image)
#     detection = detect_pothole(saved_path)

#     report = PotholeReport.objects.create(
#         user=user,
#         image=saved_path,
#         location=location,
#         latitude=latitude,
#         longitude=longitude,
#         width=detection['width'],
#         height=detection['height'],
#         depth=detection['depth'],
#         severity=detection['severity']
#     )

#     send_sms(user.phone, f"Thank you {user.name}, your pothole report has been submitted. Severity: {detection['severity']}")
#     email_subject = f"New Pothole Report - Severity: {detection['severity'].capitalize()}"
#     email_body = f"Location: {location}\nLat: {latitude}, Long: {longitude}\nSeverity: {detection['severity']}\nReported by: {user.name}, Phone: {user.phone}\nDimensions: {detection['width']}x{detection['height']}x{detection['depth']}"
#     send_alert_email("sanikapb2316@gmail.com", email_subject, email_body)
#     send_alert_email("sanika.brahmankar24@vit.edu", email_subject, email_body)

#     return Response({'message': 'Pothole report submitted', 'severity': detection['severity']})

# @api_view(['POST'])
# def list_reports(request):
#     reports = PotholeReport.objects.all().order_by('-submitted_at')
#     data = [
#         {
#             "location": report.location,
#             "latitude": report.latitude,
#             "longitude": report.longitude,
#             "severity": report.severity,
#             "submitted_at": report.submitted_at
#         }
#         for report in reports
#     ]
#     return Response(data)