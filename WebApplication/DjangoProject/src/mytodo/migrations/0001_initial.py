# Generated by Django 4.2 on 2024-01-10 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('status', models.IntegerField(choices=[(0, '進行中'), (1, '完了')], default=0)),
            ],
        ),
    ]
