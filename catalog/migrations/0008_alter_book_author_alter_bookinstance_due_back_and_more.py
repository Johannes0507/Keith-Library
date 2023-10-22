# Generated by Django 4.2.5 on 2023-10-04 07:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_bookinstance_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author', verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(blank=True, null=True, verbose_name='歸還日期'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='生成一個在圖書館獨有的書本ID', primary_key=True, serialize=False, verbose_name='自動生成編號'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='imprint',
            field=models.CharField(max_length=200, verbose_name='出版商名稱'),
        ),
    ]