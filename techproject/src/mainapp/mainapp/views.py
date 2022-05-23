from django.http import HttpResponse


def home(request):
    print(request.user)
    return HttpResponse("<h1>Welcome user!</h1>")
