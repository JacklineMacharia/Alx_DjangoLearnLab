from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget()
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        tags = self.cleaned_data['tags']
        if commit:
            instance.save()
            instance.tags.set(*[tag.strip() for tag in tags.split(',') if tag.strip()])
        return instance
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'})
        }