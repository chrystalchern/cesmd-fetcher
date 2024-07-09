DAMP_R1 = 0.01
THREADS = 8
SS_DEC = 1
PERIOD_BAND = [0.1, 8]
import sys
PYTHON = sys.executable

BUILDINGS = {
    "CE24602": {
        "cesmd": "CE24602",
        "name":  "Los Angeles - 52-story Office Bldg",
        "predictors": [
            {
                "name": "SRIM_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [2,5],
                           "outputs": [8,10,13,16,19]}
            },
            {
                "name": "SRIM_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [3,6],
                           "outputs": [9,11,14,17,20]}
            },
            {
                "name": "FDD_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [8,10,13,16,19]}
            },
            {
                "name": "FDD_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [9,11,14,17,20]}
            },
            {
                "name": "FSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [2],
                           "outputs": [19]}
            },
            {
                "name": "FSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [3],
                           "outputs": [20]}
            },
            {
                "name": "RSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [2],
                           "outputs": [19]}
            },
            {
                "name": "RSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [3],
                           "outputs": [20]}
            },
        ]
    },
    "CE24386": {
        "cesmd": "CE24386",
        "name":  "Van Nuys - 7-story Hotel",
        "predictors": [
            {
                "name": "SRIM_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [1,13,14],
                           "outputs": [7,8,6,4,2,3]}
            },
            {
                "name": "SRIM_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [16],
                           "outputs": [12,11,10,9]}
            },
            {
                "name": "FDD_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [7,8,6,4,2,3]}
            },
            {
                "name": "FDD_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [12,11,10,9]}
            },
            {
                "name": "FSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [14],
                           "outputs": [3]}
            },
            {
                "name": "FSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [16],
                           "outputs": [9]}
            },
            {
                "name": "RSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [14],
                           "outputs": [3]}
            },
            {
                "name": "RSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [16],
                           "outputs": [9]}
            },
        ]
    },
    "CE58483": {
        "cesmd": "CE58483",
        "name":  "Oakland - 24-story Residential Bldg.",
        "predictors": [
            {
                "name": "SRIM_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [16,11],
                           "outputs": [9,10,8,7,5,6]}
            },
            {
                "name": "SRIM_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [14],
                           "outputs": [13,12]}
            },
            {
                "name": "FDD_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [9,10,8,7,5,6]}
            },
            {
                "name": "FDD_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [13,12]}
            },
            {
                "name": "FSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [16],
                           "outputs": [5]}
            },
            {
                "name": "FSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [14],
                           "outputs": [12]}
            },
            {
                "name": "RSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [16],
                           "outputs": [5]}
            },
            {
                "name": "RSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [14],
                           "outputs": [12]}
            },
        ]
    },
    "CE24579": {
        "cesmd": "CE24579",
        "name":  "Los Angeles - 9-story Office Bldg",
        "predictors": [
            {
                "name": "SRIM_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [5,4],
                           "outputs": [9,11,10,16,14]}
            },
            {
                "name": "SRIM_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [7,6],
                           "outputs": [8,13,12,18,17]}
            },
            {
                "name": "FDD_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [9,11,10,16,14]}
            },
            {
                "name": "FDD_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [8,13,12,18,17]}
            },
            {
                "name": "FSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [5],
                           "outputs": [16]}
            },
            {
                "name": "FSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [6],
                           "outputs": [17]}
            },
            {
                "name": "RSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [5],
                           "outputs": [16]}
            },
            {
                "name": "RSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [6],
                           "outputs": [17]}
            },
        ]
    },
    "CE24322": {
        "cesmd": "CE24322",
        "name":  "Sherman Oaks - 13-story Commercial Bldg",
        "predictors": [
            {
                "name": "SRIM_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [15,11,12],
                           "outputs": [8,9,5,6,2,3]}
            },
            {
                "name": "SRIM_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [13,10],
                           "outputs": [7,4,1]}
            },
            {
                "name": "FDD_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [8,9,5,6,2,3]}
            },
            {
                "name": "FDD_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [7,4,1]}
            },
            {
                "name": "FSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [15],
                           "outputs": [2]}
            },
            {
                "name": "FSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [13],
                           "outputs": [1]}
            },
            {
                "name": "RSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [15],
                           "outputs": [2]}
            },
            {
                "name": "RSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [13],
                           "outputs": [1]}
            },
        ]
    },
    "CE23634": {
        "cesmd": "CE23634",
        "name":  "San Bernardino - 5-story Hospital",
        "predictors": [
            {
                "name": "SRIM_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [3],
                           "outputs": [7,11]}
            },
            {
                "name": "SRIM_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [2],
                           "outputs": [5,9]}
            },
            {
                "name": "FDD_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [7,11]}
            },
            {
                "name": "FDD_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [5,9]}
            },
            {
                "name": "FSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [3],
                           "outputs": [11]}
            },
            {
                "name": "FSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [2],
                           "outputs": [9]}
            },
            {
                "name": "RSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [3],
                           "outputs": [11]}
            },
            {
                "name": "RSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [2],
                           "outputs": [9]}
            },
        ]
    },
    "CE89494": {
        "cesmd": "CE89494",
        "name":  "Eureka - 5-story Residential Bldg.",
        "predictors": [
            {
                "name": "SRIM_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [13],
                           "outputs": [10,9]}
            },
            {
                "name": "SRIM_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [2],
                           "outputs": [3,4]}
            },
            {
                "name": "FDD_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [10,9]}
            },
            {
                "name": "FDD_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [3,4]}
            },
            {
                "name": "FSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [13],
                           "outputs": [9]}
            },
            {
                "name": "FSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [2],
                           "outputs": [4]}
            },
            {
                "name": "RSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [13],
                           "outputs": [9]}
            },
            {
                "name": "RSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [2],
                           "outputs": [4]}
            },
        ]
    },
    "CE58196": {
        "cesmd": "CE58196",
        "name":  "Berkeley - 5-story Parking Structure",
        "predictors": [
            {
                "name": "SRIM_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [2],
                           "outputs": [8,11,16]}
            },
            {
                "name": "SRIM_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "srim"],
                "config": {"decimate": SS_DEC,
                           "order": 12,
                           "horizon": 100,
                           "inputs": [4],
                           "outputs": [6,10,13]}
            },
            {
                "name": "FDD_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [8,11,16]}
            },
            {
                "name": "FDD_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fdd"],
                "config": {"period_band": PERIOD_BAND,
                           "outputs": [6,10,13]}
            },
            {
                "name": "FSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [2],
                           "outputs": [16]}
            },
            {
                "name": "FSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "fourier"],
                "config": {"period_band": PERIOD_BAND,
                           "inputs": [4],
                           "outputs": [13]}
            },
            {
                "name": "RSTF_H1",
                "description": "1st horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [2],
                           "outputs": [16]}
            },
            {
                "name": "RSTF_H2",
                "description": "2nd horizontal configuration.",
                "metrics": ["SPECTRAL_SHIFT_IDENTIFICATION"],
                "entry_point": [PYTHON, "-m", "mdof", "response"],
                "config": {"period_band": PERIOD_BAND,
                           "threads": THREADS,
                           "damping": DAMP_R1,
                           "inputs": [4],
                           "outputs": [13]}
            },
        ]
    },
}


