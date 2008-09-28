# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

"""
Python interface to the GTO RawData C++ class.
"""

import _gtoDB
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class PySwigIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PySwigIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PySwigIterator, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _gtoDB.delete_PySwigIterator
    __del__ = lambda self : None;
    def value(*args): return _gtoDB.PySwigIterator_value(*args)
    def incr(*args): return _gtoDB.PySwigIterator_incr(*args)
    def decr(*args): return _gtoDB.PySwigIterator_decr(*args)
    def distance(*args): return _gtoDB.PySwigIterator_distance(*args)
    def equal(*args): return _gtoDB.PySwigIterator_equal(*args)
    def copy(*args): return _gtoDB.PySwigIterator_copy(*args)
    def next(*args): return _gtoDB.PySwigIterator_next(*args)
    def previous(*args): return _gtoDB.PySwigIterator_previous(*args)
    def advance(*args): return _gtoDB.PySwigIterator_advance(*args)
    def __eq__(*args): return _gtoDB.PySwigIterator___eq__(*args)
    def __ne__(*args): return _gtoDB.PySwigIterator___ne__(*args)
    def __iadd__(*args): return _gtoDB.PySwigIterator___iadd__(*args)
    def __isub__(*args): return _gtoDB.PySwigIterator___isub__(*args)
    def __add__(*args): return _gtoDB.PySwigIterator___add__(*args)
    def __sub__(*args): return _gtoDB.PySwigIterator___sub__(*args)
    def __iter__(self): return self
PySwigIterator_swigregister = _gtoDB.PySwigIterator_swigregister
PySwigIterator_swigregister(PySwigIterator)

GTO_MAGIC = _gtoDB.GTO_MAGIC
GTO_MAGICl = _gtoDB.GTO_MAGICl
GTO_MAGIC_TEXT = _gtoDB.GTO_MAGIC_TEXT
GTO_MAGIC_TEXTl = _gtoDB.GTO_MAGIC_TEXTl
GTO_VERSION = _gtoDB.GTO_VERSION
class Header(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Header, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Header, name)
    __repr__ = _swig_repr
    MagicText = _gtoDB.Header_MagicText
    CigamText = _gtoDB.Header_CigamText
    Magic = _gtoDB.Header_Magic
    Cigam = _gtoDB.Header_Cigam
    __swig_setmethods__["magic"] = _gtoDB.Header_magic_set
    __swig_getmethods__["magic"] = _gtoDB.Header_magic_get
    if _newclass:magic = _swig_property(_gtoDB.Header_magic_get, _gtoDB.Header_magic_set)
    __swig_setmethods__["numStrings"] = _gtoDB.Header_numStrings_set
    __swig_getmethods__["numStrings"] = _gtoDB.Header_numStrings_get
    if _newclass:numStrings = _swig_property(_gtoDB.Header_numStrings_get, _gtoDB.Header_numStrings_set)
    __swig_setmethods__["numObjects"] = _gtoDB.Header_numObjects_set
    __swig_getmethods__["numObjects"] = _gtoDB.Header_numObjects_get
    if _newclass:numObjects = _swig_property(_gtoDB.Header_numObjects_get, _gtoDB.Header_numObjects_set)
    __swig_setmethods__["version"] = _gtoDB.Header_version_set
    __swig_getmethods__["version"] = _gtoDB.Header_version_get
    if _newclass:version = _swig_property(_gtoDB.Header_version_get, _gtoDB.Header_version_set)
    __swig_setmethods__["flags"] = _gtoDB.Header_flags_set
    __swig_getmethods__["flags"] = _gtoDB.Header_flags_get
    if _newclass:flags = _swig_property(_gtoDB.Header_flags_get, _gtoDB.Header_flags_set)
    def __init__(self, *args): 
        this = _gtoDB.new_Header(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gtoDB.delete_Header
    __del__ = lambda self : None;
Header_swigregister = _gtoDB.Header_swigregister
Header_swigregister(Header)

class ObjectHeader(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObjectHeader, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ObjectHeader, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _gtoDB.ObjectHeader_name_set
    __swig_getmethods__["name"] = _gtoDB.ObjectHeader_name_get
    if _newclass:name = _swig_property(_gtoDB.ObjectHeader_name_get, _gtoDB.ObjectHeader_name_set)
    __swig_setmethods__["protocolName"] = _gtoDB.ObjectHeader_protocolName_set
    __swig_getmethods__["protocolName"] = _gtoDB.ObjectHeader_protocolName_get
    if _newclass:protocolName = _swig_property(_gtoDB.ObjectHeader_protocolName_get, _gtoDB.ObjectHeader_protocolName_set)
    __swig_setmethods__["protocolVersion"] = _gtoDB.ObjectHeader_protocolVersion_set
    __swig_getmethods__["protocolVersion"] = _gtoDB.ObjectHeader_protocolVersion_get
    if _newclass:protocolVersion = _swig_property(_gtoDB.ObjectHeader_protocolVersion_get, _gtoDB.ObjectHeader_protocolVersion_set)
    __swig_setmethods__["numComponents"] = _gtoDB.ObjectHeader_numComponents_set
    __swig_getmethods__["numComponents"] = _gtoDB.ObjectHeader_numComponents_get
    if _newclass:numComponents = _swig_property(_gtoDB.ObjectHeader_numComponents_get, _gtoDB.ObjectHeader_numComponents_set)
    __swig_setmethods__["pad"] = _gtoDB.ObjectHeader_pad_set
    __swig_getmethods__["pad"] = _gtoDB.ObjectHeader_pad_get
    if _newclass:pad = _swig_property(_gtoDB.ObjectHeader_pad_get, _gtoDB.ObjectHeader_pad_set)
    def __init__(self, *args): 
        this = _gtoDB.new_ObjectHeader(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gtoDB.delete_ObjectHeader
    __del__ = lambda self : None;
ObjectHeader_swigregister = _gtoDB.ObjectHeader_swigregister
ObjectHeader_swigregister(ObjectHeader)

class ObjectHeader_v2(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObjectHeader_v2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ObjectHeader_v2, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _gtoDB.ObjectHeader_v2_name_set
    __swig_getmethods__["name"] = _gtoDB.ObjectHeader_v2_name_get
    if _newclass:name = _swig_property(_gtoDB.ObjectHeader_v2_name_get, _gtoDB.ObjectHeader_v2_name_set)
    __swig_setmethods__["protocolName"] = _gtoDB.ObjectHeader_v2_protocolName_set
    __swig_getmethods__["protocolName"] = _gtoDB.ObjectHeader_v2_protocolName_get
    if _newclass:protocolName = _swig_property(_gtoDB.ObjectHeader_v2_protocolName_get, _gtoDB.ObjectHeader_v2_protocolName_set)
    __swig_setmethods__["protocolVersion"] = _gtoDB.ObjectHeader_v2_protocolVersion_set
    __swig_getmethods__["protocolVersion"] = _gtoDB.ObjectHeader_v2_protocolVersion_get
    if _newclass:protocolVersion = _swig_property(_gtoDB.ObjectHeader_v2_protocolVersion_get, _gtoDB.ObjectHeader_v2_protocolVersion_set)
    __swig_setmethods__["numComponents"] = _gtoDB.ObjectHeader_v2_numComponents_set
    __swig_getmethods__["numComponents"] = _gtoDB.ObjectHeader_v2_numComponents_get
    if _newclass:numComponents = _swig_property(_gtoDB.ObjectHeader_v2_numComponents_get, _gtoDB.ObjectHeader_v2_numComponents_set)
    def __init__(self, *args): 
        this = _gtoDB.new_ObjectHeader_v2(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gtoDB.delete_ObjectHeader_v2
    __del__ = lambda self : None;
ObjectHeader_v2_swigregister = _gtoDB.ObjectHeader_v2_swigregister
ObjectHeader_v2_swigregister(ObjectHeader_v2)

Transposed = _gtoDB.Transposed
Matrix = _gtoDB.Matrix
class ComponentHeader(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ComponentHeader, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ComponentHeader, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _gtoDB.ComponentHeader_name_set
    __swig_getmethods__["name"] = _gtoDB.ComponentHeader_name_get
    if _newclass:name = _swig_property(_gtoDB.ComponentHeader_name_get, _gtoDB.ComponentHeader_name_set)
    __swig_setmethods__["numProperties"] = _gtoDB.ComponentHeader_numProperties_set
    __swig_getmethods__["numProperties"] = _gtoDB.ComponentHeader_numProperties_get
    if _newclass:numProperties = _swig_property(_gtoDB.ComponentHeader_numProperties_get, _gtoDB.ComponentHeader_numProperties_set)
    __swig_setmethods__["flags"] = _gtoDB.ComponentHeader_flags_set
    __swig_getmethods__["flags"] = _gtoDB.ComponentHeader_flags_get
    if _newclass:flags = _swig_property(_gtoDB.ComponentHeader_flags_get, _gtoDB.ComponentHeader_flags_set)
    __swig_setmethods__["interpretation"] = _gtoDB.ComponentHeader_interpretation_set
    __swig_getmethods__["interpretation"] = _gtoDB.ComponentHeader_interpretation_get
    if _newclass:interpretation = _swig_property(_gtoDB.ComponentHeader_interpretation_get, _gtoDB.ComponentHeader_interpretation_set)
    __swig_setmethods__["pad"] = _gtoDB.ComponentHeader_pad_set
    __swig_getmethods__["pad"] = _gtoDB.ComponentHeader_pad_get
    if _newclass:pad = _swig_property(_gtoDB.ComponentHeader_pad_get, _gtoDB.ComponentHeader_pad_set)
    def __init__(self, *args): 
        this = _gtoDB.new_ComponentHeader(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gtoDB.delete_ComponentHeader
    __del__ = lambda self : None;
ComponentHeader_swigregister = _gtoDB.ComponentHeader_swigregister
ComponentHeader_swigregister(ComponentHeader)

class ComponentHeader_v2(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ComponentHeader_v2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ComponentHeader_v2, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _gtoDB.ComponentHeader_v2_name_set
    __swig_getmethods__["name"] = _gtoDB.ComponentHeader_v2_name_get
    if _newclass:name = _swig_property(_gtoDB.ComponentHeader_v2_name_get, _gtoDB.ComponentHeader_v2_name_set)
    __swig_setmethods__["numProperties"] = _gtoDB.ComponentHeader_v2_numProperties_set
    __swig_getmethods__["numProperties"] = _gtoDB.ComponentHeader_v2_numProperties_get
    if _newclass:numProperties = _swig_property(_gtoDB.ComponentHeader_v2_numProperties_get, _gtoDB.ComponentHeader_v2_numProperties_set)
    __swig_setmethods__["flags"] = _gtoDB.ComponentHeader_v2_flags_set
    __swig_getmethods__["flags"] = _gtoDB.ComponentHeader_v2_flags_get
    if _newclass:flags = _swig_property(_gtoDB.ComponentHeader_v2_flags_get, _gtoDB.ComponentHeader_v2_flags_set)
    def __init__(self, *args): 
        this = _gtoDB.new_ComponentHeader_v2(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gtoDB.delete_ComponentHeader_v2
    __del__ = lambda self : None;
ComponentHeader_v2_swigregister = _gtoDB.ComponentHeader_v2_swigregister
ComponentHeader_v2_swigregister(ComponentHeader_v2)

Int = _gtoDB.Int
Float = _gtoDB.Float
Double = _gtoDB.Double
Half = _gtoDB.Half
String = _gtoDB.String
Boolean = _gtoDB.Boolean
Short = _gtoDB.Short
Byte = _gtoDB.Byte
NumberOfDataTypes = _gtoDB.NumberOfDataTypes
ErrorType = _gtoDB.ErrorType
class PropertyHeader(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PropertyHeader, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PropertyHeader, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _gtoDB.PropertyHeader_name_set
    __swig_getmethods__["name"] = _gtoDB.PropertyHeader_name_get
    if _newclass:name = _swig_property(_gtoDB.PropertyHeader_name_get, _gtoDB.PropertyHeader_name_set)
    __swig_setmethods__["size"] = _gtoDB.PropertyHeader_size_set
    __swig_getmethods__["size"] = _gtoDB.PropertyHeader_size_get
    if _newclass:size = _swig_property(_gtoDB.PropertyHeader_size_get, _gtoDB.PropertyHeader_size_set)
    __swig_setmethods__["type"] = _gtoDB.PropertyHeader_type_set
    __swig_getmethods__["type"] = _gtoDB.PropertyHeader_type_get
    if _newclass:type = _swig_property(_gtoDB.PropertyHeader_type_get, _gtoDB.PropertyHeader_type_set)
    __swig_setmethods__["width"] = _gtoDB.PropertyHeader_width_set
    __swig_getmethods__["width"] = _gtoDB.PropertyHeader_width_get
    if _newclass:width = _swig_property(_gtoDB.PropertyHeader_width_get, _gtoDB.PropertyHeader_width_set)
    __swig_setmethods__["interpretation"] = _gtoDB.PropertyHeader_interpretation_set
    __swig_getmethods__["interpretation"] = _gtoDB.PropertyHeader_interpretation_get
    if _newclass:interpretation = _swig_property(_gtoDB.PropertyHeader_interpretation_get, _gtoDB.PropertyHeader_interpretation_set)
    __swig_setmethods__["pad"] = _gtoDB.PropertyHeader_pad_set
    __swig_getmethods__["pad"] = _gtoDB.PropertyHeader_pad_get
    if _newclass:pad = _swig_property(_gtoDB.PropertyHeader_pad_get, _gtoDB.PropertyHeader_pad_set)
    def __init__(self, *args): 
        this = _gtoDB.new_PropertyHeader(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gtoDB.delete_PropertyHeader
    __del__ = lambda self : None;
PropertyHeader_swigregister = _gtoDB.PropertyHeader_swigregister
PropertyHeader_swigregister(PropertyHeader)

class PropertyHeader_v2(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PropertyHeader_v2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PropertyHeader_v2, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _gtoDB.PropertyHeader_v2_name_set
    __swig_getmethods__["name"] = _gtoDB.PropertyHeader_v2_name_get
    if _newclass:name = _swig_property(_gtoDB.PropertyHeader_v2_name_get, _gtoDB.PropertyHeader_v2_name_set)
    __swig_setmethods__["size"] = _gtoDB.PropertyHeader_v2_size_set
    __swig_getmethods__["size"] = _gtoDB.PropertyHeader_v2_size_get
    if _newclass:size = _swig_property(_gtoDB.PropertyHeader_v2_size_get, _gtoDB.PropertyHeader_v2_size_set)
    __swig_setmethods__["type"] = _gtoDB.PropertyHeader_v2_type_set
    __swig_getmethods__["type"] = _gtoDB.PropertyHeader_v2_type_get
    if _newclass:type = _swig_property(_gtoDB.PropertyHeader_v2_type_get, _gtoDB.PropertyHeader_v2_type_set)
    __swig_setmethods__["width"] = _gtoDB.PropertyHeader_v2_width_set
    __swig_getmethods__["width"] = _gtoDB.PropertyHeader_v2_width_get
    if _newclass:width = _swig_property(_gtoDB.PropertyHeader_v2_width_get, _gtoDB.PropertyHeader_v2_width_set)
    def __init__(self, *args): 
        this = _gtoDB.new_PropertyHeader_v2(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gtoDB.delete_PropertyHeader_v2
    __del__ = lambda self : None;
PropertyHeader_v2_swigregister = _gtoDB.PropertyHeader_v2_swigregister
PropertyHeader_v2_swigregister(PropertyHeader_v2)

class Property(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Property, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Property, name)
    __swig_setmethods__["name"] = _gtoDB.Property_name_set
    __swig_getmethods__["name"] = _gtoDB.Property_name_get
    if _newclass:name = _swig_property(_gtoDB.Property_name_get, _gtoDB.Property_name_set)
    __swig_setmethods__["interp"] = _gtoDB.Property_interp_set
    __swig_getmethods__["interp"] = _gtoDB.Property_interp_get
    if _newclass:interp = _swig_property(_gtoDB.Property_interp_get, _gtoDB.Property_interp_set)
    __swig_getmethods__["size"] = _gtoDB.Property_size_get
    if _newclass:size = _swig_property(_gtoDB.Property_size_get)
    __swig_getmethods__["width"] = _gtoDB.Property_width_get
    if _newclass:width = _swig_property(_gtoDB.Property_width_get)
    __swig_getmethods__["type"] = _gtoDB.Property_type_get
    if _newclass:type = _swig_property(_gtoDB.Property_type_get)
    def __init__(self, *args): 
        this = _gtoDB.new_Property(*args)
        try: self.this.append(this)
        except: self.this = this
    def __repr__(*args): return _gtoDB.Property___repr__(*args)
    def __cmp__(*args): return _gtoDB.Property___cmp__(*args)
    def __len__(*args): return _gtoDB.Property___len__(*args)
    def __getitem__(*args): return _gtoDB.Property___getitem__(*args)
    def __setitem__(*args): return _gtoDB.Property___setitem__(*args)
    def __contains__(*args): return _gtoDB.Property___contains__(*args)
    __swig_destroy__ = _gtoDB.delete_Property
    __del__ = lambda self : None;
Property_swigregister = _gtoDB.Property_swigregister
Property_swigregister(Property)

class PropertyVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PropertyVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PropertyVector, name)
    __repr__ = _swig_repr
    def iterator(*args): return _gtoDB.PropertyVector_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _gtoDB.PropertyVector___nonzero__(*args)
    def __len__(*args): return _gtoDB.PropertyVector___len__(*args)
    def pop(*args): return _gtoDB.PropertyVector_pop(*args)
    def __getslice__(*args): return _gtoDB.PropertyVector___getslice__(*args)
    def __setslice__(*args): return _gtoDB.PropertyVector___setslice__(*args)
    def __delslice__(*args): return _gtoDB.PropertyVector___delslice__(*args)
    def __delitem__(*args): return _gtoDB.PropertyVector___delitem__(*args)
    def __getitem__(*args): return _gtoDB.PropertyVector___getitem__(*args)
    def __setitem__(*args): return _gtoDB.PropertyVector___setitem__(*args)
    def append(*args): return _gtoDB.PropertyVector_append(*args)
    def empty(*args): return _gtoDB.PropertyVector_empty(*args)
    def size(*args): return _gtoDB.PropertyVector_size(*args)
    def clear(*args): return _gtoDB.PropertyVector_clear(*args)
    def swap(*args): return _gtoDB.PropertyVector_swap(*args)
    def get_allocator(*args): return _gtoDB.PropertyVector_get_allocator(*args)
    def begin(*args): return _gtoDB.PropertyVector_begin(*args)
    def end(*args): return _gtoDB.PropertyVector_end(*args)
    def rbegin(*args): return _gtoDB.PropertyVector_rbegin(*args)
    def rend(*args): return _gtoDB.PropertyVector_rend(*args)
    def pop_back(*args): return _gtoDB.PropertyVector_pop_back(*args)
    def erase(*args): return _gtoDB.PropertyVector_erase(*args)
    def __init__(self, *args): 
        this = _gtoDB.new_PropertyVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _gtoDB.PropertyVector_push_back(*args)
    def front(*args): return _gtoDB.PropertyVector_front(*args)
    def back(*args): return _gtoDB.PropertyVector_back(*args)
    def assign(*args): return _gtoDB.PropertyVector_assign(*args)
    def resize(*args): return _gtoDB.PropertyVector_resize(*args)
    def insert(*args): return _gtoDB.PropertyVector_insert(*args)
    def reserve(*args): return _gtoDB.PropertyVector_reserve(*args)
    def capacity(*args): return _gtoDB.PropertyVector_capacity(*args)
    __swig_destroy__ = _gtoDB.delete_PropertyVector
    __del__ = lambda self : None;
PropertyVector_swigregister = _gtoDB.PropertyVector_swigregister
PropertyVector_swigregister(PropertyVector)

class Component(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Component, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Component, name)
    __swig_setmethods__["name"] = _gtoDB.Component_name_set
    __swig_getmethods__["name"] = _gtoDB.Component_name_get
    if _newclass:name = _swig_property(_gtoDB.Component_name_get, _gtoDB.Component_name_set)
    __swig_setmethods__["interp"] = _gtoDB.Component_interp_set
    __swig_getmethods__["interp"] = _gtoDB.Component_interp_get
    if _newclass:interp = _swig_property(_gtoDB.Component_interp_get, _gtoDB.Component_interp_set)
    __swig_setmethods__["flags"] = _gtoDB.Component_flags_set
    __swig_getmethods__["flags"] = _gtoDB.Component_flags_get
    if _newclass:flags = _swig_property(_gtoDB.Component_flags_get, _gtoDB.Component_flags_set)
    def __init__(self, *args): 
        this = _gtoDB.new_Component(*args)
        try: self.this.append(this)
        except: self.this = this
    def __repr__(*args): return _gtoDB.Component___repr__(*args)
    def __len__(*args): return _gtoDB.Component___len__(*args)
    def __cmp__(*args): return _gtoDB.Component___cmp__(*args)
    def __getitem__(*args): return _gtoDB.Component___getitem__(*args)
    def __setitem__(*args): return _gtoDB.Component___setitem__(*args)
    def __delitem__(*args): return _gtoDB.Component___delitem__(*args)
    def __contains__(*args): return _gtoDB.Component___contains__(*args)
    def keys(*args): return _gtoDB.Component_keys(*args)
    def values(*args): return _gtoDB.Component_values(*args)
    def items(*args): return _gtoDB.Component_items(*args)
    def append(*args): return _gtoDB.Component_append(*args)
    def extend(*args): return _gtoDB.Component_extend(*args)
    __swig_destroy__ = _gtoDB.delete_Component
    __del__ = lambda self : None;
Component_swigregister = _gtoDB.Component_swigregister
Component_swigregister(Component)

class ComponentVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ComponentVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ComponentVector, name)
    __repr__ = _swig_repr
    def iterator(*args): return _gtoDB.ComponentVector_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _gtoDB.ComponentVector___nonzero__(*args)
    def __len__(*args): return _gtoDB.ComponentVector___len__(*args)
    def pop(*args): return _gtoDB.ComponentVector_pop(*args)
    def __getslice__(*args): return _gtoDB.ComponentVector___getslice__(*args)
    def __setslice__(*args): return _gtoDB.ComponentVector___setslice__(*args)
    def __delslice__(*args): return _gtoDB.ComponentVector___delslice__(*args)
    def __delitem__(*args): return _gtoDB.ComponentVector___delitem__(*args)
    def __getitem__(*args): return _gtoDB.ComponentVector___getitem__(*args)
    def __setitem__(*args): return _gtoDB.ComponentVector___setitem__(*args)
    def append(*args): return _gtoDB.ComponentVector_append(*args)
    def empty(*args): return _gtoDB.ComponentVector_empty(*args)
    def size(*args): return _gtoDB.ComponentVector_size(*args)
    def clear(*args): return _gtoDB.ComponentVector_clear(*args)
    def swap(*args): return _gtoDB.ComponentVector_swap(*args)
    def get_allocator(*args): return _gtoDB.ComponentVector_get_allocator(*args)
    def begin(*args): return _gtoDB.ComponentVector_begin(*args)
    def end(*args): return _gtoDB.ComponentVector_end(*args)
    def rbegin(*args): return _gtoDB.ComponentVector_rbegin(*args)
    def rend(*args): return _gtoDB.ComponentVector_rend(*args)
    def pop_back(*args): return _gtoDB.ComponentVector_pop_back(*args)
    def erase(*args): return _gtoDB.ComponentVector_erase(*args)
    def __init__(self, *args): 
        this = _gtoDB.new_ComponentVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _gtoDB.ComponentVector_push_back(*args)
    def front(*args): return _gtoDB.ComponentVector_front(*args)
    def back(*args): return _gtoDB.ComponentVector_back(*args)
    def assign(*args): return _gtoDB.ComponentVector_assign(*args)
    def resize(*args): return _gtoDB.ComponentVector_resize(*args)
    def insert(*args): return _gtoDB.ComponentVector_insert(*args)
    def reserve(*args): return _gtoDB.ComponentVector_reserve(*args)
    def capacity(*args): return _gtoDB.ComponentVector_capacity(*args)
    __swig_destroy__ = _gtoDB.delete_ComponentVector
    __del__ = lambda self : None;
ComponentVector_swigregister = _gtoDB.ComponentVector_swigregister
ComponentVector_swigregister(ComponentVector)

class Object(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Object, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Object, name)
    def __init__(self, *args): 
        this = _gtoDB.new_Object(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gtoDB.delete_Object
    __del__ = lambda self : None;
    __swig_setmethods__["name"] = _gtoDB.Object_name_set
    __swig_getmethods__["name"] = _gtoDB.Object_name_get
    if _newclass:name = _swig_property(_gtoDB.Object_name_get, _gtoDB.Object_name_set)
    __swig_setmethods__["protocol"] = _gtoDB.Object_protocol_set
    __swig_getmethods__["protocol"] = _gtoDB.Object_protocol_get
    if _newclass:protocol = _swig_property(_gtoDB.Object_protocol_get, _gtoDB.Object_protocol_set)
    __swig_setmethods__["protocolVersion"] = _gtoDB.Object_protocolVersion_set
    __swig_getmethods__["protocolVersion"] = _gtoDB.Object_protocolVersion_get
    if _newclass:protocolVersion = _swig_property(_gtoDB.Object_protocolVersion_get, _gtoDB.Object_protocolVersion_set)
    def __repr__(*args): return _gtoDB.Object___repr__(*args)
    def __len__(*args): return _gtoDB.Object___len__(*args)
    def __cmp__(*args): return _gtoDB.Object___cmp__(*args)
    def __getitem__(*args): return _gtoDB.Object___getitem__(*args)
    def __setitem__(*args): return _gtoDB.Object___setitem__(*args)
    def __delitem__(*args): return _gtoDB.Object___delitem__(*args)
    def __contains__(*args): return _gtoDB.Object___contains__(*args)
    def keys(*args): return _gtoDB.Object_keys(*args)
    def values(*args): return _gtoDB.Object_values(*args)
    def append(*args): return _gtoDB.Object_append(*args)
    def extend(*args): return _gtoDB.Object_extend(*args)
Object_swigregister = _gtoDB.Object_swigregister
Object_swigregister(Object)

class ObjectVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObjectVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ObjectVector, name)
    __repr__ = _swig_repr
    def iterator(*args): return _gtoDB.ObjectVector_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _gtoDB.ObjectVector___nonzero__(*args)
    def __len__(*args): return _gtoDB.ObjectVector___len__(*args)
    def pop(*args): return _gtoDB.ObjectVector_pop(*args)
    def __getslice__(*args): return _gtoDB.ObjectVector___getslice__(*args)
    def __setslice__(*args): return _gtoDB.ObjectVector___setslice__(*args)
    def __delslice__(*args): return _gtoDB.ObjectVector___delslice__(*args)
    def __delitem__(*args): return _gtoDB.ObjectVector___delitem__(*args)
    def __getitem__(*args): return _gtoDB.ObjectVector___getitem__(*args)
    def __setitem__(*args): return _gtoDB.ObjectVector___setitem__(*args)
    def append(*args): return _gtoDB.ObjectVector_append(*args)
    def empty(*args): return _gtoDB.ObjectVector_empty(*args)
    def size(*args): return _gtoDB.ObjectVector_size(*args)
    def clear(*args): return _gtoDB.ObjectVector_clear(*args)
    def swap(*args): return _gtoDB.ObjectVector_swap(*args)
    def get_allocator(*args): return _gtoDB.ObjectVector_get_allocator(*args)
    def begin(*args): return _gtoDB.ObjectVector_begin(*args)
    def end(*args): return _gtoDB.ObjectVector_end(*args)
    def rbegin(*args): return _gtoDB.ObjectVector_rbegin(*args)
    def rend(*args): return _gtoDB.ObjectVector_rend(*args)
    def pop_back(*args): return _gtoDB.ObjectVector_pop_back(*args)
    def erase(*args): return _gtoDB.ObjectVector_erase(*args)
    def __init__(self, *args): 
        this = _gtoDB.new_ObjectVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _gtoDB.ObjectVector_push_back(*args)
    def front(*args): return _gtoDB.ObjectVector_front(*args)
    def back(*args): return _gtoDB.ObjectVector_back(*args)
    def assign(*args): return _gtoDB.ObjectVector_assign(*args)
    def resize(*args): return _gtoDB.ObjectVector_resize(*args)
    def insert(*args): return _gtoDB.ObjectVector_insert(*args)
    def reserve(*args): return _gtoDB.ObjectVector_reserve(*args)
    def capacity(*args): return _gtoDB.ObjectVector_capacity(*args)
    __swig_destroy__ = _gtoDB.delete_ObjectVector
    __del__ = lambda self : None;
ObjectVector_swigregister = _gtoDB.ObjectVector_swigregister
ObjectVector_swigregister(ObjectVector)

class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr
    def iterator(*args): return _gtoDB.StringVector_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _gtoDB.StringVector___nonzero__(*args)
    def __len__(*args): return _gtoDB.StringVector___len__(*args)
    def pop(*args): return _gtoDB.StringVector_pop(*args)
    def __getslice__(*args): return _gtoDB.StringVector___getslice__(*args)
    def __setslice__(*args): return _gtoDB.StringVector___setslice__(*args)
    def __delslice__(*args): return _gtoDB.StringVector___delslice__(*args)
    def __delitem__(*args): return _gtoDB.StringVector___delitem__(*args)
    def __getitem__(*args): return _gtoDB.StringVector___getitem__(*args)
    def __setitem__(*args): return _gtoDB.StringVector___setitem__(*args)
    def append(*args): return _gtoDB.StringVector_append(*args)
    def empty(*args): return _gtoDB.StringVector_empty(*args)
    def size(*args): return _gtoDB.StringVector_size(*args)
    def clear(*args): return _gtoDB.StringVector_clear(*args)
    def swap(*args): return _gtoDB.StringVector_swap(*args)
    def get_allocator(*args): return _gtoDB.StringVector_get_allocator(*args)
    def begin(*args): return _gtoDB.StringVector_begin(*args)
    def end(*args): return _gtoDB.StringVector_end(*args)
    def rbegin(*args): return _gtoDB.StringVector_rbegin(*args)
    def rend(*args): return _gtoDB.StringVector_rend(*args)
    def pop_back(*args): return _gtoDB.StringVector_pop_back(*args)
    def erase(*args): return _gtoDB.StringVector_erase(*args)
    def __init__(self, *args): 
        this = _gtoDB.new_StringVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _gtoDB.StringVector_push_back(*args)
    def front(*args): return _gtoDB.StringVector_front(*args)
    def back(*args): return _gtoDB.StringVector_back(*args)
    def assign(*args): return _gtoDB.StringVector_assign(*args)
    def resize(*args): return _gtoDB.StringVector_resize(*args)
    def insert(*args): return _gtoDB.StringVector_insert(*args)
    def reserve(*args): return _gtoDB.StringVector_reserve(*args)
    def capacity(*args): return _gtoDB.StringVector_capacity(*args)
    __swig_destroy__ = _gtoDB.delete_StringVector
    __del__ = lambda self : None;
StringVector_swigregister = _gtoDB.StringVector_swigregister
StringVector_swigregister(StringVector)

class GtoDB(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GtoDB, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GtoDB, name)
    __repr__ = _swig_repr
    BinaryGTO = _gtoDB.GtoDB_BinaryGTO
    CompressedGTO = _gtoDB.GtoDB_CompressedGTO
    TextGTO = _gtoDB.GtoDB_TextGTO
    def __init__(self, *args): 
        this = _gtoDB.new_GtoDB(*args)
        try: self.this.append(this)
        except: self.this = this
    def read(*args): return _gtoDB.GtoDB_read(*args)
    def write(*args): return _gtoDB.GtoDB_write(*args)
    def __len__(*args): return _gtoDB.GtoDB___len__(*args)
    def __getitem__(*args): return _gtoDB.GtoDB___getitem__(*args)
    def __setitem__(*args): return _gtoDB.GtoDB___setitem__(*args)
    def __delitem__(*args): return _gtoDB.GtoDB___delitem__(*args)
    def __contains__(*args): return _gtoDB.GtoDB___contains__(*args)
    def keys(*args): return _gtoDB.GtoDB_keys(*args)
    def values(*args): return _gtoDB.GtoDB_values(*args)
    def items(*args): return _gtoDB.GtoDB_items(*args)
    def append(*args): return _gtoDB.GtoDB_append(*args)
    def extend(*args): return _gtoDB.GtoDB_extend(*args)
    def dumpInfo(*args): return _gtoDB.GtoDB_dumpInfo(*args)
    __swig_destroy__ = _gtoDB.delete_GtoDB
    __del__ = lambda self : None;
GtoDB_swigregister = _gtoDB.GtoDB_swigregister
GtoDB_swigregister(GtoDB)



