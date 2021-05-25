/* Created by Language version: 7.7.0 */
/* NOT VECTORIZED */
#define NRN_VECTORIZED 0
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "scoplib_ansi.h"
#undef PI
#define nil 0
#include "md1redef.h"
#include "section.h"
#include "nrniv_mf.h"
#include "md2redef.h"
 
#if METHOD3
extern int _method3;
#endif

#if !NRNGPU
#undef exp
#define exp hoc_Exp
extern double hoc_Exp(double);
#endif
 
#define nrn_init _nrn_init__SS
#define _nrn_initial _nrn_initial__SS
#define nrn_cur _nrn_cur__SS
#define _nrn_current _nrn_current__SS
#define nrn_jacob _nrn_jacob__SS
#define nrn_state _nrn_state__SS
#define _net_receive _net_receive__SS 
#define _f_rate _f_rate__SS 
#define rate rate__SS 
#define states states__SS 
 
#define _threadargscomma_ /**/
#define _threadargsprotocomma_ /**/
#define _threadargs_ /**/
#define _threadargsproto_ /**/
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 static double *_p; static Datum *_ppvar;
 
#define t nrn_threads->_t
#define dt nrn_threads->_dt
#define gnabar _p[0]
#define ina _p[1]
#define m _p[2]
#define h _p[3]
#define ena _p[4]
#define Dm _p[5]
#define Dh _p[6]
#define _g _p[7]
#define _ion_ena	*_ppvar[0]._pval
#define _ion_ina	*_ppvar[1]._pval
#define _ion_dinadv	*_ppvar[2]._pval
 
#if MAC
#if !defined(v)
#define v _mlhv
#endif
#if !defined(h)
#define h _mlhh
#endif
#endif
 
#if defined(__cplusplus)
extern "C" {
#endif
 static int hoc_nrnpointerindex =  -1;
 /* external NEURON variables */
 extern double celsius;
 /* declaration of user functions */
 static void _hoc_alp(void);
 static void _hoc_bet(void);
 static void _hoc_expM1(void);
 static void _hoc_rate(void);
 static void _hoc_states(void);
 static int _mechtype;
extern void _nrn_cacheloop_reg(int, int);
extern void hoc_register_prop_size(int, int, int);
extern void hoc_register_limits(int, HocParmLimits*);
extern void hoc_register_units(int, HocParmUnits*);
extern void nrn_promote(Prop*, int, int);
extern Memb_func* memb_func;
 
#define NMODL_TEXT 1
#if NMODL_TEXT
static const char* nmodl_file_text;
static const char* nmodl_filename;
extern void hoc_reg_nmodl_text(int, const char*);
extern void hoc_reg_nmodl_filename(int, const char*);
#endif

 extern void _nrn_setdata_reg(int, void(*)(Prop*));
 static void _setdata(Prop* _prop) {
 _p = _prop->param; _ppvar = _prop->dparam;
 }
 static void _hoc_setdata() {
 Prop *_prop, *hoc_getdata_range(int);
 _prop = hoc_getdata_range(_mechtype);
   _setdata(_prop);
 hoc_retpushx(1.);
}
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 "setdata_SS", _hoc_setdata,
 "alp_SS", _hoc_alp,
 "bet_SS", _hoc_bet,
 "expM1_SS", _hoc_expM1,
 "rate_SS", _hoc_rate,
 "states_SS", _hoc_states,
 0, 0
};
#define alp alp_SS
#define bet bet_SS
#define expM1 expM1_SS
 extern double alp( double , double );
 extern double bet( double , double );
 extern double expM1( double , double );
 /* declare global and static user variables */
#define inf inf_SS
 double inf[2];
#define usetable usetable_SS
 double usetable = 1;
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 "gnabar_SS", 0, 1e+009,
 "usetable_SS", 0, 1,
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "gnabar_SS", "mho/cm2",
 "ina_SS", "mA/cm2",
 0,0
};
 static double delta_t = 1;
 static double h0 = 0;
 static double m0 = 0;
 static double v = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 "usetable_SS", &usetable_SS,
 0,0
};
 static DoubVec hoc_vdoub[] = {
 "inf_SS", inf_SS, 2,
 0,0,0
};
 static double _sav_indep;
 static void nrn_alloc(Prop*);
static void  nrn_init(_NrnThread*, _Memb_list*, int);
static void nrn_state(_NrnThread*, _Memb_list*, int);
 static void nrn_cur(_NrnThread*, _Memb_list*, int);
static void  nrn_jacob(_NrnThread*, _Memb_list*, int);
 
static int _ode_count(int);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.7.0",
"SS",
 "gnabar_SS",
 0,
 "ina_SS",
 0,
 "m_SS",
 "h_SS",
 0,
 0};
 static Symbol* _na_sym;
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
 	_p = nrn_prop_data_alloc(_mechtype, 8, _prop);
 	/*initialize range parameters*/
 	gnabar = 0;
 	_prop->param = _p;
 	_prop->param_size = 8;
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 3, _prop);
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 prop_ion = need_memb(_na_sym);
 nrn_promote(prop_ion, 0, 1);
 	_ppvar[0]._pval = &prop_ion->param[0]; /* ena */
 	_ppvar[1]._pval = &prop_ion->param[3]; /* ina */
 	_ppvar[2]._pval = &prop_ion->param[4]; /* _ion_dinadv */
 
}
 static void _initlists();
 static void _update_ion_pointer(Datum*);
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, _NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _SS_reg() {
	int _vectorized = 0;
  _initlists();
 	ion_reg("na", -10000.);
 	_na_sym = hoc_lookup("na_ion");
 	register_mech(_mechanism, nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 0);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
     _nrn_thread_reg(_mechtype, 2, _update_ion_pointer);
 #if NMODL_TEXT
  hoc_reg_nmodl_text(_mechtype, nmodl_file_text);
  hoc_reg_nmodl_filename(_mechtype, nmodl_filename);
#endif
  hoc_register_prop_size(_mechtype, 8, 3);
  hoc_register_dparam_semantics(_mechtype, 0, "na_ion");
  hoc_register_dparam_semantics(_mechtype, 1, "na_ion");
  hoc_register_dparam_semantics(_mechtype, 2, "na_ion");
 	hoc_register_cvode(_mechtype, _ode_count, 0, 0, 0);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 SS C:/Users/mazar/Desktop/AIS_MODEL/SS.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
 static double _zfac [ 2 ] ;
 static double *_t_inf[2];
 static double *_t__zfac[2];
static int _reset;
static char *modelname = "HH sodium channel";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int _f_rate(double);
static int rate(double);
static int states();
 static void _n_rate(double);
 
static int  states (  ) {
   rate ( _threadargscomma_ v * 1.0 ) ;
   m = m + _zfac [ 0 ] * ( inf [ 0 ] - m ) ;
   h = h + _zfac [ 1 ] * ( inf [ 1 ] - h ) ;
   
/*VERBATIM*/
	return 0;
  return 0; }
 
static void _hoc_states(void) {
  double _r;
   _r = 1.;
 states (  );
 hoc_retpushx(_r);
}
 
double alp (  double _lv , double _li ) {
   double _lalp;
 double _la , _lb , _lc , _lq10 ;
 _lv = _lv ;
   _lq10 = pow( 3.0 , ( ( celsius - 23.0 ) / 10.0 ) ) ;
   if ( _li  == 0.0 ) {
     _lalp = _lq10 * 1.0 * .182 * expM1 ( _threadargscomma_ - _lv - 45.0 , 9.0 ) ;
     }
   else if ( _li  == 1.0 ) {
     _lalp = _lq10 * .024 * expM1 ( _threadargscomma_ - _lv - 50.0 , 5.0 ) ;
     }
   
return _lalp;
 }
 
static void _hoc_alp(void) {
  double _r;
   _r =  alp (  *getarg(1) , *getarg(2) );
 hoc_retpushx(_r);
}
 
double bet (  double _lv , double _li ) {
   double _lbet;
 double _la , _lb , _lc , _lq10 ;
 _lv = _lv ;
   _lq10 = pow( 3.0 , ( ( celsius - 23.0 ) / 10.0 ) ) ;
   if ( _li  == 0.0 ) {
     _lbet = _lq10 * 1.0 * .124 * expM1 ( _threadargscomma_ _lv + 45.0 , 9.0 ) ;
     }
   else if ( _li  == 1.0 ) {
     _lbet = _lq10 * .0091 * expM1 ( _threadargscomma_ _lv + 75.0 , 5.0 ) ;
     }
   
return _lbet;
 }
 
static void _hoc_bet(void) {
  double _r;
   _r =  bet (  *getarg(1) , *getarg(2) );
 hoc_retpushx(_r);
}
 
double expM1 (  double _lx , double _ly ) {
   double _lexpM1;
 if ( fabs ( _lx / _ly ) < 1e-6 ) {
     _lexpM1 = _ly * ( 1.0 - _lx / _ly / 2.0 ) ;
     }
   else {
     _lexpM1 = _lx / ( exp ( _lx / _ly ) - 1.0 ) ;
     }
   
return _lexpM1;
 }
 
static void _hoc_expM1(void) {
  double _r;
   _r =  expM1 (  *getarg(1) , *getarg(2) );
 hoc_retpushx(_r);
}
 static double _mfac_rate, _tmin_rate;
 static void _check_rate();
 static void _check_rate() {
  static int _maktable=1; int _i, _j, _ix = 0;
  double _xi, _tmax;
  static double _sav_dt;
  static double _sav_celsius;
  if (!usetable) {return;}
  if (_sav_dt != dt) { _maktable = 1;}
  if (_sav_celsius != celsius) { _maktable = 1;}
  if (_maktable) { double _x, _dx; _maktable=0;
   _tmin_rate =  - 150.0 ;
   _tmax =  100.0 ;
   _dx = (_tmax - _tmin_rate)/200.; _mfac_rate = 1./_dx;
   for (_i=0, _x=_tmin_rate; _i < 201; _x += _dx, _i++) {
    _f_rate(_x);
    for (_j = 0; _j < 2; _j++) { _t_inf[_j][_i] = inf[_j];
}    for (_j = 0; _j < 2; _j++) { _t__zfac[_j][_i] = _zfac[_j];
}   }
   _sav_dt = dt;
   _sav_celsius = celsius;
  }
 }

 static int rate(double _lv){ _check_rate();
 _n_rate(_lv);
 return 0;
 }

 static void _n_rate(double _lv){ int _i, _j;
 double _xi, _theta;
 if (!usetable) {
 _f_rate(_lv); return; 
}
 _xi = _mfac_rate * (_lv - _tmin_rate);
 if (isnan(_xi)) {
  for (_j = 0; _j < 2; _j++) { inf[_j] = _xi;
}  for (_j = 0; _j < 2; _j++) { _zfac[_j] = _xi;
}  return;
 }
 if (_xi <= 0.) {
 for (_j = 0; _j < 2; _j++) { inf[_j] = _t_inf[_j][0];
} for (_j = 0; _j < 2; _j++) { _zfac[_j] = _t__zfac[_j][0];
} return; }
 if (_xi >= 200.) {
 for (_j = 0; _j < 2; _j++) { inf[_j] = _t_inf[_j][200];
} for (_j = 0; _j < 2; _j++) { _zfac[_j] = _t__zfac[_j][200];
} return; }
 _i = (int) _xi;
 _theta = _xi - (double)_i;
 for (_j = 0; _j < 2; _j++) {double *_t = _t_inf[_j]; inf[_j] = _t[_i] + _theta*(_t[_i+1] - _t[_i]);}
 for (_j = 0; _j < 2; _j++) {double *_t = _t__zfac[_j]; _zfac[_j] = _t[_i] + _theta*(_t[_i+1] - _t[_i]);}
 }

 
static int  _f_rate (  double _lv ) {
   double _la , _lb , _ltau ;
 {int  _li ;for ( _li = 0 ; _li <= 1 ; _li ++ ) {
     _la = alp ( _threadargscomma_ _lv , ((double) _li ) ) ;
     _lb = bet ( _threadargscomma_ _lv , ((double) _li ) ) ;
     _ltau = 1.0 / ( _la + _lb ) ;
     if ( ((double) _li )  == 0.0 ) {
       inf [ _li ] = _la / ( _la + _lb ) ;
       }
     else if ( ((double) _li )  == 1.0 ) {
       inf [ _li ] = 1.0 / ( 1.0 + exp ( ( _lv + 75.0 ) / 9.0 ) ) ;
       }
     _zfac [ _li ] = ( 1.0 - exp ( - dt / _ltau ) ) ;
     } }
    return 0; }
 
static void _hoc_rate(void) {
  double _r;
    _r = 1.;
 rate (  *getarg(1) );
 hoc_retpushx(_r);
}
 
static int _ode_count(int _type){ hoc_execerror("SS", "cannot be used with CVODE"); return 0;}
 extern void nrn_update_ion_pointer(Symbol*, Datum*, int, int);
 static void _update_ion_pointer(Datum* _ppvar) {
   nrn_update_ion_pointer(_na_sym, _ppvar, 0, 0);
   nrn_update_ion_pointer(_na_sym, _ppvar, 1, 3);
   nrn_update_ion_pointer(_na_sym, _ppvar, 2, 4);
 }

static void initmodel() {
  int _i; double _save;_ninits++;
 _save = t;
 t = 0.0;
{
  h = h0;
  m = m0;
 {
   rate ( _threadargscomma_ v * 1.0 ) ;
   m = inf [ 0 ] ;
   h = inf [ 1 ] ;
   }
  _sav_indep = t; t = _save;

}
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v = _v;
  ena = _ion_ena;
 initmodel();
 }}

static double _nrn_current(double _v){double _current=0.;v=_v;{ {
   ina = gnabar * m * m * m * ( v - ena ) ;
   }
 _current += ina;

} return _current;
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
  ena = _ion_ena;
 _g = _nrn_current(_v + .001);
 	{ double _dina;
  _dina = ina;
 _rhs = _nrn_current(_v);
  _ion_dinadv += (_dina - ina)/.001 ;
 	}
 _g = (_g - _rhs)/.001;
  _ion_ina += ina ;
#if CACHEVEC
  if (use_cachevec) {
	VEC_RHS(_ni[_iml]) -= _rhs;
  }else
#endif
  {
	NODERHS(_nd) -= _rhs;
  }
 
}}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
#if CACHEVEC
  if (use_cachevec) {
	VEC_D(_ni[_iml]) += _g;
  }else
#endif
  {
     _nd = _ml->_nodelist[_iml];
	NODED(_nd) += _g;
  }
 
}}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; double _v = 0.0; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _nd = _ml->_nodelist[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v=_v;
{
  ena = _ion_ena;
 { error =  states();
 if(error){fprintf(stderr,"at line 49 in file SS.mod:\n	SOLVE states\n"); nrn_complain(_p); abort_run(error);}
 } }}

}

static void terminal(){}

static void _initlists() {
 int _i; static int _first = 1;
  if (!_first) return;
  for (_i=0; _i < 2; _i++) {  _t_inf[_i] = makevector(201*sizeof(double)); }
  for (_i=0; _i < 2; _i++) {  _t__zfac[_i] = makevector(201*sizeof(double)); }
_first = 0;
}

#if NMODL_TEXT
static const char* nmodl_filename = "SS.mod";
static const char* nmodl_file_text = 
  "TITLE HH sodium channel\n"
  ": Hodgkin - Huxley squid sodium channel\n"
  "\n"
  ": The model used in Safronov et al. 2000\n"
  ":\n"
  ": 5/17/2017  Revised by N.T. Carnevale for the sake of conceptual clarity\n"
  ": and to facilitate attributed reuse.\n"
  ": In this version, the reference temperature is 23 deg C\n"
  ": and the value assigned to celsius is the actual operating temperature\n"
  ": in degrees celsius.\n"
  "\n"
  "NEURON {\n"
  "	SUFFIX SS\n"
  "	USEION na READ ena WRITE ina\n"
  "	RANGE gnabar, ina\n"
  "	GLOBAL inf\n"
  "}\n"
  "\n"
  "UNITS {\n"
  "	(mA) = (milliamp)\n"
  "	(mV) = (millivolt)\n"
  "}\n"
  "\n"
  "INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}\n"
  "PARAMETER {\n"
  "	v (mV)\n"
  ":	celsius = 6.3	(degC)\n"
  "	celsius = 23 (degC) : actual operating temperature\n"
  "	dt (ms)\n"
  "	gnabar=0 (mho/cm2) <0,1e9>\n"
  "	ena = 53 (mV)\n"
  "}\n"
  "STATE {\n"
  "	m h\n"
  "}\n"
  "ASSIGNED {\n"
  "	ina (mA/cm2)\n"
  "	inf[2]\n"
  "}\n"
  "LOCAL	fac[2]\n"
  "\n"
  "INITIAL {\n"
  "	rate(v*1(/mV))\n"
  "	m = inf[0]\n"
  "	h = inf[1]\n"
  "}\n"
  "\n"
  "BREAKPOINT {\n"
  "	SOLVE states\n"
  "	ina = gnabar*m*m*m*(v - ena)\n"
  "}\n"
  "\n"
  "PROCEDURE states() {	: exact when v held constant\n"
  "	rate(v*1(/mV))\n"
  "	m = m + fac[0]*(inf[0] - m)\n"
  "	h = h + fac[1]*(inf[1] - h)\n"
  "	VERBATIM\n"
  "	return 0;\n"
  "	ENDVERBATIM\n"
  "}\n"
  "\n"
  "UNITSOFF\n"
  "FUNCTION alp(v(mV),i) { LOCAL a,b,c,q10 :rest = -70  order m,h\n"
  "	v = v :convert to hh convention\n"
  ":	q10 = 3^((celsius - 6.3)/10)\n"
  "	q10 = 3^((celsius - 23)/10) : actual reference temperature\n"
  "	if (i==0) {\n"
  "		alp = q10* 1 *.182*expM1(-v - 45, 9)\n"
  "	}else if (i==1){\n"
  "		alp = q10*.024*expM1(-v - 50, 5)\n"
  "\n"
  "\n"
  "	}\n"
  "}\n"
  "\n"
  "FUNCTION bet(v,i) { LOCAL a,b,c,q10 :rest = -70  order m,h\n"
  "	v = v \n"
  ":	q10 = 3^((celsius - 6.3)/10)\n"
  "	q10 = 3^((celsius - 23)/10) : actual reference temperature\n"
  "	if (i==0) {\n"
  "		bet = q10* 1 *.124*expM1(v + 45, 9)\n"
  "	}else if (i==1){\n"
  "		bet = q10*.0091*expM1(v + 75, 5)\n"
  "	}\n"
  "}\n"
  "\n"
  "FUNCTION expM1(x,y) {\n"
  "	if (fabs(x/y) < 1e-6) {\n"
  "		expM1 = y*(1 - x/y/2)\n"
  "	}else{\n"
  "		expM1 = x/(exp(x/y) - 1)\n"
  "	}\n"
  "}\n"
  "\n"
  "PROCEDURE rate(v) {LOCAL a, b, tau :rest = -70\n"
  "	TABLE inf, fac DEPEND dt, celsius FROM -150 TO 100 WITH 200\n"
  "	FROM i=0 TO 1 {\n"
  "		a = alp(v,i)  b=bet(v,i)\n"
  "		tau = 1/(a + b)\n"
  "		if (i==0) {		\n"
  "		inf[i] = a/(a+b)\n"
  "	}else if (i==1) {\n"
  "		inf[i] = 1/(1+exp((v+75)/9))\n"
  "	} \n"
  "		fac[i] = (1 - exp(-dt/tau))\n"
  "	}\n"
  "}\n"
  "UNITSON\n"
  ;
#endif
