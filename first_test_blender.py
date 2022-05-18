#
# NeuronsReUnited - Thalamocortical neuron model simulations
#
# Trieste, May 16th 2022
# Michele GIUGLIANO, Nestor TIMONIDIS, Ludovica LIOTTI
#
# USAGE:  > python3 -i first_test.py
#

# COMPILE MECHANISMS FIRST! (from bash)
# > nrnivmodl ./mechanisms


# On some mac, neuron complains about X11, so we disable it (from bash)
# > unset DISPLAY (from Bash, or the following NEURON code)
import os
if 'DISPLAY' in os.environ:
    del os.environ['DISPLAY']


# Importing standard (Neuron-Python) libraries
from neuron import h
import matplotlib.pyplot as plt
import numpy as np

# Import blenderneuron library / activate NeuronPython - Blender interface
from blenderneuron import neuronstart


h.load_file("stdrun.hoc")       # Load standard tools
h.cvode_active(1)               # Activatevariable time step integration method

h.load_file("./templates/cNAD_ltb_MG.hoc")  # Load the model (template)

cell = h.cNAD_ltb_MG(           # Create a cell object (instance)
    "morphologies", "EP23HI-LPLC_shrinkcorrect_splicedlayers_pictures23rotated_correctedlayers1.swc")

# Let's create a (current-clamp) DC-step stimulus, at the soma
stim = h.IClamp(0.5, sec=cell.soma[0])
stim.delay = 50  # delay before onset [ms]
stim.dur = 30    # duration [ms] - was 50
stim.amp = 0.1   # amplitude [uA]


# Simulation parameters
h.t = 0                                      # Initial time, set to 0 [ms]
h.tstop = stim.delay + stim.dur + 100        # Stop time [ms]

h.v_init = -78                               # Initial membrane potential [mV]
h.celsius = 37                               # Temperature [degrees C]

# h.run()         # RUN THE SIMULATION !!!!!!!!!!!!!
