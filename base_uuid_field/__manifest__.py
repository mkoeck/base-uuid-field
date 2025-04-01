# -*- coding: utf-8 -*-
{
    'name': "UUID Fields",
    'summary': "Implementation of UUID fields.",
    'description': """
The purpose of this module is to implement UUID fields, i.e., fields that are universally unique identifiers.
    """,

    'author': "Michael Köck",
    'license': 'LGPL-3',

    'category': 'Generic Modules',
    'version': '18.0.1.0.0',

    'depends': ['base'],

    'assets': {
        'web.assets_backend': [
            'base_uuid_field/static/src/**/*',
        ],
    },
}

