TITLE HH k channel channel
: Hodgkin - Huxley k channel

: The model used in Safronov et al. 2000 
:
: 5/17/2017  Revised by N.T. Carnevale for the sake of conceptual clarity
: and to facilitate attributed reuse.
: In this version, the reference temperature is 23 deg C
: and the value assigned to celsius is the actual operating temperature
: in degrees celsius.

NEURON {
	SUFFIX B_DR
	USEION k READ ek WRITE ik
	RANGE gkbar, ik
	GLOBAL inf
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
}

INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}
PARAMETER {
	v (mV)
	dt (ms)
	gkbar=0 (mho/cm2) <0,1e9>
	ek = -84 (mV)
:	celsius = 6.3 (degC)
	celsius = 23 (degC) : actual operating temperature
}
STATE {
	n
}
ASSIGNED {
	ik (mA/cm2)
	inf
}
LOCAL	fac

INITIAL {
	rate(v*1(/mV))
	n = inf
}

BREAKPOINT {
	SOLVE states
	ik = gkbar*n*n*n*n*(v - ek)
}

PROCEDURE states() {	: exact when v held constant
	rate(v*1(/mV))
	n = n + fac*(inf - n)
	VERBATIM
	return 0;
	ENDVERBATIM
}

UNITSOFF
FUNCTION alp(v(mV)) { LOCAL q10
	v = v
:	q10 = 3^((celsius - 6.3)/10)
	q10 = 3^((celsius - 23)/10) : actual reference temperature
	alp = q10 * .0075*expM1(-v - 30, 10)
}

FUNCTION bet(v(mV)) { LOCAL q10
	v = v
:	q10 = 3^((celsius - 6.3)/10)
	q10 = 3^((celsius - 23)/10) : actual reference temperature
	bet = q10 * .1*exp((-v - 46)/31)
}

FUNCTION expM1(x,y) {
        if (fabs(x/y) < 1e-6) {
                expM1 = y*(1 - x/y/2)
        }else{
                expM1 = x/(exp(x/y) - 1)
        }
}


PROCEDURE rate(v) {LOCAL a, b, tau :rest = -70
	TABLE inf, fac DEPEND dt, celsius FROM -150 TO 100 WITH 200
		a = alp(v)  b=bet(v)
		tau = 1/(a+b)
		inf = a/(a + b)
		fac = (1 - exp(-dt/tau))
}
UNITSON
