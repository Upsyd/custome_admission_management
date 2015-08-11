# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Browseinfo SPRL (<http://browseinfo.in>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Custom Admission Managment',
    'version': '1.0',
    'author': 'Browseinfo',
    'website': 'http://www.browseinfo.in',
    'category': 'Admission Detail',
    'summary': 'Custom Admission Detail and Registration and Show the Custom Data',
    'depends': ['website','survey','hr_recruitment',],
    'description': """
This is a simple Custom Admission Managment Process 
    """,

    'data': [
        
        'data/data.xml', 
        'views/custom_admission_detail_view.xml', 
        'views/website_custom_admission_detail.xml',
        'views/custom_application_mail.xml',
        'views/survey_result.xml',    
    ],
    'demo': [],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
