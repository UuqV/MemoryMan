from classes.Contiguous import *
from classes.Memory import *
from classes.NoncontiguousSimulator import *
from classes.VirtualMemSim import *
import sys

simInput = sys.argv[1]

sim1 = Contiguous(simInput)
sim1.simulate_first()
sim1.log("Simulation ended (Contiguous -- First-Fit)")

sim2 = Contiguous(simInput)
sim2.simulate_next()
sim2.log("Simulation ended (Contiguous -- Next-Fit)")

sim3 = Contiguous(simInput)
sim3.simulate_best()
sim3.log("Simulation ended (Contiguous -- Best-Fit)")

sim = NoncontiguousSimulator(simInput)
sim.simulate()

v_mem_input = sys.argv[2]
VirtualMemSim(v_mem_input).simulate()
