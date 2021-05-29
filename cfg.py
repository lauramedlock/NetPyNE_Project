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
cfg.hParams = {'celsius': ais_variables.CELSIUS, 'v_init': -75.0, 'clamp_resist': 0.001}
cfg.filename = 'ais'       # Set file output name
cfg.saveJson = True
cfg.printPopAvgRates = True

# Set recording traces
#cfg.recordCells = {'all'}
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
cfg.recordStep = 0.1                       

# Save and display data
#cfg.simLabel = 'model'
#cfg.saveFolder = 'data'
#cfg.savePickle = False
#cfg.saveJson = False
#cfg.saveMat = True
#cfg.saveDataInclude = ['simConfig', 'netParams']

#cfg.analysis['plotTraces'] = {'include': [0,25,30,35,38,40], 'timeRange':[0,cfg.duration],'ylim':[-100,50], 'figSize':(10, 8), 'saveFig': True} 
cfg.analysis['plotTraces'] = {'include':[25], 'saveFig':True}
cfg.analysis['plotRaster'] = {'timeRange':[0,cfg.duration], 'labels':'overlay', 'saveFig': True}
#cfg.analysis['plotSpikeHist'] = {'include':['PAN'],'timeRange':[0,cfg.duration], 'binSize': 100, 'graphType':'bar','saveFig': True}
#cfg.analysis['plot2Dnet'] = {'showConns': True,'saveFig': True}
#cfg.analysis['plotShape'] = {'includePre':['PAN'], 'includePost':[],'showSyns': False,'dist': 0.8,'showFig': True}
#cfg.analysis['plotConn'] = {'groupBy':'pop','saveFig': True}

cfg.saveDataInclude = ['simData', 'simConfig', 'netParams', 'net']

# Variable parameters (used in netParams)
cfg.spacerL = 5
cfg.connWeight = 0.01






		



