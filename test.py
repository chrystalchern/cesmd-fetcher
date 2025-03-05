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

    # Generate time array based on the time step (dt) and the number of data points
    time = [i * dt for i in range(len(accel))]

    # Plot the acceleration data vs. time
    fig, ax = plt.subplots()
    ax.plot(time, accel)  # Pass the time and acceleration data to plot
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Acceleration (cm/s^2)")
    ax.set_title(f"CE89324, {event['event_date']}, channel 7")
    plt.show()

### FINDING MODES ###

# Function to get all earthquakes for the bridge "CE89324"
def get_all_earthquakes(bridge_code):
    # Replace this with your actual function to retrieve all earthquakes
    # For example, return a list of earthquake indices or IDs
    return range(15)  # Example: Assume there are 15 earthquakes

def get_first_5_modes(modes_dict):
    # Convert the dictionary to a list of mode entries
    modes_list = list(modes_dict.items())
    
    # Sort modes by frequency (ascending order)
    sorted_modes = sorted(modes_list, key=lambda x: x[1]['freq'])
    
    # Extract the first 5 modes
    first_5_modes = sorted_modes[:5]
    
    return first_5_modes

# Main script
bridge_code = "CE89324"
input_channel = 3  # Sensor channel for inputs
output_channel = 7  # Sensor channel for outputs

# Get all earthquakes for the bridge
earthquake_indices = get_all_earthquakes(bridge_code)

# Initialize lists to store results for all earthquakes
all_frequencies = []  # Shape: [num_earthquakes, 3]
all_damping_ratios = []  # Shape: [num_earthquakes, 3]

# Loop through all earthquakes for bridge "CE89324"
for earthquake_index in earthquake_indices:
    # Get input/output data for this earthquake
    inputs, dt = get_accel(get_earthquake("CE89324", earthquake_index), 3)
    outputs, dt = get_accel(get_earthquake("CE89324", earthquake_index), 7)
    
    # Compute modal parameters
    realization = mdof.realize.srim(inputs, outputs)
    modes = mdof.modal.system_modes(realization, dt)
    print(modes)       # print(modes)

    # Extract first 5 modes (sorted by frequency)
    first_5_modes = get_first_5_modes(modes)
    
    # Store frequencies and damping ratios
    frequencies = [mode[1]['freq'] for mode in first_5_modes]
    damping_ratios = [mode[1]['damp'] for mode in first_5_modes]
    
    all_frequencies.append(frequencies)
    all_damping_ratios.append(damping_ratios)

import matplotlib.pyplot as plt

# Convert to numpy arrays
all_frequencies = np.array(all_frequencies)
all_damping_ratios = np.array(all_damping_ratios)

# Plot frequencies
fig,ax = plt.subplots(figsize=(12, 6))
fig_hist, ax_hist = plt.subplots(5, 1, figsize=(8, 12))
colors = ['skyblue', 'lightgreen', 'salmon', 'orange', 'purple']

for mode in range(5):
    ax.plot(
        earthquake_indices,
        all_frequencies[:, mode],
        marker='o',
        label=f"Mode {mode+1}"
    )
    ax_hist[mode].hist(
        all_frequencies[:, mode],
        bins=20,
        color=colors[mode],
        edgecolor=colors[mode],
        alpha=0.7,
        label=f"Mode {mode+1}"
    )
    
    ax_hist[mode].set_title(f"Mode {mode+1} Frequencies Histogram", fontsize=12, fontweight='bold')
    ax_hist[mode].set_xlabel("Frequency (Hz)", fontsize=8)
    ax_hist[mode].set_ylabel("Frequency Count", fontsize=8)
    ax_hist[mode].grid(True, linestyle='--', alpha=0.6, linewidth=0.5)

ax.set_xlabel("Earthquake Index")
ax.set_ylabel("Frequency (Hz)")
ax.set_title("First 5 Mode Frequencies Across Earthquakes")
ax.legend()
ax.grid()
fig.show()
fig.savefig('frequencies.png')
fig_hist.show()
fig_hist.savefig('frequencies_hist.png')
# Adjust layout
plt.tight_layout()
plt.show()

# Plot damping ratios
plt.figure(figsize=(12, 6))
for mode in range(5):
    plt.plot(
        earthquake_indices,
        all_damping_ratios[:, mode],
        marker='o',
        label=f"Mode {mode+1}"
    )
plt.xlabel("Earthquake Index")
plt.ylabel("Damping Ratio")
plt.title("First 5 Mode Damping Ratios Across Earthquakes")
plt.legend()
plt.grid()
plt.show()
plt.savefig('damping_ratios.png')
    
    # Care about frequencies and mode shapes
    # Different frequencies for different earthquakes, how do we find a normal condition based on those frequencies?
    # How do we compare the new frequencies from future earthquakes to the collection of the old frequencies we have?
    # Want to plot them (frequencies vs ..)
    # Maybe look at the first couple frequencies for different EQs to see if they are similar or have changed


## Questions:
# Negative damping ratios? What does that mean?
# The order of frequencies is not consistent?



## Paper: Why 0.2% off the true data?