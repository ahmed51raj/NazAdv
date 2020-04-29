from django.shortcuts import render,get_object_or_404
from .models import Slider, Service_Header, Service_Body, Projects, ProjectsImage,Category, ClientQuote, ClientBrand, Business, Technique, Technique_Info

# Create your views here.
def home(request):
  slider=Slider.objects.all()
  service_header=Service_Header.objects.all()
  service_body = Service_Body.objects.all()
  projects = Projects.objects.all()
  clientquote = ClientQuote.objects.all()
  clientbrand = ClientBrand.objects.all()
  business = Business.objects.all()
  technique = Technique.objects.all()
  technique_info = Technique_Info.objects.all()
 
  context={
    'slider':slider,
    'service_header':service_header,
    'service_body':service_body,
    'projects':projects,
    'clientquote':clientquote,
    'clientbrand':clientbrand,
    'business':business,
    'technique':technique,
    'technique_info':technique_info
  }
  return render(request,'home/index.html',context)

def project_detail(request,category,id):
  project=get_object_or_404(Projects,id=id)
  photos = ProjectsImage.objects.filter(projects=project)
  cat = get_object_or_404(Category, name=category)
  projects = Projects.objects.filter(category=cat.id)
  print(projects)
  context={
    'project':project,
    'photos':photos,
    'projects':projects
  }
  return render(request, 'portfolio/project_detail.html', context)
