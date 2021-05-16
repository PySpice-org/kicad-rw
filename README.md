# KiCad-RW : Python library to read/write KiCad Sexpr file format

**Quick Links**

  - [Devel Branch](https://github.com/FabriceSalvaire/kicad-rw/tree/devel)
  - [Production Branch](https://github.com/FabriceSalvaire/kicad-rw/tree/master)

## Overview

### What is KiCaDRW ?

**keywords:** kicad, 6, python, schema

  - **KiCadTools** is a Python module to read the KiCad version 6 schema  
    file format (<span class="title-ref">.kicad\_sch</span> file extension) and to compute the
    netlist which is not actually stored by KiCad. This module is standalone and independent of the
    KiCad Python API, thus it don't require KiCad to work.

**Note**: This proof of concept could become a standalone project and be further extended.

Examples of use cases:

  - perform checks on circuit
  - export a BOM
  - generate a customised SPICE netlist, see [PySpice](https://github.com/FabriceSalvaire/PySpice)
  - generate a [LaTeX/Tikz](https://ctan.org/pkg/pgf?lang=en) graphic **TO BE IMPLEMENTED**
  - generate a draft for [Circuit\_macros](https://ece.uwaterloo.ca/~aplevich/Circuit_macros), a
    tool for drawing electric high quality circuits, see
    <span class="title-ref">CircuitMacrosDumper</span>
  - etc.

### Where is the Documentation ?

**TO BE COMPLETED**

### Where to get help or talk about KiCaDRW ?

**TO BE DONE**

### What are the main features ?

### How to install it ?

**TO BE COMPLETED**

## Pull Request Recommendation

To make it easier to merge your pull request, you should divide your PR into smaller and
easier-to-verify units.

Please do not make a pull requests with a lot of modifications which are difficult to check. .. If I
merge pull requests blindly then there is a high risk this software will become a mess quickly for
everybody.

## Credits

Authors: [Fabrice Salvaire](http://fabrice-salvaire.fr) and
[contributors](https://github.com/FabriceSalvaire/kicad-rw/blob/master/CONTRIBUTORS.md)

## News

### V0 2020-05-xx

Started project...
