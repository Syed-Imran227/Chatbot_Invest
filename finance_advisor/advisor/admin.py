from django.contrib import admin
from .models import FinancialProfile, InvestmentAdvice, ChatMessage, LoginHistory

@admin.register(FinancialProfile)
class FinancialProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'age', 'occupation', 'risk_tolerance', 'investment_goal')
    search_fields = ('user__username', 'name', 'occupation')
    list_filter = ('risk_tolerance', 'investment_goal', 'investment_knowledge')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'age', 'occupation', 'family_size')
        }),
        ('Financial Information', {
            'fields': ('monthly_income', 'monthly_expenses', 'monthly_savings', 'current_debts', 'debt_interest_rate')
        }),
        ('Investment Profile', {
            'fields': ('risk_tolerance', 'investment_knowledge', 'has_investment_experience', 'previous_investments')
        }),
        ('Financial Goals', {
            'fields': (
                'short_term_goals', 'short_term_goal_amount',
                'medium_term_goals', 'medium_term_goal_amount',
                'long_term_goals', 'long_term_goal_amount'
            )
        }),
        ('Additional Information', {
            'fields': ('other_assets', 'retirement_plans')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

@admin.register(InvestmentAdvice)
class InvestmentAdviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')
    search_fields = ('user__username', 'title', 'content')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message_type', 'timestamp')
    search_fields = ('user__username', 'content')
    list_filter = ('message_type', 'timestamp')
    readonly_fields = ('timestamp',)

@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'login_time', 'ip_address')
    search_fields = ('user__username', 'ip_address')
    list_filter = ('login_time',)
    readonly_fields = ('user', 'login_time', 'ip_address', 'user_agent')
