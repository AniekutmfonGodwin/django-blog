from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):

    def __init__(self, *args,**kwargs):
        super(CommentForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['website'].widget.attrs['class']='form-control'
        self.fields['comment'].widget.attrs['class']='form-control'

    class Meta:
        model = Comment
        fields = ['name', 'email', 'website', 'comment']

    