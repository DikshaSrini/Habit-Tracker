from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'Today\'s Journal: \nMood (Happy/Sad/Exhausted/Bored/Excited/Other): \nBreakfast,Lunch,Dinner: \nMeditation (Meditated/No meditation done): \nReading (Read/Did not): \nWorkout (Worked out/Not Done):'})