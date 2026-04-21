from django.contrib import admin
# model.pyで作成したProductモデルをインポート
from .models import Product, Category
from django.utils.safestring import mark_safe
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # 表示するフィールドを配列で指定する
    list_display = ('id','name','price','category','image')
    # 検索対象のフィールドを配列で指定する
    search_fields = ('name',)
    # 絞り込みフィルターにカテゴリを追加
    list_filter = ('category',)
    
    def image(self,obj):
        # mark_safeはHTMLタグを有効化するための関数
        return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)

# 管理画面に登録
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
