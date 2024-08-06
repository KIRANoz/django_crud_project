# Generated by Django 5.0.7 on 2024-08-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Price', models.IntegerField()),
                ('Types', models.CharField(choices=[('plastic', 'plastic'), ('steel', 'steel'), ('wooden', 'wooden')], max_length=17)),
                ('Details', models.TextField()),
            ],
        ),
    ]