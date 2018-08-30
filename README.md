# scraping
## MineMaterials: Web scraper for crystallographic data from American Mineralogist Crystal Structure Database

## Authors:
Tonnam Balankura, The Pennsylvania State University 
Ying Li, Argonne National Laboratory
Fu-Chang Sun, The University of Connecticut 
Enshi Xu, The Pennsylvania State University

## Main contents: 

### amcsd_list.py
#### def get_list():
Scrape the list of all materials name available on http://rruff.geo.arizona.edu/AMS/all_minerals.php

### ams_lxml.py
#### def get_mineral_id( name='' ):
Scrape mineral id from AMCSD

#### def get_xray_info( name = '' ):
Scrape xray data from AMCSD

#### write_csv.py
Execute the scraping functions written and format them in .csv file, ready to submit to Citrination.com
