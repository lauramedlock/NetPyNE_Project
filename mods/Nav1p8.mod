: Nav1.8 channel

UNITS {
    (mV) = (millivolt)
    (mA) = (milliamp)
    (S) = (siemens)
}

NEURON {
    SUFFIX nav1p8
    USEION na READ ena WRITE ina
    RANGE gnabar, gna, ina
    GLOBAL vhminf, kminf, amtaul, bmtaul, cmtaul, dmtaul, amtaur, bmtaur, cmtaur,dmtaur, brkvmtau
    GLOBAL vhhinf, khinf, ahtaul, bhtaul, chtaul, dhtaul, ahtaur, bhtaur, chtaur, dhtaur, brkvhtau
}

PARAMETER{ 
    gnabar = 0 (S/cm2)
    ena = 55 (mV)
    vhminf = -11
    kminf = 3.8
    amtaul = 0.2
    bmtaul = 0.4
    cmtaul = -44.2
    dmtaul = 8.02
    brkvmtau = -30
    amtaur = 0.36
    bmtaur = 6
    cmtaur = -39.6
    dmtaur = 6.42
    vhhinf = -32.4
    khinf = 6.1
    ahtaul = 0.31
    bhtaul = 42
    chtaul = -18.5
    dhtaul = 11.1
    brkvhtau = -30
    ahtaur = 0.3
    bhtaur = 282
    chtaur = -55.8
    dhtaur = 10
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
    
    gna = gnabar * m^2 * h
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

