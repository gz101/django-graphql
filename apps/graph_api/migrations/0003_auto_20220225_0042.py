# Generated by Django 3.1.7 on 2022-02-25 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph_api', '0002_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address', to='graph_api.address'),
        ),
    ]