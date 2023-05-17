from django.contrib import admin

# Register your models here.
from .models import BookInstrument

admin.site.register(BookInstrument)
class BookInstrumentook(admin.ModelAdmin):
    fields = (('your_name', 'iname'), 'email', 'date','st','et','Aproved')