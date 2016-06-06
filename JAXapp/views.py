from django.shortcuts import render
from webform import orgform
from models import analytics, jcanalytics

def site(request):
    form = orgform()
    return render(request, 'JAXapp/index.html', {'jcform' : form})

def form_view(request):
  if request.method == 'POST':
    form =  orgform(request.POST)

    if form.is_valid():
      organization = form.cleaned_data['organization']
      y = jcanalytics.objects.filter(id=organization)
      x = y[0].org
      z = analytics.objects.filter(org=x)

      return render(request, 'JAXapp/name.html', {'jcform2' : z})
