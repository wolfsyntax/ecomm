from django.shortcuts import render

# Create your views here.
def e400(request, exception):
    return render(request, "errors/e400.html")

def e403(request, exception):
    return render(request, "errors/e403.html")

def e404(request, exception):
    return render(request, "errors/e404.html")

def e500(request):
    return render(request, "errors/e500.html")

