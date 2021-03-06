# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:12:42 2015

@author: zeke
"""

import csv
import fiona


in_shape= fiona.open('../data/census_2011/sample_shape.shp','r')
keys = []
for rec in in_shape:
    keys.append(rec['properties']['DAUID'])
    keys.append(rec['properties']['CTUID'])


f501 =open('/home/zeke/data/super_secret/data/501.csv','rb')
f401 = open('/home/zeke/data/super_secret/data/401.csv','rb')
in501 = csv.DictReader(f501,fieldnames=['Geo_Code', 'Prov_name', 'Geo_nom', 'Topic', 'Characteristic', 'Note', 'Total', 'Flag_total', 'Male', 'Flag_Male', 'Female', 'Flag_Female'])
in401 = csv.DictReader(f401,fieldnames=['Geo_Code', 'Prov_Name', 'CMA_CA_Name', 'CT_Name', 'GNR', 'Topic', 'Characteristic', 'Note', 'Total', 'Flag_Total', 'Male', 'Flag_Male', 'Female', 'Flag_Female'])

of501 =open('/home/zeke/data/super_secret/data/501a.csv','wb')
of401 = open('/home/zeke/data/super_secret/data/401a.csv','wb')

out501 = csv.DictWriter(of501,fieldnames=['Geo_Code', 'Prov_name', 'Geo_nom', 'Topic', 'Characteristic', 'Note', 'Total', 'Flag_total', 'Male', 'Flag_Male', 'Female', 'Flag_Female'])
out401 = csv.DictWriter(of401,fieldnames=['Geo_Code', 'Prov_Name', 'CMA_CA_Name', 'CT_Name', 'GNR', 'Topic', 'Characteristic', 'Note', 'Total', 'Flag_Total', 'Male', 'Flag_Male', 'Female', 'Flag_Female'])
firstline = True
c = 0
s = 0 
for row in in501:
    s+=1
    print s
    if firstline:
        out501.writerow(row)
        firstline = False
        continue
    if row['Geo_Code'] in keys:
        out501.writerow(row)
        c +=1
        print "Wrote Row 501", c
c = 0
for row in in401:
    
    if firstline:
        out401.writerow(row)
        firstline = False
        continue
    if row['Geo_Code'] in keys:
        out401.writerow(row)
        c +=1
        print "Wrote Row 401", c
        
        
of501.close()
of401.close()