# Generated by Django 4.1.2 on 2022-11-16 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_estudiante_profesor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='ID',
            new_name='id',
        ),
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.TextField()),
                ('imagen', models.URLField()),
                ('fecha', models.DateTimeField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.profesor')),
            ],
        ),
    ]