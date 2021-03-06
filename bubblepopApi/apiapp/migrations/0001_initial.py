# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 10:20
from __future__ import unicode_literals

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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='제목')),
                ('content', models.TextField(verbose_name='본문')),
                ('morphemed_content', models.TextField(verbose_name='형태소 본문')),
                ('writer', models.CharField(max_length=10, verbose_name='작성자')),
                ('published_at', models.DateField(verbose_name='발행일')),
                ('article_rss', models.URLField(verbose_name='RSS 링크')),
                ('article_url', models.URLField(verbose_name='URL 링크')),
                ('category', models.CharField(max_length=10, verbose_name='분류')),
            ],
        ),
        migrations.CreateModel(
            name='CachedArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.Article', verbose_name='기사')),
            ],
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_id', models.IntegerField(verbose_name='클러스터 식별자')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
                ('rss_list', models.TextField(verbose_name='RSS 리스트')),
                ('icon', models.URLField(verbose_name='아이콘')),
            ],
        ),
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity', models.FloatField(verbose_name='유사도')),
                ('reports', models.IntegerField(default=0, verbose_name='A-B 연결 버그 리포트 수')),
                ('article_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_article_a', to='apiapp.Article', verbose_name='기사A')),
                ('article_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_article_b', to='apiapp.Article', verbose_name='기사B')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='제보내용')),
                ('article_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_article_a', to='apiapp.Article', verbose_name='기사A')),
                ('article_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_article_b', to='apiapp.Article', verbose_name='기사B')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
        ),
        migrations.CreateModel(
            name='UserBlackList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.Media', verbose_name='언론사')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
        ),
        migrations.AddField(
            model_name='cachedarticle',
            name='cluster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.Cluster', verbose_name='클러스터'),
        ),
        migrations.AddField(
            model_name='article',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.Media', verbose_name='신문사'),
        ),
    ]
