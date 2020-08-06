# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_users_profile_response response'] = [
    {
        'mobile_number': '9876543210',
        'name': 'name_1',
        'user_id': 1,
        'username': 'user_1'
    },
    {
        'mobile_number': '9876543211',
        'name': 'name_2',
        'user_id': 2,
        'username': 'user_2'
    },
    {
        'mobile_number': '9876543212',
        'name': 'name_3',
        'user_id': 3,
        'username': 'user_3'
    },
    {
        'mobile_number': '9876543213',
        'name': 'name_4',
        'user_id': 4,
        'username': 'user_4'
    }
]
