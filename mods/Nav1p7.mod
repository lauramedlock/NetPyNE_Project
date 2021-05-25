: Nav1.7 channel

UNITS {
    (mV) = (millivolt)
    (mA) = (milliamp)
    (S) = (siemens)
}

NEURON {
    SUFFIX nav1p7
    USEION na READ ena WRITE ina
    RANGE gnabar, gna, ina
    GLOBAL vhminf, kminf, amtaul, bmtaul, cmtaul, dmtaul, amtaur, bmtaur, cmtaur,dmtaur, brkvmtau
    GLOBAL vhhinf, khinf, ahtaul, bhtaul, chtaul, dhtaul, ahtaur, bhtaur, chtaur, dhtaur, brkvhtau
}

PARAMETER{ 
    gnabar = 0.005 (S/cm2)
    ena = 55 (mV)
    vhminf = -18
    kminf = 7
    amtaul = 0.006
    bmtaul = 0.08
    cmtaul = -55
    dmtaul = 12
    brkvmtau = -50
    amtaur = 0.015
    bmtaur = 0.065
    cmtaur = -10.8
    dmtaur = 10
    vhhinf = -40
    khinf = 12
    ahtaul = 1.98
    bhtaul = 8.54
    chtaul = -73.3
    dhtaul = 4.7
    brkvhtau = -55
    ahtaur = 0.17
    bhtaur = 10.82
    chtaur = -39.1
    dhtaur = 4.59
}

ASSIGNED{
    v (mV)
    ina (mA/cm2)
    gna (S/cm2)
    minf
    hinf
    mtau (ms) 
    htau (ms)    
}

STATE{
    m h
}

BREAKPOINT{
    SOLVE states METHOD cnexp
    
    gna = gnabar * m^3 * h
    ina = gna * (v - ena)
}

UNITSOFF

INITIAL{
    settables(v)
    m = minf
    h = hinf
}

DERIVATIVE states{
    settables(v)
    m' = (minf-m)/mtau
    h' = (hinf-h)/htau
}

PROCEDURE settables(v (mV)){
    TABLE minf, mtau, hinf, htau
    FROM -100 TO 100 WITH 200
        
    minf = 1/(1+exp(-(v-vhminf)/kminf))

if (v < brkvmtau){
         mtau = amtaul+bmtaul*(1/(1+exp(-(v-cmtaul)/dmtaul)))
    }else{
         mtau = amtaur+bmtaur*(1/(1+exp((v-cmtaur)/dmtaur)))
    }

    hinf = 1/(1+exp((v-vhhinf)/khinf))

if (v < brkvhtau){
         htau = ahtaul+bhtaul*(1/(1+exp(-(v-chtaul)/dhtaul)))
    }else{
         htau = ahtaur+bhtaur*(1/(1+exp((v-chtaur)/dhtaur)))
    }

}

UNITSON

