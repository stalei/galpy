from galpy.potential_src import Potential
from galpy.potential_src import planarPotential
from galpy.potential_src import linearPotential
from galpy.potential_src import verticalPotential
from galpy.potential_src import MiyamotoNagaiPotential
from galpy.potential_src import LogarithmicHaloPotential
from galpy.potential_src import DoubleExponentialDiskPotential
from galpy.potential_src import PowerSphericalPotential
from galpy.potential_src import TwoPowerSphericalPotential
from galpy.potential_src import plotRotcurve
from galpy.potential_src import plotEscapecurve
from galpy.potential_src import KGPotential
from galpy.potential_src import interpRZPotential
from galpy.potential_src import DehnenBarPotential
from galpy.potential_src import SteadyLogSpiralPotential
from galpy.potential_src import TransientLogSpiralPotential
from galpy.potential_src import MovingObjectPotential
from galpy.potential_src import ForceSoftening
from galpy.potential_src import EllipticalDiskPotential
from galpy.potential_src import CosmphiDiskPotential
from galpy.potential_src import RazorThinExponentialDiskPotential
from galpy.potential_src import FlattenedPowerPotential
#
# Functions
#
evaluatePotentials= Potential.evaluatePotentials
evaluateDensities= Potential.evaluateDensities
evaluateRforces= Potential.evaluateRforces
evaluatephiforces= Potential.evaluatephiforces
evaluatezforces= Potential.evaluatezforces
evaluateR2derivs= Potential.evaluateR2derivs
evaluatez2derivs= Potential.evaluatez2derivs
RZToplanarPotential= planarPotential.RZToplanarPotential
RZToverticalPotential= verticalPotential.RZToverticalPotential
plotPotentials= Potential.plotPotentials
plotplanarPotentials= planarPotential.plotplanarPotentials
plotlinearPotentials= linearPotential.plotlinearPotentials
calcRotcurve= plotRotcurve.calcRotcurve
vcirc= plotRotcurve.vcirc
dvcircdR= plotRotcurve.dvcircdR
epifreq= Potential.epifreq
verticalfreq= Potential.verticalfreq
flattening= Potential.flattening
rl= Potential.rl
omegac= plotRotcurve.omegac
lindbladR= plotRotcurve.lindbladR
plotRotcurve= plotRotcurve.plotRotcurve
calcEscapecurve= plotEscapecurve.calcEscapecurve
vesc= plotEscapecurve.vesc
plotEscapecurve= plotEscapecurve.plotEscapecurve
evaluateplanarPotentials= planarPotential.evaluateplanarPotentials
evaluateplanarRforces= planarPotential.evaluateplanarRforces
evaluateplanarphiforces= planarPotential.evaluateplanarphiforces
evaluatelinearPotentials= linearPotential.evaluatelinearPotentials
evaluatelinearForces= linearPotential.evaluatelinearForces
#
# Classes
#
Potential= Potential.Potential
planarAxiPotential= planarPotential.planarAxiPotential
planarPotential= planarPotential.planarPotential
linearPotential= linearPotential.linearPotential
MiyamotoNagaiPotential= MiyamotoNagaiPotential.MiyamotoNagaiPotential
DoubleExponentialDiskPotential= DoubleExponentialDiskPotential.DoubleExponentialDiskPotential
LogarithmicHaloPotential= LogarithmicHaloPotential.LogarithmicHaloPotential
KeplerPotential= PowerSphericalPotential.KeplerPotential
PowerSphericalPotential= PowerSphericalPotential.PowerSphericalPotential
NFWPotential= TwoPowerSphericalPotential.NFWPotential
JaffePotential= TwoPowerSphericalPotential.JaffePotential
HernquistPotential= TwoPowerSphericalPotential.HernquistPotential
TwoPowerSphericalPotential= TwoPowerSphericalPotential.TwoPowerSphericalPotential
KGPotential= KGPotential.KGPotential
interpRZPotential= interpRZPotential.interpRZPotential
DehnenBarPotential= DehnenBarPotential.DehnenBarPotential
SteadyLogSpiralPotential= SteadyLogSpiralPotential.SteadyLogSpiralPotential
TransientLogSpiralPotential= TransientLogSpiralPotential.TransientLogSpiralPotential
MovingObjectPotential= MovingObjectPotential.MovingObjectPotential
EllipticalDiskPotential= EllipticalDiskPotential.EllipticalDiskPotential
LopsidedDiskPotential= CosmphiDiskPotential.LopsidedDiskPotential
CosmphiDiskPotential= CosmphiDiskPotential.CosmphiDiskPotential
RazorThinExponentialDiskPotential= RazorThinExponentialDiskPotential.RazorThinExponentialDiskPotential
FlattenedPowerPotential= FlattenedPowerPotential.FlattenedPowerPotential
#Softenings
PlummerSoftening= ForceSoftening.PlummerSoftening

#
# Constants
#
MWPotential= [MiyamotoNagaiPotential(a=0.5,b=0.0375,normalize=.6),
              NFWPotential(a=4.5,normalize=.35),
              HernquistPotential(a=0.6/8,normalize=0.05)]
