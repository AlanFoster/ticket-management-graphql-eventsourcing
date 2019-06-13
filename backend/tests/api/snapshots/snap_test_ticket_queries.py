# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_tickets_when_none_created 1'] = {
    'data': {
        'tickets': [
        ]
    }
}

snapshots['test_get_ticket 1'] = {
    'data': {
        'ticket': {
            'name': 'My ticket',
            'updatedAt': '2012-01-14T00:00:00'
        }
    }
}

snapshots['test_get_tickets_when_multiple_created 1'] = {
    'data': {
        'tickets': [
            {
                'name': 'My first ticket',
                'updatedAt': '2012-01-14T00:00:00'
            },
            {
                'name': 'My second ticket',
                'updatedAt': '2012-01-14T00:00:00'
            }
        ]
    }
}
