// Walking The PEB

int main(void) {
	char* fmt_address = "0x%08x\n";
	DWORD dwNtdllBase = 0x0;
	HINSTANCE dwLoadLibrary = 0x0;
	
	__asm
	
		xor ebx, ebx 		// Clear the ebx register
		mov ebx, fs:[0x30] 	// Move the address of the PEB (Process Environment Block) into ebx
		
		push ebx 			// Push the PEB address onto the stack
		push ebx 			// Push the PEB address again
		push fmt_address 	// Push the format string for printf onto the stack
		call printf 		// Call the printf function to print the PEB address
		add esp, 8 			// Clean up the stack (pop the two pushed PEB addresses)
		pop ebx 			// Restore the ebx register
		
		mov ebx, [ebx + 0x0C]; // Get the address of the PEB_LDR_DATA structure
		mov ebx, [ebx + 0x1C]; // Get the address of the InInitializationOrderModuleList
		mov ebx, [ebx + 0x08]; // Get the base address of ntdll.dll
		
		mov dwNtdllBase, ebx // Store the base address of ntdll.dll into the dwNtdllBase variable
	}
	
	dwLoadLibrary = LoadLibrary(TEXT("ntdll")); // Load the ntdll.dll module and get its handle
	
	printf("0x%08x <-- 0x%08x\n", dwNtdllBase, dwLoadLibrary); // Print both addresses
}
