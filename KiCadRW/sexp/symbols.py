####################################################################################################
#
# KiCad-RW — Python library to read/write KiCad Sexpr file format
# Copyright (C) 2021 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
####################################################################################################

import sys as _sys
from sexpdata import Symbol as _Symbol

####################################################################################################

_module = _sys.modules[__name__]

for _name in (
    'at',

    'background',

    'bottom',

    'color',

    'default',

    'effects',
    'end',
    'extends',

    'fill',
    'font',

    'generator',

    'hide',

    'id',
    'in_bom',
    'italic',

    'justify',

    'kicad_symbol_lib',

    'left',
    'length',
    'line',

    'name',
    'number',

    'on_board',

    'pin',
    'property',

    'rectangle',

    'size',
    'start',
    'stroke',
    'symbol',

    'top',
    'type',

    'version',

    'width',

    'yes',
):
    setattr(_module, _name.upper(), _Symbol(_name))
