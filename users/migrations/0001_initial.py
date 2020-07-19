# Generated by Django 2.2.12 on 2020-07-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.CharField(max_length=100, verbose_name='appid')),
                ('name', models.CharField(max_length=100, verbose_name='权限名')),
                ('create_name', models.CharField(max_length=100, verbose_name='创建人')),
                ('aut1', models.IntegerField(default=0)),
                ('aut2', models.IntegerField(default=0)),
                ('aut3', models.IntegerField(default=0)),
                ('aut4', models.IntegerField(default=0)),
                ('aut5', models.IntegerField(default=0)),
                ('aut6', models.IntegerField(default=0)),
                ('aut7', models.IntegerField(default=0)),
                ('aut8', models.IntegerField(default=0)),
                ('aut9', models.IntegerField(default=0)),
                ('aut10', models.IntegerField(default=0)),
                ('aut11', models.IntegerField(default=0)),
                ('aut12', models.IntegerField(default=0)),
                ('aut13', models.IntegerField(default=0)),
                ('aut14', models.IntegerField(default=0)),
                ('aut15', models.IntegerField(default=0)),
                ('aut16', models.IntegerField(default=0)),
                ('aut17', models.IntegerField(default=0)),
                ('aut18', models.IntegerField(default=0)),
                ('aut19', models.IntegerField(default=0)),
                ('aut20', models.IntegerField(default=0)),
                ('is_delete', models.IntegerField(default=0, verbose_name='删除标记')),
                ('t_code', models.CharField(max_length=100, verbose_name='后台ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, verbose_name='用户id')),
                ('name', models.CharField(max_length=80, verbose_name='登入名')),
                ('password', models.CharField(max_length=80, verbose_name='登入密码')),
                ('nickname', models.CharField(max_length=20, verbose_name='姓名')),
                ('openid', models.CharField(max_length=100, verbose_name='openid')),
                ('appid', models.CharField(max_length=100, verbose_name='appid')),
                ('is_delete', models.IntegerField(default=0, verbose_name='删除标记')),
                ('developer', models.IntegerField(default=0, verbose_name='开发者标识')),
                ('transaction_code', models.CharField(max_length=100, verbose_name='后台ID')),
                ('ip', models.CharField(max_length=100, verbose_name='注册ip')),
                ('vip', models.IntegerField(default=0, verbose_name='VIP标识')),
                ('vip_time', models.DateTimeField(auto_now_add=True)),
                ('auth_name', models.CharField(max_length=100, verbose_name='权限名')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
