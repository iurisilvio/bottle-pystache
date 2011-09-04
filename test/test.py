import unittest

import os, sys
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from bottle.ext.pystache import Template, template, view

class TestPystacheTemplate(unittest.TestCase):
    def test_interface(self):
        from bottle.ext.pystache import Template, template, view
        from bottle.ext.pystache import PystacheTemplate, pystache_template, pystache_view

    def test_string(self):
        """ Pystache string"""
        t = Template('start {{var}} end').render(var='var')
        self.assertEqual('start var end', t)

    def test_file(self):
        """ Pystache file"""
        t = Template(name='./views/simple.tpl').render(var='var')
        self.assertEqual('start var end\n', t)

    def test_name(self):
        """ Pystache lookup by name """
        t = Template(name='simple', lookup=['./views/']).render(var='var')
        self.assertEqual('start var mustache end\n', t)

    def test_notfound(self):
        """ Unavailable templates"""
        self.assertRaises(Exception, Template, name="abcdef")

    def test_error(self):
        """ Exceptions"""
        template = Template('{{#block_not_closed}}')
        self.assertRaises(Exception, template.render)

    def test_partials(self):
        """ Pystache lookup and partials """
        t = Template(name='base', lookup=['./views/']).render(var='v')
        self.assertEqual('o\ncvc\no\n', t)
        t = Template('o{{> partial}}o\n', lookup=['./views/']).render(var='v')
        self.assertEqual('o\ncvc\no\n', t)

    def test_template_shortcut(self):
        result = template('start {{var}} end', var='middle')
        self.assertEqual(u'start middle end', result)

    def test_view_decorator(self):
        @view('start {{var}} end')
        def test():
            return dict(var='middle')
        self.assertEqual(u'start middle end', test())


try:
  import pystache
except ImportError:
  print "WARNING: No Pystache template support. Skipping tests."
  del TestPystacheTemplate

if __name__ == '__main__': #pragma: no cover
    unittest.main()
