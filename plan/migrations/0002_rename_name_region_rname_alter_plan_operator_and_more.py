# Generated by Django 4.0.3 on 2022-05-03 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='region',
            old_name='name',
            new_name='rname',
        ),
        migrations.AlterField(
            model_name='plan',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operattor_set', to='plan.operator'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Region_set', to='plan.region'),
        ),
    ]
