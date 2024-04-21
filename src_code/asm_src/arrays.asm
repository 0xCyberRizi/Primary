section .data
    array db 10, 20, 30, 40, 50  ; Define an array of 5 bytes

section .text
    global _start   ; Entry point for the program

_start:
    ; Calculate the length of the array
    mov ecx, array_end  ; Load the address of the end of the array
    sub ecx, array      ; Subtract the address of the start of the array
    mov eax, ecx        ; Move the length of the array into the EAX register

    ; Print the length of the array
    mov ebx, 1          ; Set the system call number for write (1)
    mov ecx, eax        ; Move the length of the array into the ECX register (message length)
    mov edx, len_msg    ; Move the length of the message into the EDX register
    mov eax, 4          ; Set the system call number for write (4)
    mov ecx, array_msg  ; Move the address of the message into the ECX register
    int 0x80            ; Invoke the kernel to write the message to the standard output

    ; Exit the program
    mov eax, 1      ; Set the system call number for exit (1)
    xor ebx, ebx    ; Set the exit status to 0
    int 0x80        ; Invoke the kernel to exit the program

section .bss
    array_end resb 1    ; Define a placeholder for the end of the array

section .data
    array_msg db "The length of the array is: ", 0xA  ; Define a message to print
    len_msg equ $ - array_msg   ; Calculate the length of the message
