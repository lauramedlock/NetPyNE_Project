'''
This is the cfg.py file for the NetPyNE Project by L Medlock & M Mazar
'''

from netpyne import specs
from neuron import h
import numpy as np
from scipy.stats import multivariate_normal
import sys
sys.path.insert(0, 'cells')  # adding path to cells dir
import ais_variables

cfg = specs.SimConfig()	# object of class SimConfig to store simulation configuration


###############################################################################
# RECEPTIVE FIELD PARAMETERS
###############################################################################
cfg.centerX = 100
cfg.centerY = 100
cfg.radius = 75
cfg.peakWeight = 0.1
cfg.weightDecay = 1/cfg.radius # (weight/um)


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

# SAVING
cfg.simLabel = 'RF'
cfg.saveFolder = 'RFdata'
cfg.saveJson = True
cfg.saveDataInclude = ['netPops','netCells']

#cfg.analysis['plotTraces'] = {'include': [0,25,26], 'timeRange':[0,cfg.duration],'ylim':[-100,50], 'figSize':(10, 8), 'saveFig': True} # 'saveData':  'data/model_plotTraces.json'
cfg.analysis['plotRaster'] = {'timeRange':[0,cfg.duration], 'labels':'overlay', 'saveFig': True}
cfg.analysis['plotSpikeHist'] = {'include':['I_tonic','E_delay'],'overlay':False,'timeRange':[0,cfg.duration], 'binSize': 100, 'graphType':'bar','saveFig': True}
cfg.analysis['plotSpikeStats'] = {'include':['eachPop'], 'stats':['rate'],'graphType':'boxplot','xlim':[0,55], 'saveFig':True}
#cfg.analysis['plot2Dnet'] = {'showConns': True,'saveFig': True}
#cfg.analysis['plotShape'] = {'includePre':['PAN'], 'includePost':[],'showSyns': False,'dist': 0.8,'showFig': True}
#cfg.analysis['plotConn'] = {'groupBy':'cell','feature':'weight','saveFig': True}








		



