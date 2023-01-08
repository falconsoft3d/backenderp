from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Product

OBJECT_LIST_FIELDS = [
    {'string': _("Code"), 'field': 'code'},
    {'string': _("Bar Code"), 'field': 'barcode'},
    {'string': _("Name"), 'field': 'name'},
]

OBJECT_FORM_FIELDS = [
    'name',
    'code',
    'barcode',
    'description',
]

class ProductListView(LoginRequiredMixin, FatherListView):
    model = Product
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}