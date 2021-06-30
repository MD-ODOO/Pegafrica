# -*- coding: utf-8 -*-
{
    'name': "Next Of Kin",
    'sequence': '1',

    'description': """
        Long description of module's purpose
    """,

    'author': "PegAfrica",
    'website': "http://www.Pegafrica.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'contacts',  
                ],

    # always loaded
    'data': [
        'views/nextofkin.xml',
        'security/nextofkin.xml',
        'security/ir.model.access.csv'

        ],
    'demo': [
         
        ],
    'qweb': [
        
        ],
    'installable': True,
    'application': True,
    'auto_install': False
}
