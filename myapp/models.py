from django.db import models

class  Core(models.Model):
    R_loc=models.CharField(max_length=100)

    def __str__(self):
        return "location   "+self.R_loc

class Rest(models.Model):
    loc=models.ForeignKey(Core,on_delete=models.CASCADE)

    Rname=models.CharField(max_length=500)
    Rimg=models.CharField(max_length=1000)
    rating=models.IntegerField(default=0)
    usrrating=models.FloatField(default=0.0)
    review=models.TextField(max_length=1000)
    catg=models.CharField(max_length=500)

    def __str__(self):
        return "name: "+self.Rname+" categ:"+self.catg
class Menu(models.Model):
    m_rest=models.ForeignKey(Rest,on_delete=models.CASCADE)
    mcatg=models.CharField(max_length=100)
    mtitle=models.CharField(max_length=500)
    mprice=models.FloatField(default=0.0)
    mimg=models.CharField(max_length=1000)

    def __str__(self):
        return "menu  " + self.mtitle+" categ:"+self.mcatg

class Order(models.Model):
    o_id=models.ForeignKey(Menu,on_delete=models.CASCADE)
    o_qt=models.IntegerField(default=0)
    pay=models.IntegerField(default=0)
    d_time=models.DateTimeField(default=None)
    user_name=models.CharField(max_length=100)

    def __str__(self):
        return ' orderid'+str(self.id)
