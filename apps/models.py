from django.db import models


class Parking(models.Model):
    parking_name = models.CharField('Name', max_length=250, primary_key=True)

    def __str__(self):
        return self.parking_name

    class Meta:
        """Meta definition for Product."""
        verbose_name = 'Parking'
        verbose_name_plural = 'Parkings'
        ordering = ['parking_name']


class FreeSpaces(models.Model):
    parking = models.ForeignKey(Parking, verbose_name='Parking', on_delete=models.CASCADE)
    free_spaces_number = models.IntegerField('Free spaces')
    updated_at = models.DateTimeField('Update date', primary_key=True)

    def __str__(self):
        return f"{self.parking}: {self.free_spaces_number} at {self.updated_at.__str__()}"

    class Meta:
        """Meta definition for Product."""
        verbose_name = 'FreeSpace'
        verbose_name_plural = 'FreeSpaces'
        ordering = ['parking']