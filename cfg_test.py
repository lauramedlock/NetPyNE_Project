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
cfg.radius = 200
cfg.sigmaV = 20
cfg.scaleZ = 100

cfg.testWgt = 0.1

cfg.mu = np.array([cfg.centerX, cfg.centerY])  # define the center of the receptive field
cfg.x, cfg.y = np.mgrid[0:cfg.radius:200j, 0:cfg.radius:200j] # define coordinates of receptive field
cfg.xy = np.column_stack([cfg.x.flat, cfg.y.flat]) # Need an (N, 2) array of (x, y) pairs.
cfg.sigma = np.array([cfg.sigmaV, cfg.sigmaV])
cfg.covariance = np.diag(cfg.sigma**2)
cfg.z = multivariate_normal.pdf(cfg.xy, mean=cfg.mu, cov=cfg.covariance)
cfg.z = cfg.scaleZ * cfg.z.reshape(cfg.x.shape) # Reshape back to a (radius x radius) grid.


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
cfg.analysis['plotRaster'] = {'timeRange':[0,cfg.duration], 'labels':'overlay', 'saveFig': True}
cfg.analysis['plot2Dnet'] = {'showConns': True,'saveFig': True}
#cfg.analysis['plotShape'] = {'includePre':['PAN'], 'includePost':[],'showSyns': False,'dist': 0.8,'showFig': True}









		



