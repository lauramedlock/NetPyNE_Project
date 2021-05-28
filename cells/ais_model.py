from matplotlib import pyplot as plt
from ais_variables import *
from ais_plotter import *
from neuron import h, gui
import numpy as np
import csv

class laminaNeuron():
    """A ball & stick neuron model describing """
    def __init__(self):
        self.create_sections()
        self.build_topology()
        self.all = h.allsec()
        self.dendrites = [self.dend]
        self.neuron_cable = [self.soma, self.AIS, self.axon]
        self.define_geometry()
        self.set_biophysics()
        self.add_current_stim()
    def __repr__(self):
        return 'laminaNeuron'
    def create_sections(self):
        """ Create morphological sections """
        self.soma = h.Section(name='soma', cell=self)
        self.dend = h.Section(name='dend', cell=self)
        self.spacer = h.Section(name='spacer', cell=self)
        self.AIS = h.Section(name='AIS', cell=self)
        self.axon = h.Section(name='axon', cell=self)
    def build_topology(self):
        '''Connect sections together'''
        self.dend.connect(self.soma(0))
        self.spacer.connect(self.soma(1))
        self.AIS.connect(self.spacer(1))
        self.axon.connect(self.AIS(1))
    def define_geometry(self):
        '''Define Length, Diamter and        Number of Segment per Section'''
        # Dendrites
        self.dend.L = DEND_L
        self.dend.diam = DEND_DIAM
        self.dend.nseg = DEND_NSEG
        # Soma
        self.soma.L = SOMA_L
        self.soma.diam = SOMA_DIAM
        self.soma.nseg = SOMA_NSEG
        # Spacer
        self.spacer.L = SPACER_L        # change this for neuropathic conditions
        self.spacer.diam = SPACER_DIAM
        self.spacer.nseg = SPACER_NSEG
        # AIS
        self.AIS.L = AIS_L
        self.AIS.diam = AIS_DIAM
        self.AIS.nseg = AIS_NSEG
        # Axon
        self.axon.L = AXON_L
        self.axon.diam = AXON_DIAM
        self.axon.nseg = AXON_NSEG

    def set_biophysics(self):
        '''Set cell biophyisics including passive and active properties '''
        # Set passive membrane biophysics
        for sec in self.all:
            sec.Ra = R_A
            sec.cm = C_M
        # Set leaky channels for the model:
        for sec in self.all:
            sec.insert('pas')
            sec.g_pas = GPAS_NEW  # in this version its .pas.g instead of g_pas
            sec.e_pas = E_PAS
        # Insert soma mechanisms:
        self.soma.insert('B_Na')
        self.soma.insert('KDRI')
        # Insert dendrite mechanisms
        self.dend.insert('SS')
        self.dend.insert('KDRI')
        # Insert axon initial segment mechanisms
        self.AIS.insert('B_Na')
        self.AIS.insert('KDRI')
        # Insert axon mechanisms
        self.axon.insert('B_Na')
        self.axon.insert('KDRI')
        # Set Active Reversal Potentials
        for sec in self.neuron_cable + self.dendrites:
            sec.ena = E_NA
            sec.ek = E_K
        # Set channel densities:
        # Dendrites
        self.dend.gnabar_SS = 0
        self.dend.gkbar_KDRI = GK_BAR_DEND
        # Soma
        self.soma.gnabar_B_Na = GNA_BAR_SOMA
        self.soma.gkbar_KDRI = GKDR_BAR_SOMA
        # AIS
        self.AIS.gnabar_B_Na = GNA_BAR_AIS
        self.AIS.gkbar_KDRI = GK_BAR_AIS
        # axon
        self.axon.gnabar_B_Na = GNA_BAR_AXON
        self.axon.gkbar_KDRI = GK_BAR_AXON

    def add_current_stim(self, delay=DELAY, dur=DUR, current=CURRENT, loc=RECORDING_LOCATION):
        """Attach a current Clamp to a cell.
        :param cell: Cell object to attach the current clamp.
        :param delay: Onset of the injected current.
        :param dur: Duration of the stimulus.
        :param amp: Magnitude of the current.
        :param loc: Location on the dendrite where the stimulus is placed.
        """
        self.stim = h.IClamp(self.soma(loc))
        self.stim.amp = current
        self.stim.delay = delay
        self.stim.dur = dur

    def set_recording(self):
        """Set soma, axon initial segment, and time recording vectors on the cell.
        :param cell: Cell to record from.
        :return: the soma, dendrite, and time vectors as a tuple.
        """
        self.soma_v_vec = h.Vector()  # Membrane potential vector at soma
        self.AIS_v_vec = h.Vector()  # Membrane potential vector at dendrite
        self.t_vec = h.Vector()  # Time stamp vector
        self.soma_v_vec.record(self.soma(0.5)._ref_v)
        self.AIS_v_vec.record(self.AIS(0.5)._ref_v)
        self.t_vec.record(h._ref_t)


class Simulation(laminaNeuron):
    def __init__(self):
        self.id = 0
        self.rheobase = None
        self.init_simulation()
    def init_simulation(self, vinit=V_INIT, tstop=TSTOP, celsius=CELSIUS):
        """Initialize and run a simulation.
        :param celsius:
        :param v_init:
        :param tstop: Duration of the simulation.
        """
        h.v_init = vinit
        h.tstop = tstop
        h.celsius = celsius
        h.dt = DT

    def rheobase_counter(self, cell, min_current=MIN_CURRENT, max_current=MAX_CURRENT, rheobase_step=RHEOBASE_STEP):
        # Remove writing to file and put it seperately
        self.id += 1
        apc = h.APCount(cell.soma(0.5))
        apc.thresh = THRESHOLD
        current_lst = np.arange(min_current, max_current, rheobase_step)
        for new_current in current_lst:
            cell.stim.amp = new_current
            h.run()
            if apc.n > 0:
                print(apc.n)
                self.rheobase = new_current
                break

    def voltage_trace(self, cell):
        apc = h.APCount(cell.soma(RECORDING_LOCATION))
        apc.thresh = THRESHOLD
        # laminaNeuron.set_recording()
        # Setup Graphs:
        plt.figure(figsize=(20, 8))
        step = 0.04
        num_steps = 2
        for new_current in np.linspace(step, step * num_steps, num_steps):
            cell.stim.amp = new_current
            h.run()
            plt.plot(cell.t_vec, cell.soma_v_vec, label=str(new_current) + ', Spike Number = {}'.format(apc.n))
        # Design Graph
        plt.suptitle('Spike Graph', fontsize=14, fontweight='bold')
        # pyplot.text(0.1, 2.8, "The number of action potentials is {}".format(apc.n))
        plt.xlabel('time (ms)')
        plt.ylabel('mV')
        plt.legend()
        plt.show()

    def rheobase_protocol(self, cell):
        apc = h.APCount(cell.soma(0.5))
        apc.thresh = 0
        current_lst = np.arange(MIN_CURRENT, MAX_CURRENT, RHEOBASE_STEP)
        for new_current in current_lst:
            cell.stim.amp = new_current
            h.run()
            if apc.n > 0:
                pyplot.plot(cell.t_vec, cell.soma_v_vec, label=str(new_current) + ', Rheobase = {}'.format(new_current))
                pyplot.suptitle('Spike Graph', fontsize=14, fontweight='bold')
                # pyplot.text(0.1, 2.8, "The number of action potentials is {}".format(apc.n))
                pyplot.xlabel('time (ms)')
                pyplot.ylabel('mV')
                pyplot.legend()
                pyplot.show()
                self.rheobase = new_current
                break

    def plot_ais_plasticity_change(self, cell):
        time_arr = []
        soma_v_arr = []
        rheobase_arr = []
        for spacer_leng in SPACER_ARR:
            # Set up simulation
            cell.spacer.L = spacer_leng
            # Append values
            self.rheobase_counter(cell)
            rheobase_arr.append(self.rheobase)
            time_arr.append(np.array(cell.t_vec))
            soma_v_arr.append(np.array(cell.soma_v_vec))
        my_plotter(cell, time_arr, soma_v_arr, SPACER_ARR, rheobase_arr)

    def save_simulation(self, laminaNeuron, file_name):
        list_of_elem = [self.id, 1 / laminaNeuron.dend.g_pas,
                          laminaNeuron.dend.Ra, laminaNeuron.dend.cm, laminaNeuron.dend.L,
                          laminaNeuron.spacer.L, 1 / laminaNeuron.spacer.g_pas, laminaNeuron.spacer.Ra,
                          laminaNeuron.spacer.cm, 1 / laminaNeuron.AIS.g_pas, self.rheobase]
        with open(file_name, 'ab') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(list_of_elem)

