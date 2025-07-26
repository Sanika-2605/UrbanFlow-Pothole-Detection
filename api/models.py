# from django.db import models

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15, unique=True)
#     otp_verified = models.BooleanField(default=False)

#     # def __str__(self):
#     #     return f"{self.name} - {self.phone}"

# class PotholeReport(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='pothole_images/')
#     location = models.CharField(max_length=255)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     width = models.FloatField()
#     height = models.FloatField()
#     depth = models.FloatField()
#     severity = models.CharField(max_length=10)  # Yellow, Orange, Red
#     submitted_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"Pothole by {self.user.name} at {self.location} - Severity: {self.severity}"



# Create your models here.
# (MongoEngine)

# from mongoengine import Document, StringField, DateTimeField, BooleanField
# import datetime

# class PotholeReport(Document):
#     reporter_name = StringField(required=True)
#     area = StringField(required=True)
#     severity = StringField(choices=['low', 'medium', 'high'], required=True)
#     status = StringField(choices=['Detected', 'In Progress', 'Resolved'], default='Detected')
#     date_reported = DateTimeField(default=datetime.datetime.now)
#     resolved = BooleanField(default=False)
    

#      # Add metadata
#     meta = {
#         'collection': 'urbanflow',  # MongoDB collection name
#         'ordering': ['-submitted_at'],    # Default ordering by newest first
#         'indexes': [
#             'area',
#             'severity', 
#             'status',
            
#         ]
#     }
    
    # def __str__(self):
    #     return f"Pothole Report: {self.area} ({self.severity}) by {self.reporter_name}"
    
    # def save(self, *args, **kwargs):
    #     """Override save to update resolved status based on status field"""
    #     if self.status == 'Resolved':
    #         self.resolved = True
    #     else:
    #         self.resolved = False
    #     return super().save(*args, **kwargs)




from mongoengine import Document, StringField, DateTimeField, FileField
import datetime 

class PotholeReport(Document):
    name = StringField(required=True)
    phone = StringField(required=True)
    location = StringField(required=True)
    severity = StringField(required=True)
    landmark = StringField()
    submitted_at = DateTimeField()
    image = FileField()
    submitted_at = DateTimeField()
    status = StringField(choices=['Detected', 'In Progress', 'Resolved'], default='Detected')
    
    reporter_name = StringField()  # used by citizen dashboard
    area = StringField()
    image_url = StringField()
    date_reported = DateTimeField(default=datetime.datetime.now)
    def save(self, *args, **kwargs):
        print("💾 save() called in model")
        return super().save(*args, **kwargs)