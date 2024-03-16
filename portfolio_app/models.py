from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
class Tag(models.Model):
	tag_name = models.CharField(max_length=128)

	def __str__(self):
		return self.tag_name

class Blog(models.Model):
	title = models.CharField(max_length=200)
	sub_title = models.CharField(max_length=200)
	date_published = models.DateField(auto_now_add=True)
	content = RichTextUploadingField()
	tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
	blog_image = models.ImageField()
	slug = models.SlugField(default="", null=False, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("article_detail", kwargs={"slug": self.slug}) 

class Contact(models.Model):
	name = models.CharField(max_length=128)
	email = models.CharField(max_length=128)
	message = models.TextField()

	def __str__(self):
		return f"{self.name} - {self.email} message"

class Thought(models.Model):
	sender_email = models.CharField(max_length=128, default="")
	sender_thought = models.TextField()
	sender_datetime = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		if len(self.sender_email) == 0:
			return	f"Anonymous thought at {self.sender_datetime}"
		else:
			return f"{self.sender_email} thought at {self.sender_datetime}"
