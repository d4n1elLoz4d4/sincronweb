# Generated by Django 2.2.3 on 2022-10-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='subcategoria',
            fields=[
                ('idSubcategoria', models.AutoField(primary_key=True, serialize=False)),
                ('subcategoriaDescripcion', models.CharField(max_length=45, verbose_name='Descripción')),
                ('subcategoriaActivo', models.CharField(max_length=1, verbose_name='Estado')),
                ('Categoria_idCategoria', models.CharField(max_length=11, verbose_name='Categoria')),
            ],
        ),
    ]