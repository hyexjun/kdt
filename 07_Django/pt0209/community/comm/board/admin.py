from xml.etree.ElementTree import Comment
from django.contrib import admin

from board.models import Fboard
from board.models import Comment 

# Register your models here.
admin.site.register(Fboard)
admin.site.register(Comment)

