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
# File : tutorial-1c.py
#

from brian import *

tau = 20 * msecond  # time constant: RC
Vt = -50 * mvolt    # spike threshold
Vr = -60 * mvolt    # reset value

El = -49 * mvolt    # resting potential

G = NeuronGroup (N=40, model='dV/dt = -(V - El)/tau : volt', threshold=Vt,
                 reset=Vr)

M = SpikeMonitor (G)

run (1 * second)

print M.nspikes
