# Generated by Django 5.0.4 on 2024-07-28 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analyser', '0002_alter_sentimentanalysis_sentiment_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentimentanalysis',
            name='sentiment_label',
            field=models.CharField(max_length=10),
        ),
    ]
