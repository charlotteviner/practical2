import arcpy

arcpy.env.workspace = "M:/Programming/Practical1/Albertsurface"

try:
    try:
        arcpy.ImportToolbox("M:/Programming/practical1/albertsurface/Models.tbx", "models")
    except arcpy.ExecuteError as e:
	    print("Import toolbox error", e)
    if arcpy.Exists("int.shp"):
        arcpy.Delete_management("int.shp")
    if arcpy.Exists("buff.shp"):
        arcpy.Delete_management("buff.shp")
    try:
        arcpy.Explosion_models("explosion0/point","100 Meters","build0/polygon","int.shp","buff.shp")
    except arcpy.ExecuteError as e:
	    print("Model run error", e)
except Exception as e:
    print(e)

