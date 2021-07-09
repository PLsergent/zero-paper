from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
import os
import shutil


class Folder(models.Model):
    name = models.CharField(max_length=128)
    parent_folder = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'


def upload_to(instance, filename):
    upload_to = ""
    if instance.folder:
        upload_to = instance.folder.name + "/"
        instance = instance.folder
        while True:
            if not instance.parent_folder:
                break
            upload_to = instance.parent_folder.name + "/" + upload_to
            instance = instance.parent_folder
    return "files/" + upload_to + filename

class Document(models.Model):
    title = models.CharField(max_length=128)
    docfile = models.FileField(upload_to=upload_to)

    TYPES = (
        ('PDF', 'Pdf'),
        ('IMG', 'Image'),
        ('XLS', 'Excel'),
        ('DOCX', 'Docx'),
        ('TXT', 'Text')
    )
    doctype = models.CharField(max_length=128, choices=TYPES)
    description = models.TextField(max_length=250, blank=True)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Document, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.title}'


@receiver(models.signals.post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Document` object is deleted.
    """
    if instance.docfile:
        if os.path.isfile(instance.docfile.path):
            os.remove(instance.docfile.path)

@receiver(models.signals.pre_save, sender=Document)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Document` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Document.objects.get(pk=instance.pk).docfile
    except Document.DoesNotExist:
        return False

    new_file = instance.docfile
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

@receiver(models.signals.pre_save, sender=Document)
def auto_move_file_on_update(sender, instance, **kwargs):
    """
    Move old file from filesystem
    when corresponding `Document` object is updated
    with new folder.
    """
    if not instance.pk:
        return False

    try:
        old_file = Document.objects.get(pk=instance.pk).docfile
        old_folder = Document.objects.get(pk=instance.pk).folder
    except Document.DoesNotExist:
        return False

    new_folder = instance.folder
    if not old_folder == new_folder:
        new_path = upload_to(instance, os.path.basename(old_file.path))
        shutil.move(old_file.path, new_path)
