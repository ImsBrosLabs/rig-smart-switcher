{
    'p110': {
        'required': True,
        'type': 'dict',
        'schema': {
            'ip': {
                'required': True,
                'type': 'string',
            },
            'email': {
                'required': True,
                'type': 'string',
                'regex': '^[^@\s]+@[^@\s]+\.[^@\s]+$'
            },
            'password': {
                'required': True,
                'type': 'string'
            }
        }
    },
    'open_meteo': {
        'required': True,
        'type': 'dict',
        'schema': {
            'latitude': {
                'required': True,
                'type': 'float'
            },
            'longitude': {
                'required': True,
                'type': 'float'
            }
        }
    },
    'rig_ssh_creds': {
        'required': True,
        'type': 'dict',
        'schema': {
            'host': {
                'required': True,
                'type': 'string'
            },
            'username': {
                'required': True,
                'type': 'string'
            },
            'password': {
                'required': True,
                'type': 'string'
            }
        }
    }
}
