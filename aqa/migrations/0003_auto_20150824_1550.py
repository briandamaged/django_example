# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aqa', '0002_auto_20150822_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='user',
            field=models.ForeignKey(related_name='assessments', to=settings.AUTH_USER_MODEL),
        ),
    ]
