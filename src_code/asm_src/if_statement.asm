section .data
    value1 dd 10   ; Define the first value
    value2 dd 20   ; Define the second value

section .text
    global _start   ; Entry point for the program

_start:
    ; Load the values into registers
    mov eax, [value1]  ; Move the value of 'value1' into EAX
    mov ebx, [value2]  ; Move the value of 'value2' into EBX

    ; Compare the values
    cmp eax, ebx       ; Compare the values in EAX and EBX
    jle less_than     ; Jump to 'less_than' label if EAX is less than or equal to EBX

greater_than:
    ; Print message: value1 is greater than value2
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, greater_than_msg  ; Move the address of the message into ECX
    mov edx, greater_than_msg_len  ; Move the length of the message into EDX
    int 0x80            ; Invoke the kernel to write the message to the standard output
    jmp end_program     ; Jump to 'end_program' label to exit the program

less_than:
    ; Print message: value1 is less than value2
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, less_than_msg  ; Move the address of the message into ECX
    mov edx, less_than_msg_len  ; Move the length of the message into EDX
    int 0x80            ; Invoke the kernel to write the message to the standard output
    jmp end_program     ; Jump to 'end_program' label to exit the program

section .data
    greater_than_msg db 'value1 is greater than value2', 0xA  ; Define a message for greater than case
    greater_than_msg_len equ $ - greater_than_msg   ; Calculate the length of the message

    less_than_msg db 'value1 is less than value2', 0xA     ; Define a message for less than case
    less_than_msg_len equ $ - less_than_msg     ; Calculate the length of the message

section .bss
    end_program resb 1    ; Define a placeholder for the end of the program
