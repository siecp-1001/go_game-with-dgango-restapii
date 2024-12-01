# Generated by Django 5.0.6 on 2024-12-01 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_state', models.JSONField(default=dict)),
                ('next_color', models.CharField(choices=[('BLACK', 'Black'), ('WHITE', 'White')], max_length=5)),
                ('winner', models.CharField(blank=True, max_length=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]