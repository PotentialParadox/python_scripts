
# All units are given in SI

# Constants
E0 = 8.85418782E-12 #C^2*N-1*m-2
KB = 1.38064852E-23 #J*K-1

# Conversions
C_IN_CM = 299792458
HZ_TO_WAVENUMBER = 1.0 / C_IN_CM

## To SI
### From Atomic
ATOMIC_TO_METER = 5.29177E-11
ATOMIC_TO_COULOMB = 1.602176E-19
### From CGS
AE_TO_DEBYE = 4.80320454437
DEBYE_TO_COULOMBMETER = 3.335640952E-30
AE_TO_COULOMBMETER = DEBYE_TO_COULOMBMETER * AE_TO_DEBYE
CM_TO_METER = 1.0E-2
FRANKLIN_TO_COULOMB = 3.3356416E-10
### From Common Chemical
ANGSTROM_TO_METER = 1.0E-10
KCALMOLE_TO_EV = 0.043363253978578556

## To Atomic
### From SI
METER_TO_ATOMIC = 1.89E10
COULOMB_TO_ATOMIC = 6.24150934E18
### From Common Chemical
ANGSTROM_TO_ATOMIC = 1.88973
AMBERCHARGE_TO_ATOMIC = 0.0548778145

## To CSG
### From SI
COULOMBMETER_TO_DEBYE = 2.997924579E29
COULOMB_TO_FRANKLIN = 2997924579.9996
METER_TO_CM = 100.0
### From Atomic
ATOMIC_TO_FRANKLIN = 4.80320188E-10
### From Common Chemical
ANGSTROM_TO_CM = 1.0E-8
AMBERCHARGE_TO_FRANKLIN = 2.6358922177669123e-11
FRANKLINCM_TO_DEBYE = 1E18
DEBYE_TO_FRANKLINCM = 1E-18
EV_TO_KCALMOLE = 23.0610

## To Amber
### From atomic
ATOMIC_TO_AMBERCHARGE = 18.2223

#Chemistry
AVOGADRO = 6.022E23
LITER_TO_ANGSTROM = 1.0E27
MOLAR_TO_MOLANGSTROM = 0.0006022
