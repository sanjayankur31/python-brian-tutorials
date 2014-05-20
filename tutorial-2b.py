#!/usr/bin/python

# Copyright 2010 Ankur Sinha 
# Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com> 
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# File : tutorial-2b.py - excitatory and inhibitory connections
#

from brian import *

tau_a = 1 * ms
tau_b = 10 * ms
Vt = 10 * mV
Vr = 0 * mV

eqs = Equations ('''dVa/dt = -Va/tau_a : volt
                 dVb/dt = -Vb/tau_b : volt
                 ''')

# These are just input creators. They do nothing else. They're channels
# to the main processing neuron
spiketimes = [(0, 1 * ms), (0, 2 * ms), (1, 2 * ms), (1, 3 * ms)]
G1 = SpikeGeneratorGroup (2, spiketimes)

G2 = NeuronGroup(N=1, model=eqs, threshold=Vt, reset=Vr)

C1 = Connection (G1 ,G2, 'Va')
C2 = Connection (G1 ,G2, 'Vb')

C1[0, 0] = 6 * mV # why 6? Shouldn't it be 3?
C2[1, 0] = 3 * mV

Ma = StateMonitor ( G2, 'Va', record=True )
Mb = StateMonitor ( G2, 'Vb', record=True )

run (10 * ms)

plot (Ma.times, Ma[0])
plot (Mb.times, Mb[0])
show ()
