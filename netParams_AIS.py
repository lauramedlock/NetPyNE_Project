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

try:
    from __main__ import cfg
except:
    from cfg import cfg


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
netParams.cellParams['dh_tonic_interneuron']['secs']['spacer']['geom']['L'] = cfg.spacerL
netParams.cellParams['dh_tonic_interneuron']['secs']['soma']['threshold'] = 0.0

# Delayed Spiking (Excitatory)
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

# Single Spiking (Excitatory)
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

# Tonic Spiking (Excitatory)
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
    'nav1p8': {'gnabar': 0.04}
    }

###############################################################################
# POPULATION PARAMETERS
###############################################################################
# PANs 
netParams.popParams['PAN'] = {'cellType':'E_delay', 
                                  'cellModel': 'E_delay',
                                  'gridSpacing': 50,
                                  'xRange' : [0,200], 
                                  'yRange' : [0,200], 
                                  'zRange' : [0,0]
                                  }

#Tonic Pop (Inhibitory)
netParams.popParams['I_tonic'] = {'cellType': 'IHB',
                                  'numCells': 5,
                                  'cellModel': 'TONIC',
                                  'xRange' : [150,350], 
                                  'yRange' : [150,350], 
                                  'zRange' : [300,400] }

# Delayed Pop (Excitatory)
netParams.popParams['E_delay'] = {'cellType':'E_delay', 
                                  'numCells': 5, 
                                  'cellModel': 'E_delay',
                                  'xRange' : [150,350], 
                                  'yRange' : [150,350], 
                                  'zRange' : [300,400] }

# Single Spike Pop (Excitatory)
netParams.popParams['E_single'] = {'cellType':'E_single', 
                                  'numCells': 3, 
                                  'cellModel': 'E_single',
                                  'xRange' : [150,350], 
                                  'yRange' : [150,350], 
                                  'zRange' : [300,400] }

# Tonic Spike Pop (Excitatory)
netParams.popParams['E_tonic'] = {'cellType':'E_tonic', 
                                  'numCells': 2, 
                                  'cellModel': 'E_tonic',
                                  'xRange' : [150,350], 
                                  'yRange' : [150,350], 
                                  'zRange' : [300,400]}

# Spinal Projection Neurons
netParams.popParams['PROJ'] = {'cellType':'E_delay', 
                                  'numCells': 5, 
                                  'cellModel': 'E_delay',
                                  'xRange' : [150,350], 
                                  'yRange' : [150,350], 
                                  'zRange' : [400,500] }

###############################################################################
# SYNAPTIC PARAMETERS
###############################################################################

## Synaptic mechanism parameters
netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 1.0, 'e': 0}  
netParams.synMechParams['GABA'] = {'mod': 'Exp2Syn', 'tau1': 1.0, 'tau2': 20.0, 'e': -80}  

###############################################################################
# CONNECTIVITY PARAMETERS
###############################################################################
#------------------------PAN2E Connections -----------------------#
netParams.connParams['PAN->E'] = {    
    'preConds': {'pop': 'PAN'}, 'postConds': {'pop': ['E_delay','E_single','E_tonic']},  
    'probability': 0.2,             # probability of connection
    'weight': 0.04,                 # synaptic weight
    'delay': 5,                     # transmission delay (ms)
    'synMech': 'AMPA'}              # synaptic mechanism

#------------------------PAN2I Connections -----------------------#
netParams.connParams['PAN->I'] = {    
    'preConds': {'pop': 'PAN'}, 'postConds': {'pop': ['I_tonic']},  
    'probability': 0.2,             # probability of connection
    'weight': 0.04,                 # synaptic weight
    'delay': 5,                     # transmission delay (ms)
    'synMech': 'AMPA'}              # synaptic mechanism

#-----------------------I2E Connections -----------------------#
netParams.connParams['I->E'] = {    
    'preConds': {'pop': 'I_tonic'}, 'postConds': {'pop': ['E_delay','E_single','E_tonic']},  
    'probability': 0.5,             # probability of connection
    'weight': 0.05,       # synaptic weight  (original weight for network is 0.05 at 10 mN)
    'delay': 5,                     # transmission delay (ms)
    'synMech': 'GABA'}              # synaptic mechanism

#------------------------------E2PROJ Connections -----------------------#
netParams.connParams['E->PROJ'] = {
  'preConds': {'pop': ['E_delay','E_single','E_tonic']}, 'postConds': {'pop':['PROJ']},      
  'probability': 0.2,               # probability of connection
  'weight': 0.04,                   # synaptic weight 
  'delay': 5,                       # transmission delay (ms) 
  'sec': ['soma'], 
  'synMech': 'AMPA'}   


###############################################################################
# STIMULATION PARAMETERS
###############################################################################
# Stimulation Sources:                                  
netParams.stimSourceParams['IClamp'] = {'type': 'IClamp', 
                                       'del': 500,
                                       'dur': 1000,
                                       'amp': cfg.cAMP}

# netParams.stimSourceParams['IClamp2'] = {'type': 'IClamp', 
#                                        'del': 500,
#                                        'dur': 1000,
#                                        'amp': 0.5}

# netParams.stimSourceParams['Mech'] = {'type': 'NetStim', 
#                                         'rate' : 10,
#                                         'start': 200,
#                                         'interval': 'uniform(20,100)',
#                                         'noise': 0.5}

# Stimulation Targets:                                     
# netParams.stimTargetParams['Input->PAN'] = {'source': 'Mech',  # Input --> PAN
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'conds': {'pop':'PAN'}}

# netParams.stimTargetParams['Input->E_delay'] = {'source': 'IClamp',  # IClamp --> E_delay
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'conds': {'pop':'E_delay'}}

# netParams.stimTargetParams['Input->E_single'] = {'source': 'IClamp2',  # IClamp2 --> E_single
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'conds': {'pop':'E_single'}}

# netParams.stimTargetParams['Input->E_tonic'] = {'source': 'IClamp',  # IClamp --> E_tonic
#                                                   'sec':'soma',
#                                                   'loc': 0.5,
#                                                   'conds': {'pop':'E_tonic'}}

netParams.stimTargetParams['Input->I_tonic'] = {'source': 'IClamp',  # IClamp --> I_tonic
                                                  'sec':'soma',
                                                  'loc': 0.5,
                                                  'conds': {'pop':'I_tonic'}}

