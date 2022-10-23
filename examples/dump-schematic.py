
####################################################################################################

from pathlib import Path

from KiCadRW.sexp.schema import KiCadSchema

####################################################################################################

schema_path = Path(
    'kicad-examples',
    'capacitive-half-wave-rectification-pre-zener',
    'capacitive-half-wave-rectification-pre-zener.kicad_sch'
)

# schema_path = Path(
#     'kicad-examples',
#     'single-sheet',
#     'single.kicad_sch'
# )

kicad_schema = KiCadSchema(schema_path)
kicad_schema.dump_netlist()
