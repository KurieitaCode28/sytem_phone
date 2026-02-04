# tu_app/templatetags/custom_filters.py
from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def currency_format(value):
    """Formatea números como RD$3,000.00"""
    try:
        value = Decimal(str(value))
        return f"RD${value:,.2f}"
    except:
        return f"RD$0.00"

@register.filter
def number_format(value):
    """Formatea números como 3,000.00"""
    try:
        value = Decimal(str(value))
        return f"{value:,.2f}"
    except:
        return "0.00"
    