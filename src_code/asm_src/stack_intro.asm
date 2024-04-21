section .data
    message db 'Hello, Stack!', 0xA   ; Define a message to be printed

section .text
    global _start   ; Entry point for the program

_start:
    ; Pushing values onto the stack
    push dword message      ; Push the address of the message onto the stack (pointer to the message string)

    ; Calling a function to print the message
    call print_message

    ; Cleanup: restoring the stack
    add esp, 4     ; Restore the stack pointer by adding 4 bytes (size of the pushed address)

    ; Exit the program
    mov eax, 1      ; Set the system call number for exit (1)
    xor ebx, ebx    ; Set the exit status to 0
    int 0x80        ; Invoke the kernel to exit the program

; Function to print a null-terminated string
print_message:
    mov eax, 4      ; Set the system call number for write (4)
    mov ebx, 1      ; Set the file descriptor for standard output (1)
    mov ecx, [esp + 4]   ; Move the address of the message (passed as an argument) into ECX
    mov edx, message_len ; Move the length of the message into EDX
    int 0x80        ; Invoke the kernel to write the message to the standard output
    ret             ; Return from the function

section .data
    message_len equ $ - message   ; Calculate the length of the message
