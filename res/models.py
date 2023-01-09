from opcode import stack_effect
from django.db import models
from home.models import ExamDetails, staff

# Create your models here.
class Slots(models.Model):
    sno = models.IntegerField()
    Eid = models.ForeignKey(ExamDetails,on_delete=models.CASCADE)
    fid = models.ForeignKey(staff,on_delete=models.CASCADE)
    rno = models.CharField(max_length=100)
    date = models.DateField()