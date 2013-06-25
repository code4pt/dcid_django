from django.contrib import admin
from parliament.models import 
from parliament.models import Person, Proposal, Opinion, Tag

class ProposalAdmin(admin.ModelAdmin):
    search_fields = ['title', 'desc']


admin.site.register(Person)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Opinion)
admin.site.register(Tag)