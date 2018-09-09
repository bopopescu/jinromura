from django.db import models

# Create your models here.
class Village(models.Model):
    name = models.CharField(max_length=40)
    people = models.IntegerField(default=0)
    level = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    citizen = models.IntegerField(default=0)
    werewolf = models.IntegerField(default=0)
    hunter = models.IntegerField(default=0)
    f_teller = models.IntegerField(default=0)
    shaman = models.IntegerField(default=0)
    dspcho = models.IntegerField(default=0)
    bomber = models.IntegerField(default=0)
    straw_doll = models.IntegerField(default=0)
    fox = models.IntegerField(default=0)
    nekomata = models.IntegerField(default=0)
    black_cat = models.IntegerField(default=0)
    thief = models.IntegerField(default=0)
    psyco = models.IntegerField(default=0)
    martydom = models.IntegerField(default=0)
    bakery = models.IntegerField(default=0)
    mayor = models.IntegerField(default=0)
    trap_nurses = models.IntegerField(default=0)
    big_wolf = models.IntegerField(default=0)
    fugitive = models.IntegerField(default=0)
    zombi = models.IntegerField(default=0)
    teruteru = models.IntegerField(default=0)
    wiseman = models.IntegerField(default=0)
    slave = models.IntegerField(default=0)
    aristcracy = models.IntegerField(default=0)
    wolfboy = models.IntegerField(default=0)
    santa = models.IntegerField(default=0)
    pigman = models.IntegerField(default=0)
    cursed = models.IntegerField(default=0)
    dictator = models.IntegerField(default=0)
    assassin = models.IntegerField(default=0)
    sorcerer = models.IntegerField(default=0)
    bat = models.IntegerField(default=0)
    queen = models.IntegerField(default=0)
    sasaki = models.IntegerField(default=0)
    fanatic = models.IntegerField(default=0)
    goyoku = models.IntegerField(default=0)
    wisewolf = models.IntegerField(default=0)
    doctor = models.IntegerField(default=0)

    #objectの名前呼び出された時にnameを出力する
    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=200)
    ability = models.CharField(max_length=200)
    condition = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    #objectの名前呼び出された時にnameを出力する
    def __str__(self):
        return self.name
