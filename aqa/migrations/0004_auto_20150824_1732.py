# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aqa', '0003_auto_20150824_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='passing_score',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='assessment',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
