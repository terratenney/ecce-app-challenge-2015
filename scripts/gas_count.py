# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# gas_count.py
# Created on: 2015-03-02 23:11:56.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
ed_landus_cent = "ed_landus_cent"
sample_shape3_shp = "C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp"
ed_gasstation_shp = "C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\ed_gasstation.shp"
count = "C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\ed_gasstation.shp"
sample_shape4_shp = "C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape4.shp"

# Process: Select
arcpy.Select_analysis(ed_landus_cent, ed_gasstation_shp, "\"CODE\" = 2046 OR \"CODE\" = 2048")

# Process: Add Field
arcpy.AddField_management(ed_gasstation_shp, "gascount", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Spatial Join
arcpy.SpatialJoin_analysis(sample_shape3_shp, count, sample_shape4_shp, "JOIN_ONE_TO_ONE", "KEEP_ALL", "Join_Count \"Join_Count\" true true false 9 Long 0 9 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,Join_Count,-1,-1;TARGET_FID \"TARGET_FID\" true true false 9 Long 0 9 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,TARGET_FID,-1,-1;Join_Cou_1 \"Join_Cou_1\" true true false 9 Long 0 9 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,Join_Cou_1,-1,-1;TARGET_F_1 \"TARGET_F_1\" true true false 9 Long 0 9 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,TARGET_F_1,-1,-1;DAUID \"DAUID\" true true false 8 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,DAUID,-1,-1;CDUID \"CDUID\" true true false 4 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CDUID,-1,-1;CDNAME \"CDNAME\" true true false 40 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CDNAME,-1,-1;CDTYPE \"CDTYPE\" true true false 3 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CDTYPE,-1,-1;CSDUID \"CSDUID\" true true false 7 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CSDUID,-1,-1;CSDNAME \"CSDNAME\" true true false 55 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CSDNAME,-1,-1;CSDTYPE \"CSDTYPE\" true true false 3 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CSDTYPE,-1,-1;CCSUID \"CCSUID\" true true false 7 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CCSUID,-1,-1;CCSNAME \"CCSNAME\" true true false 55 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CCSNAME,-1,-1;ERUID \"ERUID\" true true false 4 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,ERUID,-1,-1;ERNAME \"ERNAME\" true true false 85 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,ERNAME,-1,-1;CMAPUID \"CMAPUID\" true true false 5 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CMAPUID,-1,-1;CMAUID \"CMAUID\" true true false 3 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CMAUID,-1,-1;CMANAME \"CMANAME\" true true false 100 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CMANAME,-1,-1;CMATYPE \"CMATYPE\" true true false 1 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CMATYPE,-1,-1;SACCODE \"SACCODE\" true true false 3 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,SACCODE,-1,-1;SACTYPE \"SACTYPE\" true true false 1 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,SACTYPE,-1,-1;CTUID \"CTUID\" true true false 10 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CTUID,-1,-1;CTNAME \"CTNAME\" true true false 7 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,CTNAME,-1,-1;PRUID \"PRUID\" true true false 2 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,PRUID,-1,-1;PRNAME \"PRNAME\" true true false 55 Text 0 0 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,PRNAME,-1,-1;UID \"UID\" true true false 4 Short 0 4 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,UID,-1,-1;reccount \"reccount\" true true false 4 Short 0 4 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,reccount,-1,-1;culcount \"culcount\" true true false 4 Short 0 4 ,First,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\sample_shape3.shp,culcount,-1,-1;gascount \"gascount\" true true false 0 Short 0 0 ,Count,#,C:\\Users\\carl\\Desktop\\webapp\\edmonton_features\\ed_gasstation.shp,gascount,-1,-1", "INTERSECT", "", "")

