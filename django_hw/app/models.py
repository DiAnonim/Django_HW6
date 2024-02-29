from django.db import models
from django.core.exceptions import ValidationError
    
class Post(models.Model):
    
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class Worker(models.Model):
    def validator_positive(self): 
        if self.salary < 0:
            raise ValidationError('Зарплата не может быть отрицательной')
        
    class Status(models.TextChoices):
        paid = 'p', 'Выплачено'
        not_paid = 'np', 'Не выплачено'

    name = models.CharField(max_length=255)
    bd = models.DateField()
    salary = models.IntegerField(validators = [validator_positive])
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.not_paid)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def get_id_plus_name(self):
        return f"{self.id} + {self.name}"

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'