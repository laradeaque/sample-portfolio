# Generated by Django 4.2.8 on 2024-02-03 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=200)),
                ('date_published', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('blog_image', models.ImageField(upload_to='media/')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.tag')),
            ],
        ),
    ]
