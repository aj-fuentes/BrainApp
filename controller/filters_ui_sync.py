#! -*- coding: cp1252 -*-

from itertools import imap
from PyQt4.QtCore import Qt
from model.application import Application

__author__ = 'Alvaro Javier'

class FiltersUiSync(object):

    def __init__(self,_properties_tree):
        self._properties_tree = _properties_tree

        root = self._properties_tree.invisibleRootItem()
        self._smoother_prop     = root.child(0)
        self._iterations_prop   = root.child(0).child(0)
        self._time_step_prop    = root.child(0).child(1)
        self._conductance_prop  = root.child(0).child(2)

        self._segment_prop          = root.child(1)
        self._seed_prop             = root.child(1).child(0)
        self._seedX_prop            = root.child(1).child(0).child(0)
        self._seedY_prop            = root.child(1).child(0).child(1)
        self._seedZ_prop            = root.child(1).child(0).child(2)
        self._min_threshold_prop    = root.child(1).child(1)
        self._max_threshold_prop    = root.child(1).child(2)
        self._replace_value_prop    = root.child(1).child(3)

        self._confidence_prop       = root.child(2)
        self._conf_seed_prop        = root.child(2).child(0)
        self._conf_seedX_prop       = root.child(2).child(0).child(0)
        self._conf_seedY_prop       = root.child(2).child(0).child(1)
        self._conf_seedZ_prop       = root.child(2).child(0).child(2)
        self._conf_radius_prop      = root.child(2).child(1)
        self._conf_mult_value_prop  = root.child(2).child(2)
        self._conf_repl_value_prop  = root.child(2).child(3)
        self._conf_iter_prop        = root.child(2).child(4)

        self._voting_prop       = root.child(3)
        self._radius_prop       = root.child(3).child(0)
        self._radiusX_prop      = root.child(3).child(0).child(0)
        self._radiusY_prop      = root.child(3).child(0).child(1)
        self._radiusZ_prop      = root.child(3).child(0).child(2)
        self._background_prop   = root.child(3).child(1)
        self._foreground_prop   = root.child(3).child(2)
        self._survival_prop     = root.child(3).child(3)
        self._birth_prop        = root.child(3).child(4)

        self._properties_tree.itemChanged.connect(self._update_filters)

    def update(self):
        self._update_editable_labels()
        self._update_filters_properties()

    def _update_editable_labels(self):
        """
        Actualiza las etiquetas de los campos editables en los árboles de propiedades para si
        se cambiaron por error
        """
        #restaurar las etiquetas de las propiedades de la imagen
        self._properties_tree.blockSignals(True) #bloquear momentáneamente las señales

        self._iterations_prop.setText(0,self._properties_tree.tr("Iteraciones"))
        self._time_step_prop.setText(0,self._properties_tree.tr("Paso de tiempo"))
        self._conductance_prop.setText(0,self._properties_tree.tr("Conductancia"))

        self._seedX_prop.setText(0,self._properties_tree.tr("X"))
        self._seedY_prop.setText(0,self._properties_tree.tr("Y"))
        self._seedZ_prop.setText(0,self._properties_tree.tr("Z"))
        self._min_threshold_prop.setText(0,self._properties_tree.tr("Mínimo"))
        self._max_threshold_prop.setText(0,self._properties_tree.tr("Máximo"))
        self._replace_value_prop.setText(0,self._properties_tree.tr("Relleno"))

        self._conf_seedX_prop.setText(0,self._properties_tree.tr("X"))
        self._conf_seedY_prop.setText(0,self._properties_tree.tr("Y"))
        self._conf_seedZ_prop.setText(0,self._properties_tree.tr("Z"))
        self._conf_radius_prop.setText(0,self._properties_tree.tr("Radio inicial"))
        self._conf_mult_value_prop.setText(0,self._properties_tree.tr("Multiplicador"))
        self._conf_repl_value_prop.setText(0,self._properties_tree.tr("Relleno"))
        self._conf_iter_prop.setText(0,self._properties_tree.tr("Iteraciones"))

        self._radiusX_prop.setText(0,self._properties_tree.tr("X"))
        self._radiusY_prop.setText(0,self._properties_tree.tr("Y"))
        self._radiusZ_prop.setText(0,self._properties_tree.tr("Z"))
        self._background_prop.setText(0,self._properties_tree.tr("Fondo"))
        self._foreground_prop.setText(0,self._properties_tree.tr("Máscara"))
        self._survival_prop.setText(0,self._properties_tree.tr("Supervivencia"))
        self._birth_prop.setText(0,self._properties_tree.tr("Nacimiento"))

        self._properties_tree.blockSignals(False) #desbloquear las señales

    def _update_filters_properties(self):
        """
        Actualiza las propiedades que se muestran de los filtros
        """
        self._properties_tree.blockSignals(True)

        smooth = Application.get_current_document()._smooth_pipe
        self._iterations_prop.setText(1,str(smooth.NumberOfIterations))
        self._time_step_prop.setText(1,str(smooth.TimeStep))
        self._conductance_prop.setText(1,str(smooth.Conductance))
        self._smoother_prop.setText(1,str([smooth.NumberOfIterations,smooth.TimeStep,
                                           smooth.Conductance]))
        state = Qt.Unchecked
        if Application.get_current_document().usingSmoother():
            state = Qt.Checked
        self._smoother_prop.setCheckState(0,state)

        segment = Application.get_current_document()._segment_pipe
        self._seed_prop.setText(1,str(segment.Seed))
        self._seedX_prop.setText(1,str(segment.Seed[0]))
        self._seedY_prop.setText(1,str(segment.Seed[1]))
        self._seedZ_prop.setText(1,str(segment.Seed[2]))
        self._min_threshold_prop.setText(1,str(segment.LowerThreshold))
        self._max_threshold_prop.setText(1,str(segment.UpperThreshold))
        self._replace_value_prop.setText(1,str(segment.ReplaceValue))
        state = Qt.Unchecked
        if Application.get_current_document().usingSegmentor():
            state = Qt.Checked
        self._segment_prop.setCheckState(0,state)


        confidence = Application.get_current_document()._confidence_connected_pipe
        self._conf_seed_prop.setText(1,str(confidence.Seed))
        self._conf_seedX_prop.setText(1,str(confidence.Seed[0]))
        self._conf_seedY_prop.setText(1,str(confidence.Seed[1]))
        self._conf_seedZ_prop.setText(1,str(confidence.Seed[2]))
        self._conf_radius_prop.setText(1,str(confidence.InitialRadius))
        self._conf_mult_value_prop.setText(1,str(confidence.Multiplier))
        self._conf_repl_value_prop.setText(1,str(confidence.ReplaceValue))
        self._conf_iter_prop.setText(1,str(confidence.NumberOfIterations))
        state = Qt.Unchecked
        if Application.get_current_document().usingConfidenceConnected():
            state = Qt.Checked
        self._confidence_prop.setCheckState(0,state)

        voting = Application.get_current_document()._voting_pipe
        self._radius_prop.setText(1,str(voting.Radius))
        self._radiusX_prop.setText(1,str(voting.Radius[0]))
        self._radiusY_prop.setText(1,str(voting.Radius[1]))
        self._radiusZ_prop.setText(1,str(voting.Radius[2]))
        self._foreground_prop.setText(1,str(voting.Foreground))
        self._background_prop.setText(1,str(voting.Background))
        self._survival_prop.setText(1,str(voting.SurvivalValue))
        self._birth_prop.setText(1,str(voting.BirthValue))
        state = Qt.Unchecked
        if Application.get_current_document().usingVoter():
            state = Qt.Checked
        self._voting_prop.setCheckState(0,state)

        self._properties_tree.blockSignals(False)

    def _update_filters(self,item,col):
        """
        Actualiza las propiedades de los filtros luego de editarlas
        @param item: item que se editó
        @param col: columna del item que se editó
        @return: None
        """
        #cambiaron la etiqueta de la propiedad no el valor
        if col == 0:
            self._update_editable_labels()
            if item.text(0) == "Suavizador":
                Application.get_current_document().useSmoother(item.checkState(0) == Qt.Checked)
            elif item.text(0) == "Segmentador":
                Application.get_current_document().useSegmentor(item.checkState(0) == Qt.Checked)
            elif item.text(0) == "Segmentador estadístico":
                Application.get_current_document().useConfidenceConnected(item.checkState(0) == Qt.Checked)
            elif item.text(0) == "Votación":
                Application.get_current_document().useVoter(item.checkState(0) == Qt.Checked)
            return
        if item.text(0) == "Iteraciones" and item.parent().text(0) == "Suavizador":
            try:
                num = int(item.text(1))
                if num<0 or num>20:
                    raise ValueError()
                Application.get_current_document()._smooth_pipe.NumberOfIterations = num
            except ValueError:
                pass
        elif item.text(0) == "Iteraciones" and item.parent().text(0) == "Segmentador estadístico":
            try:
                num = int(item.text(1))
                if num<0 or num>50:
                    raise ValueError()
                Application.get_current_document()._confidence_connected_pipe.NumberOfIterations = num
            except ValueError:
                pass
        elif item.text(0) == "Paso de tiempo":
            try:
                num = float(item.text(1))
                if num<0.0 or num>1.0: #límites del paso de tiempo
                    raise ValueError()
                Application.get_current_document()._smooth_pipe.TimeStep = num
            except ValueError:
                pass
        elif item.text(0) == "Conductancia":
            try:
                num = float(item.text(1))
                if num<0.0 or num>100.0: #límites rasonables de conductancia
                    raise ValueError()
                Application.get_current_document()._smooth_pipe.Conductance = num
            except ValueError:
                pass
        elif item.parent().text(0) == "Semilla" and item.parent().parent().text(0) == "Segmentador":
            #los hijos de 'Semilla' son las coordenadas
            seed = [ self._seedX_prop.text(1),
                     self._seedY_prop.text(1),
                     self._seedZ_prop.text(1) ]
            try:
                seed = map(int,seed)
                #verificar que no se incluya como semilla un valor mayor que el tamaño de la imagen o
                #menor que cero
                if any(map(lambda x: x<0,seed)) or\
                   any(imap(lambda x,y: x>=y,seed,Application.get_current_image().Size)):
                    raise ValueError()
                Application.get_current_document()._segment_pipe.Seed = seed
            except ValueError:
                pass
        elif item.parent().text(0) == "Semilla" and item.parent().parent().text(0) == "Segmentador estadístico":
            #los hijos de 'Semilla' son las coordenadas
            seed = [ self._conf_seedX_prop.text(1),
                     self._conf_seedY_prop.text(1),
                     self._conf_seedZ_prop.text(1) ]
            try:
                seed = map(int,seed)
                #verificar que no se incluya como semilla un valor mayor que el tamaño de la imagen o
                #menor que cero
                if any(map(lambda x: x<0,seed)) or\
                   any(imap(lambda x,y: x>=y,seed,Application.get_current_image().Size)):
                    raise ValueError()
                Application.get_current_document()._confidence_connected_pipe.Seed = seed
            except ValueError:
                pass
        elif item.text(0) == "Mínimo":
            try:
                min = float(self._min_threshold_prop.text(1))
                Application.get_current_document()._segment_pipe.LowerThreshold = min
            except ValueError:
                pass
        elif item.text(0) == "Máximo":
            try:
                max = float(self._max_threshold_prop.text(1))
                Application.get_current_document()._segment_pipe.UpperThreshold = max
            except ValueError:
                pass
        elif item.text(0) == "Relleno" and item.parent().parent().text(0) == "Segmentador":
            try:
                val = float(self._replace_value_prop.text(1))
                Application.get_current_document()._segment_pipe.ReplaceValue = val
            except ValueError:
                pass
        elif item.text(0) == "Relleno" and item.parent().parent().text(0) == "Segmentador estadístico":
            try:
                val = float(self._conf_repl_value_prop.text(1))
                Application.get_current_document()._confidence_connected_pipe.ReplaceValue = val
            except ValueError:
                pass
        elif item.parent().text(0) == "Radio":
            radius = [  self._radiusX_prop.text(1),
                        self._radiusY_prop.text(1),
                        self._radiusZ_prop.text(1) ]
            try:
                radius = map(str,radius)
                radius = map(int,radius)
                #verificar que no se incluya como radio un valor sensato (por ahora entre 0 y 20)
                if any(map(lambda x: x<0 or x>20,radius)):
                    raise ValueError()
                Application.get_current_document()._voting_pipe.Radius = radius
            except ValueError:
                pass
        elif item.text(0) == "Radio inicial":
            try:
                val = int(self._conf_radius_prop.text(1))
                if val<0 or val>20:
                    raise ValueError()
                Application.get_current_document()._confidence_connected_pipe.InitialRadius = val
            except ValueError:
                pass
        elif item.text(0) == "Multiplicador":
            try:
                val = float(self._conf_mult_value_prop.text(1))
                if val<0:
                    raise ValueError()
                Application.get_current_document()._confidence_connected_pipe.Multiplier = val
            except ValueError:
                pass
        elif item.text(0) == "Fondo":
            try:
                val = int(self._background_prop.text(1))
                if val<0 or val>255:
                    raise ValueError()
                Application.get_current_document()._voting_pipe.Background = val
            except ValueError:
                pass
        elif item.text(0) == "Máscara":
            try:
                val = int(self._foreground_prop.text(1))
                if val<0:
                    raise ValueError()
                Application.get_current_document()._voting_pipe.Foreground = val
            except ValueError:
                pass
        elif item.text(0) == "Supervivencia":
            try:
                val = int(self._survival_prop.text(1))
                if val<0:
                    raise ValueError()
                Application.get_current_document()._voting_pipe.SurvivalValue = val
            except ValueError:
                pass
        elif item.text(0) == "Nacimiento":
            try:
                val = int(self._birth_prop.text(1))
                if val<0:
                    raise ValueError()
                Application.get_current_document()._voting_pipe.BirthValue = val
            except ValueError:
                pass

        self._update_filters_properties()