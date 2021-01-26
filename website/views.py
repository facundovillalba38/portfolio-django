from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
     
     if request.method == 'POST':
          name = request.POST['name']
          email = request.POST['email']
          message = request.POST['message']

          # Send Email
          send_mail(
               'Consulta - '+email, #subject
               '\t\tConsulta: \nNombre: '+name+'\nEmail: '+email+'\nMensaje: '+message, #message
               email, #from email
               ['danielvillalba.arte@gmail.com'], #to email
          )

          context = {
               'message_name' : name,
          }

          return render(request, 'success.html', context)
     else:
          return render(request, 'index.html', {})

def success(request):
     return render(request, 'success.html', {})
     
     

     
