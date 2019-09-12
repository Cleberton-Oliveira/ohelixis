from django.form import ModelForm
from .models import Person
from .form import PersonForm


def list_person(modelForm):
    usuario = Person.objects.all()
    class Meta:
        modal = usuario

def person_new(request)

