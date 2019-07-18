from django import forms
from blog.models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author','title','content')
        widgets = {
            'title':forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'content':forms.Textarea(
                attrs={
                    'class':'form-control'
                }
            )
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','content')
        widgets = {
            'author':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'content':forms.Textarea(
                attrs={
                    'class':'form-control'
                }
            )
        }
