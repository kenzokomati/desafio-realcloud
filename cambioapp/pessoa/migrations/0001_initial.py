# Generated by Django 5.1.3 on 2024-11-17 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_nascimento', models.DateField()),
                ('quantia', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
