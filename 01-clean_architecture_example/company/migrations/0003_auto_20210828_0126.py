# Generated by Django 3.2.6 on 2021-08-28 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_shop_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='company',
            field=models.ForeignKey(db_column='company_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shops', related_query_name='shop_id', to='company.company'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='items',
            field=models.ManyToManyField(related_name='shops', related_query_name='shop_id', through='company.ShopItemRel', to='company.Item'),
        ),
    ]