# Swift Demangler
Author: **jcfg**

Demangles Swift Names

## Description:
Uses `swift-demangle` utility to demangle Swift names in compiled binaries. On run the plugin asks for the `swift-demangle` binary location and uses it to try and demangle all the symbols in the loaded file. If the symbol was already changed the plugin will leave a comment instead of changing the symbol name.

## License

This plugin is released under an [MIT license](./license).
