from django.urls import path
from .views import (
	PostListCreateAPIView , PostRetrieveUpdateDestroyAPIView,
	CommentListCreateAPIVew , CommentRetrieveUpdateDestroyAPIView,
	post_list_view, post_detail_view,

)


urlpatterns = [

    # Template views
    path('', post_list_view, name='post-list-view'),
    path('posts/<int:pk>/', post_detail_view, name='post-detail-view'),


	#API Endpoints
	# Post endpoints
	path('posts/', PostListCreateAPIView.as_view(),name='post-list-create'),
	path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),

	# Comment endpoints
    path('posts/<int:post_id>/comments/', CommentListCreateAPIVew.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
]
