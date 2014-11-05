class _source_property:
    def __init__(self, typename):
        self.typename = typename
    def __get__(self, obj, cls):
        return _class_template.format(
            typename=self.typename,
            field_names=tuple(cls._fields),
            arg_list=repr(tuple(cls._fields)).replace("'", "")[1:-1],
            field_defs='\n'.join(_field_template.format(index=index, name=name)
                                 for index, name in enumerate(cls._fields))
        )


class_template = ""
from builtins import property as _property, tuple as _tuple
from operator import itemgetter as _itemgetter
from collections import OrderedDict
from collections import OrderedDict, _source_property
class {typename}(tuple):
     '{typename}({arg_list})'
@@ -253,8 +267,9 @@ class {typename}(tuple):
     def _make(cls, iterable, new=tuple.__new__, len=len):
         'Make a new {typename} object from a sequence or iterable'
         result = new(cls, iterable)
-        if len(result) != {num_fields:d}:
-            raise TypeError('Expected {num_fields:d} arguments, got %d' % len(result))
+        if len(result) != len(cls._fields):
+            raise TypeError('Expected %d arguments, got %d'
+                            % (len(cls._fields), len(result)))
         return result
 
     def _replace(_self, **kwds):
@@ -266,7 +281,10 @@ class {typename}(tuple):
 
     def __repr__(self):
         'Return a nicely formatted representation string'
-        return self.__class__.__name__ + '({repr_fmt})' % self
+        repr_fmt = ', '.join(name + '=%r'
+                             for name in self._fields)
+        fmt = '%s(%s)' % (self.__class__.__name__, repr_fmt)
+        return fmt % self
 
     @property
     def __dict__(self):
@@ -287,11 +305,11 @@ class {typename}(tuple):
         'Exclude the OrderedDict from pickling'
         return None
 
+    _source = _source_property({typename!r})
+
 {field_defs}
 """
 
-_repr_template = '{name}=%r'
-
 _field_template = '''\
     {name} = _property(_itemgetter({index:d}), doc='Alias for field number {index:d}')
 '''
@@ -352,14 +370,11 @@ def namedtuple(typename, field_names, ve
 
     # Fill-in the class template
     class_definition = _class_template.format(
-        typename = typename,
-        field_names = tuple(field_names),
-        num_fields = len(field_names),
-        arg_list = repr(tuple(field_names)).replace("'", "")[1:-1],
-        repr_fmt = ', '.join(_repr_template.format(name=name)
-                             for name in field_names),
-        field_defs = '\n'.join(_field_template.format(index=index, name=name)
-                               for index, name in enumerate(field_names))
+        typename=typename,
+        field_names=tuple(field_names),
+        arg_list=repr(tuple(field_names)).replace("'", "")[1:-1],
+        field_defs='\n'.join(_field_template.format(index=index, name=name)
+                             for index, name in enumerate(field_names))
     )
 
     # Execute the template string in a temporary namespace and support
@@ -367,9 +382,8 @@ def namedtuple(typename, field_names, ve
     namespace = dict(__name__='namedtuple_%s' % typename)
     exec(class_definition, namespace)
     result = namespace[typename]
-    result._source = class_definition
     if verbose:
-        print(result._source)
+        print(class_definition)
 
     # For pickling to work, the __module__ variable needs to be set to the frame
     # where the named tuple is created.  Bypass this step in environments where
diff -r 1b096c601d84 Lib/test/test_collections.py
--- a/Lib/test/test_collections.py	Tue Mar 18 09:01:21 2014 +0100
+++ b/Lib/test/test_collections.py	Tue Mar 18 09:55:37 2014 +0100
@@ -8,6 +8,8 @@ from collections import namedtuple, Coun
 from test import mapping_tests
 import pickle, copy
 from random import randrange, shuffle
+import contextlib
+import io
 import keyword
 import re
 import sys
@@ -361,16 +363,25 @@ class TestNamedTuple(unittest.TestCase):
             pass
         self.assertEqual(repr(B(1)), 'B(x=1)')
 
+    def check_exec_source(self, source):
+        namespace = {}
+        exec(source, namespace, namespace)
+        self.assertIn('NTColor', namespace)
+        NTColor = namespace['NTColor']
+        c = NTColor(10, 20, 30)
+        self.assertEqual((c.red, c.green, c.blue), (10, 20, 30))
+        self.assertEqual(NTColor._fields, ('red', 'green', 'blue'))
+
     def test_source(self):
         # verify that _source can be run through exec()
         tmp = namedtuple('NTColor', 'red green blue')
-        globals().pop('NTColor', None)          # remove artifacts from other tests
-        exec(tmp._source, globals())
-        self.assertIn('NTColor', globals())
-        c = NTColor(10, 20, 30)
-        self.assertEqual((c.red, c.green, c.blue), (10, 20, 30))
-        self.assertEqual(NTColor._fields, ('red', 'green', 'blue'))
-        globals().pop('NTColor', None)          # clean-up after this test
+        self.check_exec_source(tmp._source)
+
+    def test_verbose(self):
+        stdout = io.StringIO()
+        with contextlib.redirect_stdout(stdout):
+            tmp = namedtuple('NTColor', 'red green blue', verbose=True)
+        self.check_exec_source(stdout.getvalue())
 
 
 ################################################################################