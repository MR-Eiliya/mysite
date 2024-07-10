from django.http import HttpResponse


def index_view(request):
    return HttpResponse('<h1 style="color:green;">This is home page</h1>')

def about_view(request):
    return HttpResponse('<h1 style="color:green;">This is about us</h1>')

def contact_view(request):
    return HttpResponse('<h1 style="color:green;">This is contact us</h1>')


