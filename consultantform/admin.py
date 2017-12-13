from django.contrib import admin
from .models import Article,Branch,Subsidiary,Relatedcompany,Problemsolving,Digitalization,Miom,Problemsolvingp,Digitalizationp,Miomp,Duediligence,Script,Strategy,Backgroundcheck,Backgroundcheckb,Duediligencep,Scriptp,Strategyp






class Bradmin(admin.ModelAdmin):
    list_display = ('branch_name','company_name')

class Suadmin(admin.ModelAdmin):
    list_display = ('subsidiary_name','company_name')

class Readmin(admin.ModelAdmin):
    list_display = ('related_company_name','company_name')

class Bgadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')

class BAdmin(admin.ModelAdmin):
    list_display = ('company_name','form_name','user','date')

class Dueadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')

class Duepadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')

class Scriptadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')

class Scriptpadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')

class Stratadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')

class Stratpadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')
    
    
class Psadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')

class Pspadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')

class Digiadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')

class Digipadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')

class Miomadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')

class Miompadmin(admin.ModelAdmin):
    list_display = ('form_name','company_name')



admin.site.register(Article)
admin.site.register(Branch,Bradmin)
admin.site.register(Subsidiary,Suadmin)
admin.site.register(Relatedcompany,Readmin)
admin.site.register(Backgroundcheck,Bgadmin)
admin.site.register(Backgroundcheckb,BAdmin)
admin.site.register(Duediligence,Dueadmin)
admin.site.register(Script,Scriptadmin)
admin.site.register(Strategy,Stratadmin)
admin.site.register(Problemsolving,Psadmin)
admin.site.register(Digitalization,Digiadmin)
admin.site.register(Miom,Miomadmin)
admin.site.register(Duediligencep,Duepadmin)
admin.site.register(Scriptp,Scriptpadmin)
admin.site.register(Strategyp,Stratpadmin)
admin.site.register(Problemsolvingp,Pspadmin)
admin.site.register(Digitalizationp,Digipadmin)
admin.site.register(Miomp,Miompadmin)
