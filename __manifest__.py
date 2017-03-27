# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sirop de l\'Est',
    'category': 'Vertical',
    'version': '1.0',
    'author': "Benoît Vézina & Pierre Dalpé pour Portall",
    'website': "portall.ca",
    'summary': 'Odoo adaptation for maple syrup industry.',
    'description':
        """
Initial maple data import for Sirop de l'Est.
================================================

This module provides mosly fields and views.
        """,
    'depends': [
        'maple',
    ],
    'data': [
# Chargement des groups, users et rules pour la sécurité
        'data/regions.xml',
        'data/partners.xml',
#        'data/res.partner.csv',
        'data/company.xml',
        'data/warehouses.xml',
        'data/stock_location.xml',
        'data/stock.location.csv',
        'data/operations_types.xml'
    ],
    'qweb': [
#        "static/src/xml/*.xml",
    ],
#    'bootstrap': True,  # load translations for login screen
    'installable': True,
    'application': True,
    'auto_install': False,
}

