# This file is part product_information_uom module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class ProductInformationUomTestCase(ModuleTestCase):
    'Test Product Information Uom module'
    module = 'product_information_uom'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            ProductInformationUomTestCase))
    return suite
