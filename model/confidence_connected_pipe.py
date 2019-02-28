from model.pipe import Pipe
import itk

__author__ = 'Alvaro Javier'


class ConfidenceConnectedPipe(Pipe):
    _default_replace_value = 255
    _default_seed = [0,0,0]
    _default_initial_radius = 1
    _default_multiplier = 2.5
    _default_iterations = 10
    def __init__(self, pt, dim, to_pt=None):
        super(ConfidenceConnectedPipe, self).__init__(pt, dim, to_pt)
        itkFilter = itk.ConfidenceConnectedImageFilter[self.InputImageType, self.OutputImageType].New()
        self._internal_filter = itkFilter
        self.ReplaceValue   = self._default_replace_value
        self.Seed           = self._default_seed
        self.InitialRadius  = self._default_initial_radius
        self.Multiplier     = self._default_multiplier

    @property
    def ReplaceValue(self):
        return self._internal_filter.GetReplaceValue()

    @ReplaceValue.setter
    def ReplaceValue(self,value):
        self._internal_filter.SetReplaceValue(value)

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
    def InitialRadius(self):
        return self._internal_filter.GetInitialNeighborhoodRadius()

    @InitialRadius.setter
    def InitialRadius(self,radius):
        self._internal_filter.SetInitialNeighborhoodRadius(radius)

    @property
    def Multiplier(self):
        return self._internal_filter.GetMultiplier()

    @Multiplier.setter
    def Multiplier(self,mult):
        self._internal_filter.SetMultiplier(mult)

    @property
    def NumberOfIterations(self):
        return self._internal_filter.GetNumberOfIterations()

    @NumberOfIterations.setter
    def NumberOfIterations(self, num):
        self._internal_filter.SetNumberOfIterations(num)


