# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_raise_exception_for_from_and_to_place_are_same response'] = {
    'http_status_code': 400,
    'res_status': 'InvalidToPlace',
    'response': 'from_place and to_place both are same, please enter valid to_place'
}

snapshots['test_raise_exception_for_invalid_date_time response'] = {
    'http_status_code': 400,
    'res_status': 'InvalidDatetime',
    'response': 'date_time is in past, please enter present or future date_time'
}

snapshots['test_raise_exception_for_invalid_end_datetime response'] = {
    'http_status_code': 400,
    'res_status': 'InvalidEndDatetime',
    'response': 'your end datetime is less than start datetime, please enter valid end datetime'
}

snapshots['test_raise_exception_for_invalid_assets_quantity response'] = {
    'http_status_code': 400,
    'res_status': 'InvalidAssetsQuantity',
    'response': 'your assets quantity is in negative value, please enter valid assets quantity'
}
