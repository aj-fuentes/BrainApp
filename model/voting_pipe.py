#! -*- coding: cp1252 -*-
import itk

__author__ = 'Alvaro Javier'
from model.pipe import Pipe

class VotingPipe(Pipe):
    _default_background = 0
    _default_foreground = 255

    def __init__(self, pt, dim, to_pt=None):
        super(VotingPipe, self).__init__(pt, dim, to_pt)
        self._internal_filter = itk.VotingBinaryImageFilter[self.InputImageType,self.OutputImageType].New()
        self._internal_filter.SetBackgroundValue(self._default_background)
        self._internal_filter.SetForegroundValue(self._default_foreground)

    @property
    def Radius(self):
        itk_siz = self._internal_filter.GetRadius()
        return [itk_siz.GetElement(i) for i in range(self.Dimension)]

    @Radius.setter
    def Radius(self,radius):
        self._internal_filter.SetRadius(radius)

    @property
    def Background(self):
        return self._internal_filter.GetBackgroundValue()

    @Background.setter
    def Background(self,value):
        self._internal_filter.SetBackgroundValue(value)

    @property
    def Foreground(self):
        return self._internal_filter.GetForegroundValue()

    @Foreground.setter
    def Foreground(self,value):
        self._internal_filter.SetForegroundValue(value)

    @property
    def SurvivalValue(self):
        return self._internal_filter.GetSurvivalThreshold()

    @SurvivalValue.setter
    def SurvivalValue(self,value):
        self._internal_filter.SetSurvivalThreshold(value)

    @property
    def BirthValue(self):
        return self._internal_filter.GetBirthThreshold()

    @BirthValue.setter
    def BirthValue(self,value):
        self._internal_filter.SetBirthThreshold(value)


