#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _B_A_reg();
extern void _B_DR_reg();
extern void _B_NA_reg();
extern void _KDR_reg();
extern void _KDRI_reg();
extern void _SS_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," B_A.mod");
fprintf(stderr," B_DR.mod");
fprintf(stderr," B_NA.mod");
fprintf(stderr," KDR.mod");
fprintf(stderr," KDRI.mod");
fprintf(stderr," SS.mod");
fprintf(stderr, "\n");
    }
_B_A_reg();
_B_DR_reg();
_B_NA_reg();
_KDR_reg();
_KDRI_reg();
_SS_reg();
}
