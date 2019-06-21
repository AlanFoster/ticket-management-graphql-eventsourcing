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

snapshots['test_get_tickets_when_multiple_created 1'] = {
    'data': {
        'tickets': [
            {
                'description': None,
                'name': 'My first ticket',
                'updatedAt': '2012-01-14T00:00:00'
            },
            {
                'description': None,
                'name': 'My second ticket',
                'updatedAt': '2012-01-14T00:00:00'
            }
        ]
    }
}

snapshots['test_get_ticket 1'] = {
    'data': {
        'ticket': {
            'description': 'New ticket description',
            'history': [
                {
                    '__typename': 'TicketFieldUpdated',
                    'field': 'name',
                    'newValue': 'Ticket renamed',
                    'oldValue': 'My ticket',
                    'timestamp': '2012-01-14T00:00:00'
                },
                {
                    '__typename': 'TicketFieldUpdated',
                    'field': 'description',
                    'newValue': 'New ticket description',
                    'oldValue': 'My ticket description',
                    'timestamp': '2012-01-14T00:00:00'
                }
            ],
            'name': 'Ticket renamed',
            'updatedAt': '2012-01-14T00:00:00'
        }
    }
}
