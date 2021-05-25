: leak (passive) channel.

TITLE A passive leak current

UNITS {
	(mV) = (millivolt)
	(mA) = (milliamp)
	(S) = (siemens)
}

NEURON {
	SUFFIX leak
	NONSPECIFIC_CURRENT i
	RANGE i, e, g
}

PARAMETER {
	g = .0001 (S/cm2) 
	e = -80	(mV)
}

ASSIGNED {
  i(mA/cm2)
  v(mV)
}

BREAKPOINT {
	i = g*(v - e)
}
