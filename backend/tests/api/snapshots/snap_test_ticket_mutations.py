# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_ticket 1'] = {
    'data': {
        'createTicket': {
            'ok': True,
            'ticket': {
                'name': 'testing ticket'
            }
        }
    }
}

snapshots['test_rename_ticket 1'] = {
    'name': 'My ticket'
}
