from django.forms import ModelForm
from .models import Chat
from crispy_forms.helper import FormHelper

class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = ('message',)
    def __init__(self, *args, **kwargs):
        super(ChatForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'placeholder': 'Your Message here'})
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        self.fields['txt01'].label = ''