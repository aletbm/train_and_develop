from email import message
from django.shortcuts import redirect, render
from decouple import config
from contact.forms import FormularioContacto
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def contact(request):
    mapbox_access_token = config("MAPBOX_ACCESS_TOKEN")
    if request.method == "POST":
        miForm = FormularioContacto(request.POST)
        if miForm.is_valid():
            data = miForm.cleaned_data
            mensaje = f"{data['name']}'s contact information:\nE-mail: {data['email']}\nCellphone: {data['cell']}\nMessage: {data['mensaje']}"
            try:
                send_mail(
                    data["asunto"],
                    mensaje,
                    config("EMAIL_HOST_USER"),
                    [config("EMAIL_HOST_USER")],
                )
                messages.success(request, "Message sent successfully!.")
                return redirect("/contact/")
            except Exception:
                message.error(request, "The message could not be sent.")
                return redirect("/contact/")
    miForm = FormularioContacto()
    return render(
        request,
        "contact/contact.html",
        {"mapbox_access_token": mapbox_access_token, "miForm": miForm},
    )
