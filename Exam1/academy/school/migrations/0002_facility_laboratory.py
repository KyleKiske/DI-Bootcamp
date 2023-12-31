# Generated by Django 4.2.4 on 2023-08-20 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=50)),
                ('usage_purpose', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('facility_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='school.facility')),
                ('equipment_list', models.TextField()),
            ],
            bases=('school.facility',),
        ),
    ]
