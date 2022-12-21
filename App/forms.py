from django import forms
g=[('MALE','male'),('FEMALE','female')]
c = [('PYTHON', 'python'), ('JAVA', 'java'), ('DJANGO', 'django'), ('MERN', 'mern'),
     ('SQL', 'sql'), ('HTML', 'html'),('CSS','css')]
class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=18)
    email=forms.EmailField()
    mobile=forms.IntegerField()
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    address=forms.CharField(widget=forms.Textarea)
    password=forms.CharField(widget=forms.PasswordInput)