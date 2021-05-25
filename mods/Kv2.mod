: Kv2 channel 

UNITS {
    (mV) = (millivolt)
    (mA) = (milliamp)
    (S) = (siemens)
}

NEURON {
    SUFFIX kv2
    USEION k READ ek WRITE ik
    RANGE gkbar, gk, ik
    GLOBAL vhninf, kninf, antaul, bntaul, cntaul, dntaul, antaur, bntaur, cntaur,dntaur,brkvntau
}

PARAMETER{ 
    gkbar = 0.012 (S/cm2)
    ek = -88 (mV)
    vhninf = -32
    kninf = 8.6
    antaul = 15
    bntaul = 53.1
    cntaul = -46.3
    dntaul = 14
    brkvntau = -30
    antaur = 0.75
    bntaur = 23
    cntaur = -25.6
    dntaur = 4.6
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
    
    ninf = 1/(1+exp(-((v-vhninf)/kninf)))
    
    if (v < brkvntau){
         ntau = antaul+bntaul*(1/(1+exp(-(v-cntaul)/dntaul)))
    }else{
         ntau = antaur+bntaur*(1/(1+exp((v-cntaur)/dntaur)))
    }
}

UNITSON

