# Generated by Django 2.1.15 on 2020-01-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_ks', '0009_auto_20200102_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinggou',
            name='jc_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='教材号'),
        ),
        migrations.AlterField(
            model_name='jiaocai',
            name='jc_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='教材号'),
        ),
    ]
