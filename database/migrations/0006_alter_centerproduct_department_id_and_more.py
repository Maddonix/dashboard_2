# Generated by Django 4.2.2 on 2023-07-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_alter_centerproduct_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centerproduct',
            name='department_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='centerproduct',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='centerproduct',
            name='product_doc_runnning_id',
            field=models.IntegerField(null=True),
        ),
    ]
