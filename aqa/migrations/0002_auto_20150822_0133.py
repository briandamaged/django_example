# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aqa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentanswer',
            name='assessment',
            field=models.ForeignKey(related_name='answers', to='aqa.Assessment'),
        ),
        migrations.AlterField(
            model_name='assessmentanswer',
            name='question',
            field=models.ForeignKey(related_name='answers', to='aqa.Question'),
        ),
        migrations.AlterField(
            model_name='assessmentanswer',
            name='value',
            field=models.BooleanField(default=True, verbose_name=b'They answered...', choices=[(True, b'Yes'), (False, b'No')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='article',
            field=models.ForeignKey(related_name='questions', to='aqa.Article'),
        ),
    ]
