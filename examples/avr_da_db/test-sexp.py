####################################################################################################

from pathlib import Path

from KiCadRW.sexp import loads, dumps

####################################################################################################

path = Path(__file__).parent.joinpath('MCU_Microchip_AVR_Dx.kicad_sym')
with open(path) as fh:
    orig = fh.read()
    sexp = loads(orig)

rewrite = dumps(sexp, pretty_print=True)

with open(str(path) + '-rewrite', 'w') as fh:
    fh.write(rewrite)

# Check lines
orig = orig.splitlines()
rewrite = rewrite.splitlines()
for i in range(len(orig)):
    lo = orig[i] #.rstrip()
    lr = rewrite[i] #.rstrip()
    if lr != lo:
        print()
        print(f'o|{lo}|')
        print(f'l|{lr}|')
        # break
