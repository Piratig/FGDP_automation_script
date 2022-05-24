#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import re
#pip install nums_from_string
#import nums_from_string


# In[2]:


pd.set_option('max_colwidth', 200)
pd.set_option('display.width', 500)


# In[3]:


listStations = []
listMainSP = []
listStationPath = []
listStationRout = []
listStationRout_from = []
listStationRout_to = []
listTurnoverPath = []
listRailwayStage = []
list_links_msp = []
list_links_sp = []
list_links_routes = []
list_links_routes_id = ' '
list_from_RailwayStage = []
list_to_RailwayStage = []
listLineRegion = []
list_depot = []
list_connectionBranch = []
list_pathWay = []
list_stageModeFirst = []
list_stageMode = []
list_stopMode = []
list_drivingMode = []
list_lineDrivingMode = []
link_line_regions = []
link_line_depot = []
link_lineRegion_stations = []
link_lineRegion_drivingModes = []
link_msp_turnovers = []
link_drivingMode_stages = []
link_drivingMode_stops = []
link_stageMode_stage = []
link_stageModeFirst_stage = []
link_stopMode_station = []
link_connectionBranch_from = []
link_connectionBranch_to = []
link_pathWay_start = []
link_pathWay_ways = []
objekt_drivingMode_link = []

listObjects = []
listLinks = []

stations = []


# In[4]:


def create_Modes(line_ID):
    df = pd.DataFrame(stations)
    global str_link_lineDrivingMode
    str_link_1drivingMode_first = ''
    str_link_2drivingMode_first = ''
    str_link_1drivingMode_00 = ''
    str_link_2drivingMode_00 = ''
    str_link_1drivingMode_01 = ''
    str_link_2drivingMode_01 = ''
    str_link_1drivingMode_02 = ''
    str_link_2drivingMode_02 = ''
    str_link_1stopMode_first = ''
    str_link_2stopMode_first = ''
    str_link_1stopMode_00 = ''
    str_link_2stopMode_00 = ''
    str_link_1stopMode_01 = ''
    str_link_2stopMode_01 = ''
    str_link_1stopMode_02 = ''
    str_link_2stopMode_02 = ''
    global str_link_ldm_path1
    global str_link_ldm_path2
    
    for x in df[0]:
        if x < df[0][df.shape[0]-1]:
            # StageModeFirst
            list_stageModeFirst.append('    {metro.StageModeFirst[stageModeFirst_' + df.loc[x-1][2] 
                                    + '_' + df.loc[x][2] + '],{ts.Name="' + df.loc[x-1][1] 
                                    + ' - ' + df.loc[x][1] + ' 1 поезд"}}')
            list_stageModeFirst.append('    {metro.StageModeFirst[stageModeFirst_' + df.loc[x][2] 
                                    + '_' + df.loc[x-1][2] + '],{ts.Name="' + df.loc[x][1] 
                                    + ' - ' + df.loc[x-1][1] + ' 1 поезд"}}')
            
            if x != 1:
                str_link_1drivingMode_first += ','
                str_link_2drivingMode_first += ','
            str_link_1drivingMode_first += 'metro.StageModeFirst[stageModeFirst_' + df.loc[x-1][2] + '_' + df.loc[x][2] + ']'
            str_link_2drivingMode_first += 'metro.StageModeFirst[stageModeFirst_' + df.loc[x][2] + '_' + df.loc[x-1][2] + ']'
            
            link_stageModeFirst_stage.append('      {metro.StageModeFirst,stage,metro.StageModeFirst[stageModeFirst_' + df.loc[x-1][2] + '_' + df.loc[x][2] + '],[metro.RailwayStage[railwayStage_1_' + df.loc[x-1][2] + '_' + df.loc[x][2] + ']]}')
            link_stageModeFirst_stage.append('      {metro.StageModeFirst,stage,metro.StageModeFirst[stageModeFirst_' + df.loc[x][2] + '_' + df.loc[x-1][2] + '],[metro.RailwayStage[railwayStage_2_' + df.loc[x][2] + '_' + df.loc[x-1][2] + ']]}')
            
            # StageMode
            list_stageMode.append('    {metro.StageMode[stageMode_00_' + df.loc[x-1][2] 
                                    + '_' + df.loc[x][2] + '],{ts.Name="' + df.loc[x-1][1] 
                                    + ' - ' + df.loc[x][1] + ' резерв"}}')
            list_stageMode.append('    {metro.StageMode[stageMode_00_' + df.loc[x][2] 
                                    + '_' + df.loc[x-1][2] + '],{ts.Name="' + df.loc[x][1] 
                                    + ' - ' + df.loc[x-1][1] + ' резерв"}}')
            list_stageMode.append('    {metro.StageMode[stageMode_01_' + df.loc[x-1][2] 
                                    + '_' + df.loc[x][2] + '],{ts.Name="' + df.loc[x-1][1] 
                                    + ' - ' + df.loc[x][1] + ' пик"}}')
            list_stageMode.append('    {metro.StageMode[stageMode_01_' + df.loc[x][2] 
                                    + '_' + df.loc[x-1][2] + '],{ts.Name="' + df.loc[x][1] 
                                    + ' - ' + df.loc[x-1][1] + ' пик"}}')
            list_stageMode.append('    {metro.StageMode[stageMode_02_' + df.loc[x-1][2] 
                                    + '_' + df.loc[x][2] + '],{ts.Name="' + df.loc[x-1][1] 
                                    + ' - ' + df.loc[x][1] + ' не пик"}}')
            list_stageMode.append('    {metro.StageMode[stageMode_02_' + df.loc[x][2] 
                                    + '_' + df.loc[x-1][2] + '],{ts.Name="' + df.loc[x][1] 
                                    + ' - ' + df.loc[x-1][1] + ' не пик"}}')
            
            if x != 1:
                str_link_1drivingMode_00 += ','
                str_link_2drivingMode_00 += ','
                str_link_1drivingMode_01 += ','
                str_link_2drivingMode_01 += ','
                str_link_1drivingMode_02 += ','
                str_link_2drivingMode_02 += ','
            str_link_1drivingMode_00 += 'metro.StageMode[stageMode_00_' + df.loc[x-1][2] + '_' + df.loc[x][2] + ']'
            str_link_2drivingMode_00 += 'metro.StageMode[stageMode_00_' + df.loc[x][2] + '_' + df.loc[x-1][2] + ']'
            str_link_1drivingMode_01 += 'metro.StageMode[stageMode_01_' + df.loc[x-1][2] + '_' + df.loc[x][2] + ']'
            str_link_2drivingMode_01 += 'metro.StageMode[stageMode_01_' + df.loc[x][2] + '_' + df.loc[x-1][2] + ']'
            str_link_1drivingMode_02 += 'metro.StageMode[stageMode_02_' + df.loc[x-1][2] + '_' + df.loc[x][2] + ']'
            str_link_2drivingMode_02 += 'metro.StageMode[stageMode_02_' + df.loc[x][2] + '_' + df.loc[x-1][2] + ']'
            
            link_stageMode_stage.append('      {metro.StageMode,stage,metro.StageMode[stageMode_00_' + df.loc[x-1][2] + '_' + df.loc[x][2] + '],[metro.RailwayStage[railwayStage_1_' + df.loc[x-1][2] + '_' + df.loc[x][2] + ']]}')
            link_stageMode_stage.append('      {metro.StageMode,stage,metro.StageMode[stageMode_00_' + df.loc[x][2] + '_' + df.loc[x-1][2] + '],[metro.RailwayStage[railwayStage_2_' + df.loc[x][2] + '_' + df.loc[x-1][2] + ']]}')
            link_stageMode_stage.append('      {metro.StageMode,stage,metro.StageMode[stageMode_01_' + df.loc[x-1][2] + '_' + df.loc[x][2] + '],[metro.RailwayStage[railwayStage_1_' + df.loc[x-1][2] + '_' + df.loc[x][2] + ']]}')
            link_stageMode_stage.append('      {metro.StageMode,stage,metro.StageMode[stageMode_01_' + df.loc[x][2] + '_' + df.loc[x-1][2] + '],[metro.RailwayStage[railwayStage_2_' + df.loc[x][2] + '_' + df.loc[x-1][2] + ']]}')
            link_stageMode_stage.append('      {metro.StageMode,stage,metro.StageMode[stageMode_02_' + df.loc[x-1][2] + '_' + df.loc[x][2] + '],[metro.RailwayStage[railwayStage_1_' + df.loc[x-1][2] + '_' + df.loc[x][2] + ']]}')
            link_stageMode_stage.append('      {metro.StageMode,stage,metro.StageMode[stageMode_02_' + df.loc[x][2] + '_' + df.loc[x-1][2] + '],[metro.RailwayStage[railwayStage_2_' + df.loc[x][2] + '_' + df.loc[x-1][2] + ']]}')
            
        # StopMode
        list_stopMode.append('    {metro.StopMode[stopMode_First_' + df.loc[x-1][2] 
                             + '_1],{ts.Name="1 гл. ст. путь ст. ' + df.loc[x-1][1] + ' 1 поезд"}}')
        list_stopMode.append('    {metro.StopMode[stopMode_First_' + df.loc[x-1][2] 
                             + '_2],{ts.Name="2 гл. ст. путь ст. ' + df.loc[x-1][1] + ' 1 поезд"}}')
        list_stopMode.append('    {metro.StopMode[stopMode_00_' + df.loc[x-1][2] 
                             + '_1],{ts.Name="1 гл. ст. путь ст. ' + df.loc[x-1][1] + ' резерв"}}')
        list_stopMode.append('    {metro.StopMode[stopMode_00_' + df.loc[x-1][2] 
                             + '_2],{ts.Name="2 гл. ст. путь ст. ' + df.loc[x-1][1] + ' резерв"}}')
        list_stopMode.append('    {metro.StopMode[stopMode_01_' + df.loc[x-1][2] 
                             + '_1],{ts.Name="1 гл. ст. путь ст. ' + df.loc[x-1][1] + ' пик"}}')
        list_stopMode.append('    {metro.StopMode[stopMode_01_' + df.loc[x-1][2] 
                             + '_2],{ts.Name="2 гл. ст. путь ст. ' + df.loc[x-1][1] + ' пик"}}')
        list_stopMode.append('    {metro.StopMode[stopMode_02_' + df.loc[x-1][2] 
                             + '_1],{ts.Name="1 гл. ст. путь ст. ' + df.loc[x-1][1] + ' не пик"}}')
        list_stopMode.append('    {metro.StopMode[stopMode_02_' + df.loc[x-1][2] 
                             + '_2],{ts.Name="2 гл. ст. путь ст. ' + df.loc[x-1][1] + ' не пик"}}')
        
        if x != 1:
            str_link_1stopMode_first += ','
            str_link_2stopMode_first += ','
            str_link_1stopMode_00 += ','
            str_link_2stopMode_00 += ','
            str_link_1stopMode_01 += ','
            str_link_2stopMode_01 += ','
            str_link_1stopMode_02 += ','
            str_link_2stopMode_02 += ','
        str_link_1stopMode_first += 'metro.StopMode[stopMode_First_' + df.loc[x-1][2] + '_1]'
        str_link_2stopMode_first += 'metro.StopMode[stopMode_First_' + df.loc[x-1][2] + '_2]'
        str_link_1stopMode_00 += 'metro.StopMode[stopMode_00_' + df.loc[x-1][2] + '_1]'
        str_link_2stopMode_00 += 'metro.StopMode[stopMode_00_' + df.loc[x-1][2] + '_2]'
        str_link_1stopMode_01 += 'metro.StopMode[stopMode_01_' + df.loc[x-1][2] + '_1]'
        str_link_2stopMode_01 += 'metro.StopMode[stopMode_01_' + df.loc[x-1][2] + '_2]'
        str_link_1stopMode_02 += 'metro.StopMode[stopMode_02_' + df.loc[x-1][2] + '_1]'
        str_link_2stopMode_02 += 'metro.StopMode[stopMode_02_' + df.loc[x-1][2] + '_2]'
        
        link_stopMode_station.append('      {metro.StopMode,station,metro.StopMode[stopMode_First_' + df.loc[x-1][2] + '_1],[metro.MainStationPath[mainStationPath_1_' + df.loc[x-1][2] + ']]}')
        link_stopMode_station.append('      {metro.StopMode,station,metro.StopMode[stopMode_First_' + df.loc[x-1][2] + '_2],[metro.MainStationPath[mainStationPath_2_' + df.loc[x-1][2] + ']]}')
        link_stopMode_station.append('      {metro.StopMode,station,metro.StopMode[stopMode_00_' + df.loc[x-1][2] + '_1],[metro.MainStationPath[mainStationPath_1_' + df.loc[x-1][2] + ']]}')
        link_stopMode_station.append('      {metro.StopMode,station,metro.StopMode[stopMode_00_' + df.loc[x-1][2] + '_2],[metro.MainStationPath[mainStationPath_2_' + df.loc[x-1][2] + ']]}')
        link_stopMode_station.append('      {metro.StopMode,station,metro.StopMode[stopMode_01_' + df.loc[x-1][2] + '_1],[metro.MainStationPath[mainStationPath_1_' + df.loc[x-1][2] + ']]}')
        link_stopMode_station.append('      {metro.StopMode,station,metro.StopMode[stopMode_01_' + df.loc[x-1][2] + '_2],[metro.MainStationPath[mainStationPath_2_' + df.loc[x-1][2] + ']]}')
        link_stopMode_station.append('      {metro.StopMode,station,metro.StopMode[stopMode_02_' + df.loc[x-1][2] + '_1],[metro.MainStationPath[mainStationPath_1_' + df.loc[x-1][2] + ']]}')
        link_stopMode_station.append('      {metro.StopMode,station,metro.StopMode[stopMode_02_' + df.loc[x-1][2] + '_2],[metro.MainStationPath[mainStationPath_2_' + df.loc[x-1][2] + ']]}')
        
    # DrivingMode
    list_drivingMode.append('    {metro.DrivingMode[drivingMode_1_' + line_ID 
                            + '_First],{ts.Name="1' + line_ID + ' первый",additional=false}}')
    list_drivingMode.append('    {metro.DrivingMode[drivingMode_2_' + line_ID 
                            + '_First],{ts.Name="2' + line_ID + ' первый",additional=false}}')
    list_drivingMode.append('    {metro.DrivingMode[drivingMode_1_' + line_ID 
                            + '_00],{ts.Name="1' + line_ID + ' резерв",additional=false}}')
    list_drivingMode.append('    {metro.DrivingMode[drivingMode_2_' + line_ID 
                            + '_00],{ts.Name="2' + line_ID + ' резерв",additional=false}}')
    list_drivingMode.append('    {metro.DrivingMode[drivingMode_1_' + line_ID 
                            + '_01],{ts.Name="1' + line_ID + ' пик",additional=false}}')
    list_drivingMode.append('    {metro.DrivingMode[drivingMode_2_' + line_ID 
                            + '_01],{ts.Name="2' + line_ID + ' пик",additional=false}}')
    list_drivingMode.append('    {metro.DrivingMode[drivingMode_1_' + line_ID 
                            + '_02],{ts.Name="1' + line_ID + ' не пик",additional=false}}')
    list_drivingMode.append('    {metro.DrivingMode[drivingMode_2_' + line_ID 
                            + '_02],{ts.Name="2' + line_ID + ' не пик",additional=false}}')
    
    objekt_drivingMode_link.append('    {sk.regref.comp.metro.RRI.FGDP.metro.DrivingMode[drivingMode_1_' + line_ID + '_First],{}}')
    objekt_drivingMode_link.append('    {sk.regref.comp.metro.RRI.FGDP.metro.DrivingMode[drivingMode_2_' + line_ID + '_First],{}}')
    objekt_drivingMode_link.append('    {sk.regref.comp.metro.RRI.FGDP.metro.DrivingMode[drivingMode_1_' + line_ID + '_00],{}}')
    objekt_drivingMode_link.append('    {sk.regref.comp.metro.RRI.FGDP.metro.DrivingMode[drivingMode_2_' + line_ID + '_00],{}}')
    objekt_drivingMode_link.append('    {sk.regref.comp.metro.RRI.FGDP.metro.DrivingMode[drivingMode_1_' + line_ID + '_01],{}}')
    objekt_drivingMode_link.append('    {sk.regref.comp.metro.RRI.FGDP.metro.DrivingMode[drivingMode_2_' + line_ID + '_01],{}}')
    objekt_drivingMode_link.append('    {sk.regref.comp.metro.RRI.FGDP.metro.DrivingMode[drivingMode_1_' + line_ID + '_02],{}}')
    objekt_drivingMode_link.append('    {sk.regref.comp.metro.RRI.FGDP.metro.DrivingMode[drivingMode_2_' + line_ID + '_02],{}}')

    # LineDrivingModes
    list_lineDrivingMode.append('    {metro.LineDrivingModes[lineDrivingModes_' + line_ID 
                                + '],{ts.Name="Режимы хода ' + line_ID + '"}}')
    str_link_lineDrivingMode = 'metro.LineDrivingModes[lineDrivingModes_' + line_ID + ']'
    
    # Links
    
    link_drivingMode_stages.append('      {metro.DrivingMode,stages,metro.DrivingMode[drivingMode_1_' + line_ID + '_First],[' + str_link_1drivingMode_first + ']}')
    link_drivingMode_stages.append('      {metro.DrivingMode,stages,metro.DrivingMode[drivingMode_2_' + line_ID + '_First],[' + str_link_2drivingMode_first + ']}')
    link_drivingMode_stages.append('      {metro.DrivingMode,stages,metro.DrivingMode[drivingMode_1_' + line_ID + '_00],[' + str_link_1drivingMode_00 + ']}')
    link_drivingMode_stages.append('      {metro.DrivingMode,stages,metro.DrivingMode[drivingMode_2_' + line_ID + '_00],[' + str_link_2drivingMode_00 + ']}')
    link_drivingMode_stages.append('      {metro.DrivingMode,stages,metro.DrivingMode[drivingMode_1_' + line_ID + '_01],[' + str_link_1drivingMode_01 + ']}')
    link_drivingMode_stages.append('      {metro.DrivingMode,stages,metro.DrivingMode[drivingMode_2_' + line_ID + '_01],[' + str_link_2drivingMode_01 + ']}')
    link_drivingMode_stages.append('      {metro.DrivingMode,stages,metro.DrivingMode[drivingMode_1_' + line_ID + '_02],[' + str_link_1drivingMode_02 + ']}')
    link_drivingMode_stages.append('      {metro.DrivingMode,stages,metro.DrivingMode[drivingMode_2_' + line_ID + '_02],[' + str_link_2drivingMode_02 + ']}')
    
    link_drivingMode_stops.append('      {metro.DrivingMode,stops,metro.DrivingMode[drivingMode_1_' + line_ID + '_First],[' + str_link_1stopMode_first + ']}')
    link_drivingMode_stops.append('      {metro.DrivingMode,stops,metro.DrivingMode[drivingMode_2_' + line_ID + '_First],[' + str_link_2stopMode_first + ']}')
    link_drivingMode_stops.append('      {metro.DrivingMode,stops,metro.DrivingMode[drivingMode_1_' + line_ID + '_00],[' + str_link_1stopMode_00 + ']}')
    link_drivingMode_stops.append('      {metro.DrivingMode,stops,metro.DrivingMode[drivingMode_2_' + line_ID + '_00],[' + str_link_2stopMode_00 + ']}')
    link_drivingMode_stops.append('      {metro.DrivingMode,stops,metro.DrivingMode[drivingMode_1_' + line_ID + '_01],[' + str_link_1stopMode_01 + ']}')
    link_drivingMode_stops.append('      {metro.DrivingMode,stops,metro.DrivingMode[drivingMode_2_' + line_ID + '_01],[' + str_link_2stopMode_01 + ']}')
    link_drivingMode_stops.append('      {metro.DrivingMode,stops,metro.DrivingMode[drivingMode_1_' + line_ID + '_02],[' + str_link_1stopMode_02 + ']}')
    link_drivingMode_stops.append('      {metro.DrivingMode,stops,metro.DrivingMode[drivingMode_2_' + line_ID + '_02],[' + str_link_2stopMode_02 + ']}')
    
    str_link_ldm_path1 = '      {metro.LineDrivingModes,path1,metro.LineDrivingModes[lineDrivingModes_' + line_ID + '],[metro.DrivingMode[drivingMode_1_' + line_ID + '_First],metro.DrivingMode[drivingMode_1_' + line_ID + '_00],metro.DrivingMode[drivingMode_1_' + line_ID + '_01],metro.DrivingMode[drivingMode_1_' + line_ID + '_02]]}'
    str_link_ldm_path2 = '      {metro.LineDrivingModes,path2,metro.LineDrivingModes[lineDrivingModes_' + line_ID + '],[metro.DrivingMode[drivingMode_2_' + line_ID + '_First],metro.DrivingMode[drivingMode_2_' + line_ID + '_00],metro.DrivingMode[drivingMode_2_' + line_ID + '_01],metro.DrivingMode[drivingMode_2_' + line_ID + '_02]]}'


# In[5]:


def create_Depot(depo_ID, depo_name, station_N, start_msp, depo_N):
    station_ID = stations[station_N-1][2]
    station_name = stations[station_N-1][1]
    global str_depot
    # Depot
    list_depot.append('    {metro.Depot[depot_' + depo_ID + '],{ts.Name="' + depo_name + '"}}')
    
    if depo_N == 1:
        str_depot = 'metro.Depot[depot_' + depo_ID + ']'
    else:
        str_depot += ',metro.Depot[depot_' + depo_ID + ']'
    
    if start_msp == 1:
        # ConnectionBranch
        list_connectionBranch.append('    {metro.ConnectionBranch[branch_' + station_ID + '_3sp_depot_' + depo_ID + '],{ts.Name="' + station_name + ' 3 - депо ' + depo_name + '"}}')
        list_connectionBranch.append('    {metro.ConnectionBranch[branch_depot_' + depo_ID + '_' + station_ID + '_4sp],{ts.Name="депо ' + depo_name + ' - ' + station_name + ' 4"}}')
        # Pathway
        list_pathWay.append('    {metro.Pathway[fromDepot_depot_' + depo_ID + '_' + station_ID + '_4sp_2msp],{ts.Name="депо ' + depo_name + ' - ' + station_name + ' 4 сп 2 гсп"}}')
        list_pathWay.append('    {metro.Pathway[toDepot_' + station_ID + '_1msp_3sp_depot_' + depo_ID + '],{ts.Name="' + station_name + ' 1 гсп 3 сп - депо ' + depo_name + '"}}')
        
        link_connectionBranch_from.append('      {metro.ConnectionBranch,from,metro.ConnectionBranch[branch_depot_' + depo_ID + '_' + station_ID + '_4sp],[metro.Depot[depot_' + depo_ID + ']]}')
        link_connectionBranch_from.append('      {metro.ConnectionBranch,from,metro.ConnectionBranch[branch_' + station_ID + '_3sp_depot_' + depo_ID + '],[metro.StationPath[stationPath_3_' + station_ID + ']]}')
        
        link_connectionBranch_to.append('      {metro.ConnectionBranch,to,metro.ConnectionBranch[branch_depot_' + depo_ID + '_' + station_ID + '_4sp],[metro.StationPath[stationPath_4_' + station_ID + ']]}')
        link_connectionBranch_to.append('      {metro.ConnectionBranch,to,metro.ConnectionBranch[branch_' + station_ID + '_3sp_depot_' + depo_ID + '],[metro.Depot[depot_' + depo_ID + ']]}')
        
        link_pathWay_start.append('      {metro.Pathway,start,metro.Pathway[toDepot_' + station_ID + '_1msp_3sp_depot_' + depo_ID + '],[metro.MainStationPath[mainStationPath_1_' + station_ID + ']]}')
        link_pathWay_start.append('      {metro.Pathway,start,metro.Pathway[fromDepot_depot_' + depo_ID + '_' + station_ID + '_4sp_2msp],[metro.Depot[depot_' + depo_ID + ']]}')
        
        link_pathWay_ways.append('      {metro.Pathway,ways,metro.Pathway[toDepot_' + station_ID + '_1msp_3sp_depot_' + depo_ID + '],[metro.StationRoute[stationRoute_' + station_ID + '_1msp_3sp],metro.ConnectionBranch[branch_' + station_ID + '_3sp_depot_' + depo_ID + ']]}')
        link_pathWay_ways.append('      {metro.Pathway,ways,metro.Pathway[fromDepot_depot_' + depo_ID + '_' + station_ID + '_4sp_2msp],[metro.ConnectionBranch[branch_depot_' + depo_ID + '_' + station_ID + '_4sp],metro.StationRoute[stationRoute_' + station_ID + '_4sp_2msp]]}')
        
    elif start_msp == 2:
        # ConnectionBranch
        list_connectionBranch.append('    {metro.ConnectionBranch[branch_' + station_ID + '_4sp_depot_' + depo_ID + '],{ts.Name="' + station_name + ' 4 - депо ' + depo_name + '"}}')
        list_connectionBranch.append('    {metro.ConnectionBranch[branch_depot_' + depo_ID + '_' + station_ID + '_3sp],{ts.Name="депо ' + depo_name + ' - ' + station_name + ' 3"}}')
        # Pathway
        list_pathWay.append('    {metro.Pathway[fromDepot_depot_' + depo_ID + '_' + station_ID + '_3sp_1msp],{ts.Name="депо ' + depo_name + ' - ' + station_name + ' 3 сп 1 гсп"}}')
        list_pathWay.append('    {metro.Pathway[toDepot_' + station_ID + '_2msp_4sp_depot_' + depo_ID + '],{ts.Name="' + station_name + ' 2 гсп 4 сп - депо ' + depo_name + '"}}')
        
        link_connectionBranch_from.append('      {metro.ConnectionBranch,from,metro.ConnectionBranch[branch_depot_' + depo_ID + '_' + station_ID + '_3sp],[metro.Depot[depot_' + depo_ID + ']]}')
        link_connectionBranch_from.append('      {metro.ConnectionBranch,from,metro.ConnectionBranch[branch_' + station_ID + '_4sp_depot_' + depo_ID + '],[metro.StationPath[stationPath_4_' + station_ID + ']]}')
        
        link_connectionBranch_to.append('      {metro.ConnectionBranch,to,metro.ConnectionBranch[branch_depot_' + depo_ID + '_' + station_ID + '_3sp],[metro.StationPath[stationPath_3_' + station_ID + ']]}')
        link_connectionBranch_to.append('      {metro.ConnectionBranch,to,metro.ConnectionBranch[branch_' + station_ID + '_4sp_depot_' + depo_ID + '],[metro.Depot[depot_' + depo_ID + ']]}')
        
        link_pathWay_start.append('      {metro.Pathway,start,metro.Pathway[toDepot_' + station_ID + '_2msp_4sp_depot_' + depo_ID + '],[metro.MainStationPath[mainStationPath_2_' + station_ID + ']]}')
        link_pathWay_start.append('      {metro.Pathway,start,metro.Pathway[fromDepot_depot_' + depo_ID + '_' + station_ID + '_3sp_1msp],[metro.Depot[depot_' + depo_ID + ']]}')
        
        link_pathWay_ways.append('      {metro.Pathway,ways,metro.Pathway[toDepot_' + station_ID + '_2msp_4sp_depot_' + depo_ID + '],[metro.StationRoute[stationRoute_' + station_ID + '_2msp_4sp],metro.ConnectionBranch[branch_' + station_ID + '_4sp_depot_' + depo_ID + ']]}')
        link_pathWay_ways.append('      {metro.Pathway,ways,metro.Pathway[fromDepot_depot_' + depo_ID + '_' + station_ID + '_3sp_1msp],[metro.ConnectionBranch[branch_depot_' + depo_ID + '_' + station_ID + '_3sp],metro.StationRoute[stationRoute_' + station_ID + '_3sp_1msp]]}')
        
    else:
        print('Station path Error! In non-typical cases use standard FGDP tools!')


# In[6]:


def create_Station(st_ID, st_name, number, msp, sp, sp_mode):
    stations.append([number, st_name, st_ID])
    
    sp_string = ''
    msp_string = ''
    
    
    # Object PassengerStation
    listStations.append('    {metro.PassengerStation[passStation_' + st_ID 
                        + '],{ts.Name="' + st_name 
                        + '",ts.Description="Станция ' + st_name 
                        + '",number=' + str(number) + ',ramified=true}}')
    
    # MainStationPath
    # Objects
    for x in range(msp):
        if x == 0:
            msp_string = "metro.MainStationPath[mainStationPath_1_" + st_ID + "]"
        else:
            msp_string += ",metro.MainStationPath[mainStationPath_"+ str(x+1) + "_" + st_ID + "]"
        listMainSP.append('    {metro.MainStationPath[mainStationPath_' + str(x+1) 
                          + '_' + st_ID + '],{ts.Name="'+ str(x+1) + ' Гл.ст.путь '+ st_name 
                          + '",ts.Description="'+ str(x+1) + ' Гл.ст.путь '+ st_name + '",pathNum=' + str(x+1) + '}}')
    # Link
    list_links_msp.append('      {metro.PassengerStation,platforms,metro.PassengerStation[passStation_' + st_ID 
                          + '],[' + msp_string + ']}')
    
    
    # StationPath
    if sp != 0:
        # Objects
        for x in range(sp):
            if x == 0:
                sp_string = "metro.StationPath[stationPath_" + str(sp_mode) + "_" + st_ID + "]"
            else:
                sp_string += ",metro.StationPath[stationPath_"+ str(x+sp_mode) + "_" + st_ID + "]"
            listStationPath.append('    {metro.StationPath[stationPath_' + str(x+sp_mode) 
                                   + '_' + st_ID + '],{ts.Name="'+ str(x+sp_mode) + ' ст.путь '+ st_name 
                                   + '",ts.Description="'+ str(x+sp_mode) + ' ст.путь '+ st_name + '",pathNum='+ str(x+sp_mode) + '}}')
        # Link
        list_links_sp.append("      {metro.PassengerStation,paths,metro.PassengerStation[passStation_" + st_ID 
                             + "],[" + sp_string + "]}")
             
    # StationRout
    station_rout(st_ID, st_name, msp, sp, sp_mode)


# In[7]:


def station_rout(st_ID, st_name, msp, sp, sp_mode):
    list_links_routes_id = ''
    str_1msp_turnovers = ''
    str_2msp_turnovers = ''
    for i in range(sp):
        if (i + sp_mode) == 1:
            # msp to sp
            listStationRout.append('    {metro.StationRoute[stationRoute_' + st_ID + '_' 
                                   + str(i + 1) + 'msp_' + str(i + 1) + 'sp],{ts.Name="' 
                                   + st_name + ' ' + str(i + 1) + ' Гл.ст.путь - ' + str(i + 1) 
                                   + ' ст.путь",ts.Description=" "}}')
            listStationRout_from.append('      {metro.StationRoute,from,metro.StationRoute[stationRoute_' 
                                        + st_ID + '_' + str(i + 1) + 'msp_' + str(i + 1) 
                                        + 'sp],[metro.MainStationPath[mainStationPath_' 
                                        + str(i + 1) + '_' + st_ID + ']]}')
            listStationRout_to.append('      {metro.StationRoute,to,metro.StationRoute[stationRoute_' 
                                      + st_ID + '_' + str(i + 1) + 'msp_' + str(i + 1) 
                                      + 'sp],[metro.StationPath[stationPath_' 
                                      + str(i + 1) + '_' + st_ID + ']]}')
            list_links_routes_id += 'metro.StationRoute[stationRoute_' + st_ID + '_' + str(i + 1) + 'msp_' + str(i + 1) + 'sp]'        
            # sp to msp
            listStationRout.append('    {metro.StationRoute[stationRoute_' + st_ID + '_' + str(i + 1) 
                                   + 'sp_' + str(i + 1) + 'msp],{ts.Name="'+ st_name + ' ' + str(i + 1) 
                                   + ' ст.путь - ' + str(i + 1) + ' Гл.ст.путь",ts.Description=" "}}')
            listStationRout_from.append('      {metro.StationRoute,from,metro.StationRoute[stationRoute_' 
                                        + st_ID + '_' + str(i + 1) + 'sp_' + str(i + 1) 
                                        + 'msp],[metro.StationPath[stationPath_' 
                                        + str(i + 1) + '_' + st_ID + ']]}')
            listStationRout_to.append('      {metro.StationRoute,to,metro.StationRoute[stationRoute_' 
                                      + st_ID + '_' + str(i + 1) + 'sp_' + str(i + 1) 
                                      + 'msp],[metro.MainStationPath[mainStationPath_' 
                                      + str(i + 1) + '_' + st_ID + ']]}')
            list_links_routes_id += ',metro.StationRoute[stationRoute_' + st_ID + '_' + str(i + 1) + 'sp_' + str(i + 1) + 'msp]'        
        elif (i + sp_mode) == 2:
            # msp to sp
            listStationRout.append('    {metro.StationRoute[stationRoute_' + st_ID + '_' + str(i + 1) 
                                   + 'msp_' + str(i + 1) + 'sp],{ts.Name="'+ st_name + ' ' + str(i + 1) 
                                   + ' Гл.ст.путь - ' + str(i + 1) + ' ст.путь",ts.Description=" "}}')
            listStationRout_from.append('      {metro.StationRoute,from,metro.StationRoute[stationRoute_' 
                                        + st_ID + '_' + str(i + 1) + 'msp_' + str(i + 1) 
                                        + 'sp],[metro.MainStationPath[mainStationPath_' 
                                        + str(i + 1) + '_' + st_ID + ']]}')
            listStationRout_to.append('      {metro.StationRoute,to,metro.StationRoute[stationRoute_' 
                                      + st_ID + '_' + str(i + 1) + 'msp_' + str(i + 1) 
                                      + 'sp],[metro.StationPath[stationPath_' 
                                      + str(i + 1) + '_' + st_ID + ']]}')
            list_links_routes_id += ',metro.StationRoute[stationRoute_' + st_ID + '_' + str(i + 1) + 'msp_' + str(i + 1) + 'sp]'        
            # sp to msp
            listStationRout.append('    {metro.StationRoute[stationRoute_' + st_ID + '_' + str(i + 1) 
                                   + 'sp_' + str(i + 1) + 'msp],{ts.Name="'+ st_name + ' ' + str(i + 1) 
                                   + ' ст.путь - ' + str(i + 1) + ' Гл.ст.путь",ts.Description=" "}}')
            listStationRout_from.append('      {metro.StationRoute,from,metro.StationRoute[stationRoute_' 
                                        + st_ID + '_' + str(i + 1) + 'sp_' + str(i + 1) 
                                        + 'msp],[metro.StationPath[stationPath_' 
                                        + str(i + 1) + '_' + st_ID + ']]}')
            listStationRout_to.append('      {metro.StationRoute,to,metro.StationRoute[stationRoute_' 
                                      + st_ID + '_' + str(i + 1) + 'sp_' + str(i + 1) 
                                      + 'msp],[metro.MainStationPath[mainStationPath_' + str(i + 1) 
                                      + '_' + st_ID + ']]}')
            list_links_routes_id += ',metro.StationRoute[stationRoute_' + st_ID + '_' + str(i + 1) + 'sp_' + str(i + 1) + 'msp]'
        else:
            for n in range(msp):
                # msp to sp
                listStationRout.append('    {metro.StationRoute[stationRoute_' + st_ID + '_' + str(n + 1) 
                                       + 'msp_' + str(i + sp_mode) + 'sp],{ts.Name="'+ st_name + ' ' + str(n + 1) 
                                       + ' Гл.ст.путь - ' + str(i + sp_mode) + ' ст.путь",ts.Description=" "}}')
                listStationRout_from.append('      {metro.StationRoute,from,metro.StationRoute[stationRoute_' 
                                            + st_ID + '_' + str(n + 1) + 'msp_' + str(i + sp_mode) 
                                            + 'sp],[metro.MainStationPath[mainStationPath_' 
                                            + str(n + 1) + '_' + st_ID + ']]}')
                listStationRout_to.append('      {metro.StationRoute,to,metro.StationRoute[stationRoute_' 
                                          + st_ID + '_' + str(n + 1) + 'msp_' + str(i + sp_mode) 
                                          + 'sp],[metro.StationPath[stationPath_' 
                                          + str(i + sp_mode) + '_' + st_ID + ']]}')
                if (i == 0) & (n == 0):
                    list_links_routes_id += 'metro.StationRoute[stationRoute_' + st_ID + '_' + str(n + 1) + 'msp_' + str(i + sp_mode) + 'sp]'
                list_links_routes_id += ',metro.StationRoute[stationRoute_' + st_ID + '_' + str(n + 1) + 'msp_' + str(i + sp_mode) + 'sp]'
                # sp to msp
                listStationRout.append('    {metro.StationRoute[stationRoute_' + st_ID + '_' + str(i + sp_mode) 
                                       + 'sp_' + str(n + 1) + 'msp],{ts.Name="'+ st_name + ' ' + str(i + sp_mode) 
                                       + ' ст.путь - ' + str(n + 1) + ' Гл.ст.путь",ts.Description=" "}}')
                listStationRout_from.append('      {metro.StationRoute,from,metro.StationRoute[stationRoute_' 
                                            + st_ID + '_' + str(i + sp_mode) + 'sp_' + str(n + 1) 
                                            + 'msp],[metro.StationPath[stationPath_' 
                                            + str(i + sp_mode) + '_' + st_ID + ']]}')
                listStationRout_to.append('      {metro.StationRoute,to,metro.StationRoute[stationRoute_' 
                                          + st_ID + '_' + str(i + sp_mode) + 'sp_' + str(n + 1) 
                                          + 'msp],[metro.MainStationPath[mainStationPath_' 
                                          + str(n + 1) + '_' + st_ID + ']]}')
                list_links_routes_id += ',metro.StationRoute[stationRoute_' + st_ID + '_' + str(i + sp_mode) + 'sp_' + str(n + 1) + 'msp]'
            # TurnoverPath
            listTurnoverPath.append('    {metro.TurnoverPath[turnoverPath_' + st_ID + '_1msp_' + str(i + sp_mode) + 'sp_2msp],{ts.Name="оборот '+ st_name + ' I Гл.ст.п - ' + str(i + sp_mode) + ' ст.п - II Гл.ст.п",ts.Description=" "}}')
            listTurnoverPath.append('    {metro.TurnoverPath[turnoverPath_' + st_ID + '_2msp_' + str(i + sp_mode) + 'sp_1msp],{ts.Name="оборот '+ st_name + ' II Гл.ст.п - ' + str(i + sp_mode) + ' ст.п - I Гл.ст.п",ts.Description=" "}}')
            
            link_pathWay_start.append('      {metro.Pathway,start,metro.TurnoverPath[turnoverPath_' + st_ID + '_1msp_' + str(i + sp_mode) + 'sp_2msp],[metro.MainStationPath[mainStationPath_1_' + st_ID + ']]}')
            link_pathWay_start.append('      {metro.Pathway,start,metro.TurnoverPath[turnoverPath_' + st_ID + '_2msp_' + str(i + sp_mode) + 'sp_1msp],[metro.MainStationPath[mainStationPath_2_' + st_ID + ']]}')
            
            link_pathWay_ways.append('      {metro.Pathway,ways,metro.TurnoverPath[turnoverPath_' + st_ID + '_1msp_' + str(i + sp_mode) + 'sp_2msp],[metro.StationRoute[stationRoute_' + st_ID + '_1msp_' + str(i + sp_mode) + 'sp],metro.StationRoute[stationRoute_' + st_ID + '_' + str(i + sp_mode) + '_2msp]]}')
            link_pathWay_ways.append('      {metro.Pathway,ways,metro.TurnoverPath[turnoverPath_' + st_ID + '_2msp_' + str(i + sp_mode) + 'sp_1msp],[metro.StationRoute[stationRoute_' + st_ID + '_2msp_' + str(i + sp_mode) + 'sp],metro.StationRoute[stationRoute_' + st_ID + '_' + str(i + sp_mode) + '_1msp]]}')
            
            if (i + sp_mode) < 3:
                print('Station path Error! In non-typical cases use standard FGDP tools!')
            if (i + sp_mode) == 3:
                str_1msp_turnovers += 'metro.TurnoverPath[turnoverPath_' + st_ID + '_1msp_' + str(i + sp_mode) + '_2msp]'
                str_2msp_turnovers += 'metro.TurnoverPath[turnoverPath_' + st_ID + '_2msp_' + str(i + sp_mode) + '_1msp]'
            else:
                str_1msp_turnovers += ',metro.TurnoverPath[turnoverPath_' + st_ID + '_1msp_' + str(i + sp_mode) + '_2msp]'
                str_2msp_turnovers += ',metro.TurnoverPath[turnoverPath_' + st_ID + '_2msp_' + str(i + sp_mode) + '_1msp]'
            
    # Link routes filler
    if sp != 0:
        list_links_routes.append('      {metro.PassengerStation,routes,metro.PassengerStation[passStation_' 
                                 + st_ID + '],[' + list_links_routes_id + ']}')

        link_msp_turnovers.append('      {metro.MainStationPath,turnovers,metro.MainStationPath[mainStationPath_1_' + st_ID + '],[' + str_1msp_turnovers + ']}')
        link_msp_turnovers.append('      {metro.MainStationPath,turnovers,metro.MainStationPath[mainStationPath_2_' + st_ID + '],[' + str_2msp_turnovers + ']}')


# In[8]:


def create_LineRegion(start, end, line_ID, region_N):
    start_ID = ''
    start_name = ''
    end_ID = ''
    end_name = ''
    global str_lineRegion
    
    for i in stations:
        if i[0] == start:
            start_ID = i[2]
            start_name = i[1]
        elif i[0] == end:
            end_ID = i[2]
            end_name = i[1]
            
    listLineRegion.append('    {metro.LineRegion[region_' + line_ID + '_' + start_ID + '_' + end_ID 
                          + '],{ts.Name="' + start_name + '-' + end_name 
                          + '",ts.Description="Участок ' + start_name + '-' + end_name + '",circle=false}}')
    
    if region_N == 1:
        str_lineRegion = ('metro.LineRegion[region_' + line_ID + '_' + start_ID + '_' + end_ID + ']')
    else:
        str_lineRegion += (',metro.LineRegion[region_' + line_ID + '_' + start_ID + '_' + end_ID + ']')
    


# In[9]:


def create_link_line(line_ID):
    link_line_regions.append('      {metro.Line,regions,metro.Line[line_' + line_ID
                             + '],[' + str_lineRegion + ']}')
    
    link_line_depot.append('      {metro.Line,depots,metro.Line[line_' + line_ID 
                           + '],[' + str_depot + ']}')


# In[10]:


def create_link_lineRegion(line_ID):
    link_lineRegion_stations.append('      {metro.LineRegion,stations,metro.LineRegion[region_' + line_ID + '_' + str_first_station + '_' + str_last_station + '],[' + str_link_stations + ']}')
    link_lineRegion_drivingModes.append('      {metro.LineRegion,drivingModes,metro.LineRegion[region_' + line_ID + '_' + str_first_station + '_' + str_last_station + '],[' + str_link_lineDrivingMode + ']}')


# In[11]:


def create_RailwayStage(d, line_ID):
    global str_changeStation1path
    global str_changeStation2path
    global str_first_station
    global str_last_station
    global str_link_stations
    
    df = pd.DataFrame(stations)
    display(df)
    
    if d == 1:
        d_12 = 1
        d_21 = 2
        str_first_station = df.loc[0][2]
        str_last_station = df.loc[len(df)-1][2]
    elif d ==2:
        d_12 = 2
        d_21 = 1
        str_first_station = df.loc[len(df)-1][2] 
        str_last_station = df.loc[0][2]
    else:
        print('Wrong direction!')
    
    str_changeStation1path = '      {metro.LineRegion,changeStation1path,metro.LineRegion[region_' + line_ID + '_' + str_first_station  + '_' + str_last_station + '],[metro.PassengerStation[passStation_' + str_first_station + ']]}'
    str_changeStation2path = '      {metro.LineRegion,changeStation2path,metro.LineRegion[region_' + line_ID + '_' + str_first_station  + '_' + str_last_station + '],[metro.PassengerStation[passStation_' + str_last_station + ']]}'
    
    for x in df[0]:
        if x < df[0][df.shape[0]-1]:
            # Objects
            listRailwayStage.append('    {metro.RailwayStage[railwayStage_' + str(d_12) + '_' + df.loc[x-1][2] 
                                    + '_' + df.loc[x][2] + '],{ts.Name="' + df.loc[x-1][1] 
                                    + ' - ' + df.loc[x][1] + '",ts.Description="' + df.loc[x-1][1] 
                                    + ' - ' + df.loc[x][1] + '",pathNum=' + str(d_12) + ',shortName=""}}')
            listRailwayStage.append('    {metro.RailwayStage[railwayStage_' + str(d_21) + '_' + df.loc[x][2] 
                                    + '_' + df.loc[x-1][2] + '],{ts.Name="' + df.loc[x][1] 
                                    + ' - ' + df.loc[x-1][1] + '",ts.Description="' + df.loc[x][1] 
                                    + ' - ' + df.loc[x-1][1] + '",pathNum=' + str(d_21) + ',shortName=""}}')
            # Links
            list_from_RailwayStage.append('      {metro.RailwayStage,from,metro.RailwayStage[railwayStage_' 
                                          + str(d_12) + '_' + df.loc[x-1][2] + '_' + df.loc[x][2] 
                                          + '],[metro.MainStationPath[mainStationPath_' + str(d_12) 
                                          + '_' + df.loc[x-1][2] + ']]}')
            list_from_RailwayStage.append('      {metro.RailwayStage,from,metro.RailwayStage[railwayStage_' 
                                          + str(d_21) + '_' + df.loc[x][2] + '_' + df.loc[x-1][2] 
                                          + '],[metro.MainStationPath[mainStationPath_' + str(d_21) 
                                          + '_' + df.loc[x][2] + ']]}')
            list_to_RailwayStage.append('      {metro.RailwayStage,to,metro.RailwayStage[railwayStage_' 
                                        + str(d_12) + '_' + df.loc[x-1][2] + '_' + df.loc[x][2] 
                                        + '],[metro.MainStationPath[mainStationPath_' + str(d_12) 
                                        + '_' + df.loc[x][2] + ']]}')
            list_to_RailwayStage.append('      {metro.RailwayStage,to,metro.RailwayStage[railwayStage_' 
                                        + str(d_21) + '_' + df.loc[x][2] + '_' + df.loc[x-1][2] 
                                        + '],[metro.MainStationPath[mainStationPath_' + str(d_21) 
                                        + '_' + df.loc[x-1][2] + ']]}')
            
        if x == 1:
            str_link_stations = 'metro.PassengerStation[passStation_' + df.loc[x-1][2] + ']'
        else:
            str_link_stations += ',metro.PassengerStation[passStation_' + df.loc[x-1][2] + ']'


# In[12]:


def list_objects_filler(list_input):
    i = 0
    for line in list_input:
        i += 1
        if i == len(list_input):
            listObjects.append(line)
        else:
            listObjects.append(line + ",")
    listObjects.append("  ],")


# In[13]:


def listObjects_generate():
    
    # LineRegion
    listObjects.append("  metro.LineRegion = [")
    list_objects_filler(listLineRegion)
    
    # PassengerStation
    listObjects.append("  metro.PassengerStation = [")
    list_objects_filler(listStations)
    
    # MainStationPath
    listObjects.append("  metro.MainStationPath = [")
    list_objects_filler(listMainSP)
    
    # StationPath
    listObjects.append("  metro.StationPath = [")
    list_objects_filler(listStationPath)
    
    # StationRoute
    listObjects.append("  metro.StationRoute = [")
    list_objects_filler(listStationRout)
    
    # TurnoverPath
    listObjects.append("  metro.TurnoverPath = [")
    list_objects_filler(listTurnoverPath)
    
    # RailwayStage
    listObjects.append("  metro.RailwayStage = [")
    list_objects_filler(listRailwayStage)
    
    # Depot
    listObjects.append("  metro.Depot = [")
    list_objects_filler(list_depot)
    
    # ConnectionBranch
    listObjects.append("  metro.ConnectionBranch = [")
    list_objects_filler(list_connectionBranch)
    
    # Pathway
    listObjects.append("  metro.Pathway = [")
    list_objects_filler(list_pathWay)
    
    # StageModeFirst 
    listObjects.append("  metro.StageModeFirst = [")
    list_objects_filler(list_stageModeFirst)
    
    # StageMode
    listObjects.append("  metro.StageMode = [")
    list_objects_filler(list_stageMode)
    
    # StopMode
    listObjects.append("  metro.StopMode = [")
    list_objects_filler(list_stopMode)
    
    # LineDrivingModes
    listObjects.append("  metro.LineDrivingModes = [")
    list_objects_filler(list_lineDrivingMode)
    
    # DrivingMode
    listObjects.append("  metro.DrivingMode = [")
    list_objects_filler(list_drivingMode)
    
    # DrivingMode_sk
    listObjects.append("  sk.regref.comp.metro.RRI.FGDP.metro.DrivingMode = [")
    list_objects_filler(objekt_drivingMode_link)


# In[ ]:


def list_links_filler(list_input):
    i = 0
    for line in list_input:
        i += 1
        if i == len(list_input):
            listLinks.append(line)
        else:
            listLinks.append(line + ",")


# In[14]:


def listLinks_generator():
    
    # Line
    listLinks.append("  metro.Line = [")
    # regions
    listLinks.append("    regions = [")
    list_links_filler(link_line_regions)
    listLinks.append("    ],") 
    # depots
    listLinks.append("    depots = [")
    list_links_filler(link_line_depot)
    listLinks.append("    ]") 
    listLinks.append("  ],")
    
    # LineRegion
    listLinks.append("  metro.LineRegion = [")
    # changeStation1path
    listLinks.append("    changeStation1path = [")
    listLinks.append(str_changeStation1path)
    listLinks.append("    ],") 
    # changeStation2path
    listLinks.append("    changeStation2path = [")
    listLinks.append(str_changeStation2path)
    listLinks.append("    ],") 
    # stations
    listLinks.append("    stations = [")
    list_links_filler(link_lineRegion_stations)
    listLinks.append("    ],") 
    # drivingModes
    listLinks.append("    drivingModes = [")
    list_links_filler(link_lineRegion_drivingModes)
    listLinks.append("    ]") 
    listLinks.append("  ],")
    
    # PassengerStation
    listLinks.append("  metro.PassengerStation = [")
    # platforms
    listLinks.append("    platforms = [")
    list_links_filler(list_links_msp)
    listLinks.append("    ],")
    # paths
    listLinks.append("    paths = [")
    list_links_filler(list_links_sp)
    listLinks.append("    ],")
    # routes
    listLinks.append("    routes = [")
    list_links_filler(list_links_routes)
    listLinks.append("    ],")
    # rri
    listLinks.append("    rri = [")
    listLinks.append("    ]")
    listLinks.append("  ],")
    
    # MainStationPath
    listLinks.append("  metro.MainStationPath = [")
    # turnovers
    listLinks.append("    turnovers = [")
    list_links_filler(link_msp_turnovers)
    listLinks.append("    ]") 
    listLinks.append("  ],")
    
    # StationRoute
    listLinks.append("  metro.StationRoute = [")
    # from
    listLinks.append("    from = [")
    list_links_filler(listStationRout_from)
    # to
    listLinks.append("    to = [")
    list_links_filler(listStationRout_to)
    listLinks.append("    ]")
    listLinks.append("  ],")
    
    # RailwayStage
    listLinks.append("  metro.RailwayStage = [")
    # from
    listLinks.append("    from = [")
    list_links_filler(list_from_RailwayStage)
    listLinks.append("    ],") 
    # to
    listLinks.append("    to = [")
    list_links_filler(list_to_RailwayStage)
    listLinks.append("    ]")
    listLinks.append("  ],")
    
    # ConnectionBranch
    listLinks.append("  metro.ConnectionBranch = [")
    # from
    listLinks.append("    from = [")
    list_links_filler(link_connectionBranch_from)
    listLinks.append("    ],")
    # to
    listLinks.append("    to = [")
    list_links_filler(link_connectionBranch_to)
    listLinks.append("    ]") 
    listLinks.append("  ],")
    
    # Pathway
    listLinks.append("  metro.Pathway = [")
    # start
    listLinks.append("    start = [")
    list_links_filler(link_pathWay_start)
    listLinks.append("    ],")
    # ways
    listLinks.append("    ways = [")
    list_links_filler(link_pathWay_ways)
    listLinks.append("    ]") 
    listLinks.append("  ],")
    
    # StageModeFirst
    listLinks.append("  metro.StageModeFirst = [")
    # stage
    listLinks.append("    stage = [")
    list_links_filler(link_stageModeFirst_stage)
    listLinks.append("    ]") 
    listLinks.append("  ],")
    
    # StageMode
    listLinks.append("  metro.StageMode = [")
    # stage
    listLinks.append("    stage = [")
    list_links_filler(link_stageMode_stage)
    listLinks.append("    ]") 
    listLinks.append("  ],")
    
    # StopMode
    listLinks.append("  metro.StopMode = [")
    # station
    listLinks.append("    station = [")
    list_links_filler(link_stopMode_station)
    listLinks.append("    ]") 
    listLinks.append("  ],")   
    
    # LineDrivingModes
    listLinks.append("  metro.LineDrivingModes = [")
    # path1
    listLinks.append("    path1 = [")
    listLinks.append(str_link_ldm_path1)
    listLinks.append("    ],")    
    # path2
    listLinks.append("    path2 = [")
    listLinks.append(str_link_ldm_path2)
    listLinks.append("    ]") 
    listLinks.append("  ],")
    
    # DrivingMode
    listLinks.append("  metro.DrivingMode = [")
    # stages
    listLinks.append("    stages = [")
    list_links_filler(link_drivingMode_stages)
    listLinks.append("    ],")
    # stops
    listLinks.append("    stops = [")
    list_links_filler(link_drivingMode_stops)
    listLinks.append("    ]") 
    listLinks.append("  ],")


# In[15]:


def objets_find():
    f = open('123.gdp', mode='r', encoding='utf-8')
    
    df = pd.DataFrame()

    i = 0
    itr = 0
    a = False
    stationsN = 0

    lines = f.readlines()
    for line in lines:
        if line.find("Objects") >= 0:
            a = True
        if a:
            if line.find("PassengerStation[") >= 0:
                if line.find("ts.Name=") >= 0:
                    result = re.findall('\".*?\"', line)
                    result_indname = re.findall('\[.*?\]', line)
                    subline = line[-25:-15]
                    df_row = {'0' : nums_from_string.get_nums(subline)[0], 
                              '1' : result[0], 
                              '2' : result_indname[0][-4:-1]}
                    df = df.append(df_row, ignore_index = True)
                    
                    stationsN += 1
                    itr = i
        i += 1
    display(df)    
    if stationsN == 0:
            print("Объектов станций не найдено!")
    f.close()    


# In[16]:


def write_to_file():
    f = open('123.gdp', mode='r', encoding='utf-8')
    i = 0
    itr = 0
    a = False
    lines = f.readlines()
    
# Objects
    for line in lines:
        if line.find("Objects") >= 0:
            itr = i + 1
        i += 1
    i = 0

    for line in listObjects:
        lines.insert(itr + i, line + "\n")
        i += 1
    
# Links
    i = 0
    for line in lines:
        if line.find("Links = [") >= 0:
            #print(str(i) + " " + line)
            itr = i + 1
        i += 1
    i = 0
    
    for line in listLinks:
        lines.insert(itr + i, line + "\n")
        i += 1
        
    f.close()    
    save_changes = open('123_1.gdp', mode='w', encoding='utf-8') 
    save_changes.writelines(lines) 
    save_changes.close()


# In[17]:


line = 'NKL'


# In[18]:


create_Station('nks', 'Некрасовская', 1, 2, 4, 1)


# In[19]:


create_Station('lhm', 'Лухмановская', 2, 2, 2, 3)


# In[20]:


create_Station('udm', 'Улица Дмитриевского', 3, 2, 0, 0)


# In[21]:


create_Station('ksn', 'Косино', 4, 2, 0, 0)


# In[22]:


create_Station('uyv', 'Юго-Восточная', 5, 2, 0, 0)


# In[23]:


create_Station('oks', 'Окская', 6, 2, 0, 0)


# In[24]:


create_Station('sth', 'Стахановская', 7, 2, 0, 0)


# In[25]:


create_Station('njg', 'Нижегородская', 8, 2, 1, 3)


# In[26]:


create_LineRegion(1, 8, line, 1)


# In[27]:


create_RailwayStage(1, line)


# In[28]:


create_Depot('rud', 'Руднево', 2, 2, 1)


# In[29]:


create_link_line(line)


# In[30]:


create_Modes(line)


# In[31]:


create_link_lineRegion(line)


# In[32]:


listObjects_generate()


# In[33]:


listLinks_generator()


# In[34]:


write_to_file()


# In[35]:


#objets_find()

