; Title: YesNoMessageBox.asm
; Description: Assembly code to create a Windows message box with "Yes" and "No" buttons

.386
.model flat, stdcall
option casemap:none

include windows.inc
include user32.inc
includelib user32.lib
include kernel32.inc
includelib kernel32.lib

.data
  szCaption       db "Message Box", 0
  szText          db "Do you want to proceed?", 0

.code
start:
  ; Calling MessageBoxA function
  push 0                  ; MB_YESNO style
  push offset szCaption   ; Caption
  push offset szText      ; Text
  push 0                  ; hWnd (handle to owner window, NULL for desktop)
  call MessageBoxA

  ; Check return value
  cmp eax, IDYES
  je  YesClicked
  cmp eax, IDNO
  je  NoClicked

  ; Error handling
  jmp Exit

YesClicked:
  ; Yes button clicked
  ; Handle the action here
  ; For example:
  ; call ProceedFunction
  jmp Exit

NoClicked:
  ; No button clicked
  ; Handle the action here
  ; For example:
  ; call CancelFunction
  jmp Exit

Exit:
  ; Exit the program
  push 0
  call ExitProcess
end start
