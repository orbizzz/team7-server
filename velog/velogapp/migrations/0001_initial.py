# Generated by Django 4.1 on 2023-01-24 02:15

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
            name='Post',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('thumbnail', models.ImageField(null=True, upload_to='')),
                ('title', models.TextField()),
                ('preview', models.CharField(max_length=150, null=True)),
                ('content', models.TextField()),
                ('is_private', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),                
                ('like_user', models.ManyToManyField(blank=True, related_name='user_who_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ReadingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts_liked', models.ManyToManyField(related_name='posts_liked', to='velogapp.post')),
                ('posts_viewed', models.ManyToManyField(related_name='posts_viewed', to='velogapp.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='velogapp.series'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='velogapp.tag'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='velogapp.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='velogapp.post')),
            ],
        ),
    ]
