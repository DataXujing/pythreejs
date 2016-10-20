from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ...enums import *
from ...traits import *

from ...core.BufferGeometry_autogen import BufferGeometry


class BoxBufferGeometry(BufferGeometry):
    """BoxBufferGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 12:05:52 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/BoxBufferGeometry 
    """
    
    _view_name = Unicode('BoxBufferGeometryView').tag(sync=True)
    _model_name = Unicode('BoxBufferGeometryModel').tag(sync=True)

    width = CFloat(10).tag(sync=True)
    height = CFloat(10).tag(sync=True)
    depth = CFloat(10).tag(sync=True)
    widthSegments = CInt(1).tag(sync=True)
    heightSegments = CInt(1).tag(sync=True)
    depthSegments = CInt(1).tag(sync=True)

