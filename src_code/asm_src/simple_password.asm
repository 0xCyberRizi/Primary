section .data
    password db 'password', 0   ; Define the correct password

section .text
    global _start   ; Entry point for the program

_start:
    ; Prompt the user to enter the password
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, password_prompt  ; Move the address of the prompt message into ECX
    mov edx, password_prompt_len  ; Move the length of the prompt message into EDX
    int 0x80            ; Invoke the kernel to write the prompt message to the standard output

    ; Read the password entered by the user
    mov eax, 3          ; Set the system call number for read (3)
    mov ebx, 0          ; Set the file descriptor for standard input (0)
    mov ecx, user_input    ; Move the address of the input buffer into ECX
    mov edx, 20         ; Move the maximum number of characters to read into EDX
    int 0x80            ; Invoke the kernel to read the input from the standard input

    ; Compare the entered password with the correct password
    mov eax, 0          ; Clear the EAX register
    mov ebx, password   ; Move the address of the correct password into EBX
    mov ecx, user_input    ; Move the address of the user input buffer into ECX
    call compare_strings    ; Call the compare_strings function

    ; Check if the passwords match
    cmp eax, 0          ; Compare the result of the string comparison with 0
    jne incorrect_password   ; Jump to 'incorrect_password' label if the passwords do not match

    ; If the passwords match, print a success message
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, success_msg   ; Move the address of the success message into ECX
    mov edx, success_msg_len  ; Move the length of the success message into EDX
    int 0x80            ; Invoke the kernel to write the success message to the standard output

    ; Exit the program
    mov eax, 1      ; Set the system call number for exit (1)
    xor ebx, ebx    ; Set the exit status to 0
    int 0x80        ; Invoke the kernel to exit the program

incorrect_password:
    ; If the passwords do not match, print an error message
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, incorrect_password_msg    ; Move the address of the error message into ECX
    mov edx, incorrect_password_msg_len    ; Move the length of the error message into EDX
    int 0x80            ; Invoke the kernel to write the error message to the standard output

    ; Exit the program with an error status
    mov eax, 1      ; Set the system call number for exit (1)
    mov ebx, 1      ; Set the exit status to 1 (error)
    int 0x80        ; Invoke the kernel to exit the program

section .data
    password_prompt db 'Enter the password: ', 0xA    ; Define a prompt message
    password_prompt_len equ $ - password_prompt   ; Calculate the length of the prompt message

    success_msg db 'Success! The password is correct.', 0xA  ; Define a success message
    success_msg_len equ $ - success_msg   ; Calculate the length of the success message

    incorrect_password_msg db 'Error: Incorrect password.', 0xA  ; Define an error message
    incorrect_password_msg_len equ $ - incorrect_password_msg   ; Calculate the length of the error message

section .bss
    user_input resb 20    ; Define a buffer to store the user input

section .text
    ; Compare two strings
    compare_strings:
        mov edi, ebx    ; Move the address of the first string into EDI (source)
        mov esi, ecx    ; Move the address of the second string into ESI (destination)

    compare_loop:
        lodsb           ; Load the byte from the source string (ESI) into AL and increment SI
        cmp al, byte [esi] ; Compare AL with the byte from the destination string (EDI)
        jne compare_not_equal   ; Jump if the bytes are not equal
        test al, al    ; Test if the byte is null (end of string)
        jz compare_equal    ; Jump if the byte is null (end of string)
        jmp compare_loop
