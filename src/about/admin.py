from django.contrib import admin
from .models import OurTeam, MessageFromCeo
# Register your models here.


class OurTeamAdminModel(admin.ModelAdmin):
    model = OurTeam
    search_fields = ('name', 'id')
    list_filter = ('name', 'id')
    ordering = ('id',)
    list_display = ('id', 'name', 'position')


admin.site.register(OurTeam, OurTeamAdminModel)
admin.site.register(MessageFromCeo)
