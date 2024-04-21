@echo off

rem Disable echoing of commands in the command prompt

rem Set the first command-line argument as the input filename (without extension)
set arg1=%1

rem Assemble the assembly file using NASM with the win32 format
nasm -f win32 "%arg1%.asm"

rem Compile the C driver program along with the input object file and additional object files
rem -Zi: Produce debug symbols for debugging/disassembling
rem -Fe: Specify the output filename
cl -Zi -Fe"%arg1%.exe" driver.c "%arg1%.obj" asm_io.obj /link legacy_stdio_definitions.lib
