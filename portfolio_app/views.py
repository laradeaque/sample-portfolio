from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib import messages
import mimetypes

from .models import Blog, Contact, Thought


# Create your views here.
class AllBlogsView(ListView):
    model = Blog
    paginate_by = 3
    template_name = "portfolio_app/home.html"

def home(request, page):
	if request.method == 'POST':
		name  = request.POST.get('Name', None)
		email = request.POST.get('Email',None)
		msg   = request.POST.get('Message', None)

		if not (name or email or msg):
			messages.error(request, "Enter all details to send a message")
			return redirect('home')

		contact = Contact(name=name, email=email, message=msg)
		contact.save()
		
		messages.success(request, "Message successfully received")
	
	blogs = Blog.objects.all()
	paginator = Paginator(blogs, per_page=3)
	page_object = paginator.get_page(page)
	page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
	context = {"page_obj": page_object}
	# context = {
		# 'blog_block1': blogs[:3],
		# 'blog_block2': blogs[3:],
		# 'recommended': [blogs[2]] * 2
	# }
	return render(request, "portfolio_app/home.html", context)

def blogs_api(request):
    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 3)
    startswith = request.GET.get("startswith", "")
    blogs = Blog.objects.filter(
        title__startswith=startswith
    )
    paginator = Paginator(blogs, per_page)
    page_obj = paginator.get_page(page_number)
    data = [{"title": kw.title} for kw in page_obj.object_list]

    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
        },
        "data": data
    }
    return JsonResponse(payload)

def blog(request, blog_slug):
	if request.method == "POST":
		email = request.POST.get("email", None)
		thought = request.POST.get("thought", None)

		if email or thought:
			thought_obj = Thought(sender_email=email, sender_thought=thought)
			thought_obj.save()
			messages.success(request, "Your thought was successfully received!")
		else:
			messages.error(request, "Share your thoughts!")
		return redirect('blog', blog_slug)
	blog = Blog.objects.filter(slug=blog_slug)
	if not blog:
		messages.error(request, "Failed to get the blog you requested...")
		return redirect('home')
	return render(request, "portfolio_app/blog_page.html", context={'blog': blog.first()})

def download_file(request):
    fl_path = '/home/arnold/Projects/Portfolio/portfolio_app/media/Arnold_Resume.pdf'
    filename = 'Arnold_Resume.pdf'

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
