"""test_measureobjectintensity - test the MeasureObjectIntensity module

CellProfiler is distributed under the GNU General Public License.
See the accompanying file LICENSE for details.

Developed by the Broad Institute
Copyright 2003-2009

Please see the AUTHORS file for credits.

Website: http://www.cellprofiler.org
"""
__version__="$Revision$"

import base64
import math
import numpy
from StringIO import StringIO
import unittest
import zlib

import cellprofiler.modules.injectimage as II
import cellprofiler.modules.measureobjectintensity as MOI
import cellprofiler.pipeline as P
import cellprofiler.measurements as cpmeas
#
# This is a pipeline consisting of Matlab modules for LoadImages,
# IdentifyPrimAutomatic and MeasureObjectIntensity
#
pipeline_data = 'TUFUTEFCIDUuMCBNQVQtZmlsZSwgUGxhdGZvcm06IFBDV0lOLCBDcmVhdGVkIG9uOiBXZWQgRmViIDExIDE2OjU4OjUyIDIwMDkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAABSU0PAAAAkgIAAHic7VhPb9MwFHfatPwZmsomJtRTjhzGaAUHjlQqgkqsrdg0iaObuMUoiavEnlo+xaR9EY4cOCDxxYjbpHW8UudvAamWLOs57/3eez87z04OAQCNEwDqwXg/6BWwbLVQ1oTO5QtEKXYnfg3o4Gk4/zPoV9DDcGSjK2gz5INVi+Z77phczqerR+fEYjbqQ0dUDlqfOSPk+YNxZBg+HuIZsi/wVwTiLVL7iK6xj4kb2of48uzKL6GS38OgfztY86BJPFSDfizMc/03YK2vb+CtIeg3wn6JZvT52xk0qeFAan7mOC0FTjWGUwXdfgeUaafH7HTQ7Qx73O61wq4u5cvlPjNthJd85bXPmq/Kb03yy+V26/QV95dknR9K9lzuEsMl1GB+uGGLxEnLw6dgr/+PeVRiOBXQJ/v1KDMPFc6BhMPlAfWZ8c4mI2jvPJ6i1keL4WigHdrtOg55n7RO27E40ubxMqGdXO9bZ612GfmrcB5IOFzuuRS5PqZzIZ5ofK/AeyzhcRm7Fr7GFoO2gR04Wd0CyoivrPq2KY4OoyS4UGAzQxzyvjnLwce2OLLgTTw4901oIwEna73Na6+KP+l7kDSOss+/rHy4L2Ah65CXh8j+pr793i7Wgbx1bVE0Jh5h0+JxojFLXSOjL8ikC0AjqHFomiLPTee6gJcYZ9P3zjrPZVi7jCcpzq552vO95/tv8C2PReWr8vOvj6p6ewTiPHCZMGpjF90puCJuQ/vzuSSfj1nPkQ8EWj3hIpsknycSDpd7FnIpHs+HHnbEO1wSvBMJj8vnCPrMQ4PFdhQuyfJ5X1fwUgmko+N7ub7j0vqrParc+W+kstNDnV/NH83b5tLvd5Bu/Z9t0Y/arvR/A0/mSFM='

class TestMeasureObjects(unittest.TestCase):
    def error_callback(self, calller, event):
        if isinstance(event, P.RunExceptionEvent):
            self.fail(event.error.message)
    
    def test_01_01_load(self):
        pipeline = P.Pipeline()
        pipeline.add_listener(self.error_callback)
        fd = StringIO(base64.b64decode(pipeline_data))
        pipeline.load(fd)
        self.assertEqual(len(pipeline.modules()),3)
        module = pipeline.modules()[2]
        self.assertTrue(isinstance(module,MOI.MeasureObjectIntensity))
        self.assertEqual(len(module.object_names),1)
        self.assertEqual(module.object_names[0].value,'Nuclei')
        self.assertEqual(module.image_names[0].value,'DNA')
        
    def test_01_02_load_v2(self):
        data = ('eJztW0Fv2zYUpl0nWFagS08dhhXgoYckiDXZq9E0KFo78boZqB2jNtoNadYx'
                'Mm1zkEVDotK4Re/9qTvmuONEW7IlTolkS4qdVAIE+VH8+L33+PhIyVS90n5V'
                'OYAlSYb1SjvfJSqGTRWxLtUH+1Bju/BQx4jhDqTaPmybGDboGSw+hoXifqm0'
                'X5BhUZafgsWOTK1+z7pcPANg3bp+Y51Z+9aaLWdcJ5dbmDGi9Yw1kAPf2+UX'
                '1vkG6QSdqvgNUk1szCic8prWpe3RcHqrTjumihto4K5sHQ1zcIp146jrAO3b'
                'TXKO1Rb5iAUTnGqv8RkxCNVsvN2+WDrlpUzgbfXph5e6pY7Q/gFiSr/FrB7w'
                'lnO/bf0481tG8FvOOh+6ynn938Csfs7Hz/dd9TdtmWgdckY6JlIhGaDeVGve'
                'nhzQ3h1Pe3dAtVEZ4/YCcOuCHlxumIqKSTTecgBuU+DlZxufs/wv50hhcMC7'
                'Ig79g/BrAp7Lh1hVDbA4vqJYwwaE81/Gg8+AnyPwFuTdx7KND/L/XQHP5aZO'
                'h6iHmDWIxuVh2vlWaIfLVQo1yqBp2OMoznbmjcc/rFEURz9GjaMgvbMefBY0'
                'aDRckL/9+v+IGSb8VaWnSJ36O+r4C8qDDwQ8l6u4i0yVwRpPgrBKdKwwqo8i'
                '9f+8uIIk/w+3LuCcw8Ft2NcouHKAnmH7bZH5R5bk8bFbsH/EYM8y+8sPl/Pg'
                'ctzmQpL2XTY+k+yfMHoU5GT7ddF8FqZ/QuJKqzh+N4C3X7lc0xjWDMJGrnYW'
                'iY8WVqjWQfroyGQq0S5dPyZtz2EfaRpWC/kE/DJvXpBjzOPzrH/jGI9h4rxB'
                'NZykfeL6tLAg7klIXJi8Ead9Yfw5z7xVDsD5zd/tDxQqKjIMe8RGsbcfwP9E'
                '4Ofyn1svms/4iwj8XNrZfs+lt9bS9flxJd88OZbzT08+FT9vvzf4jRaxao3L'
                'tkPZ+53Ax+Wmbj3eurLUovnuLSa9Pn9dcsZfDGiK89gexX+/B+jxSNCDy9LO'
                '8bt3P51w91RtJ04LXpsalx/56RVnXPk9P72kOu7p1NQ60f0SxH/FPFB0zwNx'
                'rAevYx5P+rl/VeycN48XF7Qvznl4FfJ/kvPwKuf7Zc7ftyGPLzP+k1z3ylJp'
                '6Xom/Z4lznXadeNWZX21av2c9Lpp1cftbctL4nqltCQ9v/www2UEnN//hdcZ'
                '3+M/F3mAD8O345cP6enfWGGzhuLU5zrznMsOSLQOHibY3rL9k+Juxji6LX67'
                'bfamuBSX4lJc1Ly4Cbx5kZ+z+WSybLhJ9n5t/g3iT9dxKS4JXBksN+5T3NeJ'
                'K4M07lJcOu+luBSX4lJciktxNwn3b2aGywg4Lrv3s/D6f7l4/Ob5HVf9TVtW'
                'sKoOdcq/a9SlwfjjO0NSKepMvmaTXlk/a64P2zjPMICnLPCUL+MhHawx0h0N'
                '+eZCk9EBYkSRanYp33JYcUo5bz+Ad0/g3QviNZzN11PO6XZszncewHcg8B1c'
                'xjfAyDB1PHmHTpwd0lJ9Unw0LhY2Totxs+HD7+7/rCU9eHh/7ap4A8AbZ7P4'
                'u3ixCF8ul83eA959d3cDcDngjXuO/wfMF+dbV9R3bFzl+vP6OWMdUf0048lN'
                'dZq0v5r1/wNnl0Vu')
        pipeline = P.Pipeline()
        def callback(caller,event):
            self.assertFalse(isinstance(event, P.LoadExceptionEvent))
        pipeline.add_listener(callback)
        pipeline.load(StringIO(zlib.decompress(base64.b64decode(data))))
        self.assertEqual(len(pipeline.modules()), 4)
        module = pipeline.modules()[-1]
        self.assertTrue(isinstance(module, MOI.MeasureObjectIntensity))
        self.assertEqual(len(module.image_names), 2)
        for expected, actual in zip(("DNA","Actin"),module.image_names):
            self.assertEqual(expected, actual)
        self.assertEqual(len(module.object_names), 2)
        for expected, actual in zip(("Cells","Nuclei"), module.object_names):
            self.assertEqual(expected, actual)
        
    def test_02_01_supplied_measurements(self):
        """Test the get_category / get_measurements, get_measurement_images functions"""
        
        moi = MOI.MeasureObjectIntensity()
        moi.image_names[0].value='MyImage'
        moi.add_cb()
        moi.object_names[0].value = 'MyObjects1'
        moi.object_names[1].value = 'MyObjects2'
        
        self.assertEqual(moi.get_categories(None, 'MyObjects1'),[MOI.INTENSITY])
        self.assertEqual(moi.get_categories(None, 'Foo'),[])
        measurements = moi.get_measurements(None,'MyObjects1',MOI.INTENSITY)
        self.assertEqual(len(measurements),len(MOI.ALL_MEASUREMENTS))
        self.assertTrue(all([m in MOI.ALL_MEASUREMENTS for m in measurements]))
        self.assertTrue(moi.get_measurement_images(None,'MyObjects1',
                                                   MOI.INTENSITY,
                                                   MOI.MAX_INTENSITY),
                        ['MyImage'])
    
    def test_02_02_get_measurement_columns(self):
        '''test the get_measurement_columns method'''
        moi = MOI.MeasureObjectIntensity()
        moi.image_names[0].value='MyImage'
        moi.add_cb()
        moi.object_names[0].value = 'MyObjects1'
        moi.object_names[1].value = 'MyObjects2'
        columns = moi.get_measurement_columns(None)
        self.assertEqual(len(columns), 2*len(MOI.ALL_MEASUREMENTS))
        for column in columns:
            self.assertTrue(column[0] in ('MyObjects1','MyObjects2'))
            self.assertEqual(column[2], cpmeas.COLTYPE_FLOAT)
            self.assertEqual(column[1].split('_')[0], MOI.INTENSITY)
            self.assertTrue(column[1][column[1].find('_')+1:] in 
                            [m+'_MyImage' for m in MOI.ALL_MEASUREMENTS])

    def features_and_columns_match(self, measurements, module):
        object_names = [x for x in measurements.get_object_names()
                        if x != cpmeas.IMAGE]
        features = [[f for f in measurements.get_feature_names(object_name)
                     if f != 'Exit_Status']
                    for object_name in object_names]
        columns = module.get_measurement_columns(None)
        self.assertEqual(sum([len(f) for f in features]), len(columns))
        for column in columns:
            index = object_names.index(column[0])
            self.assertTrue(column[1] in features[index])
            self.assertTrue(column[2] == cpmeas.COLTYPE_FLOAT)
        
    def test_03_01_zero(self):
        """Make sure we can process a blank image"""
        ii = II.InjectImage('MyImage',numpy.zeros((10,10)))
        ii.module_num = 1
        io = II.InjectObjects('MyObjects',numpy.zeros((10,10),int))
        io.module_num = 2
        moi = MOI.MeasureObjectIntensity()
        moi.image_names[0].value = 'MyImage'
        moi.object_names[0].value = 'MyObjects'
        moi.module_num = 3
        pipeline = P.Pipeline()
        pipeline.add_listener(self.error_callback)
        pipeline.add_module(ii)
        pipeline.add_module(io)
        pipeline.add_module(moi)
        m = pipeline.run()
        for meas_name in MOI.ALL_MEASUREMENTS:
            feature_name = "%s_%s_%s"%(MOI.INTENSITY, meas_name, 'MyImage')
            data = m.get_current_measurement('MyObjects',feature_name)
            self.assertEqual(numpy.product(data.shape),0,"Got data for feature %s"%(feature_name))
        self.features_and_columns_match(m, moi)
        
    def test_03_02_one(self):
        """Check measurements on a 3x3 square of 1's"""
        img = numpy.array([[0,0,0,0,0,0,0],
                           [0,0,1,1,1,0,0],
                           [0,0,1,1,1,0,0],
                           [0,0,1,1,1,0,0],
                           [0,0,0,0,0,0,0]])
        ii = II.InjectImage('MyImage',img.astype(float))
        ii.module_num = 1
        io = II.InjectObjects('MyObjects',img.astype(int))
        io.module_num = 2
        moi = MOI.MeasureObjectIntensity()
        moi.image_names[0].value = 'MyImage'
        moi.object_names[0].value = 'MyObjects'
        moi.module_num = 3
        pipeline = P.Pipeline()
        pipeline.add_listener(self.error_callback)
        pipeline.add_module(ii)
        pipeline.add_module(io)
        pipeline.add_module(moi)
        m = pipeline.run()
        for meas_name,value in ((MOI.INTEGRATED_INTENSITY,9),
                                (MOI.MEAN_INTENSITY,1),
                                (MOI.STD_INTENSITY,0),
                                (MOI.MIN_INTENSITY,1),
                                (MOI.MAX_INTENSITY,1),
                                (MOI.INTEGRATED_INTENSITY_EDGE,8),
                                (MOI.MEAN_INTENSITY_EDGE,1),
                                (MOI.STD_INTENSITY_EDGE,0),
                                (MOI.MIN_INTENSITY_EDGE,1),
                                (MOI.MAX_INTENSITY_EDGE,1),
                                (MOI.MASS_DISPLACEMENT,0),
                                (MOI.LOWER_QUARTILE_INTENSITY,1),
                                (MOI.MEDIAN_INTENSITY,1),
                                (MOI.UPPER_QUARTILE_INTENSITY,1)):
            feature_name = "%s_%s_%s"%(MOI.INTENSITY, meas_name, 'MyImage')
            data = m.get_current_measurement('MyObjects',feature_name)
            self.assertEqual(numpy.product(data.shape),1)
            self.assertEqual(data[0],value,"%s expected %f != actual %f"%(meas_name, value, data[0]))
        
    def test_03_03_mass_displacement(self):
        """Check the mass displacement of three squares"""
        
        labels = numpy.array([[0,0,0,0,0,0,0],
                              [0,1,1,1,1,1,0],
                              [0,1,1,1,1,1,0],
                              [0,1,1,1,1,1,0],
                              [0,1,1,1,1,1,0],
                              [0,1,1,1,1,1,0],
                              [0,0,0,0,0,0,0],
                              [0,2,2,2,2,2,0],
                              [0,2,2,2,2,2,0],
                              [0,2,2,2,2,2,0],
                              [0,2,2,2,2,2,0],
                              [0,2,2,2,2,2,0],
                              [0,0,0,0,0,0,0],
                              [0,3,3,3,3,3,0],
                              [0,3,3,3,3,3,0],
                              [0,3,3,3,3,3,0],
                              [0,3,3,3,3,3,0],
                              [0,3,3,3,3,3,0],
                              [0,0,0,0,0,0,0]])
        image = numpy.zeros(labels.shape,dtype=float)
        #
        # image # 1 has a single value in one of the corners
        # whose distance is sqrt(8) from the center
        #
        image[1,1] = 1
        # image # 2 has a single value on the top edge
        # and should have distance 2
        #
        image[7,3] = 1
        # image # 3 has a single value on the left edge
        # and should have distance 2
        image[15,1] = 1
        ii = II.InjectImage('MyImage',image)
        ii.module_num = 1
        io = II.InjectObjects('MyObjects',labels)
        io.module_num = 2
        moi = MOI.MeasureObjectIntensity()
        moi.image_names[0].value = 'MyImage'
        moi.object_names[0].value = 'MyObjects'
        moi.module_num = 3
        pipeline = P.Pipeline()
        pipeline.add_listener(self.error_callback)
        pipeline.add_module(ii)
        pipeline.add_module(io)
        pipeline.add_module(moi)
        m = pipeline.run()
        feature_name = '%s_%s_%s'%(MOI.INTENSITY,MOI.MASS_DISPLACEMENT,'MyImage')
        mass_displacement = m.get_current_measurement('MyObjects', feature_name)
        self.assertEqual(numpy.product(mass_displacement.shape),3)
        self.assertAlmostEqual(mass_displacement[0],math.sqrt(8.0))
        self.assertAlmostEqual(mass_displacement[1],2.0)
        self.assertAlmostEqual(mass_displacement[2],2.0)
        
    def test_03_04_quartiles(self):
        """test quartile values on a 250x250 square filled with uniform values"""
        labels = numpy.ones((250,250),int)
        numpy.random.seed(0)
        image = numpy.random.uniform(size=(250,250))
        ii = II.InjectImage('MyImage',image)
        ii.module_num = 1
        io = II.InjectObjects('MyObjects',labels)
        io.module_num = 2
        moi = MOI.MeasureObjectIntensity()
        moi.image_names[0].value = 'MyImage'
        moi.object_names[0].value = 'MyObjects'
        moi.module_num = 3
        pipeline = P.Pipeline()
        pipeline.add_listener(self.error_callback)
        pipeline.add_module(ii)
        pipeline.add_module(io)
        pipeline.add_module(moi)
        m = pipeline.run()
        feature_name = '%s_%s_%s'%(MOI.INTENSITY,MOI.LOWER_QUARTILE_INTENSITY,'MyImage')
        data = m.get_current_measurement('MyObjects',feature_name)
        self.assertAlmostEqual(data[0],.25,2)
        feature_name = '%s_%s_%s'%(MOI.INTENSITY,MOI.MEDIAN_INTENSITY,'MyImage')
        data = m.get_current_measurement('MyObjects',feature_name)
        self.assertAlmostEqual(data[0],.50,2)
        feature_name = '%s_%s_%s'%(MOI.INTENSITY,MOI.UPPER_QUARTILE_INTENSITY,'MyImage')
        data = m.get_current_measurement('MyObjects',feature_name)
        self.assertAlmostEqual(data[0],.75,2)
        
    def test_03_05_quartiles(self):
        """Regression test a bug that occurs in an image with one pixel"""
        labels = numpy.zeros((10,20))
        labels[2:7,3:8] = 1
        labels[5,15] = 2
        numpy.random.seed(0)
        image = numpy.random.uniform(size=(10,20))
        ii = II.InjectImage('MyImage',image)
        ii.module_num = 1
        io = II.InjectObjects('MyObjects',labels)
        io.module_num = 2
        moi = MOI.MeasureObjectIntensity()
        moi.image_names[0].value = 'MyImage'
        moi.object_names[0].value = 'MyObjects'
        moi.module_num = 3
        pipeline = P.Pipeline()
        pipeline.add_listener(self.error_callback)
        pipeline.add_module(ii)
        pipeline.add_module(io)
        pipeline.add_module(moi)
        # Crashes when pipeline runs in measureobjectintensity.py revision 7146
        m = pipeline.run()

        
