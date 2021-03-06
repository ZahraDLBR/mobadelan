# Generated by Django 2.1 on 2018-08-24 11:30

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_manager', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Contact_msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('text', models.CharField(max_length=255, verbose_name='message')),
                ('name', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=11)),
                ('seen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.PositiveIntegerField(default=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactions_type', models.CharField(choices=[('RCH', 'recharge wallet'), ('OUT', 'outer transfer'), ('IN', 'inner transfer'), ('EPF', 'university of EPFL'), ('ETH', 'university of ETH'), ('OXF', 'university of Oxford'), ('MIT', 'university of MIT'), ('GRE', 'GRE exam'), ('ILS', 'IELTS exam'), ('TFL', 'TOEFL exam')], default=None, max_length=3)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('value', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bank_account_number', models.CharField(max_length=16)),
                ('phone_number', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bank_account', models.CharField(default='111111111111111', max_length=16)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('salary', models.PositiveIntegerField(default=1000000)),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='corroborator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Staff'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Customer'),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('email',)},
        ),
    ]
