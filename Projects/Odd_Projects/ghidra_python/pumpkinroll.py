# Ghidra version 9+

import re
from datetime import datetime
from ghidra.program.model.symbol import ReferenceManager
from ghidra.program.model.listing import InstructionIterator
from ghidra.app.decompiler import DecompInterface

def find_functions(currentProgram):
    # Initialize the decompiler
    decompInterface = DecompInterface()
    decompInterface.openProgram(currentProgram)

    # Iterate over all functions in the program
    functions = currentProgram.getFunctionManager().getFunctions(True)
    for function in functions:
        print("Function: " + function.getName())

        # Get the decompiler results for the current function
        results = decompInterface.decompileFunction(function, 60, monitor)

        # Get the HighFunction from the decompiler results
        highFunction = results.getHighFunction()

        # Iterate over all PcodeOps in the HighFunction
        pcodeOpIterator = highFunction.getPcodeOps()
        while pcodeOpIterator.hasNext():
            pcodeOpAST = pcodeOpIterator.next()
            opcode = pcodeOpAST.getOpcode()
            if opcode == 9:  # CALL opcode
                calledAddress = pcodeOpAST.getInput(0).getAddress()
                calledFunction = getFunctionAt(calledAddress)
                if calledFunction is not None:
                    print("    Calls: " + calledFunction.getName())

    # Clean up the decompiler
    decompInterface.dispose()


def find_instructions():
    # Get the current program
    program = getCurrentProgram()

    # Get the instruction iterator
    instructionIterator = program.getListing().getInstructions(True)

    # Iterate over the instructions and print them
    for instruction in instructionIterator:
        address = instruction.getAddress()
        mnemonic = instruction.getMnemonicString()
        numOperands = instruction.getNumOperands()
        operands = []
        for i in range(numOperands):
            operands.append(instruction.getOpObjects(i))
        print("Address: {}, Mnemonic: {}, Operands: {}".format(address, mnemonic, operands))


def find_cross_references():
    # Get the current program
    program = getCurrentProgram()

    # Get the reference manager for the program
    referenceManager = program.getReferenceManager()

    # Prompt the user for input
    include_none_symbols = askYesNo("Find Cross References", "Include lines with 'Symbol: None' in the output?")

    # Iterate over all addresses in the program
    for address in program.getMemory().getAddresses(True):
        # Get the references at the current address
        references = referenceManager.getReferencesTo(address)

        # Iterate over the references and print them
        for reference in references:
            fromAddress = reference.getFromAddress()
            fromSymbol = getSymbolAt(fromAddress)
            toAddress = reference.getToAddress()
            referenceType = reference.getReferenceType()

            # Check if the line should be included based on user input
            if fromSymbol is None and not include_none_symbols:
                continue

            print("From: {}, Symbol: {}, To: {}, Type: {}".format(fromAddress, fromSymbol, toAddress, referenceType))


def find_strings_by_regex_file():
    # Prompt the user to select a file to read the regular expressions from
    file_path = askFile("Select a file", "Please select a file to read the regular expressions from:")

    if file_path is not None:
        # Open the file and read the regular expression lines
        with open(file_path.getAbsolutePath()) as file:
            regex_lines = file.readlines()

        # Access the program listing
        listing = currentProgram.getListing()

        # Retrieve the defined data based on the current selection or all data
        if currentSelection is not None:
            dataIt = listing.getDefinedData(currentSelection, True)
        else:
            dataIt = listing.getDefinedData(True)

        counter = 0
        string_map = {}  # Hash map to store the strings

        # Iterate over each regular expression line
        for regex_line in regex_lines:
            regex = regex_line.strip()

            # Split the regex line by comma and take the first part
            regex = re.split(",", regex)[0]

            if regex:
                # Reset the data iterator for each regex line
                dataIt = listing.getDefinedData(True)

                # Iterate over the defined data
                while dataIt.hasNext() and not monitor.isCancelled():
                    data = dataIt.next()
                    data_type = data.getDataType().getName().lower()

                    # Check if the data type is Unicode or String
                    if "unicode" in data_type or "string" in data_type:
                        s = data.getDefaultValueRepresentation()

                        # Iterate over matches found in the data string
                        for match in re.finditer(regex, s, re.IGNORECASE) or re.search(regex[::-1], s, re.IGNORECASE):
                            address = data.getAddress()
                            counter += 1

                            # Check if the string contains 'u"'
                            if re.search(regex, s, re.IGNORECASE):
                                println("Address: " + str(address) + " , Found String: " + s + " Poss Regex Results: " + regex_line)
                                string_map[str(address)] = s  # Store the string in the hash map

        println(str(counter) + " matching strings were found")

    else:
        println("No file selected.")


# Prompt the user for input
options = ["Functions", "Instructions", "Strings", "Cross References", "All the Above"]
choice = askChoice("Welcome to PumpkinRoll", "Please choose one of the following to find things", options, False)

# Call the respective function based on the choice
if choice == "Functions":
    find_functions(currentProgram)
elif choice == "Instructions":
    find_instructions()
elif choice == "Strings":
    find_strings_by_regex_file()
elif choice == "Cross References":
    find_cross_references()
elif choice == "All the Above":
    find_functions(currentProgram)
    find_instructions()
    find_strings_by_regex_file()
    find_cross_references()

# Output the date and time
now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")
println("Script execution completed on: " + date_time)
