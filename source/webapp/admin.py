from django.contrib import admin
from webapp.models import Announcement, Categories, Comment


admin.site.register(Announcement)
admin.site.register(Comment)
admin.site.register(Categories)
