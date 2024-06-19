from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class ResumeView(View):
    template_name = "resume/resume.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)