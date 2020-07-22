# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03LoginAPITestCase::test_case status'] = 200

snapshots['TestCase03LoginAPITestCase::test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALIDUSERNAME',
    'response': 'Invalid username, try with valid username'
}
