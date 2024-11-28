from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class CTScan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ct_scans')
    scan_result = models.TextField()

    def __str__(self):
        return f"CT Scan for {self.user.username}"


class RenalCellImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='renal_cell_images')
    image_result = models.TextField()

    def __str__(self):
        return f"Renal Cell Image for {self.user.username}"
