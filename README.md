This is a web application written in Django.

Steps to install:
 - install necessary tools like Django, pip, python, opencv, boto etc.,
 - clone into this repository
 - setup AWS credentials in views.py or you can just assignn a role
 - MAKE SURE YOU PUT THE REGION OF THE AWS BUCKET IN THE upload_to_s3 FUNCTION
 - if you plan on running the application in an EC2 instance run with the command python manage.py runserver private_ip_of_instance:8000
 - visit the URL http://public_ip_ec2_instance:8000 and upload a video file
 - once the video is uploaded you will be given an S3 bucket URL where you can download the background image extracted from the video
 - Thank you
