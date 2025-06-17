from django.shortcuts import render , get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics


# Template Views

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})






# ✅ POST Views (List, Create, Retrieve, Update, Delete)


class PostListCreateAPIView(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


# ✅ COMMENT Views (List by Post, Create, Update, Delete)

class CommentListCreateAPIVew(generics.ListCreateAPIView):
		serializer_class = CommentSerializer


		def get_queryset(self):
			post_id = self.kwargs['post_id']
			return Comment.objects.filter(post_id=post_id)
		

		def perform_create(self, serializer):
			post_id = self.kwargs['post_id']
			serializer.save(post_id=post_id)


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

	

