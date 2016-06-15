from django import forms

from .models import Post
<<<<<<< HEAD
from .models import Comment
=======
>>>>>>> b27bc22ac63317afb2c324d45f15a64202dade54

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
<<<<<<< HEAD
        fields = ('title', 'text',)
        
class CommentForm(forms.ModelForm):

	class Meta:
	    model = Comment
	    fields = ('text',)
=======
        fields = ('title', 'text',)
>>>>>>> b27bc22ac63317afb2c324d45f15a64202dade54
