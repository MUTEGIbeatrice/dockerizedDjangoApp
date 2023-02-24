from django import forms 
from django.contrib.auth.forms import UserCreationForm
from app.models import CustomUser, Report


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username', 'email','phone_number' ,'password1' ,'password2']
        # labels = {
        #     'first_name':'Name'
        # }

    
    def __init__(self,*args, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
           field.widget.attrs.update({'class':'input, form-control'})

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title','description','status', 'sensitivity_status','current_owner','date']
        
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
        
     
    def __init__(self,*args, **kwargs):
        super(ReportForm,self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
           field.widget.attrs.update({'class':'input, form-control'})

        # for fieldname in ['username', 'password1', 'password2']:
        #     self.fields[fieldname].help_text = None