# %% [markdown]
# ## Get NSMP Records

# %%
import search
from pathlib import Path
import json
import pandas as pd
import pprint
pp = pprint.PrettyPrinter().pprint

# %% [markdown]
# ### NSMP Buildings
# https://earthquake.usgs.gov/monitoring/nsmp/arrays/#Buildings has 96.
# 
# https://www.strongmotioncenter.org/wserv/stations/query?netid=NP&sttype=B&format=json&nodata=404 has 140.

# %%
# USGS
with open("./NSMP/NSMP_buildings.html", 'r') as readfile:
    NSMP_buildings_usgs = pd.read_html(readfile)[0]
NSMP_buildings_usgs = NSMP_buildings_usgs.set_index('Station Code').to_dict('index')
for key in list(NSMP_buildings_usgs):
    NSMP_buildings_usgs[key.split(" ")[0]] = NSMP_buildings_usgs.pop(key)  # Remove any footnoted keys
print(len(NSMP_buildings_usgs), list(NSMP_buildings_usgs.items())[:3])

BUILDINGS = {value['Network Code']+key:value['Name'] for key,value in NSMP_buildings_usgs.items()}

# CESMD Web Services
with open("./NSMP/NSMP_buildings_web.json", 'r') as readfile:
    NSMP_buildings_web = json.load(readfile)
NSMP_buildings_web = {station['properties']['code']:station['properties']['name'] for station in NSMP_buildings_web['features']}
print(len(NSMP_buildings_web), list(NSMP_buildings_web.items())[:3])

# %% [markdown]
# ### NSMP Bridges
# 
# https://earthquake.usgs.gov/monitoring/nsmp/arrays/#Bridges has 16.
# 
# https://www.strongmotioncenter.org/wserv/stations/query?netid=NP&sttype=Br&format=json&nodata=404 has 2.

# %%
# USGS
with open("./NSMP/NSMP_bridges.html", 'r') as readfile:
    NSMP_bridges_usgs = pd.read_html(readfile)[0]
NSMP_bridges_usgs = NSMP_bridges_usgs.set_index('Station Code').to_dict('index')
print(len(NSMP_bridges_usgs), list(NSMP_bridges_usgs.items())[:3])

BRIDGES = {value['Network Code']+key:value['Name'] for key,value in NSMP_bridges_usgs.items()}

# CESMD Web Services
with open("./NSMP/NSMP_bridges_web.json", 'r') as readfile:
    NSMP_bridges_web = json.load(readfile)
NSMP_bridges_web = {station['properties']['code']:station['properties']['name'] for station in NSMP_bridges_web['features']}
print(len(NSMP_bridges_web), list(NSMP_bridges_web.items())[:3])

# %%
building_dir = Path("./NSMP/buildings/motions_original")
if not building_dir.exists():
    Path.mkdir(building_dir)
bridge_dir = Path("./NSMP/bridges/motions_original")
if not bridge_dir.exists():
    Path.mkdir(bridge_dir)

# %%
update_files = False

# %%
BUILDING_RECORDS = {}
if update_files:
    for key in BUILDINGS.keys():
        print(key, ':', BUILDINGS[key])
        try:
            search.get_records(str(building_dir)+"/"+key, "cchern@berkeley.edu", station_code=key, process_level="processed", include_inactive=True)
        except Exception as e:
            print(e)
            continue
        BUILDING_RECORDS[key] = BUILDINGS[key]
    with open(building_dir/"station_names.json", "w") as writefile:
        json.dump(BUILDING_RECORDS, writefile)
else:
    with open(building_dir/"station_names.json", "r") as readfile:
        BUILDING_RECORDS = json.load(readfile)

# %%
BUILDING_RECORDS

# %%
BRIDGE_RECORDS = {}
if update_files:
    for key in BRIDGES.keys():
        print(key, ':', BRIDGES[key])
        try:
            search.get_records(str(bridge_dir)+"/"+key, "cchern@berkeley.edu", station_code=key, process_level="processed", include_inactive=True)
        except Exception as e:
            print(e)
            continue
        BRIDGE_RECORDS[key] = BRIDGES[key]
    with open(bridge_dir/"station_names.json", "w") as writefile:
        json.dump(BRIDGE_RECORDS, writefile)
else:
    with open(bridge_dir/"station_names.json", "r") as readfile:
        BRIDGE_RECORDS = json.load(readfile)

# %%
BRIDGE_RECORDS

# %%
print(len(BUILDING_RECORDS), len(BRIDGE_RECORDS))

# %% [markdown]
# ## Move records to top levels of unzipped folders

# %%
import glob, os
from zipfile import ZipFile

# %%
extract_new = False

# %%
if extract_new:
    for record_dir in [building_dir, bridge_dir]:
        for cesmd_zip in glob.glob(str(record_dir)+"/*.zip"):
            newdir = cesmd_zip[:-4]
            with ZipFile(cesmd_zip) as zObject: 
                zObject.extractall(path="./"+newdir)

# %%
move_new = False

# %%
if move_new:

    def delete_empty_folders(root):
        deleted = set()
        for current_dir, subdirs, files in os.walk(root, topdown=False):
            still_has_subdirs = False
            for subdir in subdirs:
                if os.path.join(current_dir, subdir) not in deleted:
                    still_has_subdirs = True
                    break
            if not any(files) and not still_has_subdirs:
                os.rmdir(current_dir)
                deleted.add(current_dir)
        return deleted

    for RECORDS,record_dir in zip([BUILDING_RECORDS, BRIDGE_RECORDS], [building_dir, bridge_dir]):
        for key in RECORDS.keys():
            for record in glob.glob(str(record_dir)+"/"+key+"/*/*/*.[zZ][iI][pP]"):
                os.replace(record, str(record_dir)+"/"+key+"/"+os.path.basename(record).lower())
    
    delete_empty_folders(".")

# %%
count_records = False

# %%
if count_records:
    BUILDING_RECORD_COUNT = {}
    BRIDGE_RECORD_COUNT = {}
    for RECORDS,RECORD_COUNT,record_dir in zip([BUILDING_RECORDS, BRIDGE_RECORDS], [BUILDING_RECORD_COUNT,BRIDGE_RECORD_COUNT], [building_dir, bridge_dir]):
        for key in RECORDS.keys():
            RECORD_COUNT[key] = len(glob.glob(str(record_dir)+"/"+key+"/*.zip"))
    with open(record_dir/"record_counts.json", "w") as writefile:
        json.dump(RECORD_COUNT, writefile)
else:
    with open(building_dir/"record_counts.json", "r") as readfile:
        BUILDING_RECORD_COUNT = json.load(readfile)
    with open(bridge_dir/"record_counts.json", "r") as readfile:
        BRIDGE_RECORD_COUNT = json.load(readfile)

pp(BUILDING_RECORD_COUNT)
pp(BRIDGE_RECORD_COUNT)
print(len([key for key,value in BUILDING_RECORD_COUNT.items() if value>=5]))
print(len([key for key,value in BRIDGE_RECORD_COUNT.items() if value>=5]))

# %%
summarize_new = True

# %%
import numpy as np
def np_encoder(object):
    if isinstance(object, np.generic):
        return object.item()

# %%
if summarize_new:
    import quakeio
    import json
    for RECORDS,record_dir in zip([BUILDING_RECORDS, BRIDGE_RECORDS], [building_dir, bridge_dir]):
        for key in RECORDS.keys():  
            events = []
            for file in glob.glob(str(record_dir)+"/"+key+"/*.zip"):
                print(f"Reading {file}")
                with ZipFile(file, "r") as readfile:
                    if any('.smc' in name for name in readfile.namelist()):
                        parser = 'smc.read_event'
                    else:
                        parser = None
                try:
                    events.append(
                        quakeio.read(file, summarize=True, parser=parser).serialize(serialize_data=False)
                    )
                except Exception as e:
                    print(e)
                    print(f"failed to read {file}")
                    # raise e
            # print(events)
            with open(str(record_dir)+"/"+key+"_meta.json", "w") as writefile:
                json.dump(events, writefile, default=np_encoder)


