# Generated by Django 4.2.2 on 2023-07-24 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EmissionCause',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EmissionFactor',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='EmissionScope',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCatalogue',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('manufacturer_product_id', models.CharField(max_length=255, null=True)),
                ('name_clean', models.CharField(max_length=255, null=True)),
                ('old_import_id', models.FloatField(null=True)),
                ('old_name', models.CharField(max_length=255, null=True)),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='ProductWeight',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('measured', models.FloatField(null=True)),
                ('verified', models.FloatField(null=True)),
                ('manufacturer', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Waste',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TransportStep',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('distance', models.IntegerField()),
                ('emission_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.emissionfactor')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.unit')),
            ],
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('reference_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.productcatalogue')),
            ],
        ),
        migrations.AddField(
            model_name='productcatalogue',
            name='product_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.productgroup'),
        ),
        migrations.AddField(
            model_name='productcatalogue',
            name='product_weight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.productweight'),
        ),
        migrations.AddField(
            model_name='emissionfactor',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.unit'),
        ),
        migrations.CreateModel(
            name='CenterWaste',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.FloatField()),
                ('year', models.IntegerField()),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.center')),
                ('emission_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.emissionfactor')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.unit')),
                ('waste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.waste')),
            ],
        ),
        migrations.CreateModel(
            name='CenterResource',
            fields=[
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('year', models.IntegerField()),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.center')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.resource')),
                ('transport_emission_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transport_emission_factors', to='database.emissionfactor')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.unit')),
                ('use_emission_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='use_emission_factors', to='database.emissionfactor')),
            ],
        ),
        migrations.CreateModel(
            name='CenterProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_product_doc_id', models.IntegerField(null=True)),
                ('product_doc_runnning_id', models.IntegerField()),
                ('department_id', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('price', models.FloatField()),
                ('product_group_intern', models.CharField(max_length=255, null=True)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.center')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.productcatalogue')),
            ],
        ),
    ]
