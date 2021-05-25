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
3. Start up the simulation with /nrngui AbLTMR.hoc/ for Abeta SA1-LTMR model,
   or /nrngui CLTMR.hoc/ for C-LTMR model in terminal.
4. To examine firing pattern, current contribution during firing, and number of APs to 
   current injection plot, initiate the session with /load_file("firing.ses")/.
5. To examine firing with a particular level of current injection, change the number 
   in amp(nA) under IClamp[0] in PointProcessGroupManager Window.
6. To generate number of APs_current injection plot, press Plot button 
   in the Grapher Window.
7. To generate data for the heatmaps as in Fig8G,8G' (both number of APs and 
   onset latency to the first spike), first initiate in the control panel with -80mV, 
   then run hoc file with /load_file("AbLTMR_Kv1_ht.hoc")/ for Kv1 or 
   /load_file("CLTMR_Kv4_ht.hoc")/ for Kv4.
   * Notice: if you are running step 7 from step 6, please close 
             PointProcessGroupManager Window before running step 8, 
             otherwise the apc will not be APCount[0], stim will not be IClamp[0], 
             instead they'd have index 1.
   * Notice: while the loop is running, you'll be able to see the firing pattern in
             the graph panel simultaneously.
8. Data is stored in either Kv1_scale.dat or Kv4_scale.dat.
   * Notice: reci column stores current amplitudes,
             recn column stores number of action potentials (AP criteria or the way it's
             determined was threshold > -20mV and height >= 30mV),
             reclat column stores latency to the first AP (this is time from recording 
             onset, need to be substracted by 100 because current was injected at 100ms,
             reclat of 600 means no AP was fired),
             recscale column stores gbar of either Kv1 or Kv4.
   * Notice: second row has two numbers which register row and column number of the 
             dataframe.
9. The heatmaps were then generated in R. Please refer to r code.
10. Additional Information:
    1). If users would like to switch between AbLTMR and CLTMR models, instead of 
        re-initiate NEURON, one could use /load_file("switch_model.hoc")/ and then run 
        either /set_AbLTMR()/ or /set_CLTMR()/ to change to AbLTMR or CLTMR model,
        respectively.
    2). If users would like to explore parameter space of kinetics of different ion
        channels, one need to disable the reuse of lookup table first, by setting usetable
        to 0, for example, /usetable_nav1p1 = 0/.
    3). If users would like to print parameters, one could use 
        /load_file("print_param.hoc")/, then call the function to print the parameters for
        the channel wanted, for example, call /nav1p1param()/ to print parameters for
        nav1.1.
    4). If users would like to restore default parameters, one could use
        /load_file("set_param.hoc")/, then call the functions to restore the parameters 
        for the channel wanted, for example, call /set_nav1p1()/ to set parameters for
        nav1.1 to default values.
   
