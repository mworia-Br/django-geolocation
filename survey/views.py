from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from forms import DataForm
from models import Data

def data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            messages.success(request, "Added successfully")
            # ...
            # redirect to a new URL:
            return redirect('datasuccess')
    else:
        form = DataForm()

    return render(request, 'data.html', {'form': form})
