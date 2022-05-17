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

# Importing standard Neuron-Python libraries
from neuron import h
import matplotlib.pyplot as plt
import numpy as np

# On some mac, neuron complains about X11, so we disable it (from bash)
# > unset DISPLAY (from Bash, or the following NEURON code)
import os
if 'DISPLAY' in os.environ:
    del os.environ['DISPLAY']


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


# Prepare for extracting numerical data from the simulation --------------------
# Declaring variable(s) to store data
recordings = {}
recordings['time'] = neuron.h.Vector()
recordings['soma(0.5)'] = neuron.h.Vector()
recordings['stim(0.5)'] = neuron.h.Vector()

# Data structures are "attached" to NEURON's internals
recordings['time'].record(neuron.h._ref_t, 0.1)                     # 0.1
recordings['soma(0.5)'].record(cell.soma[0](0.5)._ref_v, 0.1)
recordings['stim(0.5)'].record(stim._ref_i, 0.1)

# Prepare to "dump" on disk all Vm from the dendrites' sections
dend_vs = []
for sec in cell.dend:
    dend_vs.append(h.Vector())
    dend_vs[-1].record(sec(0.5)._ref_v, 0.1)

axon_vs = []
for sec in cell.axon:
    axon_vs.append(h.Vector())
    axon_vs[-1].record(sec(0.5)._ref_v, 0.1)


h.run()         # RUN THE SIMULATION !!!!!!!!!!!!!

# Plotting the results ---------------------------------------------------------
# Let's convert the data to numpy arrays...
time = np.array(recordings['time'])
soma_v = np.array(recordings['soma(0.5)'])
curr_stim = np.array(recordings['stim(0.5)'])

plt.figure(0)
plt.rcParams['figure.figsize'] = [5, 5]
plt.plot(time, soma_v, label='soma response',
         color="blue", lw=1, alpha=0.8)
plt.plot(time, 100*curr_stim, label='stimulus',
         color="red", lw=1, alpha=0.8)

plt.xlabel('time [ms]', fontsize=15)
plt.ylabel('V$_m$ [mV]', fontsize=15)
plt.minorticks_on()
plt.show(block=False)
plt.savefig('./results/soma_response.png')
# ---------------------------------------------------------

plt.figure(1)
plt.rcParams['figure.figsize'] = [5, 5]
# for vvv in list(enumerate(dend_vs))[::3]:
for vvv in list(enumerate(dend_vs)):
    plt.plot(time, np.array(vvv[-1]), label='dend_' + str(vvv[0]))

plt.xlabel('time [ms]', fontsize=15)
plt.ylabel('V$_m$ [mV]', fontsize=15)
plt.minorticks_on()
plt.show(block=False)
plt.savefig('./results/dendrites_response.png')
# ---------------------------------------------------------

plt.figure(2)
plt.rcParams['figure.figsize'] = [5, 5]
# for vvv in list(enumerate(axon_vs))[::10]:
for vvv in list(enumerate(axon_vs)):
    plt.plot(time, np.array(vvv[-1]), label='dend_' + str(vvv[0]))

plt.xlim([104, 114])
plt.xlabel('time [ms]', fontsize=15)
plt.ylabel('V$_m$ [mV]', fontsize=15)
plt.minorticks_on()
plt.show(block=False)
plt.savefig('./results/axon_response.png')
# ---------------------------------------------------------
