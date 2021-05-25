: Kv4 channel

UNITS {
    (mV) = (millivolt)
    (mA) = (milliamp)
    (S) = (siemens)
}

NEURON {
    SUFFIX kv4
    USEION k READ ek WRITE ik
    RANGE gkbar, gk, ik
    GLOBAL vhninf, kninf, antaul, bntaul, cntaul, dntaul, antaur, bntaur, cntaur, dntaur, brkvntau
    GLOBAL vhhinf, khinf, ahtaul, bhtaul, chtaul, dhtaul, ahtaur, bhtaur, chtaur, dhtaur, brkvhtau
}

PARAMETER{ 
    gkbar = 0.0008 (S/cm2)
    ek = -88 (mV)
    vhninf = -50
    kninf = 17.6
    antaul = 0.6
    bntaul = 1.5
    cntaul = -87
    dntaul = 6.16
    brkvntau = -70
    antaur = 0.5
    bntaur = 1.5
    cntaur = -50.5
    dntaur = 11.8
    vhhinf = -73
    khinf = 4
    ahtaul = 24.2
    bhtaul = 191.9
    chtaul = -79.1
    dhtaul = 4.67
    brkvhtau = -78
    ahtaur = 22.5
    bhtaur = 211.5
    chtaur = -66.3
    dhtaur = 5.59
}

ASSIGNED{
    v (mV)
    ik (mA/cm2)
    gk (S/cm2)
    ninf
    hinf
    ntau (ms) 
    htau (ms)    
}

STATE{
    n h
}

BREAKPOINT{
    SOLVE states METHOD cnexp
    
    gk = gkbar * n^4 * h
    ik = gk * (v - ek)
}

UNITSOFF

INITIAL{
    settables(v)
    n = ninf
    h = hinf
}

DERIVATIVE states{
    settables(v)
    n' = (ninf-n)/ntau
    h' = (hinf-h)/htau
}

PROCEDURE settables(v (mV)){
    TABLE ninf, ntau, hinf, htau
    FROM -100 TO 100 WITH 200
    
    ninf = 1/(1+exp(-(v-vhninf)/kninf))

if (v < brkvntau){
         ntau = antaul+bntaul*(1/(1+exp(-(v-cntaul)/dntaul)))
    }else{
         ntau = antaur+bntaur*(1/(1+exp((v-cntaur)/dntaur)))
    }

    hinf = 1/(1+exp((v-vhhinf)/khinf))

if (v < brkvhtau){
         htau = ahtaul+bhtaul*(1/(1+exp(-(v-chtaul)/dhtaul)))
    }else{
         htau = ahtaur+bhtaur*(1/(1+exp((v-chtaur)/dhtaur)))
    }

}

UNITSON

