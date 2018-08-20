from django.contrib import admin
from django.utils.safestring import mark_safe
from django.forms import ModelForm, Select, TextInput, NumberInput
from suit.widgets import AutosizedTextarea, EnclosedInput

from .models import Invoice, Goods


class GoodsInlineForm(ModelForm):
    class Meta:
        widgets = {
            'price': EnclosedInput(prepend='fa-globe', append='km<sup>2</sup>'),
            'quant': EnclosedInput(prepend='fa-users'),
        }

class GoodsInline(admin.TabularInline):
    form = GoodsInlineForm
    model = Goods
    min_num = 3
    extra = 0
    verbose_name_plural = 'Goods'
    suit_classes = 'suit-tab suit-tab-goods'
    suit_form_inlines_hide_original = True

class InvoiceForm(ModelForm):
    class Meta:
        widgets = {
            # 'code': TextInput(attrs={'class': 'input-mini'}),
            # 'independence_day': SuitDateWidget,
            'area': EnclosedInput(prepend='fa-globe', append='km<sup>2</sup>',
                                  attrs={'placeholder': 'Country area'}),
            'population': EnclosedInput(
                prepend='fa-users',
                append='<button class="btn btn-secondary" type="button" '
                       'onclick="window.open(\'https://www.google.com/\')">Search</button>',
                append_class='btn', attrs={'placeholder': 'Human population'}),
            'description': AutosizedTextarea,
            'architecture': AutosizedTextarea,
        }

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = (GoodsInline,)
    form = InvoiceForm
    list_display = ('title', 'owner', 'created',)
    readonly_fields = ('owner', 'created')    
    list_filter = ('created',)

    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['name', 'code', 'continent', 'independence_day']
        }),
        ('Statistics', {
            'classes': ('suit-tab suit-tab-general',),
            'description': 'EnclosedInput widget examples',
            'fields': ['area', 'population']}),
        ('Autosized textarea', {
            'classes': ('suit-tab suit-tab-general',),
            'description': 'AutosizedTextarea widget example - adapts height '
                           'based on user input',
            'fields': ['description']}),
        ('Architecture', {
            'classes': ('suit-tab suit-tab-cities',),
            'description': 'Tabs can contain any fieldsets and inlines',
            'fields': ['architecture']}),
    ]

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'quant', 'price', 'created')
    search_fields = ('title',)

