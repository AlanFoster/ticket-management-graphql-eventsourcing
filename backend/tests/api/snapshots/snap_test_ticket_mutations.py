# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_rename_ticket 1'] = {
    'description': None,
    'name': 'testing ticket'
}

snapshots['test_delete_ticket 1'] = None

snapshots['test_update_ticket_description 1'] = {
    'description': 'updated description',
    'name': 'My ticket'
}

snapshots['test_create_ticket 1'] = {
    'data': {
        'createTicket': {
            'ok': True,
            'ticket': {
                'description': 'testing ticket description',
                'name': 'testing ticket'
            }
        }
    }
}
