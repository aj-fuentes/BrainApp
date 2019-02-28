from model.pipe import Pipe
import itk

__author__ = 'Alvaro Javier'


class CastPipe(Pipe):
    def __init__(self, pt, dim, to_pt=None):
        super(CastPipe, self).__init__(pt, dim, to_pt or itk.F)
        itkFilter = itk.CastImageFilter[self.InputImageType, self.OutputImageType].New()
        self._internal_filter = itkFilter
