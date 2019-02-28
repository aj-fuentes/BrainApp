from model.pipe import Pipe
import itk

__author__ = 'Alvaro Javier'

class SmoothPipe(Pipe):
    _default_time_steps = {
        2: 0.125,
        3: 0.0625
    }
    _default_iterations = {
        2: 5,
        3: 5
    }
    _default_conductance_values = {
        2: 3,
        3: 3
    }

    def __init__(self, pt, dim, to_pt=None):
        super(SmoothPipe, self).__init__(pt, dim, to_pt)
        itkFilter = itk.CurvatureAnisotropicDiffusionImageFilter[self.InputImageType, self.OutputImageType].New()
        #self._pp = itk.SimpleFilterWatcher(itkFilter.GetPointer(),"smooth")
        self._internal_filter = itkFilter
        self.NumberOfIterations = self._default_iterations[dim]
        self.TimeStep = self._default_time_steps[dim]
        self.Conductance = self._default_conductance_values[dim]

    @property
    def NumberOfIterations(self):
        return self._internal_filter.GetNumberOfIterations()

    @NumberOfIterations.setter
    def NumberOfIterations(self, num):
        self._internal_filter.SetNumberOfIterations(num)

    @property
    def TimeStep(self):
        return self._internal_filter.GetTimeStep()

    @TimeStep.setter
    def TimeStep(self,step):
        self._internal_filter.SetTimeStep(step)

    @property
    def Conductance(self):
        return self._internal_filter.GetConductanceParameter()

    @Conductance.setter
    def Conductance(self,cond):
        self._internal_filter.SetConductanceParameter(cond)




