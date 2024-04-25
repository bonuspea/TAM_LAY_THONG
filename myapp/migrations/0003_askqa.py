# Generated by Django 5.0.4 on 2024-04-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_officer'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskQA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='ชื่อผู้ติดต่อ')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='อีเมล์')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='หัวข้อ')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='รายละเอียด')),
            ],
        ),
    ]
