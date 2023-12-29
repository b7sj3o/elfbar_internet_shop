from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Types, Flavours, User

class CreateProduct(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(CreateProduct, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control w-100'


class CreateType(ModelForm):
    class Meta:
        model = Types
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(CreateType, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control w-100'


class CreateFlavour(ModelForm):
    class Meta:
        model = Flavours
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(CreateFlavour, self).__init__(*args, **kwargs)

        self.fields['flavour'].widget.attrs['class'] = 'form-control'
        self.fields['is_avialable'].widget.attrs['class'] = 'form-check-input form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User      
        fields = ['username', 'email', 'password1', 'password2']  
