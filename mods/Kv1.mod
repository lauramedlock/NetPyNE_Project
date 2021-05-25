: Kv1 channel 

UNITS {
    (mV) = (millivolt)
    (mA) = (milliamp)
    (S) = (siemens)
}

NEURON {
    SUFFIX kv1
    USEION k READ ek WRITE ik
    RANGE gkbar, gk, ik
    GLOBAL vhninf, kninf, antaul, bntaul, cntaul, dntaul, antaur, bntaur, cntaur,dntaur, brkvntau
}

PARAMETER{ 
    gkbar = 0.006 (S/cm2)
    ek = -88 (mV)
    vhninf = -57
    kninf = 11
    antaul = 0
    bntaul = 4.59
    cntaul = -56
    dntaul = 15.4
    brkvntau = -60
    antaur = 0.21
    bntaur = 5.6
    cntaur = -96
    dntaur = 19.6
}

ASSIGNED{
    v (mV)
    ik (mA/cm2)
    gk (S/cm2)
    ninf
    ntau (ms) 
}

STATE{
    n
}

BREAKPOINT{
    SOLVE states METHOD cnexp
    
    gk = gkbar * n^4 
    ik = gk * (v - ek)
}

UNITSOFF

INITIAL{
    settables(v)
    n = ninf
}

DERIVATIVE states{
    settables(v)
    n' = (ninf-n)/ntau
}

PROCEDURE settables(v (mV)){
     TABLE ninf, ntau
     FROM -100 TO 100 WITH 200
    
    ninf = 1/(1+exp(-(v-vhninf)/kninf))

if (v < brkvntau){
         ntau = antaul+bntaul*(1/(1+exp(-(v-cntaul)/dntaul)))
    }else{
         ntau = antaur+bntaur*(1/(1+exp((v-cntaur)/dntaur)))
    }
}

UNITSON
