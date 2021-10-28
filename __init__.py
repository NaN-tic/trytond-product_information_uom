# This file is part product_information_uom module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import template

def register():
    Pool.register(
        template.Template,
        module='product_information_uom', type_='model')
