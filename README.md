This project is just an example of Bottle template integration, *do not use it as a real template plugin*. Take a look at https://github.com/aleiphoenix/bottle-pystache if you want to use bottle and pystache together.

To use pystache with bottle, import template handlers from pystache extension:

    from bottle.ext.pystache import view

    @route('/')
    @view('your_template')
    def func():
    	return {'hello': 'world'}

This wrapper define other handlers like core implemented templates do:

 * `PystacheTemplate`, `Template` 
 * `pystache_template`, `template`
 * `pystache_view`, `view`

Pystache is a Python implementation of Mustache.

* Pystache: https://github.com/defunkt/pystache
* Mustache: http://mustache.github.com
