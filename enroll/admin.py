from django.contrib import admin
from enroll.models import Post
# Register your models here.
@admin.register(Post)
class PostAmdin(admin.ModelAdmin):
  list_display =['id', 'title', 'desc']