# - clean names
# - add descriptions

r = 12
no=190
DAMP_R1 = 0.01
THREADS = 8
LINEAR_METRICS = ["PEAK_ACCEL", "PEAK_DRIFT", "ACC_RESPONSE_HISTORY"]
NONLINEAR_METRICS = ["COLUMN_STRAIN_STATES"]
SS_DEC = 1
PERIOD_BAND = [0.1, 8]
import sys
PYTHON = sys.executable

BRIDGES = {
    "CE13705": {
       "cesmd":  "CE13705", 
       "calid": "56-0586G (08-RIV-15-R41.57)",
       "name": "Corona - I15/Hwy91 Interchange Bridge",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [3], "outputs": [9]},  # Only 2 events
           },
           {
               "name": "Longitudinal", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [2], "outputs": [8]},  # Only 2 events
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "3", "outputs": "9"},
           },
           {
               "name": "F2", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "2", "outputs": "8"},
           },
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "3", "outputs": "9"},
           },
           {
               "name": "R2", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "2", "outputs": "8"},
           }
        ]
    },
    "CE14406": {
       "cesmd":  "CE14406", 
       "calid": "53-1471 (07-LA-47-0.86)",
       "name": "Los Angeles - Vincent Thomas Bridge",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [1,9,24], "outputs": [2,5,7]},
           },
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "reponse"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "24", "outputs": "3"},
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "24", "outputs": "3"},
           },
        #    {
        #        "name": "S2", "description": "Transverse with dense sensor configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
        #        "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [1,9,24], "outputs": [2,4,5,6,7]},
        #    },
           {
               "name": "Vertical", "description": "Vertical Configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [14,19,26], "outputs": [16,18,22]},
           },
        ]
    },
    "CE24704": {
       "cesmd":  "CE24704", 
       "calid": "53-2791 (07-LA-10-8.8)",
       "name": "Los Angeles - I10/La Cienega Bridge",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [10], "outputs": [5,8,12]},
           },
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "10", "outputs": "8"},
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "10", "outputs": "8"},
           },
        ]
    },
    "CE24706": {
       "cesmd":  "CE24706", 
       "calid": "53-1794 (07-LA-14-R57.37)",
       "name": "Palmdale - Hwy 14/Barrel Springs Bridge",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [11], "outputs": [6,8,9]},
           },
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "11", "outputs": "9"},
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "11", "outputs": "9"},
           }
        ]
    },
    "CE24775": {
       "cesmd":  "CE24775", 
       "calid": "50-0271 (06-KER-5-4.1)",
       "name": "Grapevine - I5/Lebec Rd Bridge",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration._deck", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [14], "outputs": [6,9,15]},
           },
           {
               "name": "R1", "description": "Transverse configuration._deck", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "14", "outputs": "9"},
           },
           {
               "name": "F1", "description": "Transverse configuration._deck", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "14", "outputs": "9"},
           },
        #    {
        #        "name": "S2", "description": "Transverse configuration._center_wall", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
        #        "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [14], "outputs": [12,9]},
        #    }
        ]
    },
    "CE47315": {
       "cesmd":  "CE47315", 
       "calid": "43-0031E (05-SBT-156-0.00)",
       "name": "San Juan Bautista - Hwy 101/156 Overpass",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [6], "outputs": [11,8]},
           },
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "6", "outputs": "11"},
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "6", "outputs": "11"},
           },
        #    {
        #        "name": "S2", "description": "Transverse configuration._dense", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
        #        "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [6], "outputs": [13,11,8]},
        #    }
        ]
    },
    "CE68185 (Alfred Zampa Memorial Bridge) (Carquinez West, Southbound, Suspension)": {
       "cesmd":  "CE68185", 
       "calid": "28-0352L (04-SOL-80-0.01)",
       "name": "Vallejo - Carquinez/I80 West Bridge",
       "predictors": [
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "76", "outputs": "35"},
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "76", "outputs": "35"},
           },
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [72,56,22], "outputs": [51,39,35,29]},
           },
           {
               "name": "S2", "description": "Transverse with dense sensor configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [76,72,56,22,3], "outputs": [68,65,51,39,35,29,17,7]},
           },
           {
               "name": "Vertical", "description": "Vertical configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [75,71,55,21,2], "outputs": [63,64,37,38,32,33,27,28,5,6]},
           }
        ]
    },
    "CE68184 (Carquinez East, Northbound)": {
       "cesmd":  "CE68184", 
       "calid": "23-0015R (04-SOL-80-12.8)",
       "name": "Vallejo - Carquinez/I80 East Bridge",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [48,46,32,33], "outputs": [56,41,35,27,26,21,18,11]},
               "model_types": ["TRANSVERSE", "STATE_SPACE"]
           },
           {
               "name": "S2", "description": "Vertical configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [43,42,30,28], "outputs": [34,24,20,17,9]},
               "model_types": ["VERTICAL", "STATE_SPACE"]
           },
        ]
    },
    "CE79421": {
       "cesmd":  "CE79421", 
       "calid": "10-0299 (01-MEN-101-160.03)",
       "name": "Leggett - Hwy 101/Confusion Hill Bridge",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [7,14,20], "outputs": [2,4,8,11,17]},
               "model_types": ["TRANSVERSE", "STATE_SPACE"]
           },
           {
               "name": "Longitudinal", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [6,13,19], "outputs": [3,10]},
               "model_types": ["LONGITUDINAL", "STATE_SPACE"]
           },
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "14", "outputs": "8"},
               "model_types": ["TRANSVERSE", "RESPONSE_SPECTRUM"]
           },
           {
               "name": "R2", "description": "Longitudinal configuration at the southwest (Willits) side.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "6", "outputs": "3"},
               "model_types": ["LONGITUDINAL", "RESPONSE_SPECTRUM"]
           },
           {
               "name": "R3", "description": "Longitudinal configuration at the northeast (Garberville) side.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "13", "outputs": "10"},
               "model_types": ["LONGITUDINAL", "RESPONSE_SPECTRUM"]
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "14", "outputs": "8"},
               "model_types": ["TRANSVERSE", "FOURIER"]
           }
        ]
    },
    "CE89708": {
       "cesmd":  "CE89708", 
       "calid": "04-0170 (01-HUM-101-R92.99)",
       "name": "Arcata - Hwy 101/Murray Road Bridge",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [10], "outputs": [7,9,12]},
           },
           {
               "name": "Longitudinal", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [11], "outputs": [8]},
           },
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "10", "outputs": "9"},
           },
           {
               "name": "R2", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "11", "outputs": "8"},
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "10", "outputs": "9"},
           },
           {
               "name": "F2", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "11", "outputs": "8"},
           },
        ]
    },
    "CE89735": {
       "cesmd":  "CE89735", 
       "calid": "04-0229 (01-HUM-255-0.7)",
       "name": "Eureka - Middle Channel Bridge",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [12,16], "outputs": [10,14,3]},
           },
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "12", "outputs": "10"},
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "12", "outputs": "10"},
           }
        ]
    },
    "CE89736": {
       "cesmd":  "CE89736", 
       "calid": "04-0230 (01-HUM-255-0.2)",
       "name": "Eureka - Eureka Channel Bridge",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [7,3], "outputs": [9,21,19]},
           },
        #    {
        #        "name": "S2", "description": "Transverse with dense sensor configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
        #        "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [7,3], "outputs": [9,5,21,19]},
        #    },
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "7", "outputs": "9"},
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "7", "outputs": "9"},
           }
        ]
    },
    "CE89973": {
       "cesmd":  "CE89973", 
       "calid": "04-0016R (01-HUM-101-53.9)",
       "name": "Rio Dell - Hwy 101/Eel River Bridge",
       "Location": "40.5093 N, 124.1196 W",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [4,11,16], "outputs": [7,10,13,14,18]},
           },
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "11", "outputs": "13"},
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "11", "outputs": "13"},
           }
        ]
    },
    "ridgecrest": {
       "cesmd": "CE33742", 
       "calid": "50-0340 (09-KER-395-R25.08)",
       "name": "Ridgecrest - Hwy 395/Brown Road Bridge",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [4], "outputs": [6, 7, 9]},
           },
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "4", "outputs": "7"},
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "4", "outputs": "7"},
           }
        ]
    },
    "sylmar": {
        "cesmd": "CE24694",
        "calid": "53-2795F",
        "name": "Sylmar - I5/14 Interchange Bridge",
        "Location": "34.3349 N, 118.5084 W",
        "predictors": [
            {
                "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
                "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [10,18], "outputs": [7,8,12,14,27]},  # No events
            },
            # {
            #     "name": "S2", "description": "Transverse configuration._dense",
            #     "protocol": "",
            #     "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
            #     "entry_point": [PYTHON, "-m", "ssid", "srim"],
            #     "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [1,10,18,33], "outputs": [3,5,6,7,8,12,14,27,28,29,30]},
            # }
        ]
    },
    "capistrano": {
       "cesmd": "CE13795", 
       "calid": "55-0225 (07-ORA-5-6.62)",
       "name": "Capistrano Beach - I5/Via Calif. Bridge",
       "predictors": [
           {
               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [4], "outputs": [10, 7]},
           },
           {
               "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
               "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "4", "outputs": "10"},
           },
           {
               "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
               "config": {"period_band": PERIOD_BAND, "inputs": "4", "outputs": "10"},
           }
       ]
    },
    "meloland": {
        "cesmd": "CE01336",
        "calid": "58-0215",
        "Location": "32.7735 N, 115.4481 W",
        "name": "Hwy8/Meloland Overpass",
        "predictors": [
            {
                "name": "Transverse", "description": "Transverse configuration.",
                "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [2], "outputs": [5, 7, 9]},
                "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"]
            },
            {
                "name": "Longitudinal", "description": "Longitudinal configuration.",
                "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [4], "outputs": [15]},
                "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"]
            },
            {
                "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
                "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "2", "outputs": "7"},
            },
            {
                "name": "R2", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
                "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "4", "outputs": "15"},
            },
            {
                "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
                "config": {"period_band": PERIOD_BAND, "inputs": "2", "outputs": "7"},
            },
            {
                "name": "F2", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
                "config": {"period_band": PERIOD_BAND, "inputs": "4", "outputs": "15"},
            },
            # {
            #     "name": "S2", "description": "Transverse with sparse sensor configuration.",
            #     "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [2], "outputs": [7]},
            #     "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"]
            # },
        ]
    },
    "crowley": {
        "cesmd": "CE54730",
        "calid": "47-0048",
        "Location": "37.5733 N, 118.7390 W",
        "name": "Lake Crowley - Hwy 395 Bridge",
        "predictors": [
            {
                "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
                "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [4], "outputs": [6, 7, 9]}, 
            },
            {
                "name": "Longitudinal", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
                "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [5], "outputs": [8]}, 
            },
            {
                "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
                "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "4", "outputs": "7"},
            },
            {
                "name": "R2", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
                "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "5", "outputs": "8"},
            },
            {
                "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
                "config": {"period_band": PERIOD_BAND, "inputs": "4", "outputs": "7"},
            },
            {
                "name": "F2", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
                "config": {"period_band": PERIOD_BAND, "inputs": "5", "outputs": "8"},
            },
        ],
    },
    "CE89686": {
        "cesmd": "CE89686",
        "calid": "04-0228",
        "name": "Eureka - Samoa Channel Bridge",
        "predictors": [
            {
                "name": "Transverse", "description": "Transverse configuration.",
                "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [8,16], "outputs": [10,12,21]}, "protocol": "", "metrics": {"SPECTRAL_SHIFT_IDENTIFICATION"},"entry_point": {PYTHON, "_m", "ssid", "srim"}
            },  # Ch16 has 9 events but the rest have at least 11
            {
                "name": "S2", "description": "Transverse configuration at Pier 8.",
                "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [8], "outputs": [10,12]}, "protocol": "", "metrics": {"SPECTRAL_SHIFT_IDENTIFICATION"},"entry_point": {PYTHON, "_m", "ssid", "srim"}
            },
            {
                "name": "R1", "description": "Transverse configuration at Pier 8.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
                "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "8", "outputs": "10"},
            },
            {
                "name": "F1", "description": "Transverse configuration at Pier 8.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
                "config": {"period_band": PERIOD_BAND, "inputs": "8", "outputs": "10"},
            }
        ],
    },
    "painter": {
        "cesmd": "CE89324",
        "calid": "04-0236",
        "Location": "40.5031 N, 124.1009 W",
        "name": "Rio Dell - Hwy 101/Painter St. Overcrossing",
        "predictors": [
            {
                "name": "Transverse", "description": "Transverse configuration.",
                "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [17,3,20], "outputs": [9,7,4]}, "protocol": "", "metrics": {"SPECTRAL_SHIFT_IDENTIFICATION"},"entry_point": {PYTHON, "_m", "ssid", "srim"}
            },
            {
                "name": "Longitudinal", "description": "Longitudinal configuration.",  # Sensor 11 may not be far enough away from the substructure for this configuration to be meaningful.
                "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [18], "outputs": [11]}, "protocol": "", "metrics": {"SPECTRAL_SHIFT_IDENTIFICATION"},"entry_point": {PYTHON, "_m", "ssid", "srim"}
            },
            {
                "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
                "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "3", "outputs": "7"}, 
            },
            {
                "name": "R2", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
                "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "18", "outputs": "11"}, 
            },
            {
                "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
                "config": {"period_band": PERIOD_BAND, "inputs": "3", "outputs": "7"}, 
            },
            {
                "name": "F2", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
                "config": {"period_band": PERIOD_BAND, "inputs": "18", "outputs": "11"}, 
            }
        ],
    },
    "bernardino": {
        "cesmd": "CE23631",
        "calid": "54-0823G",
        "name": "San Bernardino - I10/215 Interchange",
        "Location": "34.0650 N, 117.2962 W",
        "predictors": [
            {
                "name": "Transverse", "description": "Transverse with sparse sensor configuration.",
                "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [24], "outputs": [11,19,20,25]}, "protocol": "", "metrics": {"SPECTRAL_SHIFT_IDENTIFICATION"},"entry_point": {PYTHON, "_m", "ssid", "srim"}
            },
            {
                "name": "S2", "description": "Transverse with dense sensor configuration.",
                "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [3,6,24], "outputs": [7,8,11,19,20,25,26,29,30,31,32,36]}, "protocol": "", "metrics": {"SPECTRAL_SHIFT_IDENTIFICATION"},"entry_point": {PYTHON, "_m", "ssid", "srim"}
            },
            {
                "name": "R1", "description": "Transverse with dense sensor configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
                "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "24", "outputs": "20"},
            },
            {
                "name": "F1", "description": "Transverse with dense sensor configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
                "config": {"period_band": PERIOD_BAND, "inputs": "24", "outputs": "20"},
            }
        ],
    },
    "hayward": {
        "digital_twin": True,
        "cesmd": "CE58658",
        "calid": "33-0214L",
        "Location": "37.6907 N, 122.0993 W",
        "name": "Hayward Hwy 580-238 Interchange",
        "accelerometers": {
            "ground_channels": [1, 2, 3, 6, 7, 17, 18, 24, 25],
            "bridge_channels": [11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23],
        },
        "predictors": [
            # {
            #     "name": f"Linear",
            #     "metrics": [*LINEAR_METRICS],
            #     "protocol": "BRACE2_CLI_PREDICTOR_V1","entry_point": [PYTHON, "-mCE58658", f"Procedures/linear.tcl"]
            # },
            {
                "name": f"OpenSees",
                "metrics": [*LINEAR_METRICS, *NONLINEAR_METRICS],
                "protocol": "BRACE2_CLI_PREDICTOR_V1","entry_point": [PYTHON, "-mCE58658", f"Procedures/nonlinear.tcl"],
                "publish": True
            },
#           {
#               "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
#               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [2,7,25,18], "outputs": [13,15,23,20]},
#               "publish": True
#           },
#           {
#               "name": "Longitudinal", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
#               "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [3, 6, 17], "outputs": [12, 14, 19]},
#               "publish": True
#           },
            # {
            #     "name": "R1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
            #     "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "25", "outputs": "23"},
            # },
            # {
            #     "name": "R2", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "response"],
            #     "config": {"threads": THREADS, "damping": DAMP_R1, "inputs": "3", "outputs": "12"},
            # },
            # {
            #     "name": "F1", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
            #     "config": {"period_band": PERIOD_BAND, "inputs": "25", "outputs": "23"},
            # },
            # {
            #     "name": "F2", "description": "Longitudinal configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "fourier"],
            #     "config": {"period_band": PERIOD_BAND, "inputs": "3", "outputs": "12"},
            # },
        ]
    },
    # "CE68682": {
    #     "cesmd": "CE68682", 
    #     "calid": "28-0153 (04-CC-68-25.04)"},

    # "CE58600": {
    #    "cesmd": "CE58600", 
    #    "calid": "34-0006 (04-SF-80-13.2)",
    #    "name": "Oakland - SF Bay Bridge/East: SAS",
    #    "predictors": [
    #        {
    #            "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"], "entry_point": [PYTHON, "-m", "ssid", "srim"],
    #            "config": {
    #                 "--decimate", SS_DEC, "--ss-size", 12, "--arx-order", 190, 
    #                 "--inputs", "[4,28,71]", "--outputs", "[9,33,51,71]"
    #             ],
    #        }
    #     ]
    # },
    # "CE58700": {
    #    "cesmd":  "CE58700", 
    #    "calid": "CE58700",
    #    "name": "San Francisco - Golden Gate Bridge",
    #    "predictors": [
    #        {
    #            "name": "Transverse", "description": "Transverse configuration._suspension", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
    #            "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [47,33,18,12], "outputs": [35,26,21]},  # Suspension bridge
    #        },
    #     #    {
    #     #        "name": "S2", "description": "Transverse configuration._suspension_dense",
    #     #        "protocol": "",
    #     #        "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
    #     #        "entry_point": [PYTHON, "-m", "ssid", "srim"],
    #     #        "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [47,33,18,12], "outputs": [42,35,26,21,14]},  # Suspension bridge
    #     #    },
    #     #    {
    #     #        "name": "S3", "description": "Transverse configuration._suspension_towers",
    #     #        "protocol": "",
    #     #        "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
    #     #        "entry_point": [PYTHON, "-m", "ssid", "srim"],
    #     #        "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [47,33,18,12], "outputs": [39,23]},  # Suspension bridge
    #     #    },
    #     #    {
    #     #        "name": "S4", "description": "Transverse configuration at the north viaduct.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
    #     #        "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [12,3], "outputs": [97,96,76]},  # North Viaduct
    #     #    },
    #         #    {
    #     #        "name": "S5", "description": "Transverse configuration at the south_viaduct.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
    #     #        "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [59,47], "outputs": [61,55,54,51]},  # South Viaduct
    #     #    },
    #     ]
    # },
    # "CE58601": {
    #    "cesmd":  "CE58601", 
    #    "calid": "34-0006 (04-SF-80-8.7)",
    #    "name": "Oakland - SF Bay Bridge/East: Skyway",
    #    "predictors": [
    #        {
    #            "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
    #            "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [4,9,14,20], "outputs": [43,44,45,51]},
    #        },
    #     #    {
    #     #        "name": "S2", "description": "Transverse with dense sensor configuration.",
    #     #        "protocol": "",
    #     #        "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
    #     #        "entry_point": [PYTHON, "-m", "ssid", "srim"],
    #     #        "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [4,9,14,20], "outputs": [42,43,44,45,48,51,56,62,65]},
    #     #    }
    #     ]
    # },
    # "CE58632": {
    #    "cesmd":  "CE58632", 
    #    "calid": "34-0003 (04-SF-80-5.6)",
    #    "name": "San Francisco - Bay Bridge/West",
    #    "predictors": [
    #        {
    #            "name": "Transverse", "description": "Transverse configuration.", "protocol": "", "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],"entry_point": [PYTHON, "-m", "ssid", "srim"],
    #            "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [1,7,16,33,50,55,70], "outputs": [5,10,20,22,28,40,47,52,61,58,65,68,73,77]},
    #        },
    #     #    {
    #     #        "name": "S2", "description": "Transverse configuration at the towers.",
    #     #        "protocol": "",
    #     #        "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
    #     #        "entry_point": [PYTHON, "-m", "ssid", "srim"],
    #     #        "config": {"decimate": SS_DEC, "order": 12, "horizon": 190, "inputs": [1,7,16,33,50,55,70], "outputs": [25,44,63,75]},
    #     #    }
    #     ]
    # },
}


