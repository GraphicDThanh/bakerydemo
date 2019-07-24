from rest_framework.fields import Field, ReadOnlyField
from wagtail.api.v2.serializers import BaseSerializer, TagsField
from wagtail.images.api.fields import ImageRenditionField
from bakerydemo.blog.models import BlogPageTag


class BlogSerializer(BaseSerializer):
    image = ImageRenditionField('original')
    image_small = ImageRenditionField('fill-300x200|jpegquality-60', source='image')
    image_medium = ImageRenditionField('fill-800x600|jpegquality-50', source='image')
    tags = TagsField()