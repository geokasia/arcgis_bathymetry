# -*- coding: utf-8 -*-
"""
Copyright Katarzyna Krzyzanowska

@author: Katarzyna Krzyzanowska
@email: katarzyna.krzyzanowska@ug.edu.pl

@brief Tool for automatic bathymetric maps generation
"""

import arcpy
from arcpy import env
from arcpy.sa import *

try:
    #Params
    depth = arcpy.GetParameter(0)
    coast_line = arcpy.GetParameter(1)
    contour_interval = arcpy.GetParameter(2)
    result_path = arcpy.GetParameter(3)
    workspace_path = arcpy.GetParameter(4)
    output_name = arcpy.GetParameter(5)
    arcpy.AddMessage('Params OK')
    
except:
    #Exception handler
    arcpy.AddError('Param import fail')
    arcpy.AddMessage(arcpy.GetMessages())


try:    
    env.workspace = workspace_path
    arcpy.env.overwriteOutput=True
    
except:
    #Exception handler
    arcpy.AddError('Workspace gdb fail')
    arcpy.AddMessage(arcpy.GetMessages())
    
    
try:
    #TTR Tool
    outTTR = TopoToRaster([TopoPointElevation([[depth, 'h_m']])], 2, 
                       "#", "#", "#", "#", "NO_ENFORCE")
    #arcpy.AddMessage(result_path + r'\ttr')
    outTTR.save(result_path + r'\ttr')
    arcpy.AddMessage('TTR OK')
    
except:
    #Exception handler
    arcpy.AddError('TTR Fail')
    arcpy.AddMessage(arcpy.GetMessages())


try:
    #TTR Tool
    outFTP = arcpy.FeatureToPolygon_management(coast_line,
                                      result_path + r'\ftp',
                                      "", "NO_ATTRIBUTES", "")
    arcpy.AddMessage('FTP OK')
    
except:
    #Exception handler
    arcpy.AddError('FTP Fail')
    arcpy.AddMessage(arcpy.GetMessages())
    

try:
    #EBM Tool
    outExtractByMask = ExtractByMask(outTTR, outFTP)
    outExtractByMask.save(result_path + r'\ebm')
    arcpy.AddMessage('EBM OK')
    
except:
    #Exception handler
    arcpy.AddError('EBM Fail')
    arcpy.AddMessage(arcpy.GetMessages())


try:
    #CCR Tool
    CCR = Contour(outExtractByMask, result_path + r'\ccr', contour_interval, 0)
    arcpy.AddMessage('CCR OK')
    
except:
    #Exception handler
    arcpy.AddError('CCR Fail')
    arcpy.AddMessage(arcpy.GetMessages())


try:
    #MRQ Tool 
    MRQ = arcpy.Merge_management([CCR, coast_line], result_path + r'\\' + output_name)
    arcpy.AddMessage('MRQ OK')
    
except:
    #Exception handler
    arcpy.AddError('MRQ Fail')
    arcpy.AddMessage(arcpy.GetMessages())
