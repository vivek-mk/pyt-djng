"""# from django.db import models
# from django.urls import reverse
#
# # Create your models here.
# class Product(models.Model):
#     # title = models.TextField()#old code
#     # description = models.TextField()
#     # price = models.TextField()
#     title = models.CharField(max_length=120) #max_length is mandatory for charfield
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(decimal_places=2,max_digits=10000)
#     summary = models.TextField(blank=False,null=False)
#     featured = models.BooleanField(default=False)
#
#
#     def get_absolute_url(self):
#         #return "/products/{self.id}/"
#         return reverse("products:product-detail",kwargs={"id":self.d})"""

from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False)  # null=True, default=True

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})  # f"/products/{self.id}/"

    def __str__(self):
        return self.title
