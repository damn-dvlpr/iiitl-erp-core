from django.shortcuts import render

# Create your views here.
def login(request):
    my_dict={"insertMe":"Hello Boy"}
    return render(request, 'erpapp/ModuleRegistration/index.html', context=my_dict)