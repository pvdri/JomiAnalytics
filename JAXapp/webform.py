from django import forms
from models import analytics, jcanalytics
import sys
reload(sys)
sys.setdefaultencoding("utf8")
print "Starting UTF script..."

class orgform(forms.Form):
    choice=[(x.id,str(x.org)) for x in jcanalytics.objects.all().order_by('org')]
    organization = forms.ChoiceField(choice)
