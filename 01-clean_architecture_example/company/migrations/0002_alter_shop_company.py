# Generated by Django 3.2.6 on 2021-08-27 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='company',
            field=models.ForeignKey(db_column='company_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shops', related_query_name='shop', to='company.company'),
        ),
    ]
