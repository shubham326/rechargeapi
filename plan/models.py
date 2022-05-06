from django.db import models

# Create your models here.


class Operator(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
      return self.name

class Region(models.Model):
    rname=models.CharField(max_length=100)
    operator=models.ForeignKey(Operator,on_delete=models.CASCADE, related_name='Operator_get')

    def __str__(self):
      return self.rname




class plan(models.Model):
  rupees = models.CharField(max_length=100)
  operator = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name='op')
  region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='re')
  data = models.CharField(max_length=100)
  validity = models.CharField(max_length=100)

  def __str__(self):
    return self.rupees


class recharge(models.Model):
  mobile = models.IntegerField()
  price = models.IntegerField()
  Plan = models.ForeignKey(plan, on_delete=models.CASCADE, related_name='plan_set')
  