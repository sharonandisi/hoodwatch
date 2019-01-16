from django.contrib import admin
from .models import Neighbourhood, Profile, Post, Location, Comment

# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Comment)