# Generated by Django 3.0.11 on 2020-12-21 04:51

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("api", "0002_auto_20201130_0206"),
    ]

    operations = [
        migrations.CreateModel(
            name="DailyDigestRecord",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("timestamp", models.DateTimeField(blank=True, null=True)),
                ("messages", models.TextField(blank=True, max_length=1048, null=True)),
                ("count", models.IntegerField(null=True)),
                ("data", models.TextField(blank=True, max_length=4096, null=True)),
            ],
            options={
                "verbose_name": "Daily Digest - Record",
                "verbose_name_plural": "Daily Digest - Records",
            },
        ),
        migrations.CreateModel(
            name="DiscordChannel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("channel_id", models.CharField(max_length=4000, unique=True)),
                ("server_id", models.CharField(max_length=4000)),
                ("name", models.CharField(max_length=4000)),
            ],
            options={
                "verbose_name": "Channel",
                "verbose_name_plural": "Channels",
            },
        ),
        migrations.CreateModel(
            name="LaunchNotificationRecord",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("launch_id", models.UUIDField(default=uuid.uuid4, editable=False)),
                (
                    "wasNotifiedWebcastLive",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedTwentyFourHour",
                    models.BooleanField(blank=True, default=False),
                ),
                ("wasNotifiedOneHour", models.BooleanField(blank=True, default=False)),
                (
                    "wasNotifiedTenMinutes",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedOneMinute",
                    models.BooleanField(blank=True, default=False),
                ),
                ("wasNotifiedInFlight", models.BooleanField(blank=True, default=False)),
                ("wasNotifiedSuccess", models.BooleanField(blank=True, default=False)),
                (
                    "wasNotifiedTwentyFourHourTwitter",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedOneHourTwitter",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedTenMinutesTwitter",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedOneMinuteTwitter",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedInFlightTwitter",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedSuccessTwitter",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedWebcastLiveTwitter",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedDailyDigest",
                    models.BooleanField(blank=True, default=False),
                ),
                ("last_twitter_post", models.DateTimeField(blank=True, null=True)),
                ("last_notification_sent", models.DateTimeField(blank=True, null=True)),
                (
                    "last_notification_recipient_count",
                    models.IntegerField(blank=True, null=True),
                ),
                ("last_net_stamp", models.DateTimeField(blank=True, null=True)),
                (
                    "last_net_stamp_timestamp",
                    models.DateTimeField(blank=True, null=True),
                ),
                (
                    "wasNotifiedTwentyFourHourDiscord",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedOneHourDiscord",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedTenMinutesDiscord",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedOneMinutesDiscord",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedInFlightDiscord",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedSuccessDiscord",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "wasNotifiedWebcastDiscord",
                    models.BooleanField(blank=True, default=False),
                ),
            ],
            options={
                "verbose_name": "Notification Record",
                "verbose_name_plural": "Notification Records",
            },
        ),
        migrations.CreateModel(
            name="NewsNotificationChannel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("channel_id", models.CharField(max_length=4000, unique=True)),
                ("server_id", models.CharField(max_length=4000)),
                ("name", models.CharField(max_length=4000)),
                ("subscribed", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "News Notification Channel",
                "verbose_name_plural": "News Notification Channels",
            },
        ),
        migrations.CreateModel(
            name="SubredditNotificationChannel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("channel_id", models.CharField(max_length=4000, unique=True)),
                ("server_id", models.CharField(max_length=4000)),
                ("name", models.CharField(max_length=4000)),
            ],
            options={
                "verbose_name": "Reddit Notification Channel",
                "verbose_name_plural": "Reddit Notification Channels",
            },
        ),
        migrations.CreateModel(
            name="TwitterNotificationChannel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("channel_id", models.CharField(max_length=4000, unique=True)),
                ("server_id", models.CharField(max_length=4000)),
                ("name", models.CharField(max_length=4000)),
                ("default_subscribed", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Twitter Notification Channel",
                "verbose_name_plural": "Twitter Notification Channels",
            },
        ),
        migrations.CreateModel(
            name="TwitterUser",
            fields=[
                ("user_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("screen_name", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("profile_image", models.CharField(max_length=1048)),
                ("custom", models.BooleanField(default=False)),
                ("default", models.BooleanField(default=False)),
                (
                    "subscribers",
                    models.ManyToManyField(to="bot.TwitterNotificationChannel"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tweet",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("text", models.CharField(max_length=1048)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("read", models.BooleanField(default=False)),
                ("default", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tweets",
                        to="bot.TwitterUser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subreddit",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=1048)),
                ("initialized", models.BooleanField(default=False)),
                (
                    "subscribers",
                    models.ManyToManyField(to="bot.SubredditNotificationChannel"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RedditSubmission",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("user", models.CharField(max_length=255)),
                ("selftext", models.BooleanField(default=False)),
                ("score", models.IntegerField(default=0)),
                ("comments", models.IntegerField(default=0)),
                (
                    "title",
                    models.CharField(
                        blank=True, default="", max_length=1048, null=True
                    ),
                ),
                (
                    "thumbnail",
                    models.CharField(
                        blank=True, default="", max_length=1048, null=True
                    ),
                ),
                (
                    "text",
                    models.CharField(
                        blank=True, default="", max_length=40000, null=True
                    ),
                ),
                (
                    "link",
                    models.CharField(
                        blank=True, default="", max_length=1048, null=True
                    ),
                ),
                ("permalink", models.CharField(max_length=1048)),
                ("read", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "subreddit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="submissions",
                        to="bot.Subreddit",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(max_length=32)),
                ("message", models.TextField(max_length=300)),
                ("send_ios", models.BooleanField(default=False)),
                ("send_ios_complete", models.NullBooleanField(default=False)),
                ("send_android", models.BooleanField(default=False)),
                ("send_android_complete", models.NullBooleanField(default=False)),
                (
                    "event",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.Events",
                    ),
                ),
                (
                    "launch",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.Launch",
                    ),
                ),
                (
                    "news",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.Article",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ArticleNotification",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("read", models.BooleanField(default=False)),
                ("should_notify", models.BooleanField(default=False)),
                ("was_notified", models.BooleanField(default=False)),
                (
                    "article",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="api.Article"
                    ),
                ),
            ],
        ),
    ]
