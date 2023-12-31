# Generated by Django 4.2.5 on 2023-10-04 10:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_book_genre_alter_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='生成一個在圖書館獨有的書本ID', primary_key=True, serialize=False, verbose_name='編號'),
        ),
    ]
