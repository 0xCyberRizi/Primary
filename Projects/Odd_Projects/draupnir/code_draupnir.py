# Creator: Anthony Rizi
# Class csc842: Security Tool Development
# Professor: Dr. Welu
# Date 6/25/23
# Cycle 6
# python v3.8 scripting called Draupnir for Odin's Mythological Ring
#possible cell tower information:
#https://antennasearch.com
#https://opencellid.org/
#https://www.cellmapper.net/

# possible kml viewers:
# https://www.doogal.co.uk/KmlViewer
# https://kmlviewer.nsspot.net/ limited daily uploads


import os
import math
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculate_dist_var(Gr, Gt, Pt, Pr, Lambda):
    numerator = math.sqrt((Gr * Gt * Pt) / Pr)
    denominator = (Lambda / (4 * math.pi))
    dist_var = numerator * denominator
    return dist_var

def generate_kml_file(overlayname, lat, lng, dist_var, output_dir):
    kml_template = """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2">
      <Document>
        {placemarks}
      </Document>
    </kml>"""

    placemark_template = """<Placemark>
      <name>{location_name}</name>
      <Point>
        <coordinates>{lng},{lat},0</coordinates>
      </Point>
    </Placemark>
    <Placemark>
      <name>Circle Overlay</name>
      <Style>
        <LineStyle>
          <color>ff0000ff</color>
          <width>1</width>
        </LineStyle>
        <PolyStyle>
          <color>7f00ff00</color>
        </PolyStyle>
      </Style>
      <Polygon>
        <outerBoundaryIs>
          <LinearRing>
            <coordinates>
              {coordinates}
            </coordinates>
          </LinearRing>
        </outerBoundaryIs>
      </Polygon>
    </Placemark>"""

    # Calculate coordinates of the circle
    num_points = 100  # Number of points to approximate the circle
    coordinates = ""
    for i in range(num_points):
        angle = (2 * math.pi * i) / num_points
        lat_i = lat + (math.sin(angle) * dist_var) / 111111
        lng_i = lng + (math.cos(angle) * dist_var) / (111111 * math.cos(lat * math.pi / 180))
        coordinates += f"{lng_i},{lat_i},0\n"

    # Format the placemark with the provided data
    placemark = placemark_template.format(location_name=overlayname, lat=lat, lng=lng, coordinates=coordinates)

    # Determine the output directory
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{overlayname}_{current_datetime}.kml"
        output_path = os.path.join(output_dir, output_filename)
    else:
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{overlayname}_{current_datetime}.kml"
        output_path = output_filename

    # Check if the output file already exists
    file_exists = os.path.exists(output_path)

    # Append or create the KML file
    if file_exists:
        with open(output_path, "r+") as file:
            content = file.read()
            file.seek(0, os.SEEK_END)
            if '</Document>' in content:
                # Append the new placemark before </Document>
                file.seek(content.index('</Document>'))
            file.write(placemark)
            file.write("\n")
    else:
        kml_content = kml_template.format(placemarks=placemark)
        with open(output_path, "w") as file:
            file.write(kml_content)

    messagebox.showinfo("KML File Saved", f"KML file saved successfully at: {output_path}")

def add_entry():
    overlayname = entry_name.get() or "BaseStation"
    Gr = float(entry_gr.get() or 1)
    Gt = float(entry_gt.get() or 1)
    Pt = float(entry_pt.get() or 2000)
    Pr = float(entry_pr.get() or 4.35965E-09)
    Cf = float(entry_cf.get() or 935000000)
    Sl = 300000000  # speed of light
    Lambda = Sl / Cf  # Speed of Light / CellFrequency

    output_dir = entry_output_dir.get() or "/home/ubuntu/Desktop/"
    
    lat_lng = entry_lat_lng.get() or "0.0,0.0"
    lat, lng = map(float, lat_lng.split(","))

    dist_var = calculate_dist_var(Gr, Gt, Pt, Pr, Lambda)
    generate_kml_file(overlayname, lat, lng, dist_var, output_dir)


def show_help():
    help_text = """
Background

This project aims to develop an application that provides basic graphical visualization of the Friis Transmission Equation Pr = Pt * (Gt * Gr * (λ/(4πd))^2, which is a key formula in wireless communication. The equation calculates the received power at a receiving antenna by taking into account the transmitted power, antenna gains, wavelength, and distance between antennas. It assumes ideal conditions of free space propagation without obstacles or interference. According to the equation, as the distance between antennas increases, the received power decreases following the inverse square law. The application aims to facilitate the design and analysis of wireless systems, enable estimation of signal strength, and support optimization of antenna configurations. It is crucial, however, to acknowledge the impact of real-world factors and limitations on the equation's accuracy in practical scenarios.

d = sqrt((Gr * Gt * Pt)/Pr)(Lambda/(4PI())

d = Distance from Tower

sqrt = Squareroot The square root is a mathematical operation that determines the value which, when multiplied by itself, yields a given number. It is denoted by the symbol (√). Taking the square root of a number helps us find the side length of a square with a given area or determine the magnitude of a vector's length in mathematics. The square root operation is used to solve various equations and problems involving quadratic equations, geometry, and physics. It is a fundamental concept in mathematics and is widely utilized in various fields to calculate distances, analyze proportions, and understand the relationship between different quantities.

Gr = Receiver Gain (Perfect World 1) Receiver gain, also known as antenna gain or receiver sensitivity, is a measure of the ability of a receiver to detect and amplify weak incoming signals. It represents the ratio of the power or signal strength at the output of the receiver to the power or signal strength at the input. A higher receiver gain indicates a receiver's increased sensitivity and capability to amplify and extract useful information from low-power signals. Receiver gain is crucial in communication systems as it helps improve the receiver's ability to detect and distinguish weak signals from background noise, enhancing the overall system performance and range. By maximizing receiver gain, the system can achieve better signal reception, improved data accuracy, and extended communication coverage.

Gt = Transmitter Gain (perfect world 1) Transmitter gain is a measure of how effectively a transmitter can direct and radiate power in a specific direction. It quantifies the ability of a transmitter to focus and amplify the transmitted signal in a particular beam or pattern, resulting in a stronger signal in the desired direction and improved coverage. Transmitter gain is important in communication systems as it allows for efficient transmission over long distances and enhances the signal quality and reception at the intended receiver. By optimizing the transmitter's ability to concentrate power in the desired direction, transmitter gain plays a crucial role in improving communication range and reliability.

Pt = Tower Power Transmitted (example: 200-2000 watts)

Pr = Power Received

Lambda = Speed of light = 300,000,00 meters per second / Radio Frequency in Hertz(Hz) In radio, lambda (λ) refers to the wavelength of an electromagnetic wave. It represents the physical distance between two consecutive points of the wave that are in phase. Lambda is inversely related to the frequency of the wave, with higher frequencies having shorter wavelengths. It is a fundamental parameter used in radio engineering to determine antenna dimensions, analyze wave propagation phenomena, and design efficient communication systems. Understanding lambda allows engineers to optimize radio systems, select appropriate antennas, and study the behavior of radio waves in different environments.

Pi = 3.141592653589793 Pi (π) is a mathematical constant that represents the ratio of a circle's circumference to its diameter. It is an irrational number, meaning it cannot be expressed as a finite fraction or a repeating decimal. Pi is approximately equal to 3.14159, but its decimal representation extends infinitely without a pattern. It is a fundamental constant in mathematics and appears in various mathematical equations and formulas across different disciplines, including geometry, trigonometry, calculus, and physics. Pi has fascinated mathematicians throughout history, and its precise value has been calculated to trillions of decimal places. It is an essential concept in understanding the properties of circles, angles, and curves, and plays a significant role in numerous scientific and engineering calculations.
Prerequisites

Ubuntu 18+ or Windows
Python 3.8 or above
Tkinter library

Usage

Ensure you have Python 3.8 or above installed on your system.
Install the required Tkinter library if it is not already installed.
Run the script using the Python interpreter.
Fill in the required parameters and optional parameters in the provided entry fields.
Click the "Add Entry" button to generate the KML file with the circle overlay based on the entered parameters.
The generated KML file will be saved in the specified output directory or the current working directory if no directory is specified.
A dialog box will appear with the path to the saved KML file.
Open the generated KML file in a KML viewer to visualize the cell tower coverage area.

Resources

Possible cell tower information sources:
    OpenCellID
    CellMapper

Possible KML viewers:
    Doogal KmlViewer
    NSSpot KML Viewer (limited daily uploads)

    """

    # Create a new window for displaying help text
    help_window = tk.Toplevel(window)
    help_window.title("Help")

    # Create a text box widget to display the help text
    text_box = tk.Text(help_window, height=200, width=100, wrap="word")
    text_box.insert(tk.END, help_text)
    text_box.pack(expand=True, fill="both")

    def on_help_window_resize(event):
        text_box.config(width=(help_window.winfo_width() - 20) // 8)

    # Configure the help window to auto-adjust its width
    #help_window.update_idletasks()  # Update the window to calculate its size
    #help_window.geometry(f"{help_window.winfo_width()}x400")
    #help_window.bind("<Configure>", on_help_window_resize)

    # Disable text box editing
    text_box.configure(state="disabled")

    # Create a new window for displaying help text
    #help_window = tk.Toplevel(window)
    #help_window.title("Help")

    # Create a text box widget to display the help text
    #text_box = tk.Text(help_window, height=399, width=40)
    #text_box.insert(tk.END, help_text)
    #text_box.pack()

    # Disable text box editing
    text_box.configure(state="disabled")

def show_about():
    about_text = "Draupnir - Cell Tower Triangulation Tool \n ver 1.0 \n Created June 2023 \n By Anthony Rizi \n This application generates a KML file with a circle overlay for a cell tower."
    messagebox.showinfo("About", about_text)

# Create the main window
window = tk.Tk()
window.title("Draupnir - Cell Tower Triangulation")
window.geometry("500x400")

# Create labels and entry fields
label_name = tk.Label(window, text="Overlay Name:")
entry_name = tk.Entry(window, justify='center', width=30)
label_gr = tk.Label(window, text="Gr (Cellphone Receiver Gain):")
entry_gr = tk.Entry(window, justify='center', width=30)
label_gt = tk.Label(window, text="Gt (Celltower Transmitter Gain):")
entry_gt = tk.Entry(window, justify='center', width=30)
label_pt = tk.Label(window, text="Pt (Celltower Transmitter Power):")
entry_pt = tk.Entry(window, justify='center', width=30)
label_pr = tk.Label(window, text="Pr (Celltower Receiver Power):")
entry_pr = tk.Entry(window, justify='center', width=30)
label_cf = tk.Label(window, text="Cf (Cellphone Freq in Hz):")
entry_cf = tk.Entry(window, justify='center', width=30)
label_output_dir = tk.Label(window, text="Output Directory:")
entry_output_dir = tk.Entry(window, justify='center', width=30)
label_lat_lng = tk.Label(window, text="Latitude, Longitude:")
entry_lat_lng = tk.Entry(window, justify='center', width=30)

# Create buttons
button_add_entry = tk.Button(window, text="Add Entry", command=add_entry)
button_help = tk.Button(window, text="Help", command=show_help)
button_about = tk.Button(window, text="About", command=show_about)
button_exit = tk.Button(window, text="Exit", command=window.quit)

# Set default values for entry fields
entry_name.insert(0,"BaseStation")
entry_gr.insert(0, "1")
entry_gt.insert(0, "1")
entry_pt.insert(0, "2000")
entry_pr.insert(0, "4.35965E-09")
entry_cf.insert(0, "935000000")
entry_output_dir.insert(0, "/home/ubuntu/Desktop/")
entry_lat_lng.insert(0, "0.0,0.0")

# Grid layout
label_name.grid(row=0, column=0, sticky="E")
entry_name.grid(row=0, column=1)
label_gr.grid(row=1, column=0, sticky="E")
entry_gr.grid(row=1, column=1)
label_gt.grid(row=2, column=0, sticky="E")
entry_gt.grid(row=2, column=1)
label_pt.grid(row=3, column=0, sticky="E")
entry_pt.grid(row=3, column=1)
label_pr.grid(row=4, column=0, sticky="E")
entry_pr.grid(row=4, column=1)
label_cf.grid(row=5, column=0, sticky="E")
entry_cf.grid(row=5, column=1)
label_output_dir.grid(row=6, column=0, sticky="E")
entry_output_dir.grid(row=6, column=1)
label_lat_lng.grid(row=7, column=0, sticky="E")
entry_lat_lng.grid(row=7, column=1)

button_add_entry.grid(row=8, column=0, pady=10)
button_help.grid(row=8, column=1, pady=10)
button_about.grid(row=9, column=0, pady=10)
button_exit.grid(row=9, column=1, pady=10)

# Start the GUI event loop
window.mainloop()
