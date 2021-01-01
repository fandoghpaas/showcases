
from django.db.models.query import QuerySet
from django.contrib import admin
from .models import Image


# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/actions/#writing-action-functions
def delete_everywhere(modeladmin, request, queryset: QuerySet):
    """
    Delete object both in Django and in MinIO too.
    :param modeladmin: unused
    :param request: unused
    :param queryset: A QuerySet containing the set of objects selected by the user
    :return:
    """
    for obj in queryset:
        obj.delete()


delete_everywhere.short_description = "Delete selected objects in Django and MinIO"


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image',)
    readonly_fields = ('id', )
    model = Image
    actions = [delete_everywhere, ]
