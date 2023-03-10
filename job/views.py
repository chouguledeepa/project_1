"""Views for Job API"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

## import models
from core.models import JobTitle
from job import serializers


class JobTitleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.JobTitleSerializer

    # represents objects that are available for this viewset.
    # queryset objects that are manageable by this view.
    queryset = JobTitle.objects.all()

    # In order to use endpoint provided by this viewset, we will need ]
    # authentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        We want to filter out jobtitles for authenticated users
        """
        #breakpoint()
        return self.queryset.filter(user=self.request.user).order_by("-id")