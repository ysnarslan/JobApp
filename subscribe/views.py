from django.shortcuts import render

from subscribe.models import Subscribe


# Create your views here.
def subscribe(request):
    empty_email_error = ""
    if request.POST:
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        print(email)
        if email == "":
            empty_email_error = "No email entered"

        subscribe = Subscribe(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        subscribe.save()

    context = {
        'empty_email_error': empty_email_error,
    }

    return render(request, "subscribe/subscribe.html", context)
