from django.db import models



class Post(models.Model):
		title = models.CharField(max_length=100)
		content = models.TextField()
		created_at = models.DateTimeField()


		def __str__(self):
			return self.title 
		

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	author_name = models.CharField(max_length=100)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'comment by {self.author_name}'