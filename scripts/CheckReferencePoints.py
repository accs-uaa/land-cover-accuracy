# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Check Reference Points
# Author: Timm Nawrocki, Alaska Center for Conservation Science
# Created on: 2016-11-12
# Usage: Must be executed as an ArcPy Script.
# Description: This tool creates a csv file comparing a reference field in a point feature class to a field in a raster dataset for the purpose of assessing raster attribute accuracy.
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy, os, numpy, pandas, xlsxwriter
from arcpy.sa import *

# Set overwrite option
arcpy.env.overwriteOutput = True

# Define reference point feature class
Reference_Points = arcpy.GetParameterAsText(0)

# Define target field from reference points
ReferenceField = arcpy.GetParameterAsText(1)

# Define input raster
Input_Raster = arcpy.GetParameterAsText(2)

# Define target field from raster
RasterField = arcpy.GetParameterAsText(3)

# Define location of a workspace folder
Workspace = arcpy.GetParameterAsText(4)

# Define output csv
Pivot_Table = arcpy.GetParameterAsText(5)

# Define intermediate files for user selected workspace
Reference_Points_Extract = os.path.join(Workspace, "Reference_Points_Extract.shp")
Reference_CSV = os.path.join(Workspace, "Reference.csv")

# Extract values from raster to points
ExtractValuesToPoints(Reference_Points, Input_Raster, Reference_Points_Extract, "NONE", "ALL")

# Add quotes to reference field
ReferenceExpression = "AddQuotes(!" + ReferenceField + "!)"
codeBlock = "def AddQuotes(Field):\\n    QuoteBlock = \"\\\"\" + Field + \"\\\"\"\\n    return QuoteBlock"
arcpy.CalculateField_management(Reference_Points_Extract, ReferenceField, ReferenceExpression, "PYTHON", codeBlock)

# Add quotes to raster field
RasterExpression = "AddQuotes(!" + RasterField + "!)"
arcpy.CalculateField_management(Reference_Points_Extract, RasterField, RasterExpression, "PYTHON", codeBlock)

# Add and calculate a value field
ValueField = "Count"
ValueExpression = 1
arcpy.AddField_management(Reference_Points_Extract, ValueField, "Long")
arcpy.CalculateField_management(Reference_Points_Extract, ValueField, ValueExpression, "PYTHON")

# Export raster field and reference field to csv
Value_Field = "\"" + ReferenceField + ";" + RasterField + ";" + ValueField + "\""
arcpy.ExportXYv_stats(Reference_Points_Extract, Value_Field, "COMMA", Reference_CSV, "ADD_FIELD_NAMES")

# Read output CSV into data frame
dataFrame = pandas.read_csv(Reference_CSV)
dataFrame.head()

# Generate pivot table from data frame
pivotTable = pandas.pivot_table(dataFrame, index=RasterField.upper(), columns=[ReferenceField.upper()], values=ValueField.upper(), aggfunc=numpy.sum, fill_value="")

# Generate an excel file to store pivot table
writer = pandas.ExcelWriter(Pivot_Table, engine='xlsxwriter')
pivotTable.to_excel(writer, sheet_name='ReferenceData')
writer.save()

# Delete intermediate data
arcpy.Delete_management(Reference_Points_Extract)
os.remove(Reference_CSV)
XML = os.path.join(Workspace, "Reference.txt.xml")
if os.path.exists(XML) == True:
    os.remove(XML)