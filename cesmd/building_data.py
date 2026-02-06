# %% [markdown]
# ## Get zip files of building records using cesmd fetcher

# %%
import search
from pathlib import Path

# %%

print(search.__file__)


# %%
from buildings import BUILDINGS

building_dir = Path("CSMIP/buildings")
if not building_dir.exists():
    Path.mkdir(building_dir)

# %%
update_files = True

# %%
if update_files:
    for cesmd in BUILDINGS.keys():
        print(BUILDINGS[cesmd])
        search.get_records(str(building_dir)+"/"+cesmd, "cchern@berkeley.edu", station_code=cesmd, process_level="processed", include_inactive=True)

# %%
search.get_records(
    output="tmp_northridge",
    email="cchern@berkeley.edu",
    return_type="dataset",
    process_level="processed",
    group_by="station",
    eventid="ci3144585",
    unpack=True,
)


# %% [markdown]
# ## Move records to top levels of unzipped folders

# %%
import glob
from zipfile import ZipFile

# %%
extract_new = True

# %%
if extract_new:
    for cesmd_zip in glob.glob(str(building_dir)+"/*.zip"):
        newdir = cesmd_zip[:-4]
        with ZipFile(cesmd_zip) as zObject: 
            zObject.extractall(path="./"+newdir)

# %%
move_new = True

# %%
if move_new:
    import os

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

    for cesmd in BUILDINGS.keys():
        for record in glob.glob(str(building_dir)+"/"+cesmd+"/*/*/*.zip"):
            os.replace(record, str(building_dir)+"/"+cesmd+"/"+os.path.basename(record))
    
    delete_empty_folders(".")
    

# %%
summarize_new = True

# %%
if summarize_new:
    import quakeio
    import json
    for cesmd in BUILDINGS.keys():  
        events = []
        for file in glob.glob(str(building_dir)+"/"+cesmd+"/*.zip"):
            print(f"Reading {file}")
            try:
                events.append(
                    quakeio.read(file, summarize=True).serialize(serialize_data=False)
                )
            except:
                print(f"failed to read {file}")
        with open(str(building_dir)+"/"+cesmd+"_meta.json", "w") as writefile:
            json.dump(events, writefile)

# %%
building_names = [{'cesmd': cesmd, 'name': name} for cesmd,name in BUILDINGS.items()]

# %%
with open(str(building_dir)+"/building_names.json", "w") as writefile:
    json.dump(building_names, writefile)

# %%
# Don't worry about this; it's for making webpages of plots of building accelerations

for cesmd in BUILDINGS.keys():  
    print(f"""
    <div id='{cesmd}_PeakAccelHistDiv' style="width:800px;height:400px;"></div>
    <div id='{cesmd}_PeakAccelPlotDiv' style="width:800px;height:400px;"></div>""", end="")

# %%



