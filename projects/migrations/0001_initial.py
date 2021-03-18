# Generated by Django 2.2.2 on 2019-10-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название проекта')),
                ('name1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Уникальный номер проекта')),
                ('fond', models.CharField(blank=True, max_length=200, null=True, verbose_name='Фонд')),
                ('foundation', models.CharField(blank=True, max_length=200, null=True, verbose_name='Основание для проведения проекта')),
                ('start', models.CharField(blank=True, max_length=200, null=True, verbose_name='Дата начала проекта')),
                ('finish', models.CharField(blank=True, max_length=200, null=True, verbose_name='Дата конца проекта')),
                ('pr_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Тип проекта')),
                ('pr_cost', models.CharField(blank=True, max_length=200, null=True, verbose_name='Полная сумма проекта')),
                ('pr_org', models.CharField(blank=True, max_length=200, null=True, verbose_name='Организация')),
                ('pr_also', models.CharField(blank=True, max_length=200, null=True, verbose_name='Соисполнители')),
                ('pr_notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='Примечания')),
                ('pr_comments', models.CharField(blank=True, max_length=200, null=True, verbose_name='Комментарии')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]