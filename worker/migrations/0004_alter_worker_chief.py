# Generated by Django 3.2 on 2021-12-28 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0003_alter_worker_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='chief',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjects', to='worker.worker'),
        ),
    ]
