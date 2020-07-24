# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03LoginAPITestCase::test_case status'] = 200

snapshots['TestCase03LoginAPITestCase::test_case body'] = {
    'access_token': 'SwB855xVFhvMnI5ci59ylTstvi5CoB',
    'expires_in': '2052-04-01 00:33:11.590336',
    'refresh_token': 'ztQmkfr0AKA5YxeKQOuDaOH5mtWtyp',
    'user_id': 1
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
        '159'
    ),
    'content-type': (
        'Content-Type',
        '200'
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
