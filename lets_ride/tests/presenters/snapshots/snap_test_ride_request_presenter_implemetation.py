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
    'res_status': 'InvaidDatetime',
    'response': 'date_time is in past, please enter present or future date_time'
}

snapshots['test_raise_exception_for_invalid_end_datetime response'] = {
    'http_status_code': 400,
    'res_status': 'InvalidEndDatetime',
    'response': 'your end datetime is less than start datetime, please enter valid end datetime'
}

snapshots['test_raise_exception_for_invalid_no_of_seats response'] = {
    'http_status_code': 400,
    'res_status': 'InvalidNoOfSeats',
    'response': 'the no of seats should be positive, please enter valid no of seats'
}

snapshots['test_raise_exception_for_invalid_luggage_quantity response'] = {
    'http_status_code': 400,
    'res_status': 'InvalidLuggageQuantity',
    'response': 'your luggage quantity is in negative value, please enter valid luggage quantity'
}
