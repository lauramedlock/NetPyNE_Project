: Nav1.6 channel

UNITS {
    (mV) = (millivolt)
    (mA) = (milliamp)
    (S) = (siemens)
}

NEURON {
    SUFFIX nav1p6
    USEION na READ ena WRITE ina
    RANGE gnabar, gna, ina
    GLOBAL vhminf, kminf, amtaul, bmtaul, cmtaul, dmtaul, amtaur, bmtaur, cmtaur,dmtaur, brkvmtau
    GLOBAL vhhinf, khinf, ahtaul, bhtaul, chtaul, dhtaul, ahtaur, bhtaur, chtaur, dhtaur, brkvhtau
}

PARAMETER{ 
    gnabar = 0.04 (S/cm2)
    ena = 55 (mV)
    vhminf = -39
    kminf = 5.5
    amtaul = 0.006
    bmtaul = 0.08
    cmtaul = -55
    dmtaul = 12
    brkvmtau = -50
    amtaur = 0.015
    bmtaur = 0.065
    cmtaur = -10.8
    dmtaur = 10
    vhhinf = -53
    khinf = 5.4
    ahtaul = 0.7
    bhtaul = 8.5
    chtaul = -60.1
    dhtaul = 8.4
    brkvhtau = -50
    ahtaur = 0.1
    bhtaur = 52.2
    chtaur = -59.5
    dhtaur = 5
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

UNITSOFF

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

