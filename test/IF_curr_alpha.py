"""
Simple test to compare iaf_neuron in NEST with StandardIF in NEURON.

Andrew Davison, UNIC, CNRS
May 2006

$Id$
"""

import sys

if hasattr(sys,"argv"):     # run using python
    simulator = sys.argv[-1]
else:
    simulator = "oldneuron"    # run using nrngui -python


exec("from pyNN.%s import *" % simulator)


setup(timestep=0.01,min_delay=0.01,max_delay=4.0)

ifcell = create(IF_curr_alpha, {'i_offset' : 0.1,   'tau_refrac' : 3.0,
                                'v_thresh' : -51.0, 'tau_syn_E'  : 2.0,
                                'tau_syn_I': 5.0,   'v_reset'    : -70.0, 
                                'v_init'   : -54.2})

spike_sourceE = create(SpikeSourceArray, {'spike_times': [float(i) for i in range(5,105,10)]})
spike_sourceI = create(SpikeSourceArray, {'spike_times': [float(i) for i in range(100,255,10)]})
 
connE = connect(spike_sourceE, ifcell, weight=1.5, synapse_type='excitatory', delay=2.0)
connI = connect(spike_sourceI, ifcell, weight=-1.5, synapse_type='inhibitory', delay=4.0)
    
record_v(ifcell,"IF_curr_alpha_%s.v" % simulator)
run(200.0)

end()
