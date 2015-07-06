# -*- coding: utf-8 -*-
##############################################################################
#
#    
#    Copyright (C) 2014-2015 Browseinfo SPRL (<http://Browseinfo.in>).
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

from datetime import datetime, timedelta
import time
from dateutil.relativedelta import relativedelta
from openerp.osv import fields, osv
from openerp.tools.translate import _



class customadmission_customadmission(osv.osv):
    _name = "customadmission.customadmission"
    _description = "Custom Admission Detail and Registration and Show the Custom Data"
    _columns = {
        'name' : fields.char('First Name',required=True),
	'image':fields.binary('Image'),
        'mname' : fields.char('Middle Name'),
	'lname' : fields.char('Last Name'),
	'mobile': fields.char('Mobile'),
	'email': fields.char('Email Address',required=True),
	'cemail': fields.char('Confirm Email'),
	'address' : fields.char('Street-1'),
	'street2' : fields.char('Street-2'),
	'gender': fields.selection([('m', 'Male'),('f', 'Female')],string="Gender"),
	'dob': fields.date('Date of Birth'),        
	'city' : fields.char('City'),
	'state' : fields.char('State'),
        'pincode' : fields.char('Pincode'),
        'exp': fields.char('Experience'),
	'year': fields.integer('Year of expirience'),
	'month': fields.integer('Month of expirience'),
	'frmemail': fields.char('From Email'),
    }
    
    
class surve_new_result(osv.Model):
    _inherit = "survey.user_input"
    def _func_result(self, cr, uid, ids, name, args, context=None):
        ret = {}
        for user_input in self.browse(cr, uid, ids, context=context):
	    if user_input.quizz_score > 60:
            	ret[user_input.id]= "Pass"
	    else:
		ret[user_input.id]= "Fail"
        return ret

    _columns = {
		'score_result': fields.function(_func_result, type="char", string="Result"),
        
    }
'''class exam_url(osv.Model):
    _inherit="res.partner"
    def _get_signup_url(self, cr, uid, ids, name, arg, context=None):
	context={'exam':'exam'}
        """ proxy for function field towards actual implementation """
	print "hiiiiiiiiiiiiiiiiiiiiiii"
        return self._get_signup_url_for_action(cr, uid, ids, context=context)
'''
