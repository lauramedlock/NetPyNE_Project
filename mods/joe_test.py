from netpyne import specs, sim
netParams = specs.NetParams()



# # import the delayed spike model
# netParams.importCellParams(
#     label='delaySpike_hoc',
#     conds={'cellType':'E_delay', 'cellModel':'CF'},
#     fileName='delaySpike.hoc',
#     cellName='CF')


netParams.cellParams['E_delay'] = {'secs': {'soma': {}}}
netParams.cellParams['E_delay']['secs']['soma']['geom'] = {
    'diam': 19.55,
    'L'   : 19.55,
    'Ra'  : 1000,
    'nseg': 1,
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
netParams.cellParams['E_delay']['secs']['soma']['ions'] = {
    'k': {'e': -88.0},
    'na': {'e': 55.0},
}

netParams.popParams['E_delay'] = {'cellType':'E_delay', 'numCells': 1}

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
cfg.hParams = {'v_init': -80.0}  
cfg.duration = 2*1e3                                    
cfg.dt = 0.01                                           
#cfg.verbose = 1                                            
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
cfg.recordStep = 0.1            
cfg.filename = 'model_output'
cfg.analysis['plotTraces'] = {'include': [0],'saveFig': True}



sim.createSimulateAnalyze(netParams = netParams, simConfig = cfg)

