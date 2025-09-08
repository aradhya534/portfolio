from django.contrib import admin
from .models import ContactMessage

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'subject', 'message', 'submitted_at')  # adjust if you have a timestamp
    search_fields = ('full_name', 'email', 'subject')