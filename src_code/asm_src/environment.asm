section .data
    env_var_name db 'USERNAME', 0  ; Define the name of the environment variable

section .bss
    env_var_value resb 256  ; Reserve space for the environment variable value

section .text
    global _start   ; Entry point for the program

_start:
    ; Call the GetEnvironmentVariableA function to retrieve the value of the environment variable
    mov ebx, env_var_name  ; Move the address of the environment variable name into EBX
    mov ecx, env_var_value ; Move the address of the buffer for the value into ECX
    mov edx, 256           ; Move the maximum number of characters to retrieve into EDX
    call GetEnvironmentVariableA  ; Call the function

    ; Check if the function was successful (return value = length of the environment variable value)
    test eax, eax
    jz error   ; If the function failed, jump to the error label

    ; Print the environment variable value
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, env_var_value  ; Move the address of the buffer containing the environment variable value into ECX
    int 0x80            ; Invoke the kernel to write the value to the standard output

    ; Exit the program
    mov eax, 1      ; Set the system call number for exit (1)
    xor ebx, ebx    ; Set the exit status to 0
    int 0x80        ; Invoke the kernel to exit the program

error:
    ; Print an error message
    mov eax, 4          ; Set the system call number for write (4)
    mov ebx, 1          ; Set the file descriptor for standard output (1)
    mov ecx, error_msg  ; Move the address of the error message into ECX
    int 0x80            ; Invoke the kernel to write the message to the standard output

    ; Exit the program with an error status
    mov eax, 1      ; Set the system call number for exit (1)
    mov ebx, 1      ; Set the exit status to 1 (error)
    int 0x80        ; Invoke the kernel to exit the program

section .data
    error_msg db 'Error: Unable to retrieve environment variable.', 0xA  ; Define an error message
