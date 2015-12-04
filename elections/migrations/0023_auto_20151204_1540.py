# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0022_remove_candidate_election'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='did_not_pass_primaries',
            field=models.BooleanField(default=False, help_text='Marca esto si quieres el candidato no pas&oacute; las primarias'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='elections',
            field=models.ManyToManyField(related_name='candidates', to='elections.Election'),
        ),
    ]
