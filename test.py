import mdof.realize
import numpy as np

import quakeio # read earthquake data, e.g. from CGS V2 files
# V2: time vs. accel/veloc/displ
# V3: frequency vs. amplitude
# bridge folder (CE.....)
# --> earthquake zip (.zip)
# ------> channel data (.v2)

from pathlib import Path # represent paths from strings

# Define a function that gives me an earthquake event
# based on a bridge code (e.g. "CE13705") and an event index (e.g. 0, 1, ...)
def get_earthquake(code, index):
    # if code = "CE13705", I want "CSMIP/bridges/motions_original/CE13705"
    # use an f-string to make the path to the folder based on the variable `code`
    path_to_bridge_folder = Path(f"cesmd/CSMIP/bridges/motions_original/{code}") # get the bridge folder
    # use glob, a function of Path, to give me a list of all the earthquakes in the folder
    earthquakes = list(path_to_bridge_folder.glob("*.[zZ][iI][pP]"))
    # print(earthquakes)
    # TODO: get the earthquake based on its index (if index=0, eq = the first item in earthquakes)
    eq = earthquakes[index] if index < len(earthquakes) else None # get the path to earthquake zip file
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
        dt = getattr(chan_data,'accel')["time_step"]
    return data, dt

if __name__ == "__main__":
    # Test the functions
    event = get_earthquake("CE89324",3)
    accel, dt = get_accel(event, 7)

    import matplotlib.pyplot as plt
    # TODO: plot the acceleration. label the plot with the 
    # bridge code (CE89324), earthquake date, and channel number.
    # TODO: plot the acceleration data vs. time
    fig,ax = plt.subplots()
    ax.plot() 
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Acceleration (cm/s^2)")
    ax.set_title(f"CE89324, {event['event_date']}, channel 7")
    plt.show()

    # TODO: Get modes; for now just use Sensors 3 and 7; Want to loop through all the earthquakes; We have desired sensors for each bridge
    inputs, dt = get_accel(get_earthquake("CE89324",3), 3)
    outputs, dt = get_accel(get_earthquake("CE89324",3), 7)
    import mdof
    # https://chrystalchern.github.io/mdof/library/mdof.realize.html
    realization = mdof.realize.srim(inputs,outputs)
    # https://chrystalchern.github.io/mdof/library/mdof.modal.html
    modes = mdof.modal.system_modes(realization,dt)
    print(modes)
    
    # Care about frequencies and mode shapes
    # Different frequencies for different earthquakes, how do we find a normal condition based on those frequencies?
    # How do we compare the new frequencies from future earthquakes to the collection of the old frequencies we have?
    # Want to plot them (frequencies vs ..)
    # Maybe look at the first couple frequencies for different EQs to see if they are similar or have changed



