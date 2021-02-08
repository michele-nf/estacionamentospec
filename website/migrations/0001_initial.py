# Generated by Django 3.1.5 on 2021-02-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('mensagem', models.TextField()),
                ('receber_noticias', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
