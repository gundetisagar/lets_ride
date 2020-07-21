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

snapshots['TestCase03LoginAPITestCase::test_case header_params'] = {
    'allow': (
        'Allow',
        'OPTIONS, POST'
    ),
    'content-language': (
        'Content-Language',
        'en'
    ),
    'content-length': (
        'Content-Length',
        '115'
    ),
    'content-type': (
        'Content-Type',
        '404'
    ),
    'vary': (
        'Vary',
        'Accept-Language, Origin, Cookie'
    ),
    'x-frame-options': (
        'X-Frame-Options',
        'SAMEORIGIN'
    )
}
