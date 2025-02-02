{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Tools',
    'author': 'Estevez.Jor',
    'license': 'LGPL-3',
    'sumary': 'Real Estate Management',
    'description': 'Nuevo modulo para la gestion de inmuebles',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menu.xml',
    ]
}