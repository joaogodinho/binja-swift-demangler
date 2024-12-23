import subprocess

from binaryninja import *


def run_cmd(path, data):
	# Remove last newline
	return subprocess.check_output([path, '--simplified', '--compact', '--no-sugar'], input='\n'.join(data).encode()).decode().split('\n')[:-1]


def demangler(bv):
	# Ask for swift-demangle location
	swift_path = get_open_filename_input('swift-demangle binary location')
	symbols = bv.get_symbols()
	result = run_cmd(swift_path, [s.name for s in symbols])

	with bv.bulk_modify_symbols():
		for i in range(len(symbols)):
			old = symbols[i].name
			new = result[i]
			# symbols that are not swift mangled do not change
			if old != new:
				new = new.replace(' ', '-').split('(')[0]
				sym = symbols[i]
				# if the symbol was already changed, do not overwrite it, instead set a comment
				if sym.auto:
					bv.define_user_symbol(Symbol(sym.type, sym.address, new))
				else:
					bv.set_comment_at(sym.address, new)


PluginCommand.register("Swift Demangler", "Demangles Swift names", demangler)