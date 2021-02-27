# import ModelForm class from django
from django.forms import ModelForm
from .models import Feeding

# feedingform inherits from modelform
class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']