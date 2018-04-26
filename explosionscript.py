import arcpy
import sys
import traceback

bomb = arcpy.GetParameterAsText(0)

distance = arcpy.GetParameterAsText(1)

buildings = arcpy.GetParameterAsText(2)

int = arcpy.GetParameterAsText(3)
if int == '#' or not int:
    int = "\\\\ds.leeds.ac.uk\\student\\student13\\gy17cev\\ArcGIS\\Default.gdb\\Intersect" # provide a default value if unspecified

buff = arcpy.GetParameterAsText(4)

try:
    try:
        arcpy.ImportToolbox("M:/Programming/practical1/albertsurface/Models.tbx", "models")
    except arcpy.ExecuteError as e:
        print("Import toolbox error", e)
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        print(tbinfo)
        arcpy.AddError(tbinfo)
        
    if arcpy.Exists("int.shp"):
        arcpy.Delete_management("int.shp")
    if arcpy.Exists("buff.shp"):
        arcpy.Delete_management("buff.shp")
        
    try:
        arcpy.Explosion_models(bomb,distance,buildings,int,buff)
    except arcpy.ExecuteError as e:
        print("Model run error", e)
        tb2 = sys.exc_info()[2]
        tb2info = traceback.format_tb(tb2)[0]
        print(tb2info)
        arcpy.AddError(tb2info)
        
except Exception as e:
    print(e)
    tb3 = sys.exc_info()[2]
    tb3info = traceback.format_tb(tb3)[0]
    print(tb3info)
    arcpy.AddError(tb3info)


