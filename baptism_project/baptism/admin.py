from django.contrib import admin
from .models import Baptism, ParishDetails, LoginDetails, BaptismAdvanced, FieldTable

@admin.register(Baptism)
class BaptismAdmin(admin.ModelAdmin):
    list_display = (
        'basic_baptism_id', 'child_name_first', 'child_name_second',
        'place_of_baptism', 'date_of_baptism', 'status'
    )
    search_fields = ('child_name_first', 'child_name_second', 'place_of_baptism')
    list_filter = ('status', 'date_of_baptism')

@admin.register(ParishDetails)
class ParishDetailsAdmin(admin.ModelAdmin):
    list_display = ('parish_id', 'name_of_parish', 'place_of_parish', 'status', 'created_time')
    list_filter = ('status',)
    search_fields = ('name_of_parish', 'place_of_parish')



from django.contrib import admin
from .models import LoginDetails, ParishDetails

class LoginDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role', 'contact_no', 'email', 'status', 'parish_id', 'last_login')  # Fields from the model
    list_filter = ('role', 'status')  # Add filters to the admin panel
    search_fields = ('user__username', 'email', 'contact_no')  # Search by username, email, or contact number
    ordering = ('-last_login',)  # Default ordering by last login time

admin.site.register(LoginDetails, LoginDetailsAdmin)




@admin.register(BaptismAdvanced)
class BaptismAdvancedAdmin(admin.ModelAdmin):
    list_display = ('advanced_baptism_id', 'basic_baptism_id', 'question', 'question_type', 'compulsary', 'status', 'created_time')
    search_fields = ('question', 'question_type')
    list_filter = ('status', 'compulsary')
    ordering = ('-created_time',)
