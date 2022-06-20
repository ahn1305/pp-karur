from django.contrib.auth.signals import user_logged_out,user_logged_in
from django.dispatch import receiver
from django.contrib import messages

# @receiver(user_logged_in)
# def on_user_logged_in(sender,request,**kwargs):
#     messages.add_message(request,messages.INFO,f'You are logged in successfully {request.user}')

@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, 'you are logged out.')
