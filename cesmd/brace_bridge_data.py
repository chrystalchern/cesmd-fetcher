# %% [markdown]
# ## Get zip files of bridge records using cesmd fetcher

# %%
from bridges import BRIDGES
import search
from pathlib import Path

# %%
update_files = True

# %%
out_dir = Path("CSMIP/bridges/motions_original")
if not out_dir.exists():
    out_dir.mkdir()

# %%
if update_files:
    for bridge_key in BRIDGES.keys():
        cesmd = BRIDGES[bridge_key]["cesmd"]
        print(BRIDGES[bridge_key]["name"])
        bridge_directory = out_dir/cesmd
        if not bridge_directory.exists():
            bridge_directory.mkdir()
        search.get_records(str(out_dir)+"/"+cesmd, "cchern@berkeley.edu", station_code=cesmd, process_level="processed", include_inactive=True)

# %%
import glob
from zipfile import ZipFile

# %%
extract_new = True

# %%
if extract_new:
    for cesmd_zip in glob.glob(str(out_dir)+"/*.[zZ][]iI][pP]"):
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

    for bridge_key in BRIDGES.keys():
        cesmd = BRIDGES[bridge_key]["cesmd"]
        for record in glob.glob(str(out_dir)+"/"+cesmd+"/*/*/*.[zZ][iI][pP]"):
            os.replace(record, str(out_dir)+"/"+cesmd+"/"+os.path.basename(record))
    
    delete_empty_folders(".")
    

# %%
summarize_new = True

# %%
if summarize_new:
    import quakeio
    import json
    for bridge_key in BRIDGES.keys():  
        cesmd = BRIDGES[bridge_key]["cesmd"] 
        events = []
        for file in glob.glob(str(out_dir)+"/"+cesmd+"/*.[zZ][iI][pP]"):
            print(f"Reading {file}")
            try:
                events.append(
                    quakeio.read(file, summarize=True).serialize(serialize_data=False)
                )
            except:
                print(f"failed to read {file}")
        with open(str(out_dir)+"/"+cesmd+"_meta.json", "w") as writefile:
            json.dump(events, writefile)

# %%
bridge_names = [{'cesmd': value['cesmd'], 'name': value['name']} for value in BRIDGES.values()]

# %%
with open(str(out_dir)+"/bridge_names.json", "w") as writefile:
    json.dump(bridge_names, writefile)

# %%
for bridge_key in BRIDGES.keys():  
    cesmd = BRIDGES[bridge_key]["cesmd"] 
    print(f"""
	<div id='{cesmd}_PeakAccelHistDiv' style="width:800px;height:400px;"></div>
	<div id='{cesmd}_PeakAccelPlotDiv' style="width:800px;height:400px;"></div>""", end="")

# %%



