from matplotlib import pyplot as plt
from ais_model import *
from neuron import h, gui

def simulation_gui():
    # Add cell to each of the components
    #Contorl Panel
    sim_control = h.HBox()
    sim_control.intercept(1)
    h.nrncontrolmenu()
    # attach_current_clamp(cell)
    h.xpanel('TEST')
    h.xlabel('Choose a  simulation to run')
    h.xbutton('Spike Protocol',(sim.voltage_trace, cell))
    h.xbutton('Rheobase Protocol',(sim.rheobase_protocol, cell))
    h.xbutton('Examine AIS change effect on cell Rheobase', (sim.plot_ais_plasticity_change, cell))
    h.xpanel()
    #Output panel
    g = h.Graph()
    g.addvar('soma(0.5).v', cell.soma(0.5)._ref_v)
    g.addvar('AIS(0.5).v', cell.AIS(0.5)._ref_v)
    g.size(0, 1000, -90, 90)
    h.graphList[0].append(g)
    h.MenuExplore()
    sim_control.intercept(0)
    sim_control.map()
    input()

if __name__ == "__main__":
    cell = laminaNeuron()
    cell.set_recording()
    sim = Simulation()
    simulation_gui()