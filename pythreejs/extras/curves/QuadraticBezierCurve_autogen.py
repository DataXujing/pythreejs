from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ...enums import *
from ...traits import *

from ..._base.Three import ThreeWidget


class QuadraticBezierCurve(ThreeWidget):
    """QuadraticBezierCurve
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 12:05:52 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Curves/QuadraticBezierCurve 
    """
    
    _view_name = Unicode('QuadraticBezierCurveView').tag(sync=True)
    _model_name = Unicode('QuadraticBezierCurveModel').tag(sync=True)


