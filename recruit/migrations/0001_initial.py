# Generated by Django 4.0.5 on 2022-06-22 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='회사명')),
                ('country', models.CharField(max_length=20, verbose_name='국가')),
                ('region', models.CharField(max_length=20, verbose_name='지역')),
            ],
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, verbose_name='채용포지션')),
                ('reward', models.IntegerField(default=0, verbose_name='채용보상금')),
                ('description', models.TextField(verbose_name='채용내용')),
                ('tech_stack', models.CharField(max_length=100, verbose_name='사용기술')),
                ('applicant', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='지원자')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_jobposting', to='recruit.company', verbose_name='회사_id')),
            ],
        ),
    ]
