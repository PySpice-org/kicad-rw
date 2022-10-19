# KiCad File Format

## Spectra DSN / S-expression

Since version 6, KiCad uses as a format based on the Specctra DSN file format.  It is based on
`S-expression <https://en.wikipedia.org/wiki/S-expression`_, also called symbolic expressions and
abbreviated as sexprs, is a notation for nested list (tree-structured) data, invented for and
popularized by the programming language Lisp.

In comparison to XML:

* We cannot validate the format using a kind of DTD.
* S-expression support is quite limited in comparison to XML libraries.  The sexpdata Python module
  provides data at a very low level in comparison to XML and even JSON/YAML.  For example, there is
  no XPath feature, no tool to deserialise to an oriented object API, and no linter.

## How KiCad handles S-expression

* KiCad expects a particular order
* KiCad uses localised property names, e.g. for sheet filename.  The key will be in French if you
  saved the file with the UI language set to French.

* How are gnerated uuid ? *Symbols have uuid with a lot of (left) zeros, but not pins.*

The data types ares:

* tuple
* Symbol
* string
* integer
* float

## Project .kicad_pro

This is a JSON file.

## .kicad_prl

This is a JSON file.

## Schematic .kicad_sch

This is a S-expression file.

To understand what contain the file, you must understand this format is roughly equivalent to a SVG
export of the schematic, with additional information like the value and footprint of a symbol.  The
data are thus purely graphical.  When you draw a schematic on KiCad, you are just drawing and not
building a graph.

KiCad don't store fundamental information like the netlist, thus we have to guess it using object
coordinates.

## PCB .kicad_pcb

This is a S-expression file.

## Symbol .kicad_sym

## Module .kicad_mod
