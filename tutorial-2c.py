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
# File : tutorial-2c.py - excitatory and inhibitory currents
#

from brian import *

taum = 20 * ms
taue = 1 * ms
taui = 10 * ms
Vt = 10 * mV
Vr = 0 * mV

eqs = Equations ('''dV/dt = (-V + ge - gi)/taum :volt
                 dge/dt = -ge/taue              :volt
                 dgi/dt = -gi/taui              :volt
                 ''')

# These are just input creators. They do nothing else. They're channels
# to the main processing neuron
spiketimes = [(0, 1 * ms), (0, 10 * ms), (1, 40 * ms), (0, 50 * ms), (0, 55 * ms)]
G1 = SpikeGeneratorGroup (2, spiketimes)

G2 = NeuronGroup(N=1, model=eqs, threshold=Vt, reset=Vr)

C1 = Connection (G1 ,G2, 'ge')
C2 = Connection (G1 ,G2, 'gi')

C1[0, 0] = 3 * mV
C2[1, 0] = 3 * mV

Mv = StateMonitor (G2, 'V', record=True)
Me = StateMonitor ( G2, 'ge', record=True )
Mi = StateMonitor ( G2, 'gi', record=True )

run (100 * ms)

figure ()
subplot (211)
plot(Mv.times, Mv[0])
subplot (212)
plot(Me.times, Me[0])
plot(Mi.times, Mi[0])
show ()
