from django.contrib import admin

from board.models import Board
from board.models import Comment

# Register your models here.

admin.site.register(Board)
admin.site.register(Comment)