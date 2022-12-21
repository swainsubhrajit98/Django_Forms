from django.shortcuts import render
from App.forms import *
# Create your views here.
def Django_Forms(request):
    form=NameForm()
    d={'form':form}
    
    if request.method == "POST":
        form_data = NameForm(request.POST)
        if form_data.is_valid():
            name = form_data.cleaned_data['name']
            age = form_data.cleaned_data['age']
            email = form_data.cleaned_data['email']
            gender = form_data.cleaned_data['gender']
            course = form_data.cleaned_data['course']
            mobile = form_data.cleaned_data['mobile']
            address = form_data.cleaned_data['address']
            D = {'n': name, 'a': age, 'e': email,
                 'g': gender, 'c': course, 'm': mobile, 'ad': address}
            return render(request, 'Form_Data.html', D)
    return render(request,'Django_Forms.html',d)