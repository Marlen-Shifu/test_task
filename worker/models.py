from django.db import models



class Worker(models.Model):
    full_name = models.CharField(max_length=255)
    employment_date = models.DateField()

    posts = (
        ('Работник', 'Работник'),
        ('Старший работник', 'Старший работник'),
        ('Начальник', 'Начальник'),
        ('Зам. Директора', 'Зам. Директора'),
        ('Директор', 'Директор'),
    )
    post = models.CharField(max_length=255, choices=posts)

    salary = models.PositiveIntegerField()

    chief = models.ForeignKey('self', related_name='subjects', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.post} - {self.full_name}'