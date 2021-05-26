'''
This is the netParams.py file for the NetPyNE Project by L Medlock & M Mazar
'''

from netpyne import specs, sim
from neuron import h, gui
import matplotlib
import numpy as np
import os
import sys
sys.path.insert(0, 'cells')  # adding path to cells dir
import ais_variables

try:
    from __main__ import cfg
except:
    from cfg_test import cfg

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

# Excitatory Spinal Neurons (Tonic Spiking)
netParams.cellParams['E_tonic'] = {'secs': {'soma': {}}}
netParams.cellParams['E_tonic']['secs']['soma']['geom'] = {
    'diam': 19.55,
    'L'   : 19.55,
    'Ra'  : 1000,
    'nseg': 1
}
netParams.cellParams['E_tonic']['secs']['soma']['ions'] = {
    'k': {'e': -88.0},
    'na': {'e': 55.0},
}
netParams.cellParams['E_tonic']['secs']['soma']['mechs'] = {
    'leak':   {'g': 0.00002},
    'kv1':    {'gkbar': 0.00006},
    'kv2':    {'gkbar': 0.002},
    'kv3':    {'gkbar': 0.00005},
    'kv4':    {'gkbar': 0.0001},
    'nav1p1': {'gnabar': 0},
    'nav1p6': {'gnabar': 0},
    'nav1p7': {'gnabar': 0.03},
    'nav1p8': {'gnabar': 0.04},
}

###############################################################################
# POPULATION PARAMETERS
###############################################################################
# Tonic Pop (Inhibitory)
netParams.popParams['I_tonic'] = {'cellType': 'IHB',
                                    'numCells': 1,
                                    'cellModel': 'TONIC',
                                    'xRange' : [150,350], 
                                    'yRange' : [150,350], 
                                    'zRange' : [300,400] }

# Delayed Pop (Excitatory)
netParams.popParams['E_delay'] = {'cellType':'E_delay', 
                                  'numCells': 1, 
                                  'cellModel': 'E_delay',
                                  'xRange' : [150,350], 
                                  'yRange' : [150,350], 
                                  'zRange' : [300,400] }

# Single Spike Pop (Excitatory)
netParams.popParams['E_single'] = {'cellType':'E_single', 
                                  'numCells': 1, 
                                  'cellModel': 'E_single',
                                  'xRange' : [150,350], 
                                  'yRange' : [150,350], 
                                  'zRange' : [300,400] }

# Tonic Spike Pop (Excitatory)
netParams.popParams['E_tonic'] = {'cellType':'E_tonic', 
                                  'numCells': 1, 
                                  'cellModel': 'E_tonic',
                                  'xRange' : [150,350], 
                                  'yRange' : [150,350], 
                                  'zRange' : [300,400]}

# PANs 
netParams.popParams['PAN'] = {'cellType':'E_tonic', 
                                  'gridSpacing': 50,
                                  'xRange' : [0,200], 
                                  'yRange' : [0,200], 
                                  'zRange' : [0,0], 
                                  'cellModel': 'E_tonic'}

###############################################################################
# SYNAPTIC PARAMETERS
###############################################################################

## Synaptic mechanism parameters
netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 5.0, 'e': 0}  
netParams.synMechParams['GABA'] = {'mod': 'Exp2Syn', 'tau1': 1.0, 'tau2': 20.0, 'e': -80}  

###############################################################################
# CONNECTIVITY PARAMETERS
###############################################################################



netParams.connParams['PAN->E_delay'] = {    #  PAN --> E_delay
        'preConds': {'pop': 'PAN'},
        'postConds': {'pop': 'E_delay'},
        'sec': 'soma',                  # target postsyn section
        'synMech': 'AMPA',              # target synaptic mechanism
        'weight': cfg.z[testX,testY],   # synaptic weight
        'prob': 0.1,                    # synaptic weight
        'delay': 10,                    # transmission delay (ms)
        }


###############################################################################
# STIMULATION PARAMETERS
###############################################################################
# Stimulation Sources:                                  
netParams.stimSourceParams['IClamp'] = {'type': 'IClamp', 
                                       'del': 500,
                                       'dur': 1000,
                                       'amp': 0.08}

netParams.stimSourceParams['Mech'] = {'type': 'IClamp', 
                                       'del': 500,
                                       'dur': 500,
                                       'amp': 0.01}

# Stimulation Targets:                                     
# netParams.stimTargetParams['Input->I_tonic'] = {'source': 'IClamp',  # IClamp --> I_tonic
#                                                   'sec':'soma',
#                                                   'loc': ais_variables.RECORDING_LOCATION,
#                                                   'conds': {'pop':'I_tonic'}}

# netParams.stimTargetParams['Input->E_delay'] = {'source': 'IClamp',  # IClamp --> E_delay
#                                                   'sec':'soma',
#                                                   'loc': ais_variables.RECORDING_LOCATION,
#                                                   'conds': {'pop':'E_delay'}}

# netParams.stimTargetParams['Input->E_single'] = {'source': 'IClamp',  # IClamp --> E_single
#                                                   'sec':'soma',
#                                                   'loc': ais_variables.RECORDING_LOCATION,
#                                                   'conds': {'pop':'E_single'}}

# netParams.stimTargetParams['Input->E_tonic'] = {'source': 'IClamp',  # IClamp --> E_tonic
#                                                   'sec':'soma',
#                                                   'loc': ais_variables.RECORDING_LOCATION,
#                                                   'conds': {'pop':'E_tonic'}}

netParams.stimTargetParams['Input->PAN'] = {'source': 'Mech',  # Mech --> PAN
                                                  'sec':'soma',
                                                  'loc': ais_variables.RECORDING_LOCATION,
                                                  'conds': {'pop':'PAN'}}



