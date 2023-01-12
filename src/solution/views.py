
# third-party
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
import django_filters
from rest_framework.response import Response
from.models import Solution
from .serializers import SolutionSerializer
from rest_framework import permissions



class FilterForSolution(django_filters.FilterSet):
    # for date range filter after_date and before_date
    date = django_filters.DateFromToRangeFilter(field_name="created_date_ad")

    # iexact is used for Case-insensitive exact match in search field. Nepal and nEpaL are same
    name = django_filters.CharFilter(lookup_expr='iexact')
    
    

    class Meta:
        model = Solution
        fields = [ 'active', 'id', 'name']


class SolutionViewSet(viewsets.ModelViewSet):
    # permission
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filter_class = FilterForSolution
    search_fields = ['name', 'id']
    ordering_fields = ['name', 'id']
    http_method_names = ['get', 'head', 'post', 'patch']


    def partial_update(self, request, *args, **kwargs):
        try:
            remarks = str(request.data['remarks']).strip()
            if len(remarks) <= 0:
                return Response({'remarks': 'Please give at least one word for remarks'},
                                status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'remarks': 'Please Provide remarks'}, status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
