# Generated by Django 2.2 on 2019-05-15 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='daerah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinsi', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tb_daerah',
            },
        ),
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('luas', models.IntegerField()),
                ('tahun', models.IntegerField()),
                ('provinsi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lahan.daerah')),
            ],
            options={
                'db_table': 'tb_area',
            },
        ),
    ]