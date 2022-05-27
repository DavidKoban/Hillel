# Generated by Django 3.2.12 on 2022-05-26 12:57

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Ivan', max_length=50)),
                ('username', models.CharField(db_index=True, max_length=255, null=True, unique=True)),
                ('surname', models.CharField(default='Ivanov', max_length=50)),
                ('patronymic', models.CharField(default='Ivanovich', max_length=50, null=True)),
                ('email', models.EmailField(default='owner@mail.com', max_length=254, unique=True)),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'swappable': 'AUTH_USER_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Ivan', max_length=50)),
                ('description', models.CharField(default='Description', max_length=200, null=True)),
                ('start_price', models.FloatField(default=0)),
                ('end_price', models.FloatField(null=True)),
                ('auctioneer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Ivan', max_length=50)),
                ('photo', models.ImageField(null=True, upload_to='img')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sloter.slot')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
