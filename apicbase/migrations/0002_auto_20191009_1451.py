# Generated by Django 2.2.6 on 2019-10-09 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apicbase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient_cost',
            new_name='cost',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient_unit_size',
            new_name='unit_size',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_name',
            new_name='name',
        ),
    ]
