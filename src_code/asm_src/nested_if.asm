section .data
    v1 dd 10    ; First value
    v2 dd 20    ; Second value

section .text
    global _start   ; Entry point

_start:
    ; Load values into registers
    mov eax, [v1]   ; Move value of 'v1' into EAX
    mov ebx, [v2]   ; Move value of 'v2' into EBX

    ; Compare values
    cmp eax, ebx    ; Compare values in EAX and EBX
    jle v1_le_v2    ; Jump if EAX is less than or equal to EBX

    ; Print message and exit if EAX > EBX
    mov eax, 4      ; System call number for write
    mov ebx, 1      ; File descriptor for standard output
    mov ecx, gt_msg    ; Address of the message
    mov edx, gt_msg_len    ; Length of the message
    int 0x80        ; Invoke kernel to write to stdout
    jmp end_prog    ; Jump to exit program

v1_le_v2:
    ; Compare if EAX < EBX - 5
    sub ebx, 5      ; Subtract 5 from EBX
    cmp eax, ebx    ; Compare EAX to EBX
    jge v1_lt_v2_p  ; Jump if EAX >= EBX

    ; Print message and exit if EAX < EBX - 5
    mov eax, 4      ; System call number for write
    mov ebx, 1      ; File descriptor for standard output
    mov ecx, v1_lt_v2_msg  ; Address of the message
    mov edx, v1_lt_v2_msg_len  ; Length of the message
    int 0x80        ; Invoke kernel to write to stdout
    jmp end_prog    ; Jump to exit program

v1_lt_v2_p:
    ; Print message if EAX < EBX - 5
    mov eax, 4      ; System call number for write
    mov ebx, 1      ; File descriptor for standard output
    mov ecx, v1_lt_v2_p_msg    ; Address of the message
    mov edx, v1_lt_v2_p_msg_len    ; Length of the message
    int 0x80        ; Invoke kernel to write to stdout

end_prog:
    ; Exit the program
    mov eax, 1      ; System call number for exit
    xor ebx, ebx    ; Exit status
    int 0x80        ; Invoke kernel to exit

section .data
    gt_msg db 'v1 is greater than v2', 0xA    ; Message for greater than case
    gt_msg_len equ $ - gt_msg  ; Length of the message

    v1_lt_v2_msg db 'v1 is less than v2 - 5', 0xA  ; Message for less than case
    v1_lt_v2_msg_len equ $ - v1_lt_v2_msg  ; Length of the message

    v1_lt_v2_p_msg db 'v1 is less than v2', 0xA  ; Message for less than case
    v1_lt_v2_p_msg_len equ $ - v1_lt_v2_p_msg  ; Length of the message
