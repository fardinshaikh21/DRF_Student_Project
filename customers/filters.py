import django_filters
from .models import Customer

class CustomerFilter(django_filters.FilterSet):

    #cid = django_filters.RangeFilter(field_name='cid')
    cname = django_filters.CharFilter(field_name='cname', lookup_expr = 'iexact' )
    address = django_filters.CharFilter(field_name='address', lookup_expr = 'icontains')

    id_min = django_filters.CharFilter(method='filter_by_id_range',label='From Cid')
    id_max = django_filters.CharFilter(method='filter_by_id_range',label='To Cid')

    class Meta:
        model = Customer
        fields = ['cid','cname','address']

    def filter_by_id_range(self, queryset, name, value):

        if name == 'id_min':
            return queryset.filter(cid__gte=value)
        
        elif name == 'id_max':
            return queryset.filter(cid__lte=value)
        
        return queryset         