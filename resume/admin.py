from django.contrib import admin
from .models import People, People2, People3, People4


# Register your models here.



class PeopleAdmin(admin.ModelAdmin):
    list_display = ['name', 'message']


admin.site.register(People, PeopleAdmin)
admin.site.register(People2, PeopleAdmin)
admin.site.register(People3, PeopleAdmin)
admin.site.register(People4, PeopleAdmin)
