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
    jle value1_less_than_value2  ; Jump to 'value1_less_than_value2' label if EAX is less than or equal to EBX

    ; If EAX is greater than EBX, print a message and exit
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, greater_than_msg  ; Move the address of the message into ECX
    mov edx, greater_than_msg_len  ; Move the length of the message into EDX
    int 0x80            ; Invoke the kernel to write the message to the standard output
    jmp end_program     ; Jump to 'end_program' label to exit the program

value1_less_than_value2:
    ; Compare if EAX is less than EBX - 5
    sub ebx, 5          ; Subtract 5 from EBX
    cmp eax, ebx        ; Compare the value in EAX to the value in EBX
    jge value1_less_than_value2_print  ; Jump to 'value1_less_than_value2_print' label if EAX is greater than or equal to EBX

    ; If EAX is less than EBX - 5, print a message and exit
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, value1_less_than_value2_msg  ; Move the address of the message into ECX
    mov edx, value1_less_than_value2_msg_len  ; Move the length of the message into EDX
    int 0x80            ; Invoke the kernel to write the message to the standard output
    jmp end_program     ; Jump to 'end_program' label to exit the program

value1_less_than_value2_print:
    ; If EAX is less than EBX - 5, print a message and exit
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, value1_less_than_value2_print_msg  ; Move the address of the message into ECX
    mov edx, value1_less_than_value2_print_msg_len  ; Move the length of the message into EDX
    int 0x80            ; Invoke the kernel to write the message to the standard output

end_program:
    ; Exit the program
    mov eax, 1      ; Set the system call number for exit (1)
    xor ebx, ebx    ; Set the exit status to 0
    int 0x80        ; Invoke the kernel to exit the program

section .data
    greater_than_msg db 'value1 is greater than value2', 0xA  ; Define a message for greater than case
    greater_than_msg_len equ $ - greater_than_msg   ; Calculate the length of the message

    value1_less_than_value2_msg db 'value1 is less than value2 - 5', 0xA  ; Define a message for less than case
    value1_less_than_value2_msg_len equ $ - value1_less_than_value2_msg   ; Calculate the length of the message

    value1_less_than_value2_print_msg db 'value1 is less than value2', 0xA  ; Define a message for less than case
    value1_less_than_value2_print_msg_len equ $ - value1_less_than_value2_print_msg   ; Calculate the length of the message
