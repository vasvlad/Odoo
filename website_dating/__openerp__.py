{
    'name': "Website Dating (Beta)",
    'version': "0.2",
    'author': "Sythil Tech",
    'category': "Tools",
    'support': "steven@sythiltech.com.au",
    'summary': "A directory of single people",
    'license':'LGPL-3',
    'data': [
        'views/res_dating_views.xml',
        'views/res_partner_views.xml',
        'views/res_country_state_city.xml',
        'views/res_country_state_city_import.xml',
        'views/res_country_state_views.xml',
        'views/website_dating_templates.xml',
        'views/menus_views.xml',
        'data/ir.cron.csv',
        'data/res.partner.gender.csv',
        'data/res.dating.fake.first.csv',
        'data/res.dating.fake.last.csv',
        'data/website.menu.csv',
        'data/res.groups.csv',
        'data/ir.rule.csv',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'depends': ['crm', 'website'],
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
}