from django.shortcuts import render

# Create your views here.
def Index(request):
    data = {}
    template_name = 'Index.html'
    return render(request,template_name,data) 