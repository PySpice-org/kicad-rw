####################################################################################################

from pathlib import Path

from KiCadRW.schema import KiCadSchema
from KiCadRW.drawings.CircuitMacros import CircuitMacrosDumper

####################################################################################################

schema_path = Path(
    'kicad-examples',
    'capacitive-half-wave-rectification-pre-zener',
    'capacitive-half-wave-rectification-pre-zener.kicad_sch'
)

kicad_schema = KiCadSchema(schema_path)
cm_code = CircuitMacrosDumper(kicad_schema)
print(cm_code)
