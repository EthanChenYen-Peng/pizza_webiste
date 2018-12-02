from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # print(form)
        # if form.is_valid():

        #     username = form.cleaned_data.get('username')
        #     print(username)
        messages.success(request , f"Account created for!")
        return redirect('orders_index')
    else:
        form = UserCreationForm()
    return render(request , "users/register.html" , context = {"form" : form})
