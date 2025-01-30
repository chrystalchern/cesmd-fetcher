import numpy as np

import quakeio # read earthquake data, e.g. from CGS V2 files
# V2: time vs. accel/veloc/displ
# V3: frequency vs. amplitude
# bridge folder (CE.....)
# --> earthquake zip (.zip)
# ------> channel data (.v2)

from pathlib import Path # represent paths from strings

# TODO: Define a function that gives me an earthquake event
# based on a bridge code (e.g. "CE13705") and a event index (e.g. 0, 1, ...)
def get_earthquake(code, index):
    # if code = "CE13705", I want "CSMIP/bridges/motions_original/CE13705"
    # TODO: use an f-string to make the path to the folder based on the variable `code`
    path_to_bridge_folder = Path("CSMIP/bridges/motions_original/CE13705/anza_12jun2005_CE13705P.ZIP") # get the bridge folder
    print(path_to_bridge_folder) # debugging code. I should expect a path object with the correct path
    # TODO: use glob, a function of Path, to give me a list of all the earthquakes in the folder
    earthquakes = path_to_bridge_folder.glob("...")
    # TODO: get the earthquake based on its index (if index=0, eq = the first item in earthquakes)
    eq = ...
    print(eq) # debugging code. I should expect a path to a .zip file here.
    # event is something that was read by quakeio. read and return the event
    event = quakeio.read(eq)
    return event

# Define a function that gives me a numpy array of acceleration data
# based on the earthquake event and the channel number (e.g. 7)
def get_accel(event, channel):
    """
    a function that gives me a numpy array of acceleration data
    based on the earthquake event and the channel number (e.g. 7)
    """
    chan_data = event.match("l", station_channel=f"{channel}") 
    if chan_data is not None:
        # extract the acceleration attribute from chan_data
        data = np.asarray(getattr(chan_data,'accel').data)
    return data

# Test the functions
accel = get_accel(get_earthquake("CE89324",3), 7)
print(accel)

