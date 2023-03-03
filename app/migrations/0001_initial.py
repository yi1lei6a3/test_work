# Generated by Django 4.1.7 on 2023-03-03 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreeMenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('verbose_name', models.CharField(blank=True, max_length=255, verbose_name='Verbose name')),
            ],
            options={
                'verbose_name': 'Menu category',
                'verbose_name_plural': 'Menu categories',
            },
        ),
        migrations.CreateModel(
            name='TreeMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('path', models.CharField(blank=True, max_length=1000, verbose_name='Link')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.treemenucategory', verbose_name='Category')),
                ('parent', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.treemenu', verbose_name='Parent element')),
            ],
            options={
                'verbose_name': 'Menu item',
                'verbose_name_plural': 'Menu items',
            },
        ),
    ]
