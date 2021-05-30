############################
# Batch file
from netpyne import specs
from netpyne.batch import Batch
# Create variable of type ordered dictionary (NetPyNE's customized version)
params = specs.ODict()

# fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
params['spacerL'] = [5, 25, 30, 50, 100]
params['cAMP'] = [0.005, 0.01, 0.05, 0.08, 0.1]
#params['connWeight'] = [0.005, 0.01, 0.025, 0.05]

# create Batch object with parameters to modify, and specifying files to use
b = Batch(params=params, cfgFile='cfg.py', netParamsFile='netParams.py',)

# Set output folder, grid method (all param combinations), and run configuration
b.batchLabel = 'disinhibition'
b.saveFolder = 'data'
b.method = 'grid'
b.runCfg = {'type': 'mpi_bulletin',
                    'script': 'init.py',
                    'skip': True}
# Run batch simulations
b.run()