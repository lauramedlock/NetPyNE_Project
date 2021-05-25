# NetPyNE_Project

## Network model of spinal dorsal horn by L Medlock & M Mazar

Cell models are in folder 'cells' which contains the .mod, .hoc, and .py files  
Excitatory Neurons --> single and delayed spiking (specified in netParams)  
Inhibitory Neurons --> ais_model.py (for tonic spiking, detailed morphology)  
  
To run the model...  
In bash terminal:
1. cd to directory (../NetPyNE-Project)
2. compile .mods using nrnivmodl mods
  
Open iPython terminal then:  
3. run init.py
