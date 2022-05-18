#
# Helper script - Michele GIUGLIANO
#

def attach_recor


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
