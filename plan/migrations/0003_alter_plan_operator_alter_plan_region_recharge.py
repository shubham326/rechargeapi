# Generated by Django 4.0.3 on 2022-05-03 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_rename_name_region_rname_alter_plan_operator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='op', to='plan.operator'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='re', to='plan.region'),
        ),
        migrations.CreateModel(
            name='recharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField()),
                ('price', models.IntegerField()),
                ('Plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_set', to='plan.plan')),
            ],
        ),
    ]
