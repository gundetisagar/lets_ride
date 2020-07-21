# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetProfileAPITestCase::test_case status'] = 200

snapshots['TestCase01GetProfileAPITestCase::test_case body'] = {
    'mobile_number': 1,
    'name': 'string',
    'username': 'string'
}

snapshots['TestCase01GetProfileAPITestCase::test_case header_params'] = {
    'allow': (
        'Allow',
        'OPTIONS, GET'
    ),
    'content-language': (
        'Content-Language',
        'en'
    ),
    'content-length': (
        'Content-Length',
        '55'
    ),
    'content-type': (
        'Content-Type',
        'application/json'
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
