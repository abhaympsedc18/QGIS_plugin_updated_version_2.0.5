# -*- coding: utf-8 -*-

def classFactory(iface):
    from .exact_raster_boundary import ExactRasterBoundary
    return ExactRasterBoundary(iface)
