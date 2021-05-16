####################################################################################################

from pathlib import Path

from KiCadRW.Objectifier import Objectifier
from KiCadRW.Logging import setup_logging

####################################################################################################

logger = setup_logging()

####################################################################################################

schema_path = Path(
    'kicad-examples',
    'capacitive-half-wave-rectification-pre-zener',
    'capacitive-half-wave-rectification-pre-zener.kicad_sch'
)

objectifier = Objectifier(schema_path)
