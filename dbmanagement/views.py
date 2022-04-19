from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from . import forms, models


@login_required
def db_upload(request):
    form = forms.DbForm()
    if request.method == 'POST':
        form = forms.DbForm(request.POST, request.FILES)
        if form.is_valid():
            db = form.save(commit=False)
            # set the uploader to the user before saving the model
            db.uploader = request.user
            # now we can save
            db.save()
            return redirect('home2')
    return render(request, 'dbmanagement/db_upload.html', context={'form': form})


@login_required
def home2(request):
    db = models.Db.objects.all()
    return render(request, 'dbmanagement/home2.html', context={'db': db})