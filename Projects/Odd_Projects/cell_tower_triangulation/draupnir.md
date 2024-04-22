Draupnir - Cell Tower Triangulation Tool
===
This is a Python v3.8 script called "Draupnir" that generates a KML file with a circle overlay for a cell tower. The KML file can be used to visualize the coverage area of the cell tower on various KML viewers.
Features

    Calculates the distance variable for the circle overlay using the Friis transmission equation.
    Generates a KML file with a circle overlay for a given cell tower location and parameters.
    Supports customization of cell tower parameters such as receiver gain (Gr), transmitter gain (Gt), transmitter power (Pt), receiver power (Pr), and cellphone frequency (Cf).
    Provides default values for the parameters if not specified.
    Allows specification of an output directory for the generated KML file.
    Displays a dialog box with information on the saved KML file location.
    Provides a Help button to show information about the input parameters and their default values.
    Provides an About button to display information about the script.

Background
===
This project aims to develop an application that provides basic graphical visualization of the Friis Transmission Equation Pr = Pt * (Gt * Gr * (λ/(4πd))^2, which is a key formula in wireless communication. The equation calculates the received power at a receiving antenna by taking into account the transmitted power, antenna gains, wavelength, and distance between antennas. It assumes ideal conditions of free space propagation without obstacles or interference. According to the equation, as the distance between antennas increases, the received power decreases following the inverse square law. The application aims to facilitate the design and analysis of wireless systems, enable estimation of signal strength, and support optimization of antenna configurations. It is crucial, however, to acknowledge the impact of real-world factors and limitations on the equation's accuracy in practical scenarios.

d = sqrt((Gr * Gt * Pt)/Pr)*(Lambda/(4*PI()) 

d = Distance from Tower

sqrt = Squareroot The square root is a mathematical operation that determines the value which, when multiplied by itself, yields a given number. It is denoted by the symbol (√). Taking the square root of a number helps us find the side length of a square with a given area or determine the magnitude of a vector's length in mathematics. The square root operation is used to solve various equations and problems involving quadratic equations, geometry, and physics. It is a fundamental concept in mathematics and is widely utilized in various fields to calculate distances, analyze proportions, and understand the relationship between different quantities.

Gr = Receiver Gain (Perfect World 1) Receiver gain, also known as antenna gain or receiver sensitivity, is a measure of the ability of a receiver to detect and amplify weak incoming signals. It represents the ratio of the power or signal strength at the output of the receiver to the power or signal strength at the input. A higher receiver gain indicates a receiver's increased sensitivity and capability to amplify and extract useful information from low-power signals. Receiver gain is crucial in communication systems as it helps improve the receiver's ability to detect and distinguish weak signals from background noise, enhancing the overall system performance and range. By maximizing receiver gain, the system can achieve better signal reception, improved data accuracy, and extended communication coverage.

Gt = Transmitter Gain (perfect world 1) Transmitter gain is a measure of how effectively a transmitter can direct and radiate power in a specific direction. It quantifies the ability of a transmitter to focus and amplify the transmitted signal in a particular beam or pattern, resulting in a stronger signal in the desired direction and improved coverage. Transmitter gain is important in communication systems as it allows for efficient transmission over long distances and enhances the signal quality and reception at the intended receiver. By optimizing the transmitter's ability to concentrate power in the desired direction, transmitter gain plays a crucial role in improving communication range and reliability.

Pt = Tower Power Transmitted (example: 200-2000 watts)

Pr = Power Received

Lambda = Speed of light = 300,000,00 meters per second / Radio Frequency in Hertz(Hz) In radio, lambda (λ) refers to the wavelength of an electromagnetic wave. It represents the physical distance between two consecutive points of the wave that are in phase. Lambda is inversely related to the frequency of the wave, with higher frequencies having shorter wavelengths. It is a fundamental parameter used in radio engineering to determine antenna dimensions, analyze wave propagation phenomena, and design efficient communication systems. Understanding lambda allows engineers to optimize radio systems, select appropriate antennas, and study the behavior of radio waves in different environments.

Pi = 3.141592653589793 Pi (π) is a mathematical constant that represents the ratio of a circle's circumference to its diameter. It is an irrational number, meaning it cannot be expressed as a finite fraction or a repeating decimal. Pi is approximately equal to 3.14159, but its decimal representation extends infinitely without a pattern. It is a fundamental constant in mathematics and appears in various mathematical equations and formulas across different disciplines, including geometry, trigonometry, calculus, and physics. Pi has fascinated mathematicians throughout history, and its precise value has been calculated to trillions of decimal places. It is an essential concept in understanding the properties of circles, angles, and curves, and plays a significant role in numerous scientific and engineering calculations.

Prerequisites
===
    Ubuntu 18+ or Windows
    Python 3.8 or above
    Tkinter library

Usage
===
    Ensure you have Python 3.8 or above installed on your system.
    Install the required Tkinter library if it is not already installed.
    Run the script using the Python interpreter.
    Fill in the required parameters and optional parameters in the provided entry fields.
    Click the "Add Entry" button to generate the KML file with the circle overlay based on the entered parameters.
    The generated KML file will be saved in the specified output directory or the current working directory if no directory is specified.
    A dialog box will appear with the path to the saved KML file.
    Open the generated KML file in a KML viewer to visualize the cell tower coverage area.

Resources
===
    Possible cell tower information sources:
        OpenCellID
        CellMapper

    Possible KML viewers:
        Doogal KmlViewer
        NSSpot KML Viewer (limited daily uploads)

Disclaimer
===
Please note that this script assumes ideal conditions and does not consider real-world factors such as terrain, interference, atmospheric conditions, or the presence of obstacles. The generated coverage area is an approximation based on the provided parameters and should be used for demonstration purposes only.
