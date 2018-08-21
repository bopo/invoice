from django.contrib import admin
from django.forms import ModelForm, TextInput
from django.http import HttpResponseRedirect
from django.utils.html import format_html

from .models import Invoice, Goods, Department


# Inlines for ContinentAdmin
class GoodsInlineForm(ModelForm):
    class Meta:
        widgets = {
            # 'title': TextInput(attrs={'class': 'input-mini'}),
            # 'price': TextInput(attrs={'class': 'input-medium'}),
            # 'quant': SuitDateWidget,
        }


class GoodsInline(admin.TabularInline):
    form = GoodsInlineForm
    model = Goods
    fields = ('title', 'price', 'quant')
    extra = 1
    verbose_name_plural = '商品项目'
    sortable = 'id'
    show_change_link = False
    show_delete_link = False


class InvoiceForm(ModelForm):
    class Meta:
        widgets = {
            'title': TextInput(attrs={'class': 'input-mini'}),
        }


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'department', 'total', 'created', 'export_excel')
    list_filter = ('owner', 'title', 'created')
    search_fields = ('title', 'owner')
    exclude = ['owner', 'created']
    inlines = (GoodsInline,)
    sortable = 'id'

    def export_excel(self, obj):
        return format_html('<a href="/export/excels/{}">导出Excel</>', obj.pk)

    export_excel.short_description = '导出Excel'

    def print_selected_objects(modeladmin, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        return HttpResponseRedirect("/export/report/?ids=%s" % (",".join(selected)))

    print_selected_objects.short_description = "多票据显示"

    actions = ['print_selected_objects']

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for instance in instances:
            instance.total = instance.price * instance.quant
            instance.save()

        if instances:
            invoice = instances[0].invoice
            invoice.total = 0

            for i in invoice.goods_set.all():
                invoice.total += i.price * i.quant

            invoice.save()
