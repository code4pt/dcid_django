from django.contrib import admin
from parliament.models import *

class ProposalAdmin(admin.ModelAdmin):
    search_fields = ['title', 'desc']


admin.site.register(Person)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Opinion)
admin.site.register(Tag)