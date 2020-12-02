from django import  forms
from blog.models import  Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author','title', 'category','post_pic','content')

        widgets = {
            'author': forms.TextInput(attrs ={ 'class': '', 'name':'author','placeholder': 'Enter Author', 'value':'', 'id': 'author', 'type':'hidden'}),
            'title' : forms.TextInput(attrs = {'class': ' form w-full h-6/12 mt-2 ', 'name':'title','placeholder': 'Enter Title',}),
            'category' : forms.Select(attrs = {'class': 'inline-block bg-gray-200 w-full h-6/12 mt-2 p-2 rounded border mb-4', 'size':'4', 'name':'category','placeholder': 'Enter Author',}),
            'post_pic' : forms.FileInput(attrs = {'class': 'inline-block btn w-full h-6/12 mt-2 shadow-lg bg-gray-200 mb-4 text-center', 'name':'post_pic','placeholder': 'Enter Author',}),
            'content' : forms.Textarea( attrs = { 'class': ' w-full h-6/12 mt-2 mb-4', 'name':'content','placeholder': 'Enter Content Here',}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text')


        widgets = {
            'author': forms.TextInput(attrs ={ 'class': 'w-full px-4 py-3 rounded-lg bg-gray-200 mt-2 border focus:border-blue-500 focus:bg-white focus:outline-none', 'value':'', 'id': 'author', 'type':'hidden'}),
            'text': forms.Textarea(attrs = {'class': 'w-full px-4 py-3 rounded-lg bg-gray-200 mt-2 border focus:border-blue-500 focus:bg-white focus:outline-none'})
        }