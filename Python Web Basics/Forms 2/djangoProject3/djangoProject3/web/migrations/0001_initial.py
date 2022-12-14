# Generated by Django 4.1.2 on 2022-10-18 16:34

from django.db import migrations, models
import djangoProject3.web.validate


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=25, validators=[djangoProject3.web.validate.validate_text])),
                ('priority', models.IntegerField(validators=[djangoProject3.web.validate.ValidationRange(1, 10)])),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
