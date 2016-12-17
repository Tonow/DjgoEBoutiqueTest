from django.db import models

# Create your models here.

class Product(models.Model):
    """
    Documentation Product Class
    - name CharField(max_length=100)
    - code IntegerField()
    """
    name = models.CharField(max_length=100)
    code = models.IntegerField()

    def __unicode__(self):
        return "{0} [{1}]".format(self.name, self.code)


class ProductItem(models.Model):
    color   = models.CharField(max_length=100)
    product = models.ForeignKey('Product')
    code    = models.IntegerField()

    def __unicode__(self):
        return "{0} {{1}} [{2}]".format(self.product.name, self.color, self.code)
