from django.db import models
from django.utils import timezone

# ↓これはただのテストモデル
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# レコメンドテーブルのモデル
class Recommend(models.Model):
    #id                 = models.IntegerField(primary_key=True)  # AutoField?
    ym                 = models.CharField(db_column='YM', max_length=6)
    poi_id             = models.CharField(db_column='POI_ID', max_length=18)
    poi                = models.CharField(db_column='POI', max_length=100, blank=True, null=True)
    a0                 = models.CharField(max_length=2, blank=True, null=True)
    a1                 = models.CharField(max_length=3, blank=True, null=True)
    a2                 = models.CharField(max_length=3, blank=True, null=True)
    a3                 = models.CharField(max_length=3, blank=True, null=True)
    arr_an             = models.CharField(max_length=300, blank=True, null=True)
    c_rank             = models.IntegerField(db_column='C_RANK', blank=True, null=True)
    score_rank         = models.FloatField(db_column='SCORE_RANK', blank=True, null=True)
    recommend_id       = models.IntegerField(db_column='RECOMMEND_ID', blank=True, null=True)
    recommend_text     = models.CharField(db_column='RECOMMEND_TEXT', max_length=200, blank=True, null=True)
    available_flg      = models.CharField(db_column='AVAILABLE_FLG', max_length=1, blank=True, null=True)
    available_str_date = models.DateField(db_column='AVAILABLE_STR_DATE', blank=True, null=True)
    available_end_date = models.DateField(db_column='AVAILABLE_END_DATE', blank=True, null=True)
    create_date        = models.DateField(db_column='CREATE_DATE')

    class Meta:
        #managed = False #Falseにしておくとmigrationの対象外となる
        db_table = 'recommend'

    def publish(self):
        self.save()

    def __str__(self):
        return self.poi

