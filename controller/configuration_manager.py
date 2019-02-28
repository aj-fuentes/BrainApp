#! -*- coding: cp1252 -*-
from PyQt4.QtGui import QFileDialog
from model.application import Application
__author__ = 'Alvaro Javier'

class ConfigurationManager(object):
    
    @classmethod
    def init(cls):
        cls._file_save_dialog = QFileDialog()
        #configuración del fileDialog de Qt
        cls._file_save_dialog.setAcceptMode(QFileDialog.AcceptSave) #Sólo se acepta salvar fichero
        cls._file_save_dialog.setViewMode(QFileDialog.Detail) #La vista se muestra en detalles

        cls._file_load_dialog = QFileDialog()
        #configuración del fileDialog de Qt
        cls._file_load_dialog.setAcceptMode(QFileDialog.AcceptOpen) #Sólo se acepta abrir fichero
        cls._file_load_dialog.setViewMode(QFileDialog.Detail) #La vista se muestra en detalles

    def save_configuration(self):
        res = self._file_save_dialog.exec_() #ejecutar el diálogo para obtener el nombre del fichero
        if res == QFileDialog.Rejected: #se canceló la salva
            return
        file_name = unicode(self._file_save_dialog.selectedFiles()[0]) #obtener el nombre del fichero
        doc =  Application.get_current_document() #referencia al docmento actual de la aplicación
        f = open(file_name,"wt")
        try:
            smoother = doc._smooth_pipe
            f.write(str(doc.usingSmoother())+"\n")
            f.write(str(smoother.NumberOfIterations)+"\n")
            f.write(str(smoother.TimeStep)+"\n")
            f.write(str(smoother.Conductance)+"\n")

            segmentor = doc._segment_pipe
            f.write(str(doc.usingSegmentor())+"\n")
            f.write(str(segmentor.Seed)+"\n")
            f.write(str(segmentor.LowerThreshold)+"\n")
            f.write(str(segmentor.UpperThreshold)+"\n")
            f.write(str(segmentor.ReplaceValue)+"\n")

            conf_conn = doc._confidence_connected_pipe
            f.write(str(doc.usingConfidenceConnected())+"\n")
            f.write(str(conf_conn.Seed)+"\n")
            f.write(str(conf_conn.InitialRadius)+"\n")
            f.write(str(conf_conn.Multiplier)+"\n")
            f.write(str(conf_conn.ReplaceValue)+"\n")
            f.write(str(conf_conn.NumberOfIterations)+"\n")

            voter = doc._voting_pipe
            f.write(str(doc.usingVoter())+"\n")
            f.write(str(voter.Radius)+"\n")
            f.write(str(voter.Background)+"\n")
            f.write(str(voter.Foreground)+"\n")
            f.write(str(voter.SurvivalValue)+"\n")
            f.write(str(voter.BirthValue)+"\n")
        finally:
            f.close()

    def _read_int(self,f):
        return int(f.readline().replace("\n",""))

    def _read_float(self,f):
        return float(f.readline().replace("\n",""))

    def _read_bool(self,f):
        return (f.readline().replace("\n","")=="True")

    def _read_int_list(self,f):
        return map(int,f.readline().replace("\n","").replace("]","").replace("[","").split(", "))

    def load_configuration(self):
        res = self._file_load_dialog.exec_() #ejecutar el diálogo para obtener el nombre del fichero
        if res == QFileDialog.Rejected: #se canceló la salva
            return
        file_name = unicode(self._file_load_dialog.selectedFiles()[0]) #obtener el nombre del fichero
        doc =  Application.get_current_document() #referencia al docmento actual de la aplicación
        f = open(file_name,"rt")
        try:
            smoother = doc._smooth_pipe
            doc.useSmoother(self._read_bool(f))
            smoother.NumberOfIterations = self._read_int(f)
            smoother.TimeStep = self._read_float(f)
            smoother.Conductance = self._read_float(f)

            segmentor = doc._segment_pipe
            doc.useSegmentor(self._read_bool(f))
            segmentor.Seed = self._read_int_list(f)
            segmentor.LowerThreshold = self._read_float(f)
            segmentor.UpperThreshold = self._read_float(f)
            segmentor.ReplaceValue = self._read_float(f)

            conf_conn = doc._confidence_connected_pipe
            doc.useConfidenceConnected(self._read_bool(f))
            conf_conn.Seed = self._read_int_list(f)
            conf_conn.InitialRadius = self._read_int(f)
            conf_conn.Multiplier = self._read_float(f)
            conf_conn.ReplaceValue = self._read_float(f)
            conf_conn.NumberOfIterations = self._read_int(f)

            voter = doc._voting_pipe
            doc.useVoter(self._read_bool(f))
            voter.Radius = self._read_int_list(f)
            voter.Background = self._read_float(f)
            voter.Foreground = self._read_float(f)
            voter.SurvivalValue = self._read_int(f)
            voter.BirthValue = self._read_int(f)
        finally:
            f.close()