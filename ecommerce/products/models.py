from django.db import models
from django.urls import reverse

# create categary model
class Categary(models.Model):
    title = models.CharField(max_length=300)
    primary_categary = models.BooleanField(default=False)

    def __str__(self) :
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

#create product model
class Product(models.Model):
    name = models.CharField(max_length=300)
    Categary = models.ForeignKey(Categary,on_delete=models.CASCADE)
    slug = models.SlugField()
    price = models.FloatField()

    def __str__(self) :
        return self.name

    def get_absolute_url(self):
        return reverse("mainapp:product", kwargs={"slug": self.slug})
    

