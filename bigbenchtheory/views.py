from django.shortcuts import render
from bigbenchtheory.forms import AddFood
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.template import RequestContext

def sub(request):
    error = False

    if request.method == 'POST':
        form = AddFood(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            return HttpResponse('<p>Thanks for being a nigga!</p>')
            #HttpResponseRedirect('/thanks/')
        else:
            error = True
    else:
        form = AddFood()
    return render(request, 'test_foods.html', \
                context_instance=RequestContext(request, {'form': form, \
                    'error': error}))