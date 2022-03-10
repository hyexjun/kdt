from django.contrib import admin
from students.models import Student   #3 여기에 알아서 추가가 되는데 암튼 지금은 안됨

# Register your models here.  #2 add 가능한 목록이 뜨고 그걸 선택하면
admin.site.register(Student)  #1 원래는 여기 스튜던트에 커서 놓고 컨트롤쩜하면