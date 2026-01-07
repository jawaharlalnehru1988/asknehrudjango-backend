from django.db import models

class Audio(models.Model):
    audioTitle = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=100)
    filePath = models.FileField(upload_to='audios/', max_length=500)
    audioImage = models.ImageField(upload_to='audio_images/', blank=True, null=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'audios'
        ordering = ['-created_at']

    def __str__(self):
        return self.audioTitle
