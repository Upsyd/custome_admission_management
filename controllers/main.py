# -*- coding: utf-8 -*-
import werkzeug

from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request
from openerp import SUPERUSER_ID
from openerp.tools.translate import _
from openerp.addons.website.models.website import slug
from openerp.addons.web.controllers.main import login_redirect






class customadmission_customadmission(http.Controller):
    
    @http.route('/admission/', type='http', auth="public", website=True)
    def admission(self,**post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
    
        return request.website.render("custome_admission_management.admission")


    @http.route(['/admission/success'], type='http', auth="public", website=True)
    def success(self, **form_data):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        orm_partner = request.registry.get('customadmission.customadmission')
        res_users = request.registry.get('res.users')
        res_partner = request.registry.get('res.partner')       
        vals = {
                    'name': form_data.get('fname') or False,
                    'mname':form_data.get('mname') or False,
                    'lname': form_data.get('lname') or False,
                    'mobile': form_data.get('mobile') or False,
                    'email':form_data.get('email') or False,
                    'gender': form_data.get('gender'),
                    'dob': form_data.get('dob') or False,
                    'address': form_data.get('address'),
                    'street2': form_data.get('street2') or False,
                    'city': form_data.get('city') or False,
                    'state': form_data.get('state'),
                    'pincode': form_data.get('pincode') or False,
                    'exp': form_data.get('exp') or False,
                    'month': form_data.get('Month') or False,
                    'year': form_data.get('year') or False,
                    #'frmemail': 'odooparth@gmail.com',
                    }
        print "@@@@@@@@@@",vals, context
        new_addmission = orm_partner.create(cr, SUPERUSER_ID, vals, context=context)
        res_vals = {
                    'name': form_data.get('fname'),
                    'login':form_data.get('email'),
                    'email':form_data.get('email'),
                   }
        print "SSSSSSSSSSSsss",res_vals
        new_res_users = res_users.create(cr, SUPERUSER_ID, res_vals, context=context)
        access=request.registry.get('res.groups')
        print "\n)))))))))))))))))))))))))))))",new_res_users
        access_user=access.search(cr,SUPERUSER_ID,[('name','=','Survey / User')],context=context)
        grp_users=access.write(cr,SUPERUSER_ID,access_user,{'users': [(4,new_res_users)]},context)
        print access_user,"%%%%%%%%%%%%%%5access_user__________group_users",grp_users
        '''res_partner_vals={
                            'email':form_data.get('email'),
                         }
        print "##############33",res_partner_vals
        new_res_partner = res_partner.create(cr, uid, res_partner_vals, context=context)
        '''
        
        return request.website.render("custome_admission_management.success")
                   

    
    
    
# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4:
