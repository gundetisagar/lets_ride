# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02RideRequestAPITestCase::test_case status'] = 403

snapshots['TestCase02RideRequestAPITestCase::test_case body'] = b''

snapshots['TestCase02RideRequestAPITestCase::test_case header_params'] = {
    'allow': (
        'Allow',
        'POST, OPTIONS'
    ),
    'content-language': (
        'Content-Language',
        'en'
    ),
    'content-length': (
        'Content-Length',
        '0'
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
