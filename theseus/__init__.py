# Copyright (c) Aaron Gallagher <_@habnab.it>
# See COPYING for details.

try:
    from theseus._cytracer import CythonTracer as Tracer
except ImportError:
    from theseus._tracer import Tracer

__sha__ = None
__version__ = '0.14.1.2'

__all__ = ['__version__', '__sha__', 'Tracer']
