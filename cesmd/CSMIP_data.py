"""
Get zip files of station records using cesmd fetcher
"""

import search
from pathlib import Path
import os
import glob
from zipfile import ZipFile

STATION_TYPE = "buildings"  # "bridges", "buildings"

OUT_DIR = Path(f"CSMIP/{STATION_TYPE}")
Path.mkdir(OUT_DIR, exist_ok=True)

UPDATE_FILES = True
MOVE_NEW = True
EXTRACT_NEW = True
SUMMARIZE_NEW = True
ACCEL_PLOT_HTML = False

if STATION_TYPE == "bridges":
    from bridges import BRIDGES as STATIONS
elif STATION_TYPE == "buildings":
    from buildings import BUILDINGS as STATIONS

if __name__ == "__main__":

    if UPDATE_FILES:
        for station_key in STATIONS.keys():
            cesmd = STATIONS[station_key]["cesmd"]
            print(f"{STATIONS[station_key]["name"]} ({cesmd})")
            search.get_records(str(OUT_DIR/cesmd), "cchern@berkeley.edu", station_code=cesmd, process_level="processed", include_inactive=True)
            # Example: specific station
            # search.get_records(
            #     output="out/CE89324",
            #     email="cchern@berkeley.edu",
            #     station_code="CE89324"
            #     process_level="processed",
            #     include_inactive=True,
            # )
            # Example: specific event
            # search.get_records(
            #     output="northridge_directory",
            #     email="cchern@berkeley.edu",
            #     return_type="dataset",
            #     process_level="processed",
            #     group_by="station",
            #     eventid="ci3144585",
            #     unpack=True,
            # )


    # Move records to top levels of unzipped folders
    if EXTRACT_NEW:
        for cesmd_zip in glob.glob(str(OUT_DIR)+"/*.[zZ][]iI][pP]"):
            newdir = cesmd_zip[:-4]
            with ZipFile(cesmd_zip) as zObject: 
                zObject.extractall(path="./"+newdir)
    if MOVE_NEW:
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

        for station_key in STATIONS.keys():
            cesmd = STATIONS[station_key]["cesmd"]
            for record in glob.glob(str(OUT_DIR)+"/"+cesmd+"/*/*/*.[zZ][iI][pP]"):
                os.replace(record, str(OUT_DIR)+"/"+cesmd+"/"+os.path.basename(record))
        
        delete_empty_folders(".")

    if SUMMARIZE_NEW:
        import quakeio
        import json
        for station_key in STATIONS.keys():  
            cesmd = STATIONS[station_key]["cesmd"]
            events = []
            for file in glob.glob(str(OUT_DIR)+"/"+cesmd+"/*.[zZ][iI][pP]"):
                print(f"Reading {file}")
                try:
                    events.append(
                        quakeio.read(file, summarize=True).serialize(serialize_data=False)
                    )
                except:
                    print(f"failed to read {file}")
            with open(str(OUT_DIR)+"/"+cesmd+"_meta.json", "w") as writefile:
                json.dump(events, writefile)


    station_names = [{'cesmd': value["cesmd"], 'name': value["name"]} for value in STATIONS.values()]
    with open(str(OUT_DIR)+f"/{STATION_TYPE}_names.json", "w") as writefile:
        json.dump(station_names, writefile)


    if ACCEL_PLOT_HTML:
        # Don't worry about this; it's for making webpages of plots of station accelerations
        for station_key in STATIONS.keys():  
            cesmd = STATIONS[station_key]["cesmd"]
            print(f"""
            <div id='{cesmd}_PeakAccelHistDiv' style="width:800px;height:400px;"></div>
            <div id='{cesmd}_PeakAccelPlotDiv' style="width:800px;height:400px;"></div>""", end="")
