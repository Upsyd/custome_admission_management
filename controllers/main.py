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
        res_users = request.registry.get('res.users')
        res_vals = {
                    'name': form_data.get('fname'),
                    'login':form_data.get('email'),
                    'email':form_data.get('email'),
                   }
        print "SSSSSSSSSSSsss",res_vals
        new_res_users = res_users.create(cr, SUPERUSER_ID, res_vals, context=context)
        res_partner = request.registry.get('res.partner')       
        new_partner_users = res_partner.search(cr, SUPERUSER_ID,[('email','=',form_data.get('email'))], context=context)
        print "mmmmkddskfkdskfkdkfkdksfksakfkdsfkdskfk_____-----",new_partner_users
        hr_new_applicant = request.registry.get('hr.applicant')
        vals = {
                    'name':'Job Application From'+':'+form_data.get('fname') or False,
                    'partner_name':form_data.get('fname') or False,
                    'partner_id':new_partner_users[0] or False,
                    'mname':form_data.get('mname') or False,
                    'lname': form_data.get('lname') or False,
                    'partner_mobile': form_data.get('mobile') or False,
                    'email_from':form_data.get('email') or False,
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
        new_addmission = hr_new_applicant.create(cr, SUPERUSER_ID, vals, context=context)
        
        access=request.registry.get('res.groups')
        ir_mod_cat=request.registry.get('ir.module.category')
        ir_mod_cat_id=ir_mod_cat.search(cr,SUPERUSER_ID,[('name','=','Human Resources')],context=context)
        print "\n)))))))))))))))))))))))))))))",new_res_users,"\ncate====",ir_mod_cat_id
        if ir_mod_cat_id:
            hr_search_id=access.search(cr,SUPERUSER_ID,[('category_id','=',ir_mod_cat_id[0]),('name','=','Manager')],context=context)
            print "hr_search_id=====>>>>",hr_search_id
            hr_search_id_del=access.search(cr,SUPERUSER_ID,[('category_id','=',ir_mod_cat_id[0]),('name','=','Employee')],context=context)
        access_user=access.search(cr,SUPERUSER_ID,[('name','=','Survey / User')],context=context)
        grp_users=access.write(cr,SUPERUSER_ID,access_user,{'users': [(4,new_res_users)]},context)
        grp_users=access.write(cr,SUPERUSER_ID,hr_search_id_del,{'users': [(3,new_res_users)]},context)
        grp_users=access.write(cr,SUPERUSER_ID,hr_search_id,{'users': [(4,new_res_users)]},context)
        print access_user,"%%%%%%%%%%%%%%5access_user__________group_users",grp_users
        '''res_partner_vals={
                            'email':form_data.get('email'),
                         }
        print "##############33",res_partner_vals
        new_res_partner = res_partner.create(cr, uid, res_partner_vals, context=context)
        '''
        
        return request.website.render("custome_admission_management.success")
                   

    
    
    
# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4:
