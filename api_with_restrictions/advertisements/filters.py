from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter, NumberFilter, CharFilter
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    status = CharFilter(field_name='status')
    creator = NumberFilter(field_name='creator')
    created_at = DateFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Advertisement
        fields = ['status', 'creator', 'created_at']
