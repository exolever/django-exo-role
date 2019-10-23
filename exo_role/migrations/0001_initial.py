# Generated by Django 2.2.6 on 2019-10-22 14:09

from django.db import migrations, models

import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(
                    choices=[('SP', 'ExO Sprint'), ('FA', 'Fastrack'), ('WO', 'Workshop'), ('SW', 'Swarm'),
                             ('SU', 'Summit'), ('AC', 'Advisory Call'), ('DS', 'Disruption Session'), ('TA', 'Talk')],
                    max_length=2)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ExORole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(
                    choices=[('SHC', 'Head Coach'), ('SSH', 'Sprint Coach'), ('SAS', 'Awake Speaker'),
                             ('SAT', 'Align Trainer'), ('SAD', 'Advisor'),
                             ('SDI', 'Disruptor'), ('SDS', 'Disruptor Speaker'),
                             ('SDM', 'Delivery Manager'), ('SPA', 'Sprint Participant'), ('SCO', 'Sprint Contributor'),
                             ('SRE', 'Reporter'), ('SAM', 'Account Manager'), ('SSC', 'Shadow Coach'),
                             ('SOT', 'Other'), ('FTL', 'Team Leader'),
                             ('FTM', 'Team Member'), ('FCU', 'Curator'), ('FCC', 'Co-Curator'),
                             ('FSA', 'Solution Accelerator'), ('FOE', 'Observer/Evaluator'),
                             ('FLM', 'Local Team Member'),
                             ('WSP', 'Speaker'), ('WTR', 'Trainer'), ('SWA', 'Advisor'), ('SUC', 'Collaborator'),
                             ('SUS', 'Speaker'), ('SUF', 'Facilitator'), ('SUO', 'Organizer'), ('ACA', 'Advisor'),
                             ('TAS', 'Speaker'), ('DSD', 'Disruptor')], max_length=3, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('categories', models.ManyToManyField(related_name='roles', to='exo_role.Category')),
            ],
            options={
                'verbose_name': 'ExORole',
                'verbose_name_plural': 'ExORoles',
                'ordering': ['name'],
            },
        ),
    ]
