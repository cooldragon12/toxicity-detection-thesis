# Generated by Django 4.2 on 2023-05-22 11:28

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import report.models
import report.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerDemography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('province', models.CharField(max_length=50)),
                ('ethnicity', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, validators=[report.validators.validate_username_tag])),
                ('average_hours', models.IntegerField(verbose_name='How many hours do you play on average?')),
                ('frequency', models.IntegerField(verbose_name='How often do you play?')),
                ('in_game_rank', models.CharField(max_length=50, verbose_name='What is your in-game rank?')),
                ('often_server', models.CharField(max_length=50, verbose_name='In which server do you play the most?')),
            ],
            options={
                'verbose_name_plural': 'Player Demographics',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.CharField(default=report.models.Entry.generate_id, max_length=8, primary_key=True, serialize=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('text', models.CharField(max_length=1000)),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='chat_screenshots')),
                ('description', models.TextField(blank=True, null=True)),
                ('emotion', models.CharField(blank=True, max_length=50, null=True)),
                ('toxicity', models.CharField(blank=True, max_length=50, null=True)),
                ('sentiment', models.CharField(blank=True, max_length=50, null=True)),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_entries', to='report.playerdemography')),
            ],
            options={
                'verbose_name_plural': 'Entries',
                'ordering': ['-date_created'],
            },
        ),
    ]
