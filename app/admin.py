from django.contrib import admin

# Register your models here.
from .models import CTScan,RenalCellImage,User

admin.site.register(CTScan)
admin.site.register(RenalCellImage)
admin.site.register(User)