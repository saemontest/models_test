# Generated by Django 2.2.6 on 2019-10-16 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_model', '0005_abssum'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsMethodExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('named', models.CharField(default='Name AbsMethod class', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]