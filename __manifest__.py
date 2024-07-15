{
    'name': 'Task Management',
    'version': '15.0',
    'sequence': 1,
    'category': '',
    'website': '',
    'author': "Udeshini",
    'depends': ['base'],
    "data": [
        "data/ir_sequence_data.xml",
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/user_department_views.xml",
        "views/task_type_views.xml",
        "views/branch_views.xml",
        "views/task_views.xml"
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
