# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python 3 imports
from __future__ import absolute_import, unicode_literals

# python imports
import logging

# 3rd. libraries imports
from appconf import AppConf

# django imports
from django.conf import settings  # noqa

logger = logging.getLogger(__name__)


class ExORoleConfigConfig(AppConf):
    # Types
    CATEGORY_EXO_SPRINT = 'SP'
    CATEGORY_FASTRACK = 'FA'
    CATEGORY_WORKSHOP = 'WO'
    CATEGORY_SWARM = 'SW'
    CATEGORY_SUMMIT = 'SU'

    CATEGORY_CHOICES = (
        (CATEGORY_EXO_SPRINT, 'ExO Sprint'),
        (CATEGORY_FASTRACK, 'Fastrack'),
        (CATEGORY_WORKSHOP, 'Workshop'),
        (CATEGORY_SWARM, 'Swarm'),
        (CATEGORY_SUMMIT, 'Summit'),
    )

    CODE_SPRINT_HEAD_COACH = 'SHC'
    CODE_SPRINT_COACH = 'SSC'
    CODE_AWAKE_SPEAKER = 'SAS'
    CODE_ALIGN_TRAINER = 'SAT'
    CODE_ADVISOR = 'SAD'

    CODE_CHOICES = (
        (CODE_SPRINT_HEAD_COACH, 'Head Coach'),
        (CODE_SPRINT_COACH, 'Sprint Coach'),
        (CODE_AWAKE_SPEAKER, 'Awake Speaker'),
        (CODE_ALIGN_TRAINER, 'Align Trainer'),
        (CODE_ADVISOR, 'Advisor'),
    )
