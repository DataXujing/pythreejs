from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget


class Plane(ThreeWidget):
    """Plane
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 12:05:52 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Math/Plane 
    """
    
    _view_name = Unicode('PlaneView').tag(sync=True)
    _model_name = Unicode('PlaneModel').tag(sync=True)

    normal = Vector3(default=[0,0,0]).tag(sync=True)
    constant = CFloat(0).tag(sync=True)

