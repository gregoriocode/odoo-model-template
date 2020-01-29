# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError

class TemplateTemplate(models.Model):
    _name = 'template.template'
    _order = 'name desc'
    _description = 'Template Description'

    name  = fields.Char(string='Name')
    code = fields.Integer(string='Code')
