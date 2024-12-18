# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Item(models.Model):

    #__Item_FIELDS__
    itemid = models.IntegerField(null=True, blank=True)
    itemname = models.CharField(max_length=255, null=True, blank=True)
    itemcode = models.IntegerField(null=True, blank=True)
    itemgroup1id = models.ForeignKey(ItemGroup1, on_delete=models.CASCADE)
    itemgroup2id = models.ForeignKey(ItemGroup2, on_delete=models.CASCADE)
    itemgroup3id = models.ForeignKey(ItemGroup3, on_delete=models.CASCADE)
    creationdate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Item_FIELDS__END

    class Meta:
        verbose_name        = _("Item")
        verbose_name_plural = _("Item")


class Users(models.Model):

    #__Users_FIELDS__
    usergroupid = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    creationdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    employeeid = models.ForeignKey(Employee, on_delete=models.CASCADE)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class Employee(models.Model):

    #__Employee_FIELDS__
    employeeid = models.IntegerField(null=True, blank=True)
    employeename = models.CharField(max_length=255, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    contactno = models.IntegerField(null=True, blank=True)
    whatsappno = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    cityid = models.ForeignKey(City, on_delete=models.CASCADE)
    countryid = models.ForeignKey(Country, on_delete=models.CASCADE)
    address2 = models.CharField(max_length=255, null=True, blank=True)

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")


class Customer(models.Model):

    #__Customer_FIELDS__
    customerid = models.IntegerField(null=True, blank=True)
    customername = models.CharField(max_length=255, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    contactno = models.IntegerField(null=True, blank=True)
    whatsappno = models.IntegerField(null=True, blank=True)
    phoneno = models.IntegerField(null=True, blank=True)
    cityid = models.IntegerField(null=True, blank=True)
    countryid = models.ForeignKey(Country, on_delete=models.CASCADE)
    customercode = models.ForeignKey(City, on_delete=models.CASCADE)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Country(models.Model):

    #__Country_FIELDS__
    countryid = models.IntegerField(null=True, blank=True)
    countryname = models.CharField(max_length=255, null=True, blank=True)

    #__Country_FIELDS__END

    class Meta:
        verbose_name        = _("Country")
        verbose_name_plural = _("Country")


class City(models.Model):

    #__City_FIELDS__
    cityname = models.CharField(max_length=255, null=True, blank=True)
    countryid = models.ForeignKey(Country, on_delete=models.CASCADE)

    #__City_FIELDS__END

    class Meta:
        verbose_name        = _("City")
        verbose_name_plural = _("City")


class Supplier(models.Model):

    #__Supplier_FIELDS__
    supplierid = models.IntegerField(null=True, blank=True)
    suppliername = models.CharField(max_length=255, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    contactno = models.IntegerField(null=True, blank=True)
    phoneno = models.IntegerField(null=True, blank=True)
    whatsappno = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    cityid = models.ForeignKey(City, on_delete=models.CASCADE)
    countryid = models.ForeignKey(Country, on_delete=models.CASCADE)

    #__Supplier_FIELDS__END

    class Meta:
        verbose_name        = _("Supplier")
        verbose_name_plural = _("Supplier")


class Itemgroup1(models.Model):

    #__Itemgroup1_FIELDS__
    itemgroup1id = models.IntegerField(null=True, blank=True)
    itemgroup1name = models.CharField(max_length=255, null=True, blank=True)

    #__Itemgroup1_FIELDS__END

    class Meta:
        verbose_name        = _("Itemgroup1")
        verbose_name_plural = _("Itemgroup1")


class Itemgroup2(models.Model):

    #__Itemgroup2_FIELDS__
    itemgroup2id = models.IntegerField(null=True, blank=True)
    itemgroup2name = models.CharField(max_length=255, null=True, blank=True)

    #__Itemgroup2_FIELDS__END

    class Meta:
        verbose_name        = _("Itemgroup2")
        verbose_name_plural = _("Itemgroup2")


class Itemgroup3(models.Model):

    #__Itemgroup3_FIELDS__
    itemgroup3id = models.IntegerField(null=True, blank=True)
    itemgroup3name = models.CharField(max_length=255, null=True, blank=True)

    #__Itemgroup3_FIELDS__END

    class Meta:
        verbose_name        = _("Itemgroup3")
        verbose_name_plural = _("Itemgroup3")



#__MODELS__END
