# Generated by Django 3.0.3 on 2020-03-02 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concoreapi', '0002_auto_20200228_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='Empresa',
            new_name='Social',
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='Empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concoreapi.Empresa'),
        ),
    ]
