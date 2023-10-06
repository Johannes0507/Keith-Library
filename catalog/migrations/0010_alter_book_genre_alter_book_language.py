# Generated by Django 4.2.5 on 2023-10-04 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_bookinstance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='選擇你的書本類別', to='catalog.genre', verbose_name='書本類型'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='選擇你的書本語言種類', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language', verbose_name='書本語言'),
        ),
    ]
