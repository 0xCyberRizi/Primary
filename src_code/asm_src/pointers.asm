section .data
    value dd 42   ; Define a value

section .text
    global _start   ; Entry point for the program

_start:
    ; Load the address of the 'value' variable into the EAX register
    lea eax, [value]

    ; Load the value from the memory address pointed to by EAX into EBX
    mov ebx, [eax]

    ; Print the value
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, ebx        ; Move the value in EBX (the value from memory) into ECX
    int 0x80            ; Invoke the kernel to write the value to the standard output

    ; Exit the program
    mov eax, 1      ; Set the system call number for exit (1)
    xor ebx, ebx    ; Set the exit status to 0
    int 0x80        ; Invoke the kernel to exit the program

section .bss
    value resd 1    ; Define a placeholder for the 'value' variable
