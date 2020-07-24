# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02LoginAPITestCase::test_case status'] = 400

snapshots['TestCase02LoginAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALIDPASSWORD',
    'response': 'Invalid password, try with valid password'
}

snapshots['TestCase02LoginAPITestCase::test_case header_params'] = {
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
        'text/html; charset=utf-8'
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
