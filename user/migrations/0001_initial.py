# Generated by Django 4.0.5 on 2022-06-22 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='사용자 계정')),
                ('email', models.EmailField(max_length=100, verbose_name='이메일 주소')),
                ('password', models.CharField(max_length=60, verbose_name='비밀번호')),
                ('fullname', models.CharField(max_length=20, verbose_name='이름')),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
                ('company', models.CharField(max_length=20, verbose_name='회사')),
                ('birthday', models.DateField(verbose_name='생일')),
                ('age', models.IntegerField(verbose_name='나이')),
            ],
        ),
    ]
