import functools
import threading

import bottle

__all__ = ['PystacheTemplate', 'Template',
           'pystache_template', 'template',
           'pystache_view', 'view']

class PystacheTemplate(bottle.BaseTemplate):
    ''' Pystache is a Python Mustache implementation.
        Set `View.template_extension` to be able to use partials,
        because partial calls are not handled by Bottle and Pystache works
        with only one extension, defined as `mustache` by default.
    '''

    try:
        extensions = bottle.BaseTemplate.extensions
    except AttributeError:
        # Bottle had a misspelling in BaseTemplate.
        # It is fixed in Bottle v0.10.
        extensions = bottle.BaseTemplate.extentions
    extensions.insert(0, 'mustache')

    def prepare(self, **options):
        from pystache import Template, View
        View.template_path = self.lookup
        self.context = threading.local()
        self.context.vars = {}
        if self.source:
            self.tpl = Template(self.source)
        else:
            view = View()
            view.template_file = self.filename
            view.template_name = self.name
            view.template_encoding = self.encoding
            template = view.load_template()
            self.tpl = Template(template)

    def render(self, *args, **kwargs):
        for dictarg in args:
            kwargs.update(dictarg)
        self.context.vars.update(self.defaults)
        self.context.vars.update(kwargs)
        out = self.tpl.render(context=self.context.vars, encoding=self.encoding)
        self.context.vars.clear()
        return out


pystache_template = functools.partial(bottle.template, template_adapter=PystacheTemplate)
pystache_view = functools.partial(bottle.view, template_adapter=PystacheTemplate)

Template = PystacheTemplate
template = pystache_template
view = pystache_view
