# Generated by Django 2.1.7 on 2019-04-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VerboseTitle', models.CharField(max_length=50, verbose_name='Название фильтра')),
                ('Title', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Filter',
                'verbose_name_plural': 'Filters',
                'managed': True,
            },
        ),
    ]
