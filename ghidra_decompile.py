from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

args = getScriptArgs()

program = getCurrentProgram()
ifc = DecompInterface()
ifc.openProgram(program)

function = getFirstFunction()

output = ""

while function is not None:
    results = ifc.decompileFunction(function, 0, ConsoleTaskMonitor())
    output += results.getDecompiledFunction().getC()
    function = getFunctionAfter(function)

with open(args[0], "w") as f:
    f.write(output)
