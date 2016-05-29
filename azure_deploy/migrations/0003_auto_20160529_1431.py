# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azure_deploy', '0002_auto_20160529_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsonfile',
            name='file',
            field=models.FileField(null=True, upload_to=b'media/'),
        ),
    ]
