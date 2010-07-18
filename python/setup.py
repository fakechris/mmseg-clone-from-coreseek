from distutils.core import setup, Extension

cmmseg = Extension('cmmseg',
                    define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '0')],
                    include_dirs = ['/usr/local/include/mmseg'],
                    libraries = ['mmseg'],
                    library_dirs = ['/usr/local/lib'],
                    sources = ['mmseg_interface.cpp', 'pymmseg.c'])

setup (name = 'cmmseg',
       version = '1.0',
       description = 'This is cmmseg package',
       author = 'li monan',
       author_email = 'li.monan@gmail.com',
       url = 'http://www.coreseek.com',
       long_description = '''This is cmmseg python binding.''',
       ext_modules = [cmmseg])
