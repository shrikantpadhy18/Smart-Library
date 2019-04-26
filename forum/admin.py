from django.contrib import admin
from .models import Image,ITBooks,COMPSBooks,ELECTRONICSBooks,EXTCBooks,INSTRUBooks,Books,Branch,BookId,FE
def make_issued(ModelAdmin,request,queryset):
	queryset.update(issuingstatus='issued')
make_issued.short_description="Mark selected books as issued_to_student"



def make_notissued(ModelAdmin,request,queryset):
	queryset.update(issuingstatus='not_issued')
make_notissued.short_description="Mark selected books as not issued_to_student"

def make_returned(ModelAdmin,request,queryset):
	queryset.update(returningstatus='returned')
make_notissued.short_description="Mark selected books as returned_by_student"

def make_notreturned(ModelAdmin,request,queryset):
	queryset.update(returningstatus='not_returned')
make_notissued.short_description="Mark selected books as not returned_by_student"



class ITadmin(admin.ModelAdmin):
	list_display=('bookid','bookname','author','publisher','year')
	search_fields = ['bookname','bookid','author']
	list_filter=('year',)

class COMPSadmin(admin.ModelAdmin):
	list_display=('bookid','bookname','author','publisher','year')
	search_fields = ['bookname','bookid','author']
	list_filter=('year',)

class ELECTRONICSadmin(admin.ModelAdmin):
	list_display=('bookid','bookname','author','publisher','year')
	search_fields = ['bookname','bookid','author']
	list_filter=('year',)

class INSTRUadmin(admin.ModelAdmin):
	list_display=('bookid','bookname','author','publisher','year')
	search_fields = ['bookname','bookid','author']
	list_filter=('year',)

class EXTCadmin(admin.ModelAdmin):
	list_display=('bookid','bookname','author','publisher','year')
	search_fields = ['bookname','bookid','author']
	list_filter=('year',)

class Bookadmin(admin.ModelAdmin):
	list_display=('bookid','rollno','issuingdate','issuingstatus','returningstatus','DUE_DATE')
	actions=[make_notissued,make_issued,make_returned,make_notreturned]
	search_fields = ['bookid','issuingstatus','returningstatus']
	list_editable=('DUE_DATE',)
	list_filter=('issuingstatus','returningstatus')

class Branchadmin(admin.ModelAdmin):
	list_display=('branch',)

class Bookidadmin(admin.ModelAdmin):
	list_display=('bookid',)

admin.site.register(Branch,Branchadmin)
admin.site.register(BookId,Bookidadmin)


#
admin.site.register(Books,Bookadmin)
admin.site.register(Image)


admin.site.register(ITBooks,ITadmin)
admin.site.register(COMPSBooks,COMPSadmin)
admin.site.register(ELECTRONICSBooks,ELECTRONICSadmin)
admin.site.register(INSTRUBooks,INSTRUadmin)
admin.site.register(EXTCBooks,EXTCadmin)

admin.site.site_header = "LIBRARY MANAGEMENT SYSTEM ";
admin.site.site_title = "LIBRARY MANAGEMENT SYSTEM ";
admin.site.index_title="LIBRARIAN"

class FEadmin(admin.ModelAdmin):
	list_display=('bookid','bookname','author','publisher','year')
	search_fields = ['bookname','bookid']
	list_filter=('bookid',)
admin.site.register(FE,FEadmin)