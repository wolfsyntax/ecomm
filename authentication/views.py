from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, RedirectView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, authenticate, login

from django.views import View

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authentication.forms import UserRegistrationForm
import re, string

string.punctuation
class LoginView(TemplateView):

    template_name = ""
    #success_url = "auth/join/" # None
    redirect_authenticated_user = True
    redirect_field_name = 'next'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
       # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {

        }

        return render(request, "authentication/login.html", context)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        #print("\n\n\nUsername: {}\n\n\n".format(request.POST["username"]))
        #return HttpResponse("LOGIN ATTEMPT")
        username =  request.POST["username"]
        password = request.POST["password"]

        userdata = authenticate(username=username, password=password)

        if userdata is not None:
            if userdata.is_active :
                login(request, userdata)
                return HttpResponseRedirect("/dashboard")
            else:
                return HttpResponse("Inactive user")
        else:
            return HttpResponse("LOGIN ATTEMPT")

        return HttpResponse("LOGIN POST")

#    def get_context_data(self, **kwargs):
#        context = {}
#        return context

class SignupView(View):
    #model = User
    fields = [
        'first_name', 'last_name', 'username', 'email', 'password',
    ]

    template_name = "authentication/register.html"
    form_class = UserRegistrationForm
    success_url = "auth/login"

    def get(self, request, *args, **kwargs):

        form = self.form_class()
        sec_pass = string.ascii_letters + string.digits + string.punctuation

        generated_pass = User.objects.make_random_password(15, sec_pass)

        while not re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$', generated_pass):
            generated_pass = User.objects.make_random_password(15, "abcdefghjklmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789!@#$%^&*()_-+[]:;\/<>?.,")

        return render(request, self.template_name, {"form": form, "strong_pass": generated_pass})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect('/auth/login/?next=/')
        return render(request, self.template_name, {"form": form})

class LogoutView(RedirectView):

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        next_page = "/"
        if next_page:
            # Redirect to this page until the session has been cleared.
            return HttpResponseRedirect(next_page)

        return super().dispatch(request, *args, **kwargs)