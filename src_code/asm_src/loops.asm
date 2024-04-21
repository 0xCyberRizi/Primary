section .text
    global _start   ; Entry point for the program

_start:
    mov ecx, 1      ; Initialize loop counter to 1

loop_start:
    ; Print the value of the loop counter
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, counter    ; Move the address of the counter variable into ECX
    mov edx, 1          ; Move the length of the message (1 byte) into EDX
    int 0x80            ; Invoke the kernel to write the message to the standard output

    ; Print a space
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, space      ; Move the address of the space character into ECX
    mov edx, 1          ; Move the length of the message (1 byte) into EDX
    int 0x80            ; Invoke the kernel to write the message to the standard output

    ; Increment the loop counter
    inc ecx             ; Increment the value in ECX

    ; Check if the loop counter is less than or equal to 10
    cmp ecx, 11         ; Compare the value in ECX to 11 (10 + 1)
    jle loop_start      ; Jump back to loop_start if ECX is less than or equal to 10

end_program:
    ; Exit the program
    mov eax, 1      ; Set the system call number for exit (1)
    xor ebx, ebx    ; Set the exit status to 0
    int 0x80        ; Invoke the kernel to exit the program

section .data
    counter db '0', 0xA  ; Define a variable to store the loop counter (initialized to '0')
    space db ' ', 0      ; Define a variable for a space character
