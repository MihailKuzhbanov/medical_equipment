from django.db import models


class Equipment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description_id = models.BigIntegerField()
    description_name = models.CharField(max_length=100)
    description_brand = models.CharField(max_length=100)
    description_model = models.CharField(max_length=100)
    description_manufacturer_id = models.IntegerField()
    description_manufacturer_name = models.BigIntegerField()
    description_manufacturer_country = models.CharField(max_length=100)
    description_category_id = models.DateTimeField()
    description_category_code = models.BigIntegerField()
    description_category_name = models.CharField(max_length=100)
    serial = models.BigIntegerField()
    inventory = models.BigIntegerField()
    date = models.DateTimeField()
    storage_building = models.IntegerField()
    storage_room = models.IntegerField()
    condition_id = models.BigIntegerField()
    condition_works = models.BooleanField()
    condition_location = models.CharField(max_length=100)
