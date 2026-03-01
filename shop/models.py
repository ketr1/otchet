# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Discounts(models.Model):
    percent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'discounts'


class Manufactures(models.Model):
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'manufactures'


class OrderProducts(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_products'
        unique_together = (('order', 'product'),)


class OrderStatuses(models.Model):
    status = models.CharField()

    class Meta:
        managed = False
        db_table = 'order_statuses'


class Orders(models.Model):
    order_date = models.DateField()
    delivery_date = models.DateField()
    pickup_point = models.ForeignKey('PickupPoints', models.DO_NOTHING)
    client_user_id = models.IntegerField()
    status = models.ForeignKey(OrderStatuses, models.DO_NOTHING)
    pickup_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orders'


class PickupPoints(models.Model):
    postal_code = models.CharField(max_length=10)
    city = models.CharField()
    street = models.CharField()
    house = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pickup_points'


class ProductCategories(models.Model):
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'product_categories'


class ProductUnits(models.Model):
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'product_units'


class Products(models.Model):
    article = models.CharField(unique=True)
    name = models.CharField()
    unit = models.ForeignKey(ProductUnits, models.DO_NOTHING)
    price = models.IntegerField()
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)
    manufacturer = models.ForeignKey(Manufactures, models.DO_NOTHING)
    category = models.ForeignKey(ProductCategories, models.DO_NOTHING)
    discount = models.ForeignKey(Discounts, models.DO_NOTHING)
    stock_qty = models.IntegerField()
    description = models.TextField()
    photo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Roles(models.Model):
    role = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Suppliers(models.Model):
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'suppliers'


class Users(models.Model):
    fio = models.CharField()
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    login = models.CharField(unique=True)
    password = models.CharField()

    class Meta:
        managed = False
        db_table = 'users'
