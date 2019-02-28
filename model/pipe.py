#! -*- coding: cp1252 -*-
from model.image import Image

__author__ = 'Alvaro Javier'

import itk

class Pipe(object):
    def __init__(self, pt, dim, to_pt=None):
        self._input_pixel_type = pt
        if to_pt is None:
            to_pt = pt
        self._output_pixel_type = to_pt
        self._dimension = dim
        self._input_image_type = itk.Image[pt, dim]
        self._output_image_type = itk.Image[to_pt, dim]
        self._internal_filter = None
        self._output_image = Image(self._output_pixel_type, self._dimension)

    @property
    def InputPixelType(self):
        return self._input_pixel_type

    @property
    def OutputPixelType(self):
        return self._output_pixel_type

    @property
    def Dimension(self):
        return self._dimension

    @property
    def InputImageType(self):
        return self._input_image_type

    @property
    def OutputImageType(self):
        return self._output_image_type

    def update(self):
        if self._internal_filter is not None:
            self._internal_filter.Update()

    def setInput(self, img):
        self._internal_filter.SetInput(img.InternalImage)

    def getOutput(self):
        self._output_image.InternalImage = self._internal_filter.GetOutput()
        return self._output_image

    def connect(self,pipe):
        """
        se usa para conectar esta tubería a otra de manera que funcione como una tubería ITK
        @param pipe: nueva tubería a conectar
        """
        self._internal_filter.SetInput(pipe._internal_filter.GetOutput())