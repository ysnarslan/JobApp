from django.shortcuts import render
from uploadpp.forms import UploadPPForm, UploadFileForm


# Create your views here.
def upload_pp(request):
    upload_form = UploadPPForm()
    if request.method == 'POST':
        upload_form = UploadPPForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            saved_object = upload_form.instance
            context = {
                'upload_form': upload_form,
                'saved_object': saved_object,
            }
            return render(request, 'uploadpp/add_image.html', context)
    else:
        upload_form = UploadPPForm()

    context = {
        'upload_form': upload_form,
    }
    return render(request, "uploadpp/add_image.html", context=context)


def upload_file(request):
    upload_form = UploadFileForm()
    if request.method == 'POST':
        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            saved_object = upload_form.instance
            context = {
                'upload_form': upload_form,
                'saved_object': saved_object,
            }
            return render(request, 'uploadpp/add_file.html', context)
    else:
        upload_form = UploadFileForm()

    context = {
        'upload_form': upload_form,
    }
    return render(request, "uploadpp/add_file.html", context=context)
