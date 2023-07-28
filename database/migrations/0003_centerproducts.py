# Generated by Django 4.2.2 on 2023-07-25 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_material_productgroup_emission_factor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CenterProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('weight_per_product', models.FloatField()),
                ('reference_emission_per_weight', models.FloatField()),
                ('total_emission', models.FloatField()),
                ('year', models.IntegerField()),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.center')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.productcatalogue')),
            ],
            options={
                'unique_together': {('center', 'year', 'product')},
            },
        ),
    ]