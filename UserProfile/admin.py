from django.contrib import admin
from .models import * #Userprofile, Grade, Subject, Video, Admission
# Register your models here.


admin.site.register(Userprofile)
admin.site.register(Grade)
admin.site.register(Subjects)
admin.site.register(Video)