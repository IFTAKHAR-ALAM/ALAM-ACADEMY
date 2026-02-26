"""
ALAM-ACADEMY IT & Computer Science Book Generator
Generates a comprehensive PDF book with definitions, descriptions, step-by-step examples
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import os

# Academy Information
ACADEMY_NAME = "ALAM-ACADEMY"
OWNER_NAME = "M IFTIKHAR ALAM"
CONTACT = "0333-9257987"
EMAIL = "alammiftikhar@gmail.com"
GITHUB = "https://github.com/IFTAKHAR-ALAM/ALAM-ACADEMY"
ADDRESS = "Karachi, PAKISTAN"

BOOK_TITLE = "IT & COMPUTER SCIENCE"
SUBTITLE = "A Comprehensive Guide with Definitions, Descriptions & Step-by-Step Examples"

def get_book_content():
    """Generate comprehensive book content with definitions, descriptions, and examples"""
    chapters = []
    
    # Chapter 1: Introduction to Computer Science
    chapters.append({
        'title': 'Chapter 1: Introduction to Computer Science',
        'content': """
1.1 DEFINITION: Computer Science

Computer Science is the systematic study of computation, automation, algorithms, data structures, and information processing using computers.

Detailed Description:
Computer Science encompasses both theoretical foundations and practical applications. It involves understanding how computers work, how to solve problems using computational thinking, and how to design efficient algorithms and software systems.

Key Components:
- Algorithms: Step-by-step procedures for solving problems
- Data Structures: Methods for organizing and storing data
- Programming: Writing instructions for computers to execute
- Theory: Mathematical foundations of computation
- Applications: Real-world problem solving using computers

Example: When you use a search engine like Google, computer science principles are applied:
- Algorithms determine which results are most relevant
- Data structures store billions of web pages efficiently
- Programming creates the user interface and backend systems
- Theory ensures the search completes in milliseconds

1.2 DEFINITION: Algorithm

An Algorithm is a finite sequence of well-defined, computer-implementable instructions designed to solve a class of problems or perform a computation.

Step-by-Step Example: Making a Cup of Tea (as an algorithm)

Step 1: START
Step 2: Fill kettle with water
Step 3: Turn on kettle and wait for boiling
Step 4: Place tea bag in cup
Step 5: Pour boiling water into cup
Step 6: Wait 3 minutes for tea to steep
Step 7: Remove tea bag
Step 8: Add milk and sugar (optional)
Step 9: Stir the tea
Step 10: END

Programming Example: Simple Algorithm to Add Two Numbers

def add_numbers(num1, num2):
    # Step 1: Receive two numbers as input
    # Step 2: Add the numbers together
    result = num1 + num2
    # Step 3: Return the result
    return result

# Usage:
sum = add_numbers(5, 3)
print(sum)  # Output: 8

1.3 DEFINITION: Data Structure

A Data Structure is a specialized format for organizing, processing, retrieving, and storing data in a computer so that it can be used efficiently.

Types of Data Structures with Examples:

1. Array: A collection of elements stored at contiguous memory locations

Example:
students = ["Ali", "Ahmed", "Sara", "Fatima"]
# Access first student: students[0] = "Ali"
# Access third student: students[2] = "Sara"

2. Stack: Last-In-First-Out (LIFO) structure

Example: Browser Back Button
- You visit: Google → YouTube → Facebook → Twitter
- Press Back: Returns to Facebook (last visited)
- Press Back: Returns to YouTube
- Press Back: Returns to Google

3. Queue: First-In-First-Out (FIFO) structure

Example: Printer Queue
- Document A sent to printer first
- Document B sent second
- Document C sent third
- Printer prints: A → B → C (in order received)

4. Linked List: Elements linked via pointers

Example: Train cars connected together
- Each car (node) contains data and connection to next car
- Can easily add/remove cars without reorganizing entire train

1.4 DEFINITION: Programming

Programming is the process of creating a set of instructions that tell a computer how to perform a task.

Step-by-Step Programming Process:

Step 1: Problem Definition
- Clearly understand what needs to be solved
- Example: Calculate student grade average

Step 2: Algorithm Design
- Plan the solution steps
- Example: Add all grades, divide by number of grades

Step 3: Code Writing
- Translate algorithm into programming language
Example in Python:
def calculate_average(grades):
    total = sum(grades)
    count = len(grades)
    average = total / count
    return average

Step 4: Testing
- Run the program with sample data
grades = [85, 90, 78, 92, 88]
result = calculate_average(grades)
print(f"Average: {result}")  # Output: Average: 86.6

Step 5: Debugging
- Fix any errors found during testing

Step 6: Documentation
- Add comments and user instructions

1.5 DEFINITION: Software Development Life Cycle (SDLC)

SDLC is a systematic process for building software that ensures the quality and correctness of the software built.

Phases with Examples:

Phase 1: Requirements Gathering
- Collect what the software should do
- Example: Client needs an online shopping website
- Features: Product catalog, shopping cart, checkout, payment

Phase 2: Design
- Plan the architecture and user interface
- Example: Create wireframes, database schema
- Database tables: Users, Products, Orders, Payments

Phase 3: Implementation (Coding)
- Write the actual code
- Example: Develop frontend with HTML/CSS/JavaScript
- Develop backend with Python/Node.js/PHP

Phase 4: Testing
- Verify the software works correctly
- Example: Test adding items to cart, checkout process
- Fix bugs found during testing

Phase 5: Deployment
- Release the software to users
- Example: Upload website to web server
- Make it accessible at www.example.com

Phase 6: Maintenance
- Update and fix issues after release
- Example: Add new features, security patches
- Respond to user feedback
"""
    })
    
    # Chapter 2: Computer Hardware
    chapters.append({
        'title': 'Chapter 2: Computer Hardware - Definitions & Examples',
        'content': """
2.1 DEFINITION: Computer Hardware

Computer Hardware refers to the physical, tangible components of a computer system that can be seen and touched.

Detailed Description:
Hardware includes all electronic and mechanical parts that make up a computer. Without hardware, software has nothing to run on. Hardware executes the instructions provided by software.

Classification of Hardware:
1. Input Devices: Keyboard, Mouse, Scanner
2. Output Devices: Monitor, Printer, Speakers
3. Processing Devices: CPU, GPU
4. Storage Devices: HDD, SSD, RAM
5. Communication Devices: Network Card, Modem

2.2 DEFINITION: Central Processing Unit (CPU)

The CPU (Central Processing Unit) is the primary component of a computer that performs most of the processing inside a computer. It is called the "brain" of the computer.

Detailed Description:
The CPU executes instructions from programs by performing basic arithmetic, logic, controlling, and input/output operations specified by the instructions.

CPU Components:

1. ALU (Arithmetic Logic Unit):
   - Performs mathematical operations (+, -, *, /)
   - Performs logical operations (AND, OR, NOT)
   - Example: 5 + 3 = 8 (calculated by ALU)

2. Control Unit (CU):
   - Directs the flow of data
   - Fetches instructions from memory
   - Decodes what the instruction means
   - Executes the instruction

3. Registers:
   - Small, fast storage locations within CPU
   - Hold data temporarily during processing
   - Example: Accumulator register holds calculation results

Step-by-Step CPU Operation:

Step 1: FETCH
- CPU gets instruction from RAM
- Example: Instruction "ADD A, B" is fetched

Step 2: DECODE
- CPU understands what instruction means
- "ADD A, B" means add values in A and B

Step 3: EXECUTE
- CPU performs the operation
- ALU adds the values: 5 + 3 = 8

Step 4: STORE
- Result is stored back in memory
- Value 8 is stored in register C

Example: CPU Specifications Explained

Intel Core i7-12700K:
- Cores: 12 (8 performance + 4 efficiency)
- Threads: 20 (can handle 20 tasks simultaneously)
- Base Clock: 3.6 GHz (3.6 billion cycles per second)
- Boost Clock: 5.0 GHz (maximum speed)
- Cache: 25 MB (fast internal memory)

Real-World Performance Example:
- Single-core tasks (gaming): Uses high clock speed
- Multi-core tasks (video editing): Uses all cores
- More cores = better multitasking

2.3 DEFINITION: Memory (RAM)

RAM (Random Access Memory) is a type of computer memory that can be accessed randomly; any byte of memory can be accessed without touching the preceding bytes.

Detailed Description:
RAM is volatile memory, meaning it loses its data when power is turned off. It stores data that the CPU needs quick access to while the computer is running.

Types of RAM:

1. DRAM (Dynamic RAM):
   - Needs constant refreshing to hold data
   - Used for main system memory
   - Example: DDR4, DDR5 modules

2. SRAM (Static RAM):
   - Does not need refreshing
   - Faster but more expensive
   - Example: CPU cache memory

Step-by-Step: How RAM Works

Step 1: Program Launch
- User double-clicks Chrome icon

Step 2: Loading to RAM
- Operating system loads Chrome from hard drive to RAM
- Reason: RAM is much faster than hard drive

Step 3: Execution
- CPU accesses Chrome from RAM for quick processing
- Tabs, bookmarks, and settings loaded in RAM

Step 4: Multitasking
- Open Word, Excel, and Spotify
- Each application uses portion of RAM
- 8GB RAM example:
  * Chrome: 2GB
  * Word: 500MB
  * Excel: 400MB
  * Spotify: 300MB
  * Windows: 3GB
  * Available: 1.8GB

Step 5: Closing Application
- When you close Chrome, RAM is freed
- That memory becomes available for other programs

RAM Capacity Examples:

4GB RAM: Basic tasks (web browsing, documents)
8GB RAM: Moderate multitasking, light gaming
16GB RAM: Gaming, video editing, heavy multitasking
32GB RAM: Professional video editing, 3D rendering
64GB+ RAM: Servers, workstations, virtual machines

2.4 DEFINITION: Storage Devices

Storage Devices are hardware components that store data permanently or semi-permanently in a computer system.

Detailed Description:
Unlike RAM, storage devices retain data even when power is turned off. They are used for long-term data storage.

Types of Storage with Examples:

1. HDD (Hard Disk Drive):

Definition: A storage device that uses magnetic storage to store data on spinning platters.

How it Works (Step-by-Step):
Step 1: Platters spin at high speed (5400-7200 RPM)
Step 2: Read/write head moves to correct position
Step 3: Magnetic particles on platter represent 0s and 1s
Step 4: Head reads magnetic patterns as data
Step 5: Data is sent to computer

Example Specifications:
- Capacity: 1TB, 2TB, 4TB
- Speed: 7200 RPM
- Interface: SATA III (6 Gbps)
- Use Case: Bulk storage, backups

2. SSD (Solid State Drive):

Definition: A storage device that uses flash memory to store data with no moving parts.

How it Works (Step-by-Step):
Step 1: Data arrives as electrical signals
Step 2: Controller converts to binary data
Step 3: Data stored in NAND flash cells
Step 4: Each cell holds electrical charge (0 or 1)
Step 5: Reading detects charge level

Example Specifications:
- Capacity: 256GB, 500GB, 1TB, 2TB
- Speed: Read 3500 MB/s, Write 3000 MB/s
- Interface: NVMe PCIe
- Use Case: Operating system, applications, games

Comparison Example:

Task: Boot Windows 10
- HDD: 45-60 seconds
- SSD: 10-15 seconds

Task: Launch Photoshop
- HDD: 25-30 seconds
- SSD: 5-8 seconds

Task: Copy 10GB file
- HDD: 3-4 minutes
- SSD: 30-45 seconds

3. External Storage:

USB Flash Drive:
- Portable storage device
- Example: 32GB, 64GB, 128GB
- Use: Transfer files between computers

External Hard Drive:
- Larger capacity portable storage
- Example: 1TB, 2TB, 5TB
- Use: Backups, media storage

Cloud Storage:
- Remote servers accessed via internet
- Example: Google Drive, OneDrive, Dropbox
- Use: Sync files across devices, backup

2.5 DEFINITION: Motherboard

A Motherboard is the main printed circuit board (PCB) in a computer that connects all components together and allows them to communicate.

Detailed Description:
The motherboard is the backbone of a computer system. It distributes power to all components and provides pathways for data to travel between components.

Motherboard Components with Examples:

1. CPU Socket:
   - Holds the processor
   - Example: LGA 1700 (Intel), AM4 (AMD)
   - Must match CPU type

2. RAM Slots:
   - Hold memory modules
   - Example: 4 DDR4 slots, up to 128GB
   - Dual-channel for better performance

3. PCIe Slots:
   - Connect expansion cards
   - Example: PCIe x16 for graphics card
   - PCIe x1 for sound card, network card

4. SATA Ports:
   - Connect storage devices
   - Example: 6 SATA III ports
   - Connect HDD, SSD, optical drives

5. M.2 Slot:
   - Connect NVMe SSDs directly
   - Example: M.2 PCIe 4.0 x4
   - Faster than SATA

6. I/O Ports:
   - External connections
   - Example: USB 3.0, USB-C, HDMI, Ethernet
   - Connect peripherals

Step-by-Step: Data Flow Through Motherboard

Step 1: User Input
- Press keyboard key "A"

Step 2: Signal to Motherboard
- USB port receives signal
- Signal travels through motherboard traces

Step 3: To CPU
- Signal reaches CPU via chipset
- CPU processes the input

Step 4: To RAM
- CPU may store data temporarily in RAM
- Quick access for processing

Step 5: To Output
- Result sent to monitor via graphics card
- Letter "A" appears on screen

Motherboard Form Factors:

ATX: 12 × 9.6 inches (standard desktop)
Micro-ATX: 9.6 × 9.6 inches (compact)
Mini-ITX: 6.7 × 6.7 inches (small form factor)
"""
    })
    
    # Chapter 3: Input/Output Devices
    chapters.append({
        'title': 'Chapter 3: Input and Output Devices',
        'content': """
3.1 DEFINITION: Input Devices

Input Devices are hardware components that allow users to send data and control signals to a computer for processing.

Detailed Description:
Input devices convert human actions (typing, clicking, speaking) into digital signals that the computer can understand and process.

Keyboard - Detailed Example:

Definition: An input device with keys that represent letters, numbers, and functions.

Types of Keyboards:

1. Membrane Keyboard:
   - Rubber membrane under keys
   - Quiet operation
   - Example: Standard office keyboards
   - Price: $10-30

2. Mechanical Keyboard:
   - Individual mechanical switches
   - Tactile feedback, audible click
   - Example: Gaming keyboards
   - Switch types:
     * Blue: Clicky, tactile (typing)
     * Red: Linear, smooth (gaming)
     * Brown: Tactile, quiet (both)
   - Price: $50-200

Step-by-Step: How Keyboard Works

Step 1: Key Press
- User presses "A" key

Step 2: Switch Activation
- Key cap pushes down on switch
- Switch completes electrical circuit

Step 3: Signal Generation
- Keyboard controller detects circuit closure
- Generates scan code for "A" key

Step 4: USB Transmission
- Scan code sent via USB cable
- Data packet: 0x1C (scan code for "A")

Step 5: OS Processing
- Operating system receives scan code
- Keyboard driver translates to character
- "A" sent to active application

Mouse - Detailed Example:

Definition: A pointing device that detects two-dimensional motion relative to a surface.

Types of Mice:

1. Optical Mouse:
   - Uses LED light
   - Works on most surfaces
   - Example: Logitech M185
   - DPI: 1000-1600

2. Laser Mouse:
   - Uses laser light
   - Works on glossy surfaces
   - Example: Logitech MX Master
   - DPI: 1000-4000

3. Gaming Mouse:
   - High precision sensor
   - Programmable buttons
   - Example: Razer DeathAdder
   - DPI: Up to 20000

Step-by-Step: How Mouse Works

Step 1: Movement Detection
- User moves mouse on surface
- Sensor captures images of surface

Step 2: Image Processing
- DSP (Digital Signal Processor) analyzes images
- Compares consecutive images
- Calculates direction and distance

Step 3: Coordinate Calculation
- Movement converted to X, Y coordinates
- Example: Move right 5 units, up 3 units

Step 4: Signal Transmission
- Coordinates sent to computer via USB
- 1000 Hz polling rate = 1000 reports per second

Step 5: Cursor Movement
- Operating system updates cursor position
- Cursor moves on screen accordingly

3.2 DEFINITION: Output Devices

Output Devices are hardware components that receive data from a computer and convert it into human-perceptible form.

Detailed Description:
Output devices convert digital signals from the computer into forms that humans can understand: visual (monitors), audio (speakers), or physical (printers).

Monitor - Detailed Example:

Definition: An electronic visual display for computers.

Types of Display Technology:

1. LCD (Liquid Crystal Display):
   - Uses liquid crystals with backlight
   - Example: Standard office monitors
   - Price: $100-300

2. LED (Light Emitting Diode):
   - LCD with LED backlight
   - Better energy efficiency
   - Example: Most modern monitors
   - Price: $150-500

3. OLED (Organic LED):
   - Each pixel produces its own light
   - Perfect blacks, vibrant colors
   - Example: High-end monitors, TVs
   - Price: $500-2000

Monitor Specifications Explained:

Resolution:
- Definition: Number of pixels on screen
- Examples:
  * Full HD: 1920 × 1080 = 2 million pixels
  * QHD: 2560 × 1440 = 3.7 million pixels
  * 4K: 3840 × 2160 = 8.3 million pixels
- More pixels = sharper image

Refresh Rate:
- Definition: How many times screen updates per second
- Examples:
  * 60Hz: Standard (60 updates/second)
  * 144Hz: Gaming (144 updates/second)
  * 240Hz: Professional gaming
- Higher = smoother motion

Response Time:
- Definition: Time for pixel to change color
- Examples:
  * 1ms: Excellent (gaming)
  * 5ms: Good (general use)
  * 10ms: Acceptable (office work)
- Lower = less motion blur

Step-by-Step: How Monitor Displays Image

Step 1: Graphics Processing
- Graphics card renders image
- Converts 3D scene to 2D image
- Example: Video game frame

Step 2: Signal Transmission
- Image sent via HDMI/DisplayPort
- Digital signal with color information
- Each pixel has RGB values

Step 3: Pixel Activation
- Monitor receives pixel data
- Each pixel activated with specific color
- 1920×1080 = 2,073,600 pixels activated

Step 4: Backlight (LCD/LED)
- Backlight illuminates pixels
- Liquid crystals control light passage
- Color filters create RGB colors

Step 5: Image Display
- Human eye perceives combined pixels
- Brain interprets as complete image
- 60 times per second (60Hz)

Printer - Detailed Example:

Definition: A device that produces a physical copy of digital documents.

Types of Printers:

1. Inkjet Printer:
   - Sprays liquid ink on paper
   - Good for photos
   - Example: Canon PIXMA
   - Price: $50-200

2. Laser Printer:
   - Uses toner and heat
   - Fast, good for text
   - Example: HP LaserJet
   - Price: $150-500

3. 3D Printer:
   - Creates three-dimensional objects
   - Layers of plastic/metal
   - Example: Creality Ender 3
   - Price: $200-1000

Step-by-Step: How Laser Printer Works

Step 1: Data Reception
- Printer receives document from computer
- Example: Word document sent to print

Step 2: Raster Image Processing
- Printer converts document to bitmap
- Each dot mapped to toner placement
- Resolution: 600-1200 DPI (dots per inch)

Step 3: Charging Drum
- Photosensitive drum receives uniform charge
- Example: Negative electrostatic charge
- Drum rotates continuously

Step 4: Laser Writing
- Laser beam draws image on drum
- Discharges areas where toner should stick
- Creates electrostatic image

Step 5: Toner Application
- Toner (powdered ink) applied to drum
- Toner sticks to charged areas
- Color: Cyan, Magenta, Yellow, Black (CMYK)

Step 6: Transfer to Paper
- Paper passes by drum
- Toner transferred from drum to paper
- Opposite charge pulls toner

Step 7: Fusing
- Paper passes through hot rollers (200°C)
- Toner melts and bonds with paper
- Permanent image created

Step 8: Output
- Printed page exits printer
- Drum cleaned for next page
- Process repeats for each page

3.3 DEFINITION: Input/Output (I/O) Devices

I/O Devices are hardware components that can both send data to a computer and receive data from a computer.

Detailed Description:
I/O devices serve dual purposes, acting as both input and output interfaces.

Examples of I/O Devices:

1. Touchscreen:
   - Input: Touch gestures
   - Output: Visual display
   - Example: Smartphones, tablets, kiosks

2. Network Card:
   - Input: Receives data from network
   - Output: Sends data to network
   - Example: Ethernet card, Wi-Fi adapter

3. Sound Card:
   - Input: Microphone input
   - Output: Speaker output
   - Example: Audio interface cards

4. USB Drive:
   - Input: Reading data from drive
   - Output: Writing data to drive
   - Example: Flash drives, external SSDs

Step-by-Step: Touchscreen Operation

Step 1: Display Output
- Screen shows user interface
- Example: App icons on smartphone

Step 2: Touch Input
- User taps icon with finger
- Capacitive sensor detects touch

Step 3: Coordinate Detection
- Touch location calculated (X, Y)
- Example: X=500, Y=300 pixels

Step 4: Processing
- Operating system interprets touch
- Determines which icon was tapped

Step 5: Response Output
- Application opens
- Screen updates with new content
- Haptic feedback (vibration)

Step 6: Continuous Interaction
- User scrolls, types, swipes
- Continuous input/output cycle
"""
    })
    
    # Chapter 4: Software
    chapters.append({
        'title': 'Chapter 4: Software - Definitions & Examples',
        'content': """
4.1 DEFINITION: Software

Software is a collection of programs, data, and instructions that tell a computer how to perform specific tasks.

Detailed Description:
Software is intangible (cannot be touched) and exists as code stored on storage devices. When executed, software is loaded into RAM and processed by the CPU.

Classification of Software:

1. System Software
   - Operating Systems
   - Device Drivers
   - Utilities

2. Application Software
   - Productivity (Word, Excel)
   - Entertainment (Games, Media)
   - Education (E-learning)

4.2 DEFINITION: Operating System

An Operating System (OS) is system software that manages computer hardware and software resources and provides common services for computer programs.

Detailed Description:
The OS acts as an intermediary between users and computer hardware. It manages memory, processes, files, and provides user interface.

Functions of Operating System:

1. Process Management:
   - Creates, schedules, and terminates processes
   - Example: Running Chrome, Word, and Spotify simultaneously
   - CPU scheduling decides which process runs when

2. Memory Management:
   - Allocates and deallocates memory
   - Example: Chrome gets 500MB, Word gets 200MB
   - Virtual memory extends RAM using hard drive

3. File Management:
   - Organizes files in directories
   - Example: C:\\Users\\Documents\\file.txt
   - Controls read, write, execute permissions

4. Device Management:
   - Controls hardware devices via drivers
   - Example: Printer driver, graphics driver
   - Plug and Play automatically detects devices

5. Security:
   - User authentication (passwords)
   - File permissions
   - Example: Administrator vs Standard user

Windows Operating System - Step-by-Step Boot Process:

Step 1: Power On
- User presses power button
- Power supply activates motherboard

Step 2: BIOS/UEFI
- Basic Input/Output System initializes
- POST (Power-On Self-Test) checks hardware
- RAM, CPU, storage verified

Step 3: Bootloader
- BIOS finds boot device (SSD/HDD)
- Loads Windows Boot Manager
- Location: EFI partition

Step 4: Kernel Loading
- Windows kernel loaded into RAM
- Core system files initialized
- Drivers loaded for hardware

Step 5: System Initialization
- Windows services start
- Registry loaded
- User profile prepared

Step 6: Login Screen
- User authentication required
- Enter username and password
- Windows verifies credentials

Step 7: Desktop Loaded
- User interface appears
- Startup programs launch
- System ready for use

Linux Operating System - Example Commands:

File Operations:
ls              # List files
cd Documents    # Change directory
mkdir NewFolder # Create directory
cp file1 file2  # Copy file
mv file1 file2  # Move/rename file
rm file         # Remove file

System Information:
uname -a        # System information
df -h           # Disk space
free -m         # Memory usage
top             # Process viewer

4.3 DEFINITION: Application Software

Application Software is a program or group of programs designed to perform specific tasks for users.

Detailed Description:
Unlike system software, application software is designed for end-users to accomplish specific goals like writing documents, browsing the web, or editing photos.

Types with Examples:

1. Word Processing Software:
   - Purpose: Create and edit documents
   - Examples: Microsoft Word, Google Docs
   - Features: Formatting, spell check, templates

Step-by-Step: Creating a Document in Word

Step 1: Launch Application
- Click Word icon
- Application loads into RAM
- Blank document opens

Step 2: Enter Text
- Type: "Hello, World!"
- Keyboard input captured
- Text appears on screen

Step 3: Format Text
- Select text with mouse
- Click Bold button
- Font size changed to 14
- Text color changed to blue

Step 4: Insert Image
- Click Insert → Pictures
- Browse and select image
- Image placed in document
- Resize and position

Step 5: Save Document
- Click File → Save As
- Choose location: Documents folder
- Filename: "MyDocument.docx"
- Click Save

Step 6: Print Document
- Click File → Print
- Select printer
- Choose number of copies
- Click Print button

2. Spreadsheet Software:
   - Purpose: Organize and analyze data
   - Examples: Microsoft Excel, Google Sheets
   - Features: Formulas, charts, pivot tables

Example: Creating a Budget in Excel

    A           B           C
1   Item        Cost        Quantity
2   Pen         10          5
3   Notebook    50          3
4   Total       =B2*C2+B3*C3

Formula Explanation:
- B2*C2 = 10 × 5 = 50 (Pen total)
- B3*C3 = 50 × 3 = 150 (Notebook total)
- Total = 50 + 150 = 200

3. Web Browser Software:
   - Purpose: Access and view websites
   - Examples: Chrome, Firefox, Edge
   - Features: Tabs, bookmarks, extensions

Step-by-Step: How Browser Works

Step 1: Enter URL
- Type: www.google.com
- Browser parses the URL

Step 2: DNS Lookup
- Browser asks DNS server for IP
- www.google.com → 142.250.185.68

Step 3: HTTP Request
- Browser sends request to server
- GET / HTTP/1.1
- Host: www.google.com

Step 4: Server Response
- Server sends HTML, CSS, JavaScript
- Status: 200 OK
- Content-Type: text/html

Step 5: Rendering
- Browser parses HTML
- Builds DOM (Document Object Model)
- Applies CSS styles
- Executes JavaScript

Step 6: Display
- Webpage rendered on screen
- User can interact with page
- Click links, submit forms

4.4 DEFINITION: Programming Software

Programming Software is a set of tools used by developers to create, debug, maintain, and support other software.

Detailed Description:
Programming software provides the environment and tools necessary for writing and testing code.

Types of Programming Software:

1. Text Editors:
   - Simple code editing
   - Examples: Notepad++, Sublime Text, VS Code
   - Features: Syntax highlighting, code completion

2. IDE (Integrated Development Environment):
   - Complete development environment
   - Examples: Visual Studio, IntelliJ, Eclipse
   - Features: Editor, debugger, compiler, tester

3. Compilers:
   - Convert source code to machine code
   - Examples: GCC, Clang, MSVC
   - Example: C++ code → Executable

4. Interpreters:
   - Execute code line by line
   - Examples: Python interpreter, Node.js
   - Example: Python code → Direct execution

Step-by-Step: Creating a Program in Python

Step 1: Install Python
- Download from python.org
- Run installer
- Check "Add Python to PATH"
- Click Install

Step 2: Write Code
- Open text editor or IDE
- Type the following code:

def greet(name):
    return f"Hello, {name}!"

print(greet("World"))

Step 3: Save File
- Save as: hello.py
- Location: C:\\Projects\\

Step 4: Run Program
- Open Command Prompt
- Navigate to folder: cd C:\\Projects\\
- Run: python hello.py

Step 5: View Output
- Program executes
- Output displayed: Hello, World!

Step 6: Debug (if needed)
- Add print statements
- Use debugger to step through code
- Fix any errors

4.5 DEFINITION: Utility Software

Utility Software is system software designed to help analyze, configure, optimize, or maintain a computer system.

Detailed Description:
Utility programs perform specific maintenance tasks to keep the computer running smoothly.

Types with Examples:

1. Antivirus Software:
   - Purpose: Protect against malware
   - Examples: Windows Defender, Norton, Kaspersky
   - Features: Real-time scanning, quarantine

Step-by-Step: Virus Scan Process

Step 1: Initiate Scan
- User clicks "Scan Now"
- Or scheduled scan starts

Step 2: File Analysis
- Antivirus reads each file
- Compares against virus database
- Example: 100,000+ virus signatures

Step 3: Heuristic Analysis
- Checks for suspicious behavior
- Identifies unknown threats
- Example: File trying to modify system files

Step 4: Threat Detection
- Virus found: Trojan.exe
- Matched signature: Trojan.Win32.Generic

Step 5: Action Taken
- File quarantined (isolated)
- User notified
- Option to delete or restore

Step 6: Report Generated
- Scan complete summary
- Files scanned: 50,000
- Threats found: 1
- Time taken: 15 minutes

2. Disk Cleanup Utility:
   - Purpose: Free up disk space
   - Example: Windows Disk Cleanup
   - Features: Remove temporary files, cache

3. Backup Software:
   - Purpose: Create copies of data
   - Examples: Acronis, Time Machine
   - Features: Scheduled backups, cloud sync

4. File Compression:
   - Purpose: Reduce file size
   - Examples: WinZip, 7-Zip, WinRAR
   - Features: Compress, extract archives

Step-by-Step: Compressing Files with 7-Zip

Step 1: Select Files
- Right-click folder to compress
- Example: "MyDocuments" folder

Step 2: Choose 7-Zip
- Select: 7-Zip → Add to archive
- Compression window opens

Step 3: Configure Settings
- Archive format: 7z or zip
- Compression level: Ultra
- Password: (optional)

Step 4: Start Compression
- Click OK
- Files compressed
- Original: 100MB
- Compressed: 60MB (40% reduction)

Step 5: Archive Created
- New file: MyDocuments.7z
- Original files can be deleted
- Extract when needed
"""
    })
    
    # Chapter 5: Programming Languages
    chapters.append({
        'title': 'Chapter 5: Programming Languages with Examples',
        'content': """
5.1 DEFINITION: Programming Language

A Programming Language is a formal language comprising a set of instructions that produce various kinds of output when executed by a computer.

Detailed Description:
Programming languages provide syntax (grammar rules) and semantics (meaning) for writing programs. They allow humans to communicate with computers in a more understandable way than machine code.

Levels of Programming Languages:

1. Low-Level Languages:
   - Close to machine code
   - Example: Assembly language
   - Fast but difficult to write

2. High-Level Languages:
   - Closer to human language
   - Example: Python, Java, JavaScript
   - Easier to read and write

5.2 DEFINITION: Syntax

Syntax refers to the set of rules that define the combinations of symbols that are considered to be correctly structured programs in a programming language.

Detailed Description:
Just as human languages have grammar rules, programming languages have syntax rules. Violating these rules results in syntax errors.

Example: Python Syntax

# Correct syntax:
if age >= 18:
    print("Adult")

# Incorrect syntax (error):
if age >= 18
    print("Adult")
# Missing colon causes SyntaxError

Example: JavaScript Syntax

// Correct syntax:
function greet(name) {
    return "Hello, " + name;
}

// Incorrect syntax (error):
function greet(name)
    return "Hello, " + name;
}
// Missing opening brace causes SyntaxError

5.3 DEFINITION: Variable

A Variable is a named storage location in memory that holds a value which can be changed during program execution.

Detailed Description:
Variables have a name (identifier), a data type, and a value. They allow programs to store and manipulate data.

Step-by-Step: Working with Variables in Python

Step 1: Variable Declaration
- Create a variable with a name
- Example: age = 25
- Name: age, Value: 25

Step 2: Variable Usage
- Use variable in operations
- Example: next_year = age + 1
- Result: next_year = 26

Step 3: Variable Modification
- Change the value
- Example: age = 26
- Old value (25) replaced with new value (26)

Step 4: Variable Display
- Show the value
- Example: print(age)
- Output: 26

Data Types with Examples:

1. Integer (int):
   - Whole numbers
   - Example: age = 25
   - Example: count = 100

2. Float (float):
   - Decimal numbers
   - Example: price = 19.99
   - Example: pi = 3.14159

3. String (str):
   - Text data
   - Example: name = "Ali"
   - Example: message = 'Hello'

4. Boolean (bool):
   - True or False
   - Example: is_active = True
   - Example: has_error = False

5.4 DEFINITION: Function

A Function is a named block of code that performs a specific task and can be called (executed) from other parts of the program.

Detailed Description:
Functions promote code reusability and modularity. They can accept input (parameters) and return output (return value).

Step-by-Step: Creating and Using Functions

Step 1: Function Definition
- Declare function with name and parameters
Example in Python:
def calculate_area(length, width):
    area = length * width
    return area

Step 2: Function Call
- Execute the function with arguments
result = calculate_area(10, 5)

Step 3: Parameter Assignment
- Arguments assigned to parameters
- length = 10
- width = 5

Step 4: Code Execution
- Function body runs
- area = 10 * 5 = 50

Step 5: Return Value
- Result sent back to caller
- return 50

Step 6: Result Usage
- Returned value stored in variable
- result = 50
- print(result)  # Output: 50

Complete Example with Multiple Functions:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Using the functions
num1 = 20
num2 = 5

print(f"Addition: {add(num1, num2)}")      # 25
print(f"Subtraction: {subtract(num1, num2)}")  # 15
print(f"Multiplication: {multiply(num1, num2)}")  # 100
print(f"Division: {divide(num1, num2)}")    # 4.0

5.5 DEFINITION: Loop

A Loop is a programming construct that repeats a block of code multiple times until a specified condition is met.

Detailed Description:
Loops automate repetitive tasks, making code more efficient. There are two main types: for loops and while loops.

For Loop - Step-by-Step Example:

# Print numbers 1 to 5
for i in range(1, 6):
    print(i)

Execution Steps:

Step 1: Initialize
- i = 1 (first value in range)

Step 2: Check Condition
- Is i <= 5? Yes
- Execute loop body

Step 3: Execute Body
- print(1)
- Output: 1

Step 4: Increment
- i = i + 1 = 2

Step 5: Repeat
- Check condition: Is 2 <= 5? Yes
- print(2)
- Continue until i = 6

Step 6: Terminate
- Is 6 <= 5? No
- Exit loop

Final Output:
1
2
3
4
5

While Loop - Step-by-Step Example:

# Count down from 5 to 1
count = 5
while count > 0:
    print(count)
    count = count - 1
print("Liftoff!")

Execution Steps:

Step 1: Initialize
- count = 5

Step 2: Check Condition
- Is count > 0? Yes (5 > 0)

Step 3: Execute Body
- print(5)
- count = 5 - 1 = 4

Step 4: Repeat
- Is 4 > 0? Yes
- print(4)
- count = 3
- Continue...

Step 5: Final Iteration
- Is 1 > 0? Yes
- print(1)
- count = 0

Step 6: Terminate
- Is 0 > 0? No
- Exit loop
- print("Liftoff!")

Final Output:
5
4
3
2
1
Liftoff!

5.6 DEFINITION: Conditional Statement

A Conditional Statement is a programming construct that performs different actions based on whether a specified condition is true or false.

Detailed Description:
Conditional statements allow programs to make decisions and execute different code paths based on different situations.

If-Else Statement - Step-by-Step Example:

# Check if student passed or failed
marks = 75

if marks >= 50:
    print("PASSED")
    print("Congratulations!")
else:
    print("FAILED")
    print("Try again next time")

Execution Steps:

Step 1: Evaluate Condition
- Is marks >= 50?
- Is 75 >= 50? TRUE

Step 2: Execute True Branch
- Run code inside if block
- print("PASSED")
- print("Congratulations!")

Step 3: Skip False Branch
- else block is skipped

Output:
PASSED
Congratulations!

Multiple Conditions (elif) Example:

# Grade calculator
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")

Execution Steps:

Step 1: Check First Condition
- Is 85 >= 90? NO
- Move to next condition

Step 2: Check Second Condition
- Is 85 >= 80? YES
- grade = "A"

Step 3: Skip Remaining Conditions
- Rest of elif/else skipped

Step 4: Continue Program
- print(f"Grade: A")

Output:
Grade: A

5.7 DEFINITION: Array/List

An Array (or List in Python) is a data structure that stores multiple values of the same type in a single variable.

Detailed Description:
Arrays allow storing collections of data that can be accessed using an index. They are useful for managing multiple related values.

Step-by-Step: Working with Lists in Python

Step 1: Create List
students = ["Ali", "Ahmed", "Sara", "Fatima"]

Step 2: Access Elements
- Index starts at 0
- students[0] = "Ali"
- students[2] = "Sara"

Step 3: Modify Elements
- students[1] = "Hassan"
- List now: ["Ali", "Hassan", "Sara", "Fatima"]

Step 4: Add Elements
- students.append("Zain")
- List now: ["Ali", "Hassan", "Sara", "Fatima", "Zain"]

Step 5: Remove Elements
- students.remove("Ali")
- List now: ["Hassan", "Sara", "Fatima", "Zain"]

Step 6: Get Length
- count = len(students)
- count = 4

Step 7: Iterate Through List
for student in students:
    print(student)

Output:
Hassan
Sara
Fatima
Zain

Complete Program Example: Student Management System

def main():
    students = []
    
    while True:
        print("\\n=== Student Management ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Remove Student")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == "1":
            name = input("Enter name: ")
            students.append(name)
            print(f"Added: {name}")
            
        elif choice == "2":
            print("\\nStudent List:")
            for i, student in enumerate(students, 1):
                print(f"{i}. {student}")
                
        elif choice == "3":
            name = input("Enter name to remove: ")
            if name in students:
                students.remove(name)
                print(f"Removed: {name}")
            else:
                print("Student not found")
                
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice")

# Run the program
main()
"""
    })
    
    return chapters

def build_pdf():
    """Generate the complete PDF book"""
    
    output_path = os.path.join(os.path.dirname(__file__), "ALAM_ACADEMY_IT_Book.pdf")
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.5*inch
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.darkblue,
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.gray,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )
    
    chapter_style = ParagraphStyle(
        'ChapterTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.darkblue,
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['BodyText'],
        fontSize=10,
        leading=13,
        alignment=TA_JUSTIFY,
        spaceAfter=6
    )
    
    # Title Page
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph(ACADEMY_NAME, title_style))
    story.append(Paragraph(BOOK_TITLE, subtitle_style))
    story.append(Paragraph(SUBTITLE, subtitle_style))
    story.append(Spacer(1, 0.5*inch))
    
    publisher_info = [
        [Paragraph(f"<b>Publisher:</b> {ACADEMY_NAME}", body_style)],
        [Paragraph(f"<b>Owner:</b> {OWNER_NAME}", body_style)],
        [Paragraph(f"<b>Contact:</b> {CONTACT}", body_style)],
        [Paragraph(f"<b>Email:</b> {EMAIL}", body_style)],
        [Paragraph(f"<b>GitHub:</b> {GITHUB}", body_style)],
        [Paragraph(f"<b>Address:</b> {ADDRESS}", body_style)]
    ]
    
    info_table = Table(publisher_info, colWidths=[5*inch])
    info_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SPACEAFTER', (0, 0), (-1, -1), 10),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph(f"<i>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</i>", body_style))
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("TABLE OF CONTENTS", chapter_style))
    story.append(Spacer(1, 12))
    
    chapters = get_book_content()
    for i, chapter in enumerate(chapters, 1):
        story.append(Paragraph(f"{i}. {chapter['title']}", body_style))
    story.append(PageBreak())
    
    # Generate chapters
    for chapter in chapters:
        story.append(Paragraph(chapter['title'], chapter_style))
        story.append(Spacer(1, 6))
        
        paragraphs = chapter['content'].strip().split('\\n')
        for para in paragraphs:
            if para.strip():
                story.append(Paragraph(para.strip(), body_style))
        
        story.append(Spacer(1, 12))
        story.append(PageBreak())
    
    # Back Cover
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph(ACADEMY_NAME, title_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("<b>Contact Information</b>", chapter_style))
    story.append(Paragraph(f"Owner: {OWNER_NAME}", body_style))
    story.append(Paragraph(f"Phone: {CONTACT}", body_style))
    story.append(Paragraph(f"Email: {EMAIL}", body_style))
    story.append(Paragraph(f"GitHub: {GITHUB}", body_style))
    story.append(Paragraph(f"Address: {ADDRESS}", body_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("<i>© 2026 ALAM-ACADEMY. All Rights Reserved.</i>", body_style))
    
    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    return output_path

def add_header_footer(canvas, doc):
    """Add header and footer to each page"""
    canvas.saveState()
    
    canvas.setFont('Helvetica-Bold', 10)
    canvas.setFillColor(colors.darkblue)
    header_text = f"{ACADEMY_NAME} | {BOOK_TITLE}"
    canvas.drawCentredString(A4[0]/2, A4[1] - 0.5*inch, header_text)
    
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.gray)
    
    now = datetime.now()
    footer_left = f"Owner: {OWNER_NAME}"
    footer_center = f"Date: {now.strftime('%Y-%m-%d')} | Time: {now.strftime('%H:%M:%S')}"
    footer_right = f"Page {doc.page}"
    
    canvas.drawString(0.75*inch, 0.4*inch, footer_left)
    canvas.drawCentredString(A4[0]/2, 0.4*inch, footer_center)
    canvas.drawRightString(A4[0] - 0.75*inch, 0.4*inch, footer_right)
    
    canvas.restoreState()

if __name__ == "__main__":
    print("Generating ALAM-ACADEMY IT & Computer Science Book...")
    print("With definitions, descriptions, and step-by-step examples...")
    output_file = build_pdf()
    print(f"Book generated successfully: {output_file}")
    print(f"Owner: {OWNER_NAME}")
    print(f"Contact: {CONTACT}")
    print(f"Email: {EMAIL}")
    print(f"GitHub: {GITHUB}")
