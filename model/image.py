__author__ = 'Alvaro Javier'

import itk

class Image(object):
    _counter = 0

    def __init__(self, pt, dim, displayName="", originalFormat="", originalFile=""):
        self._id = Image._counter
        Image._counter += 1
        self._pixel_type = pt
        self._dimension = dim
        self._image_type = itk.Image[pt, dim]
        self._internal_image = None
        self._display_name = displayName
        if not displayName:
            self._display_name = "img" + str(self._id)
        self._original_format = originalFormat
        self._original_file = originalFile

    @property
    def InternalImage(self):
        return self._internal_image

    @InternalImage.setter
    def InternalImage(self, inter_img):
        self._internal_image = inter_img

    @property
    def Id(self):
        return self._id

    @property
    def PixelType(self):
        return self._pixel_type

    @property
    def Dimension(self):
        return self._dimension

    @property
    def ImageType(self):
        return self._image_type

    @property
    def DisplayName(self):
        return self._display_name

    @DisplayName.setter
    def DisplayName(self, value):
        self._display_name = value

    @property
    def OriginalFormat(self):
        return self._original_format

    @property
    def OriginalFile(self):
        return self._original_file

    @property
    def Size(self):
        itk_siz = self.InternalImage.GetLargestPossibleRegion().GetSize()
        return [itk_siz.GetElement(i) for i in range(self.Dimension)]

    @property
    def Spacing(self):
        itk_spc = self.InternalImage.GetSpacing()
        return [itk_spc.GetElement(i) for i in range(self.Dimension)]

    @Spacing.setter
    def Spacing(self,spc):
        self.InternalImage.SetSpacing(tuple(spc))

    @property
    def Origin(self):
        itk_org = self.InternalImage.GetOrigin()
        return [itk_org.GetElement(i) for i in range(self.Dimension)]

    @Origin.setter
    def Origin(self,org):
        itk_org = self.InternalImage.SetOrigin(org)
