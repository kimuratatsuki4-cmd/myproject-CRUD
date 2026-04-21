from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    # 金額を正の整数型で定義する
    price = models.PositiveBigIntegerField()
    # categoryクラスに対する外部キーを設定（１：多　＝ category : product）
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 画像フィールドの追加、任意項目、デフォルト値の設定
    img = models.ImageField(blank=True,default='noImage.png')
    
    def __str__(self):
        return self.name
    
    # 新奇作成・編集完了時のリダイレクト設定
    def get_absolute_url(self):
        # 名前からURLを取得
        return reverse('list')
    