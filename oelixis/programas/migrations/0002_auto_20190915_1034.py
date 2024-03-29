# Generated by Django 2.1 on 2019-09-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Transação',
            },
        ),
        migrations.AlterModelOptions(
            name='produto',
            options={'verbose_name': 'Produto'},
        ),
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
