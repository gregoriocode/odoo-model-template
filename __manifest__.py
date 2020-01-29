# -*- encoding: utf-8 -*-
{
    'name':
    'template',
    'version':
    '1.0',
    'author':
    'gregoriocode.com',
    'website':
    '',
    'category':
    'account',
    'depends': ['stock'],
    'description':
    """Template""",
    'demo': [
        'demo/template_demo.xml'
    ],
    'data': [
        'views/template.xml',
        'security/group_template.xml',
        'security/ir.model.access.csv',
        'data/template_data.xml',
    ],
    'auto_install':
    False,
    'installable':
    True
}
