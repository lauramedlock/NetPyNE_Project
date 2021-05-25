from netpyne import specs, sim
netParams = specs.NetParams()



# import the delayed spike model
netParams.importCellParams(
    label='delaySpike_hoc',
    conds={'cellType':'E_delay', 'cellModel':'CF'},
    fileName='delaySpike.hoc',
    cellName='CF')

netParams.popParams['E_delay'] = {'cellType':'E_delay', 'numCells': 1, 'cellModel':'CF'}

# Stim Source:
netParams.stimSourceParams['Input_1'] = {
    'type': 'IClamp', 
    'del' : 500,
    'dur': 800,
    'amp': 0.1}

# Stim Target:
netParams.stimTargetParams['Input_1->E_delay'] = {
    'source': 'Input_1', 
    'sec':'soma', 
    'loc': 0.5, 
    'conds': {'pop':'E_delay'}}



## cfg  
cfg = specs.SimConfig()					            
cfg.duration = 2*1e3 						            
cfg.dt = 0.01							                
#cfg.verbose = 1							                
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
cfg.recordStep = 0.1 			
cfg.filename = 'model_output'
cfg.analysis['plotTraces'] = {'include': [0],'saveFig': True}



sim.createSimulateAnalyze(netParams = netParams, simConfig = cfg)

