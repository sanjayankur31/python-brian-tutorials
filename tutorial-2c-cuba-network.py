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
# File : tutorial-2c-cuba-network.py - CUBA network


from brian import *
taum = 20 * ms
taue = 5 * ms
taui = 10 * ms
Vt = -50 * mV
Vr = -60 * mV
El = -49 * mV

we = (60 * 0.27 / 10) * mV
wi = (20 * 4.5 / 10) * mV

eqs = Equations ('''
                 dV/dt = (ge - gi - (V - El))/taum  :volt
                 dge/dt = -ge/taue                  :volt
                 dgi/dt = -gi/taui                  :volt
                 ''')

G = NeuronGroup (4000, model=eqs, threshold=Vt, reset=Vr)

Ge = G.subgroup(3200)   #excitatory
Gi = G.subgroup(800)    #inhibitory

Ce = Connection(Ge, G, 'ge', sparseness=0.02, weight=we)
Ci = Connection(Gi, G, 'gi', sparseness=0.02, weight=wi)


M = SpikeMonitor(G)
MV = StateMonitor(G, 'V', record=0)
Mge = StateMonitor(G, 'ge', record=0)
Mgi = StateMonitor(G, 'gi', record=0)

G.V = Vr + (Vt - Vr) * rand (len(G)) # initial state randomly somewhere between
# rest and threshold potential

run(500 * ms)


subplot(211)
raster_plot(M, title="The CUBA network", newfigure=False)
subplot(223)
plot(MV.times / ms, MV[0] / mV)
xlabel('Time (ms)')
ylabel('V (mV)')
subplot(224)
plot(Mge.times / ms, Mge[0] / mV)
plot(Mgi.times / ms, Mgi[0] / mV)
xlabel('Time (ms)')
ylabel('ge and gi (mV)')
legend(('ge', 'gi'), 'upper right')
show()
