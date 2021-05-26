'''
This is the cfg.py file for the NetPyNE Project by L Medlock & M Mazar
'''

from netpyne import specs
from neuron import h
import sys
sys.path.insert(0, 'cells')  # adding path to cells dir
import ais_variables

cfg = specs.SimConfig()	# object of class SimConfig to store simulation configuration

###############################################################################
# SIMULATION PARAMETERS
###############################################################################
cfg.duration = 2000 # Duration of the simulation, in ms
cfg.dt = ais_variables.DT # Internal integration timestep to use

cfg.createNEURONObj = 1  # create HOC objects when instantiating network
cfg.createPyStruct = 1  # create Python structure (simulator-independent) when instantiating network
cfg.hParams = {'celsius': ais_variables.CELSIUS, 'v_init': -75.0, 'clamp_resist': 0.001}

# Set recording traces
cfg.recordCells = {'all'}
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
cfg.recordStep = 0.01                       

# Save and display data
cfg.simLabel = 'model'
cfg.saveFolder = 'data'
#cfg.savePickle = False
#cfg.saveJson = False
#cfg.saveMat = True
#cfg.saveDataInclude = ['simConfig', 'netParams']

cfg.analysis['plotTraces'] = {'include': [0,1,2,3], 'timeRange':[0,cfg.duration],'ylim':[-100,50], 'figSize':(10, 8), 'saveFig': True} # 'saveData':  'data/model_plotTraces.json'









		



