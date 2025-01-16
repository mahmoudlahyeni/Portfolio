from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage


# Create your views here.
def home(request):
    return render (request,"home.html")

def about (request):
    return render (request,"about.html")


def projects (request):
    projects_show=[
        {
            'title': '',
            'path': '',
        },


    ]
    return render (request,"projects.html",{"projects_show": projects_show})


def experience(request):
    experience=[
        {"company":"Tunisian Company of Electricity and Gas",
         "position":"During my internship at the Tunisian Company of Electricity and Gas (STEG), I  had the opportunity to learn about the protocols used in managing communication and data flow within the company’s networks, particularly in relation to Local Area Networks (LANs) and other IT infrastructure."},
        {"company":"SOTUFAC",
         "position":"I completed an internship at Sotufac, where I contributed to the development of an e-commerce webpage. This experience allowed me to apply the skills I had acquired in my studies and work on real-world projects. Collaborating with a talented team, I gained valuable insights into e-commerce design, user experience, and backend functionality. This internship not only enhanced my technical abilities but also deepened my understanding of industry best practices, setting a strong foundation for my career in web development."},
        {"company":"KMF",
         "position":"Our project at KMF aims to develop a robust DevOps solution specifically for applications using Kubernetes. This approach allows us to accelerate and enhance the reliability of our software deliveries while fostering close collaboration between development and operations teams. By integrating continuous integration and continuous deployment (CI/CD) pipelines tailored for Kubernetes, we aim to optimize development cycles, reduce time-to-market, and improve the quality of deployments."}
    ]
    return render (request,"experience.html",{"experience":experience})


def certificate(request):
    return render (request, "certificate.html")


def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)
