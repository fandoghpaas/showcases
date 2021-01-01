import uuid

from django.db import models


class Image(models.Model):
    """
    This is just for uploaded image
    """
    objects = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='fandogh')

    def delete(self, *args, **kwargs):
        """
        Delete must be overridden because the inherited delete method does not call `self.file.delete()`.
        """
        self.image.delete()
        super(Image, self).delete(*args, **kwargs)
