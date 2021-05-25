: Kv3 channel

UNITS {
    (mV) = (millivolt)
    (mA) = (milliamp)
    (S) = (siemens)
}

NEURON {
    SUFFIX kv3
    USEION k READ ek WRITE ik
    RANGE gkbar, gk, ik
    GLOBAL vhninf, kninf, antaul, bntaul, cntaul, dntaul, antaur, bntaur, cntaur,dntaur, brkvntau
}

PARAMETER{ 
    gkbar = 0.004 (S/cm2)
    ek = -88 (mV)
    vhninf = -15
    kninf = 8
    antaul = 1
    bntaul = 15
    cntaul = -50
    dntaul = 10
    brkvntau = -20
    antaur = 0.15
    bntaur = 10
    cntaur = -10
    dntaur = 6
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
         ntau = antaul+bntaul*exp(-((v-cntaul)/dntaul)^2)
    }else{
         ntau = antaur+bntaur*(1/(1+exp((v-cntaur)/dntaur)))
    }
}

UNITSON

