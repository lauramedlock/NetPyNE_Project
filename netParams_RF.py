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
    from cfg_RF import cfg

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

netParams.defaultThreshold = 0.0

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

# PANs 
netParams.popParams['PAN'] = {'cellType':'E_delay', 
                                  'gridSpacing': 50,
                                  'xRange' : [0,400], 
                                  'yRange' : [0,200], 
                                  'zRange' : [0,0], 
                                  'cellModel': 'E_delay'}

# Delayed Pop (Excitatory)
netParams.popParams['E_delay'] = {'cellType':'E_delay', 
                                  'numCells': 2, 
                                  'cellModel': 'E_delay',
                                  'xRange' : [150,350], 
                                  'yRange' : [150,350], 
                                  'zRange' : [300,400] }

# # Single Spike Pop (Excitatory)
# netParams.popParams['E_single'] = {'cellType':'E_single', 
#                                   'numCells': 1, 
#                                   'cellModel': 'E_single',
#                                   'xRange' : [150,350], 
#                                   'yRange' : [150,350], 
#                                   'zRange' : [300,400] }

# # Tonic Spike Pop (Excitatory)
# netParams.popParams['E_tonic'] = {'cellType':'E_tonic', 
#                                   'numCells': 1, 
#                                   'cellModel': 'E_tonic',
#                                   'xRange' : [150,350], 
#                                   'yRange' : [150,350], 
#                                   'zRange' : [300,400]}

#Tonic Pop (Inhibitory)
netParams.popParams['I_tonic'] = {'cellType': 'IHB',
                                    'numCells': 2,
                                    'cellModel': 'TONIC',
                                    'xRange' : [150,350], 
                                    'yRange' : [150,350], 
                                    'zRange' : [300,400] }

###############################################################################
# SYNAPTIC PARAMETERS
###############################################################################

## Synaptic mechanism parameters
netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 1.0, 'e': 0}  
netParams.synMechParams['GABA'] = {'mod': 'Exp2Syn', 'tau1': 1.0, 'tau2': 20.0, 'e': -80}  

###############################################################################
# CONNECTIVITY PARAMETERS
###############################################################################
# Receptive Field Structure
netParams.centerRF1 = [6,11,16,7,12,17,8,13,18]
netParams.surrRF1 = [0,5,10,15,20,1,21,2,22,3,23,4,24]
netParams.allRF1 = np.arange(25)
netParams.RF1exc1 = np.ones(25, dtype='int8')
netParams.Pre2PostRF1 = []
netParams.Pre2PostRF1 = list(zip(netParams.allRF1, netParams.RF1exc1))

netParams.centerRF2 = [x+20 for x in netParams.centerRF1]
netParams.surrRF2 = [x+20 for x in netParams.surrRF1]
netParams.allRF2 = [x+20 for x in netParams.allRF1]
netParams.Pre2PostRF2 = []
netParams.RF1exc2 = np.zeros(25, dtype='int8')
netParams.Pre2PostRF2 = list(zip(netParams.allRF2, netParams.RF1exc2))

netParams.connParams['PAN->E_delay1'] = {    #  PAN --> E_delay1
        'preConds': {'pop':'PAN'},
        'postConds': {'pop':'E_delay'},
        'sec': 'soma',                  # target postsyn section
        'synMech': 'AMPA',              # target synaptic mechanism
        'weight': 'max(0,1.0 - ((1/100)* (((pre_x - 100)**2 + (pre_y - 100)**2)**0.5)))',                  # synaptic weight
        'prob': 0.05,                    # synaptic probability
        'delay': 10,                     # transmission delay (ms)
        'connList': netParams.Pre2PostRF1 # connection between specific neurons
        }

netParams.connParams['PAN->E_delay2'] = {    #  PAN --> E_delay2
        'preConds': {'pop':'PAN'},
        'postConds': {'pop':'E_delay'},
        'sec': 'soma',                  # target postsyn section
        'synMech': 'AMPA',              # target synaptic mechanism
        'weight': 'max(0,1.0 - ((1/100)*(((pre_x - 300)**2 + (pre_y - 100)**2)**0.5)))',                  # synaptic weight
        'prob': 0.05,                    # synaptic probability
        'delay': 10,                     # transmission delay (ms)
        'connList': netParams.Pre2PostRF2  # connection between specific neurons
        }

netParams.connParams['PAN->I_tonic1'] = {    #  PAN --> I_tonic1
        'preConds': {'pop': 'PAN'},
        'postConds': {'pop': 'I_tonic'},
        'sec': 'soma',                  # target postsyn section
        'synMech': 'AMPA',              # target synaptic mechanism
        'weight': 'max(0,0.1*(0.5 - ((1/300)* (((pre_x - 100)**2 + (pre_y - 100)**2)**0.5))))',                  # synaptic weight
        'prob': 0.05,                    # synaptic probability
        'delay': 10,                     # transmission delay (ms)
        'connList': netParams.Pre2PostRF1 # connection between specific neurons
        }

netParams.connParams['PAN->I_tonic2'] = {    #  PAN --> I_tonic1
        'preConds': {'pop': 'PAN'},
        'postConds': {'pop': 'I_tonic'},
        'sec': 'soma',                  # target postsyn section
        'synMech': 'AMPA',              # target synaptic mechanism
        'weight': 'max(0,0.1*(0.5 - ((1/300)* (((pre_x - 300)**2 + (pre_y - 100)**2)**0.5))))',                  # synaptic weight
        'prob': 0.05,                    # synaptic probability
        'delay': 10,                     # transmission delay (ms)
        'connList': netParams.Pre2PostRF2 # connection between specific neurons
        }

netParams.connParams['I_tonic->E_delay'] = {    #  I --> E
        'preConds': {'pop': 'I_tonic'},
        'postConds': {'pop': 'E_delay'},
        'sec': 'soma',                   # target postsyn section
        'synMech': 'GABA',               # target synaptic mechanism
        'weight': 0,                  # synaptic weight
        'prob': 0.1,                    # synaptic probability
        'delay': 10,                    # transmission delay (ms)
        'connList': [[0,0],[1,1]] # connection between specific neurons
        }


###############################################################################
# STIMULATION PARAMETERS
###############################################################################
# Stimulation Sources:                                  
# netParams.stimSourceParams['IClamp'] = {'type': 'IClamp', 
#                                        'del': 500,
#                                        'dur': 1000,
#                                        'amp': 0.08}

netParams.stimSourceParams['Mech'] = {'type': 'NetStim', 
                                        'rate' : 7,
                                        'start': 1,
                                        'noise': 0.5}

# netParams.stimSourceParams['Mech2'] = {'type': 'NetStim', 
#                                         'rate' : 10,
#                                         'start': 200,
#                                         'noise': 0.5}

# netParams.stimSourceParams['Mech3'] = {'type': 'NetStim', 
#                                         'rate' : 10,
#                                         'start': 400,
#                                         'noise': 0.5}

# netParams.stimSourceParams['Mech4'] = {'type': 'NetStim', 
#                                         'rate' : 10,
#                                         'start': 600,
#                                         'noise': 0.5}

# netParams.stimSourceParams['Mech5'] = {'type': 'NetStim', 
#                                         'rate' : 10,
#                                         'start': 800,
#                                         'noise': 0.5}

# netParams.stimSourceParams['Mech6'] = {'type': 'NetStim', 
#                                         'rate' : 10,
#                                         'start': 1000,
#                                         'noise': 0.5}

# netParams.stimSourceParams['Mech7'] = {'type': 'NetStim', 
#                                         'rate' : 10,
#                                         'start': 1200,
#                                         'noise': 0.5}

# netParams.stimSourceParams['Mech8'] = {'type': 'NetStim', 
#                                         'rate' : 10,
#                                         'start': 1400,
#                                         'noise': 0.5}

# netParams.stimSourceParams['Mech9'] = {'type': 'NetStim', 
#                                         'rate' : 10,
#                                         'start': 1600,
#                                         'noise': 0.5}


# Stimulation Targets:  
#----------------------- For Static Stimuli ---------------------------------------------#
netParams.stimTargetParams['Input->PAN'] = {'source': 'Mech',  # Mech --> PAN
                                                  'sec':'soma',
                                                  'loc': 0.5,
                                                  'weight': 0.5,
                                                  'delay' : 1,
                                                  'conds': {'pop':'PAN','cellList':[10,11,12,13,14]} }

#----------------------- For Dynamic Stimuli ---------------------------------------------#
# netParams.stimTargetParams['Input->PAN'] = {'source': 'Mech',  # Mech --> PAN
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'weight': 0.5,
#                                                   'delay' : 1,
#                                                   'conds': {'pop':'PAN','cellList': [0,1,2,3,4]}} 
                                                   
# netParams.stimTargetParams['Input2->PAN'] = {'source': 'Mech2',  # Mech --> PAN
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'weight': 0.5,
#                                                   'delay' : 1,
#                                                   'conds': {'pop':'PAN','cellList': [5,6,7,8,9]}} 

# netParams.stimTargetParams['Input3->PAN'] = {'source': 'Mech3',  # Mech --> PAN
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'weight': 0.5,
#                                                   'delay' : 1,
#                                                   'conds': {'pop':'PAN','cellList': [10,11,12,13,14]}} 

# netParams.stimTargetParams['Input4->PAN'] = {'source': 'Mech4',  # Mech --> PAN
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'weight': 0.5,
#                                                   'delay' : 1,
#                                                   'conds': {'pop':'PAN','cellList': [15,16,17,18,19]}} 

# netParams.stimTargetParams['Input5->PAN'] = {'source': 'Mech5',  # Mech --> PAN
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'weight': 0.5,
#                                                   'delay' : 1,
#                                                   'conds': {'pop':'PAN','cellList': [20,21,22,23,24]}} 

# netParams.stimTargetParams['Input6->PAN'] = {'source': 'Mech6',  # Mech --> PAN
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'weight': 0.5,
#                                                   'delay' : 1,
#                                                   'conds': {'pop':'PAN','cellList': [25,26,27,28,29]}}

# netParams.stimTargetParams['Input7->PAN'] = {'source': 'Mech7',  # Mech --> PAN
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'weight': 0.5,
#                                                   'delay' : 1,
#                                                   'conds': {'pop':'PAN','cellList': [30,31,32,33,34]}}

# netParams.stimTargetParams['Input8->PAN'] = {'source': 'Mech8',  # Mech --> PAN
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'weight': 0.5,
#                                                   'delay' : 1,
#                                                   'conds': {'pop':'PAN','cellList': [35,36,37,38,39]}}

# netParams.stimTargetParams['Input9->PAN'] = {'source': 'Mech9',  # Mech --> PAN
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'weight': 0.5,
#                                                   'delay' : 1,
#                                                   'conds': {'pop':'PAN','cellList': [40,41,42,43,44]}}
                                                   





