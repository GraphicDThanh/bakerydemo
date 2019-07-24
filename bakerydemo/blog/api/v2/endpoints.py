from wagtail.api.v2.endpoints import BaseAPIEndpoint
from bakerydemo.blog.models import BlogPage
from .serializers import BlogSerializer


class BlogAPIEndpoint(BaseAPIEndpoint):
    base_serializer_class = BlogSerializer
    model = BlogPage
    name = 'blog'
    body_fields = BaseAPIEndpoint.body_fields + [
        'title',
        'introduction',
        'image',
        'image_small',
        'image_medium',
        'body',
        'subtitle',
        'tags',
        'date_published',
    ]

    def listing_view(self, request, *args, **kwargs):
        return super(BlogAPIEndpoint, self).listing_view(request, *args, **kwargs)

    def detail_view(self, request, *args, **kwargs):
        return super(BlogAPIEndpoint, self).detail_view(request, kwargs.pop('pk'), *args, **kwargs)
