# Generated by Django 4.0.2 on 2024-04-19 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_guild_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.race'),
        ),
    ]