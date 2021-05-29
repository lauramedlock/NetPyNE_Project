'''
Initialize NetPyNE file 

Running this code will use netParams and cfg for the network model

Steps:
In bash Terminal:
1. cd to directory (../NetPyNE-Project)
2. compile .mods using >> nrnivmodl mods
In iPython terminal:
3. >> run init.py
'''

from netpyne import sim
from neuron import h
					
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='cfg_RF.py', netParamsDefault='netParams_RF.py')

# Create network and run simulation
sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)