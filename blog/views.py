from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django.http import HttpResponse



def index_view(request):
    return HttpResponse("Sachins Blog API")


class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-timestamp')
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny, )
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']



class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-timestamp')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

