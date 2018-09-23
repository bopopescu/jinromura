from django.db import models

# Create your models here.
class Village(models.Model):
    name = models.CharField('村名',max_length=40)
    people = models.IntegerField('人数',default=0)
    level = models.IntegerField('難易度',default=0)
    category = models.CharField('種類',max_length=200)
    description = models.CharField('説明',max_length=200)
    citizen = models.IntegerField('市民',default=0)
    werewolf = models.IntegerField('人狼',default=0)
    hunter = models.IntegerField('狩人',default=0)
    f_teller = models.IntegerField('占い師',default=0)
    shaman = models.IntegerField('霊能者',default=0)
    dspcho = models.IntegerField('狂人',default=0)
    straw_doll = models.IntegerField('わら人形',default=0)
    lover = models.IntegerField('恋人',default=0)
    fox = models.IntegerField('妖狐',default=0)
    nekomata = models.IntegerField('猫又',default=0)
    black_cat = models.IntegerField('黒猫',default=0)
    thief = models.IntegerField('怪盗',default=0)
    psyco = models.IntegerField('サイコ',default=0)
    martydom = models.IntegerField('殉教者',default=0)
    bakery = models.IntegerField('パン屋',default=0)
    mayor = models.IntegerField('市民',default=0)
    trap_nurses = models.IntegerField('罠師',default=0)
    big_wolf = models.IntegerField('大狼',default=0)
    fugitive = models.IntegerField('逃亡者',default=0)
    zombi = models.IntegerField('ゾンビ',default=0)
    teruteru = models.IntegerField('てるてる坊主',default=0)
    wiseman = models.IntegerField('賢者',default=0)
    slave = models.IntegerField('奴隷',default=0)
    aristcracy = models.IntegerField('貴族',default=0)
    wolfboy = models.IntegerField('狼少年',default=0)
    santa = models.IntegerField('サンタ',default=0)
    pigman = models.IntegerField('豚男',default=0)
    cursed = models.IntegerField('呪われし者',default=0)
    dictator = models.IntegerField('独裁者',default=0)
    assassin = models.IntegerField('暗殺者',default=0)
    sorcerer = models.IntegerField('妖術師',default=0)
    bat = models.IntegerField('コウモリ',default=0)
    queen = models.IntegerField('女王',default=0)
    sasaki = models.IntegerField('ささやく狂人',default=0)
    fanatic = models.IntegerField('狂信者',default=0)
    goyoku = models.IntegerField('強欲な人狼',default=0)
    wisewolf = models.IntegerField('賢狼',default=0)
    doctor = models.IntegerField('医者',default=0)

    #objectの名前呼び出された時にnameを出力する
    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField('キャラ名',max_length=40)
    category = models.CharField('種類',max_length=200)
    ability = models.CharField('能力',max_length=200)
    condition = models.CharField('勝つ条件',max_length=200)
    description = models.CharField('説明',max_length=200)

    #objectの名前呼び出された時にnameを出力する
    def __str__(self):
        return self.name
