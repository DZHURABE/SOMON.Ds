from django.db import models
class Elom (models.Mobel):
    sarlavha = models.CharField (max_length=200)
    tavsif = models. TextField()
    narx = models.DecimalField(max_digits=10, dacimal_places=2)
    rasm = models. ImageField(upload_to='rasmlar/')
    sana = models.DateTimeField(auto_now_add=True)
    tel = models.CharField(max_length=20)

    def  __str__(self):
        return self.sarlavha