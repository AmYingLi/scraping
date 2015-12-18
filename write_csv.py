# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 20:02:56 2015

@author: Tonnam
"""
# pip install scraperwiki

import amcsd_list
import ams_lxml

# Get list of crystal structure names
name_list = amcsd_list.get_list()

# Formatting strings of .csv file for DIF files scraping
doi = '10.1130/2006.2397(06)'
sub_citation_1 = 'American Mineralogist Crystal Structure Database'
url = 'http://rruff.geo.arizona.edu/AMS/amcsd.php'
m_name = 'X-ray diffraction'
unit_intensity = 'Arb. units'
unit_two_theta = '$^{\\circ}$'
unit_wavelength = '$\\AA$'
unit_cellparam_abc = '$\\AA$'
unit_cellparam_theta = '$^{\\circ}$'

# Write .csv file in appropriate format
with open('xray_diffraction.csv', 'w') as fout:
    fout.write('Citation,Sub citation,Sub citation,Sub url,Common name,Measurement method,'+\
    'Measurement name,Measurement value,Measurement units,'+\
    'Measurement condition name,Measurement condition value,Measurement condition units,'+\
    'Measurement condition name,Measurement condition value,Measurement condition units\n')
    for name in name_list:
        print name
        xray_info = ams_lxml.get_xray_info(name)
        two_theta = xray_info.two_theta
        intensity = xray_info.intensity
        ref_format = xray_info.author+'. '+xray_info.journal+'.' # +xray_info.title
        # remove title from reference because sometime they span to the 4th line
        fout.write(doi+','+sub_citation_1+',\"'+ref_format+'\",'+url+','+name+',' \
        +m_name+',Intensity,\"'+repr(intensity)+'\",'+unit_intensity \
        +',2$\Theta$,\"'+repr(two_theta)+'\",'+unit_two_theta \
        +',X-ray wavelength,'+str(xray_info.wavelength)+','+unit_wavelength+'\n')
        # write cell parameters rows
        fout.write(doi+','+sub_citation_1+',\"'+ref_format+'\",'+url+','+name+',' \
        +m_name+',Cell parameter (a),'+xray_info.cellparam[0]+','+unit_cellparam_abc+'\n')
        fout.write(doi+','+sub_citation_1+',\"'+ref_format+'\",'+url+','+name+',' \
        +m_name+',Cell parameter (b),'+xray_info.cellparam[1]+','+unit_cellparam_abc+'\n')
        fout.write(doi+','+sub_citation_1+',\"'+ref_format+'\",'+url+','+name+',' \
        +m_name+',Cell parameter (c),'+xray_info.cellparam[2]+','+unit_cellparam_abc+'\n')
        fout.write(doi+','+sub_citation_1+',\"'+ref_format+'\",'+url+','+name+',' \
        +m_name+',Cell parameter ($\\alpha$),'+xray_info.cellparam[3]+','+unit_cellparam_theta+'\n')
        fout.write(doi+','+sub_citation_1+',\"'+ref_format+'\",'+url+','+name+',' \
        +m_name+',Cell parameter ($\\beta$),'+xray_info.cellparam[4]+','+unit_cellparam_theta+'\n')
        fout.write(doi+','+sub_citation_1+',\"'+ref_format+'\",'+url+','+name+',' \
        +m_name+',Cell parameter ($\\gamma$),'+xray_info.cellparam[5]+','+unit_cellparam_theta+'\n')
        # write space group row     
        fout.write(doi+','+sub_citation_1+',\"'+ref_format+'\",'+url+','+name+',' \
        +m_name+',Space group,\"'+xray_info.spacegroup+'\"\n')
fout.close()