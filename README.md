# UrbanFlow_Pothole-Detection🚧

UrbanFlow is a computer vision-based pothole detection and road quality reporting system. It leverages YOLOv8 for real-time pothole detection and provides dedicated dashboards for Users, Corporators, and MNC Road Departments to streamline monitoring, reporting, and resolution of road damage.


## 🚀 Features
- YOLOv8-based pothole detection from uploaded images or video frames
- OTP login via phone number (Twilio)
- Role-based dashboards:
  - **User**: Report potholes with media and location, track status
  - **Corporator**: View reports, approve requests, track progress
  - **MNC**: Oversee multiple zones, generate analytics
- Real-time SMS and email alerts
- MongoDB integration
- Video frame analysis for automated detection

## 📦 Tech Stack
- **Frontend**: HTML, CSS, Javascript, Jquery
- **Backend**: Django
- **Database**: MongoDB
- **Object Detection**: YOLOv8
- **Communication**: Twilio API (SMS, OTP)

## 📁 Folder Structure


UrbanFlow_Pothole-Detection/
├── backend/ # Django project and APIs
├── frontend/ # HTML, CSS, Javascript based UI
├── yolo_model/ # YOLOv8 detection scripts and weights
├── requirements.txt # Python dependencies
├── .env # Environment variables (Twilio, DB config)
├── README.md
├── LICENSE
└── CONTRIBUTING.md





## 🛠️ Setup Instructions

1. Clone the repository  
   
   git clone https://github.com/Sanika-2605/UrbanFlow_Pothole-Detection.git
   cd UrbanFlow_Pothole-Detection


   2. Install backend dependencies
      pip install -r requirements.txt


3. Set up .env file with:

Twilio credentials
MongoDB URI
Django secret key


4. Run the server
   python manage.py runserver
