README: 
##########################################################################################
The model is associated with the paper
Yang Zheng, Pin Liu, Ling Bai, James S. Trimmer, Bruce P. Bean, David D. Ginty (2019)
Deep Sequencing of Somatosensory Neurons reveals Molecular Determinants of Intrinsic 
Physiological Properties. 
Neuron

These models were written in NEURON.  
##########################################################################################
USER GUIDE (For MaxOS) (All codes are in //): 
1. Download and expand the archive (zip) file. 
2. cd to the directory and run /nrnivmodl/.  
3. Start up the simulation with /nrngui singleSpike.hoc/ for Abeta SA1-LTMR model,
   or /nrngui delaySpike.hoc/ for C-LTMR model in terminal.
4. To examine firing pattern, current contribution during firing, and number of APs to 
   current injection plot, initiate the session with /load_file("firing.ses")/.
5. To examine firing with a particular level of current injection, change the number 
   in amp(nA) under IClamp[0] in PointProcessGroupManager Window.
6. To generate number of APs_current injection plot, press Plot button 
   in the Grapher Window.
  
