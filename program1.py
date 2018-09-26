# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 17:52:49 2018

@author: Katarzyna Krzyzanowska
"""

#Skypt do buforowania

import arcpy
from arcpy import env

arcpy.env.overwriteOutput=True

env.workspace=r"C:\Users\Win7\Documents\Analityk_GIS_STUDIA\HEL_2018\warsztaty_A\warsztaty_A.gdb"


try:
        #Parametry
        #inwarstwa=arcpy.getParameterAsText(0)
        #outwarstwa=arcpy.GetParameterAsText(1)
        #dystans=arcpy.GetParameter(2)
        inwarstwa="jezioro11"
        outwarstwa="bufjezioro"
        dystans=8000
        #Narzędzie Bufor
        arcpy.Buffer_analysis(inwarstwa,outwarstwa,dystans,"","","ALL")
        #wykonanie OK
        #arcpy.AddMessage('Wszystko OK :)')
except:
        #raport problemu
        arcpy.AddError("Kiepsko:(")
        #raport błędów z narzędzi obecnych w skrypcie
        arcpy.AddMessage(arcpy.GetMessages())