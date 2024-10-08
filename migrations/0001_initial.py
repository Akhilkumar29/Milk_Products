# Generated by Django 5.0.6 on 2024-07-14 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('WES', 'western wear'), ('BW', 'Bridal wear'), ('PW', 'Party wear'), ('EW', 'Ethnic wear'), ('FW', 'Fussion wear'), ('WIN', 'winter wear'), ('AW', 'Active wear'), ('SW', 'Summer wear')], max_length=4)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
