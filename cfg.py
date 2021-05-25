'''
This is the cfg.py file for the NetPyNE Project by L Medlock & M Mazar
'''

from netpyne import specs
from neuron import h
from ais_variables import *

cfg = specs.SimConfig()	# object of class SimConfig to store simulation configuration

###############################################################################
# SIMULATION PARAMETERS
###############################################################################
cfg.duration = TSTOP # Duration of the simulation, in ms
cfg.dt = DT # Internal integration timestep to use

cfg.createNEURONObj = 1  # create HOC objects when instantiating network
cfg.createPyStruct = 1  # create Python structure (simulator-independent) when instantiating network
cfg.hParams = {'celsius': CELSIUS, 'v_init': -75.0, 'clamp_resist': 0.001}

# Set recording traces
cfg.recordCells = {'all'}
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
cfg.recordStep = 0.01 
cfg.filename = 'model_output'  			# Set file output name                         

# Save and display data
cfg.analysis['plotTraces'] = {'include': [0,1,2], 'saveFig': True} # Plot recorded traces for this list of cells
cfg.saveJson = False








		



