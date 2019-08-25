from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, RedirectView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, authenticate, login

#from django.views import View

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

class LoginView(TemplateView):

    template_name = ""
    success_url = "auth/join" # None
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

class SignupView(CreateView):

    template_name = "authentication/register.html"

    def get(self, request, *args, **kwargs):
        context = {

        }

        return render(request, "authentication/register.html", context)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        print("\n\n\nUsername: {}\n\n\n".format(request.POST["username"]))
        #return HttpResponse("SIGNUP ATTEMPT")
        form = self.get_form()
        if form.is_valid():


            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(RedirectView):

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        next_page = "/"
        if next_page:
            # Redirect to this page until the session has been cleared.
            return HttpResponseRedirect(next_page)

        return super().dispatch(request, *args, **kwargs)