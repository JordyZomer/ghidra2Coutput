# ghidra2Coutput
A little ghidra headless script to decompile all the functions and write it to an output file.

# Installation/Usage

```bash
$ git clone https://github.com/JordyZomer/ghidra2Coutput
$ cd ghidra2Coutput
$ vim run.sh
// Now you want to edit GHIDRA_DIR to the directory where Ghidra is installed on your system.
// And then you're ready to execute run.sh (a wrapper to Ghidra's headless analyzer to load the script) to actually output the C.
// REMEMBER TO ALWAYS RUN IT FROM THIS DIRECTORY DUE TO THE UGLY NATURE OF THE BASH SCRIPT.
$ ./run.sh binary_to_analyze file_to_put_c_output
```
