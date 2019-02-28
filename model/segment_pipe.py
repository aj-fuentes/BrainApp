from model.pipe import Pipe
import itk

__author__ = 'Alvaro Javier'

class SegmentPipe(Pipe):
    _default_replace_value = 255
    _default_lower_threshold = 0
    _default_upper_threshold = 255
    _default_seed = [0,0,0]

    def __init__(self, pt, dim, to_pt=None):
        super(SegmentPipe, self).__init__(pt, dim, to_pt)
        itkFilter = itk.ConnectedThresholdImageFilter[self.InputImageType, self.OutputImageType].New()
        self._internal_filter = itkFilter
        self.ReplaceValue   = self._default_replace_value
        self.LowerThreshold = self._default_lower_threshold
        self.UpperThreshold = self._default_upper_threshold
        self.Seed           = self._default_seed

    @property
    def LowerThreshold(self):
        return self._internal_filter.GetLower()

    @LowerThreshold.setter
    def LowerThreshold(self,val):
        self._internal_filter.SetLower(val)

    @property
    def UpperThreshold(self):
        return self._internal_filter.GetUpper()

    @UpperThreshold.setter
    def UpperThreshold(self,val):
        self._internal_filter.SetUpper(val)

    @property
    def Seed(self):
        return self._seed

    @Seed.setter
    def Seed(self,seed):
        self._seed = seed
        self._internal_filter.SetSeed(seed)

    def addSeed(self, seed):
        self._internal_filter.AddSeed(seed)

    @property
    def ReplaceValue(self):
        return self._internal_filter.GetReplaceValue()

    @ReplaceValue.setter
    def ReplaceValue(self,value):
        self._internal_filter.SetReplaceValue(value)


