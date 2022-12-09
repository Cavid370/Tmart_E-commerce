import datetime 
from Tmart.celery import app
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from .models import SubscriberEmail
from Product.models import ProductModel

@app.task(name = "send_mail")
def send_mail_task():
    
    print("Mail sending.......")
    subscribers = SubscriberEmail.objects.all()    
    for subscriber in subscribers:   
        print("send")   
        subject = 'welcome to Celery world'
        products = ProductModel.objects.all().order_by('-rating')[:3]
        message =  render_to_string('email/email-subscribers.html', {
                "products" : products
            })

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [subscriber.email]
        send_mail(subject=subject, message="", from_email=email_from, recipient_list=recipient_list, html_message=message)
    return "Mail has been sent........"


#   redis-server
#   celery -A Tmart beat -l info
#   celery -A Tmart worker --pool=solo -l info