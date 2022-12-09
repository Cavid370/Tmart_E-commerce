from re import I
from django import forms
from .models import Contact_form


class Test_form(forms.ModelForm):
    class Meta:
        model = Contact_form
        fields = '__all__'
        widgets = {
            'full_name' : forms.TextInput(
                attrs = {         
                    "class":"contact-box name", 
                    'placeholder': 'Your name*',
                    'label': ''
                }
            ),
            'mail': forms.EmailInput(
                attrs = {
                    "class":"contact-box name",
                    'placeholder': 'Email*',
                    'label': ''
                }
            ),
            'subject' : forms.TextInput(
                 attrs = {
                    "class":"contact-box subject",
                    'placeholder': 'Subject*',    
                    'label': ''  
                }
            ),
            'message' : forms.TextInput(
                 attrs = {
                    "class":"contact-box message",
                    'placeholder': 'Message*',    
                    'label': ''  
                }
            ),
        }
