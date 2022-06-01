from cProfile import Profile
import imp
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ProfileForm
from .models import profiles


def  profiles_page(request):
    profile = profiles.objects.all()
    return render(request, 'profiles/profiles_page.html', {'profiles': profile})

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(profiles, pk=pk)
    form = ProfileForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 =form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'profiles/present_profile.html', {'form':form})



