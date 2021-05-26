'''
This is the netParams.py file for the NetPyNE Project by L Medlock & M Mazar
'''

from netpyne import specs, sim
from neuron import h, gui
import matplotlib
import os
import sys
sys.path.insert(0, 'cells')  # adding path to cells dir
import ais_variables


# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

###############################################################################
# CELL PARAMETERS
###############################################################################
# Inhibitory Spinal Neurons (Tonic Spiking)
netParams.importCellParams(
        label='dh_tonic_interneuron',
        conds={'cellType': 'IHB', 'cellModel': 'TONIC'},
        fileName=('ais_model.py'),
        cellName='laminaNeuron',
        importSynMechs=False)

# Excitatory Spinal Neurons (Delayed Spiking)
netParams.cellParams['E_delay'] = {'secs': {'soma': {}}}
netParams.cellParams['E_delay']['secs']['soma']['geom'] = {
    'diam': 19.55,
    'L'   : 19.55,
    'Ra'  : 1000,
    'nseg': 1
}
netParams.cellParams['E_delay']['secs']['soma']['ions'] = {
    'k': {'e': -88.0},
    'na': {'e': 55.0},
}
netParams.cellParams['E_delay']['secs']['soma']['mechs'] = {
    'leak':   {'g': 0.00002},
    'kv1':    {'gkbar': 0.00006},
    'kv2':    {'gkbar': 0.002},
    'kv3':    {'gkbar': 0.00005},
    'kv4':    {'gkbar': 0.011},
    'nav1p1': {'gnabar': 0},
    'nav1p6': {'gnabar': 0},
    'nav1p7': {'gnabar': 0.03},
    'nav1p8': {'gnabar': 0.04},
}

# Excitatory Spinal Neurons (Single Spiking)
netParams.cellParams['E_single'] = {'secs': {'soma': {}}}
netParams.cellParams['E_single']['secs']['soma']['geom'] = {
    'diam': 30.90,
    'L'   : 30.90,
    'Ra'  : 1000,
    'nseg': 1
}
netParams.cellParams['E_single']['secs']['soma']['ions'] = {
    'k': {'e': -88.0},
    'na': {'e': 55.0},
}
netParams.cellParams['E_single']['secs']['soma']['mechs'] = {
    'leak':   {'g': 0.0001},
    'kv1':    {'gkbar': 0.006},
    'kv2':    {'gkbar': 0.012},
    'kv3':    {'gkbar': 0.004},
    'kv4':    {'gkbar': 0.0008},
    'nav1p1': {'gnabar': 0.008},
    'nav1p6': {'gnabar': 0.04},
    'nav1p7': {'gnabar': 0.005},
    'nav1p8': {'gnabar': 0},
}

###############################################################################
# POPULATION PARAMETERS
###############################################################################
# Tonic Pop (Inhibitory)
netParams.popParams['I_tonic'] = {'cellType': 'IHB',
                                    'numCells': 1,
                                    'cellModel': 'TONIC'}

# Delayed Pop (Excitatory)
netParams.popParams['E_delay'] = {'cellType':'E_delay', 
                                  'numCells': 1, 
                                  'cellModel': 'E_delay'}

# Single Spike Pop (Excitatory)
netParams.popParams['E_single'] = {'cellType':'E_single', 
                                  'numCells': 1, 
                                  'cellModel': 'E_single'}

###############################################################################
# STIMULATION PARAMETERS
###############################################################################
# Stimulation Sources:                                  
netParams.stimSourceParams['IClamp'] = {'type': 'IClamp', 
                                       'del': ais_variables.DELAY,
                                       'dur': ais_variables.DUR,
                                       'amp': 0.1}

# Stimulation Targets:                                     
netParams.stimTargetParams['Input->I_tonic'] = {'source': 'IClamp',  # IClamp --> I_tonic
                                                  'sec':'soma',
                                                  'loc': ais_variables.RECORDING_LOCATION,
                                                  'conds': {'pop':'I_tonic'}}

netParams.stimTargetParams['Input->E_delay'] = {'source': 'IClamp',  # IClamp --> E_delay
                                                  'sec':'soma',
                                                  'loc': ais_variables.RECORDING_LOCATION,
                                                  'conds': {'pop':'E_delay'}}

netParams.stimTargetParams['Input->E_single'] = {'source': 'IClamp',  # IClamp --> E_single
                                                  'sec':'soma',
                                                  'loc': ais_variables.RECORDING_LOCATION,
                                                  'conds': {'pop':'E_single'}}
