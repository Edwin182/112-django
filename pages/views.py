from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render

# Create your views here.
class HomePageView(TemplateView):                   # class page views # Inheritance -OOP
    template_name = "pagesTemplates/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Edwin"
        print(context)
        return(context)


class AboutPageView(TemplateView):
    template_name = "pagesTemplates/about.html"

# Function Based Views 
def contact_page(request):
    #print(request.__dict__)
    # return HttpResponse("Hello World from a FBV")

    contact_info = {
        "name": "Edwin",
        "address": "123 Main Street, Los Angeles, CA",
        "email": "edwinfirstblog@firstblog.com"
    }

    return render(request, "pagesTemplates/contact.html", contact_info)