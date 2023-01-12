from django.db import models
from io import BytesIO
from soori_website import settings
from PIL import Image
from django.core.exceptions import ValidationError
from django.core.files import File
from src.core_app.models import CreateInfoModel

def upload_path_item(instance, filename):
    return '/'.join(['item_image', filename])


def validate_image(image):
    file_size = image.size
    limit_byte_size = settings.MAX_UPLOAD_SIZE
    if file_size > limit_byte_size:
        # converting into kb
        f = limit_byte_size / 1024
        # converting into MB
        f = f / 1024
        raise ValidationError("Max size of file is %s MB" % f)


class Blog(CreateInfoModel):
    name=models.CharField(max_length=50, unique=True, help_text=" name can be max. of 50 characters")
    image = models.ImageField(upload_to="blog", validators=[validate_image],
                              blank=True)

    description=models.TextField(max_length=200, blank=True, help_text="descriptions should be maximum of 200 characters and can be blank")
    active = models.BooleanField(default=True, help_text="By default active=True")

    def __str__(self):
        return "id {}".format(self.id)


    def save(self, *args, **kwargs):
        if self.image is True:
            img = Image.open(self.image).convert('RGB')
            im_io = BytesIO()
            img.save(im_io, format="webp")
            new_image = File(im_io, name="%s.webp" % self.image.name.split('.')[0], )
            self.image = new_image
        super().save(*args, **kwargs)


