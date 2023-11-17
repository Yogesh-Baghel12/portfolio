from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs
#sending mails

from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.
def home(request):
    return render(request,'home.html')

def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request,'handleblog.html',context)


def about(request):
    return render(request,'about.html')



def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        from_email=settings.EMAIL_HOST_USER
        from_password=settings.EMAIL_HOST_PASSWORD
        connection=mail.get_connection()
        connection.open()
        email_message=mail.EmailMessage(f'Email from {fname}', f'UserEmail: {femail}\nUserPhoneNumber:{fphoneno}\n\n\n QUERY:{fdesc}',from_email,['yashbaghel613@gmail.com',],connection=connection)
        
        email_client=mail.EmailMessage(f'Yogesh Baghel Response','Thanks For Reaching Out. I will connect you soon\n\nName: Yogesh baghel\n\nContact : 8130135305\n\nEmail:yashhbaghel613@gmail.com',from_email,[femail],connection=connection)
        connection.send_messages([email_message,email_client])
        connection.close()
        
        
        messages.info(request,"Thanks for contact me! we will get back you soon....")
        return redirect('/contact')
        
    return render(request,'contact.html')