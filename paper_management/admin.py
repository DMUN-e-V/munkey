from django.contrib import admin

from paper_management.models import Conference, Committee, MunkeyUser, Paper

admin.site.register(Conference)
admin.site.register(Committee)
admin.site.register(MunkeyUser)
admin.site.register(Paper)
