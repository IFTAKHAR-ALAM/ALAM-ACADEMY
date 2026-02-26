"""
Microwave Systems Book Generator
Publisher: ALAM-ACADEMY
Owner: M IFTIKHAR ALAM
Company: Sony Ericsson
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime

# Book Information
ACADEMY_NAME = "ALAM-ACADEMY"
OWNER_NAME = "M IFTIKHAR ALAM"
CONTACT_NO = "0333-9257987"
EMAIL_ID = "alammiftikhar@gmail.com"
GITHUB_ACCOUNT = "https://github.com/IFTAKHAR-ALAM/ALAM-ACADEMY"
COMPANY_NAME = "Sony Ericsson"
PUBLISHER_ADDRESS = "Karachi, PAKISTAN"


class MicrowaveBook:
    def __init__(self, filename="Microwave_Systems_Complete_Book.pdf"):
        self.filename = filename
        self.doc = SimpleDocTemplate(filename, pagesize=A4,
                                      rightMargin=2*cm, leftMargin=2*cm,
                                      topMargin=2.5*cm, bottomMargin=2*cm)
        self.story = []
        self.styles = getSampleStyleSheet()
        self.setup_styles()

    def setup_styles(self):
        def add_style(name, **kwargs):
            try:
                self.styles.add(ParagraphStyle(name=name, **kwargs))
            except KeyError:
                pass
        
        add_style('CustomTitle', parent=self.styles['Heading1'],
                                        fontSize=24, textColor=colors.darkblue,
                                        spaceAfter=30, alignment=TA_CENTER, fontName='Helvetica-Bold')
        add_style('ChapterTitle', parent=self.styles['Heading1'],
                                        fontSize=18, textColor=colors.darkblue,
                                        spaceAfter=20, spaceBefore=20, fontName='Helvetica-Bold')
        add_style('SectionTitle', parent=self.styles['Heading2'],
                                        fontSize=14, textColor=colors.darkgreen,
                                        spaceAfter=12, spaceBefore=12, fontName='Helvetica-Bold')
        add_style('SubSectionTitle', parent=self.styles['Heading3'],
                                        fontSize=12, textColor=colors.black,
                                        spaceAfter=10, spaceBefore=10, fontName='Helvetica-Bold')
        add_style('BodyText', parent=self.styles['Normal'],
                                        fontSize=11, alignment=TA_JUSTIFY,
                                        spaceAfter=8, leading=16)
        add_style('Definition', parent=self.styles['Normal'],
                                        fontSize=11, leftIndent=20, rightIndent=20,
                                        backColor=colors.lightgrey, borderPadding=10,
                                        spaceAfter=12, leading=16)
        add_style('Example', parent=self.styles['Normal'],
                                        fontSize=11, leftIndent=20, rightIndent=20,
                                        textColor=colors.darkblue, spaceAfter=12, leading=16)
        add_style('HeaderInfo', parent=self.styles['Normal'],
                                        fontSize=9, textColor=colors.grey, alignment=TA_CENTER)

    def add_header(self, canvas_obj, doc):
        canvas_obj.saveState()
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")
        page_num = doc.page
        header_text = f"{ACADEMY_NAME} | {current_date} | {current_time} | Page {page_num}"
        canvas_obj.setFont("Helvetica", 9)
        canvas_obj.setFillColor(colors.grey)
        canvas_obj.drawCentredString(A4[0]/2, A4[1] - 1.5*cm, header_text)
        footer_text = f"Copyright {ACADEMY_NAME} - Microwave Systems Book"
        canvas_obj.drawCentredString(A4[0]/2, 1*cm, footer_text)
        canvas_obj.restoreState()

    def create_title_page(self):
        self.story.append(Spacer(1, 1.5*inch))
        self.story.append(Paragraph(f"<b><font size='28' color='darkblue'>{ACADEMY_NAME}</font></b>", self.styles['CustomTitle']))
        self.story.append(Spacer(1, 0.5*inch))
        self.story.append(Paragraph(f"<b><font size='24' color='darkgreen'>MICROWAVE SYSTEMS</font></b>", self.styles['CustomTitle']))
        self.story.append(Paragraph(f"<b><font size='18' color='black'>Complete Guide with Software and Hardware</font></b>", self.styles['CustomTitle']))
        self.story.append(Spacer(1, 0.8*inch))
        self.story.append(Paragraph(f"<b><font size='16' color='navy'>Company: {COMPANY_NAME}</font></b>", self.styles['SectionTitle']))
        self.story.append(Spacer(1, 0.5*inch))
        
        publisher_info = [
            ["Publisher:", ACADEMY_NAME],
            ["Address:", PUBLISHER_ADDRESS],
            ["Owner:", OWNER_NAME],
            ["Contact No:", f"<b>{CONTACT_NO}</b>"],
            ["Email ID:", EMAIL_ID],
            ["GitHub:", GITHUB_ACCOUNT]
        ]
        pub_table = Table(publisher_info, colWidths=[2*cm, 5*cm])
        pub_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BACKGROUND', (0, 3), (-1, 3), colors.lightyellow),
        ]))
        self.story.append(pub_table)
        self.story.append(Spacer(1, 0.8*inch))
        
        contact_box = f"<b><font size='16' color='darkred'>For Inquiries: Contact No: {CONTACT_NO}</font></b>"
        self.story.append(Paragraph(contact_box, self.styles['SectionTitle']))
        self.story.append(Spacer(1, 0.5*inch))
        
        current_date = datetime.now().strftime("%B %Y")
        self.story.append(Paragraph(f"<b><font size='14' color='grey'>First Edition - {current_date}</font></b>", self.styles['SectionTitle']))
        self.story.append(Spacer(1, 0.5*inch))
        self.story.append(Paragraph(f"<font size='10' color='grey'>Copyright {datetime.now().year} {ACADEMY_NAME}. All rights reserved.</font>", self.styles['BodyText']))
        self.story.append(PageBreak())

    def create_table_of_contents(self):
        self.story.append(Paragraph(f"<b><font size='20' color='darkblue'>TABLE OF CONTENTS</font></b>", self.styles['ChapterTitle']))
        self.story.append(Spacer(1, 0.5*inch))
        chapters = [
            "Chapter 1: Introduction to Microwave Systems",
            "Chapter 2: Microwave Fundamentals and Theory",
            "Chapter 3: Microwave Hardware Components",
            "Chapter 4: Microwave Software and Tools",
            "Chapter 5: Microwave Accessories",
            "Chapter 6: Tower Installation and Setup",
            "Chapter 7: Real-Life Applications and Case Studies",
            "Chapter 8: Troubleshooting and Maintenance",
            "Chapter 9: Safety Standards and Regulations",
            "Chapter 10: Future Trends in Microwave Technology",
            "Glossary of Terms",
            "References and Resources"
        ]
        for i, chapter in enumerate(chapters, 1):
            self.story.append(Paragraph(f"{i:2d}. {chapter}", self.styles['BodyText']))
            self.story.append(Spacer(1, 0.1*inch))
        self.story.append(PageBreak())

    def create_chapter(self, title, content_list):
        self.story.append(Paragraph(title, self.styles['ChapterTitle']))
        for item in content_list:
            if isinstance(item, tuple):
                if item[0] == 'section':
                    self.story.append(Paragraph(item[1], self.styles['SectionTitle']))
                elif item[0] == 'subsection':
                    self.story.append(Paragraph(item[1], self.styles['SubSectionTitle']))
                elif item[0] == 'body':
                    self.story.append(Paragraph(item[1], self.styles['BodyText']))
                elif item[0] == 'definition':
                    self.story.append(Paragraph(item[1], self.styles['Definition']))
                elif item[0] == 'example':
                    self.story.append(Paragraph(item[1], self.styles['Example']))
                elif item[0] == 'table':
                    self.story.append(item[1])
                elif item[0] == 'spacer':
                    self.story.append(Spacer(1, item[1]))
                elif item[0] == 'pagebreak':
                    self.story.append(PageBreak())
                elif item[0] == 'list':
                    for li in item[1]:
                        self.story.append(Paragraph(li, self.styles['BodyText']))

    def create_frequency_table(self):
        data = [
            ["Band", "Frequency Range", "Wavelength", "Applications"],
            ["L Band", "1-2 GHz", "30-15 cm", "Satellite, GPS"],
            ["S Band", "2-4 GHz", "15-7.5 cm", "Weather radar"],
            ["C Band", "4-8 GHz", "7.5-3.75 cm", "Satellite TV"],
            ["X Band", "8-12 GHz", "3.75-2.5 cm", "Radar, satellite"],
            ["Ku Band", "12-18 GHz", "2.5-1.67 cm", "Satellite TV, VSAT"],
            ["K Band", "18-27 GHz", "1.67-1.11 cm", "Police radar"],
            ["Ka Band", "27-40 GHz", "1.11-0.75 cm", "High-speed satellite, 5G"],
            ["V Band", "40-75 GHz", "7.5-4 mm", "Millimeter wave, 5G"],
            ["W Band", "75-110 GHz", "4-2.7 mm", "Advanced radar"]
        ]
        table = Table(data, colWidths=[1.2*inch, 1.2*inch, 1.2*inch, 2.4*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
        ]))
        return table

    def create_chapter_1(self):
        content = [
            ('section', "1.1 What are Microwave Systems?"),
            ('body', "Microwave systems are communication systems that use electromagnetic waves in the microwave frequency range (typically 300 MHz to 300 GHz) to transmit information from one point to another. These systems form the backbone of modern telecommunications, enabling wireless communication, satellite communications, radar systems, and various other applications."),
            ('definition', "<b>Definition:</b> Microwave Communication is a method of transmitting information using high-frequency radio waves in the microwave spectrum, typically between 1 GHz and 300 GHz, characterized by short wavelengths ranging from 1 millimeter to 1 meter."),
            ('section', "1.2 Historical Background"),
            ('body', "The development of microwave technology began during World War II for radar applications. Post-war, this technology found applications in civilian communications. The first commercial microwave relay systems were installed in the 1950s, revolutionizing long-distance telephone and television signal transmission."),
            ('example', "<b>Example:</b> The first transcontinental microwave radio relay system was completed in 1951 by AT&T in the United States, spanning over 4,000 miles and connecting New York to San Francisco with 107 relay stations."),
            ('section', "1.3 Frequency Bands in Microwave Communication"),
            ('table', self.create_frequency_table()),
            ('spacer', 0.3*inch),
            ('section', "1.4 Advantages of Microwave Communication"),
            ('list', [
                "High bandwidth capacity for data transmission",
                "No need for physical cables or right-of-way acquisition",
                "Quick deployment compared to fiber optic systems",
                "Cost-effective for difficult terrain (mountains, water bodies)",
                "Reliable communication with minimal interference",
                "Supports multiple channels simultaneously",
                "Lower latency compared to satellite systems",
                "Scalable and upgradeable infrastructure"
            ]),
            ('section', "1.5 Limitations and Challenges"),
            ('list', [
                "Line-of-sight (LOS) requirement between antennas",
                "Signal attenuation due to rain, fog, and atmospheric conditions",
                "Limited range per hop (typically 30-50 km)",
                "Requires tall towers for long-distance transmission",
                "Susceptible to interference from other microwave systems",
                "Higher frequencies experience more atmospheric absorption",
                "Initial infrastructure cost can be high"
            ]),
            ('section', "1.6 Applications of Microwave Systems"),
            ('body', "Microwave systems are used in various applications across multiple industries:"),
            ('pagebreak',)
        ]
        self.create_chapter("Chapter 1: Introduction to Microwave Systems", content)

    def create_chapter_2(self):
        content = [
            ('section', "2.1 Electromagnetic Wave Theory"),
            ('body', "Microwaves are a form of electromagnetic radiation, consisting of oscillating electric and magnetic fields perpendicular to each other and to the direction of wave propagation."),
            ('subsection', "Key Parameters"),
            ('body', "Frequency (f): f = c/lambda (Hz) | Wavelength (lambda): lambda = c/f (m) | Velocity (c): 3x10^8 m/s | Period (T): T = 1/f (s)"),
            ('example', "<b>Example Calculation:</b> Calculate the wavelength of a microwave signal at 6 GHz frequency. Solution: lambda = c/f = (3 x 10^8) / (6 x 10^9) = 0.05 m = 5 cm"),
            ('section', "2.2 Propagation Characteristics"),
            ('subsection', "Free Space Path Loss (FSPL)"),
            ('body', "Free Space Path Loss is the attenuation of signal strength that occurs when electromagnetic waves travel through free space. Formula: FSPL (dB) = 32.45 + 20 log10(d_km) + 20 log10(f_MHz)"),
            ('example', "<b>Example:</b> For a 6 GHz signal traveling 50 km: FSPL = 32.45 + 20 log10(50) + 20 log10(6000) = 32.45 + 33.98 + 75.56 = 142 dB"),
            ('subsection', "Rain Attenuation"),
            ('body', "Rain causes significant signal attenuation, especially at frequencies above 10 GHz. During heavy rainstorms, satellite TV signals (typically in Ku-band at 12-18 GHz) may experience temporary degradation or complete loss, known as rain fade."),
            ('section', "2.3 Fresnel Zone"),
            ('body', "The Fresnel zone is an elliptical region around the direct line-of-sight path between transmitter and receiver. For optimal signal strength, this zone must be kept clear of obstacles."),
            ('definition', "First Fresnel Zone Radius: r = 17.32 x sqrt(d1 x d2 / (f x d)) where r is in meters, d1 and d2 are distances from endpoints in km, f is frequency in GHz, d is total distance in km"),
            ('example', "<b>Practical Example:</b> For a 10 km link at 6 GHz: r = 17.32 x sqrt(5 x 5 / (6 x 10)) = 11.18 meters. Obstacles should not penetrate more than 40% of this zone."),
            ('section', "2.4 Modulation Techniques"),
            ('body', "Modulation is the process of varying one or more properties of a carrier wave to transmit information. Common types: AM (Amplitude Modulation), FM (Frequency Modulation), PM (Phase Modulation), QPSK (4 phase states), 16-QAM (4 bits/symbol), 64-QAM (6 bits/symbol), 256-QAM (8 bits/symbol)"),
            ('section', "2.5 Link Budget Analysis"),
            ('definition', "Link Budget Equation: P_rx = P_tx + G_tx - L_tx + G_rx - L_rx - L_path - L_misc where P_rx is received power, P_tx is transmitter power, G_tx/G_rx are antenna gains, L_tx/L_rx are cable losses, L_path is path loss, L_misc is miscellaneous losses"),
            ('example', "<b>Complete Link Budget Example:</b> Transmitter Power: 30 dBm, Tx Antenna Gain: 40 dBi, Tx Cable Loss: 2 dB, Path Loss: 142 dB, Rx Antenna Gain: 40 dBi, Rx Cable Loss: 2 dB, Rain Fade: 5 dB. P_rx = 30 + 40 - 2 - 142 + 40 - 2 - 5 = -41 dBm"),
            ('pagebreak',)
        ]
        self.create_chapter("Chapter 2: Microwave Fundamentals and Theory", content)

    def create_chapter_3(self):
        content = [
            ('section', "3.1 Overview of Microwave Hardware"),
            ('body', "Microwave systems consist of various hardware components that work together to transmit and receive signals. Understanding each component's function is essential for system design, installation, and maintenance."),
            ('section', "3.2 Antennas"),
            ('body', "Antennas are the most visible components of microwave systems, responsible for radiating and receiving electromagnetic waves."),
            ('subsection', "Parabolic Dish Antennas"),
            ('body', "Parabolic dish antennas are the most common type used in microwave point-to-point links. They consist of a parabolic reflector that focuses signals to/from a feed horn at the focal point."),
            ('list', [
                "High gain (typically 30-50 dBi)",
                "Narrow beamwidth (1-5 degrees)",
                "Excellent front-to-back ratio",
                "Available in various sizes (0.3m to 4m diameter)"
            ]),
            ('subsection', "Horn Antennas"),
            ('body', "Horn antennas are flared metal waveguides that direct radio waves in a beam. Types include: Pyramidal Horn (flared in both planes), Sectoral Horn (flared in one plane), Conical Horn (circular cross-section)"),
            ('section', "3.3 Radio Units (ODU - Outdoor Unit)"),
            ('body', "The Outdoor Unit (ODU) is the radio transceiver mounted near the antenna. It handles frequency conversion, amplification, and modulation/demodulation of microwave signals."),
            ('list', [
                "Transmitter: Generates and amplifies the RF signal",
                "Receiver: Amplifies and processes received signals",
                "Local Oscillator: Provides frequency reference",
                "Power Amplifier: Boosts transmit signal strength",
                "Low Noise Amplifier (LNA): Amplifies weak received signals",
                "Modem: Modulates/demodulates digital data"
            ]),
            ('subsection', "ODU Specifications Example"),
            ('body', "Frequency Range: 6 GHz (5.925-6.425 GHz) | Output Power: +10 to +30 dBm | Receiver Sensitivity: -75 dBm | Modulation: QPSK to 1024-QAM | Operating Temp: -40C to +55C"),
            ('section', "3.4 Indoor Unit (IDU)"),
            ('body', "The Indoor Unit (IDU) is located inside a building. It interfaces between the ODU and user equipment, handling signal processing, multiplexing, and network management."),
            ('section', "3.5 Waveguides and Feeders"),
            ('body', "Waveguides are hollow metallic structures that guide electromagnetic waves from the transmitter to the antenna with minimal loss. Common types: WR-284 (2.6-3.95 GHz), WR-137 (5.85-8.2 GHz), WR-90 (8.2-12.4 GHz), WR-62 (12.4-18 GHz)"),
            ('section', "3.6 Amplifiers"),
            ('body', "Power Amplifiers (PA) increase transmitted signal power (1-10 Watts output). Low Noise Amplifiers (LNA) amplify weak received signals with minimal added noise (Noise Figure: 0.5-2 dB)"),
            ('section', "3.7 Filters"),
            ('body', "Filters select desired frequencies and reject unwanted signals. Types: Bandpass Filter (passes specific band), Lowpass Filter (passes below cutoff), Highpass Filter (passes above cutoff), Bandstop Filter (rejects specific band)"),
            ('pagebreak',)
        ]
        self.create_chapter("Chapter 3: Microwave Hardware Components", content)

    def create_chapter_4(self):
        content = [
            ('section', "4.1 Overview of Microwave Software"),
            ('body', "Modern microwave systems rely heavily on software for design, simulation, monitoring, and optimization. Software tools enable engineers to model systems, predict performance, and troubleshoot issues efficiently."),
            ('section', "4.2 Path Loss and Link Budget Calculators"),
            ('body', "These tools calculate signal attenuation and predict system performance based on frequency, distance, terrain, and environmental factors."),
            ('subsection', "Popular Link Budget Software"),
            ('list', [
                "Radio Mobile: Terrain analysis, coverage maps (Network planning)",
                "Pathloss 4.0: Detailed link analysis (Microwave link design)",
                "ATDI HTZ: 3D propagation modeling (Cellular and microwave)",
                "InfoVista: Network planning suite (Enterprise networks)",
                "SatMaster Pro: Satellite link calculations"
            ]),
            ('section', "4.3 Network Management Systems (NMS)"),
            ('body', "NMS software provides centralized monitoring and control of microwave networks."),
            ('list', [
                "Fault Management: Detect, isolate, and correct network problems",
                "Configuration Management: Configure devices remotely",
                "Performance Management: Monitor throughput, BER, signal levels",
                "Security Management: Control access and detect intrusions"
            ]),
            ('subsection', "Popular NMS Platforms"),
            ('body', "SolarWinds NPM (SNMP monitoring), PRTG Network Monitor (Sensor-based), Nagios (Open-source), Zabbix (Enterprise-grade), Cisco Prime (Cisco devices)"),
            ('section', "4.4 Spectrum Analyzers (Software-Defined)"),
            ('body', "Software-defined spectrum analyzers use SDR hardware with PC-based software to analyze RF spectrum. Popular tools: SDR# (SDR Sharp), HDSDR, GNU Radio (open-source toolkit), RF Explorer"),
            ('section', "4.5 Simulation and Modeling Software"),
            ('body', "Electromagnetic simulation software models antenna patterns and waveguide behavior. Tools: HFSS by Ansys (3D EM simulation), CST Studio Suite (EM field simulation), ADS by Keysight (RF/microwave design), Sonnet (Planar EM simulation)"),
            ('section', "4.6 Configuration and Commissioning Tools"),
            ('list', [
                "Set operating frequency and channel spacing",
                "Configure modulation scheme (QPSK, 16-QAM, 64-QAM)",
                "Set transmit power levels",
                "Configure interface types (E1, Ethernet, SDH)",
                "Set up alarm thresholds and notifications",
                "Perform alignment and optimization"
            ]),
            ('section', "4.7 Mobile Apps for Field Engineers"),
            ('body', "Smartphone apps provide convenient tools: Microwave Link Calculator (path loss), RF Unit Converter (dBm/Watts), GPS Coordinates (site location), Bubble Level/Clinometer (antenna alignment)"),
            ('pagebreak',)
        ]
        self.create_chapter("Chapter 4: Microwave Software and Tools", content)

    def create_chapter_5(self):
        content = [
            ('section', "5.1 Overview of Microwave Accessories"),
            ('body', "Accessories are essential components that support, protect, and enhance the performance of microwave systems. Proper selection and installation ensures reliable operation and longevity."),
            ('section', "5.2 Mounting Hardware"),
            ('body', "Mounting hardware secures antennas and radio units to towers, poles, and buildings."),
            ('subsection', "Antenna Mounts"),
            ('list', [
                "Pipe Mount: Clamps to vertical pipe (Small antennas, up to 50 kg)",
                "Wall Mount: Bracket for wall attachment (up to 30 kg)",
                "Pole Mount: Adjustable pole attachment (Light poles, up to 40 kg)",
                "Tower Mount: Heavy-duty tower bracket (up to 200 kg)",
                "Parabolic Mount: Precision dish mount (up to 150 kg)"
            ]),
            ('section', "5.3 Lightning Protection and Grounding"),
            ('body', "Lightning protection is critical for outdoor microwave installations, especially on tall towers."),
            ('subsection', "Lightning Arrestors"),
            ('list', [
                "Gas Discharge Tube (GDT): Gas-filled spark gap (RF lines, power)",
                "Metal Oxide Varistor (MOV): Voltage-dependent resistor (Power supplies)",
                "Transient Suppression Diode: Avalanche diode (Data lines)",
                "Hybrid Protector: Multiple technologies (Comprehensive protection)"
            ]),
            ('subsection', "Grounding Components"),
            ('list', [
                "Ground Rods: Copper or copper-clad steel rods (8-10 feet long)",
                "Ground Wire: Heavy gauge copper wire (6 AWG or larger)",
                "Ground Bus Bar: Central connection point for multiple grounds",
                "Ground Clamps: Secure connections to rods and equipment",
                "Exothermic Welding: Permanent, low-resistance connections"
            ]),
            ('section', "5.4 Cables and Connectors"),
            ('subsection', "RF Connectors"),
            ('body', "N-Type: DC-11 GHz, 50/75 ohm (Most common for microwave) | SMA: DC-18 GHz, 50 ohm (Small devices) | TNC: DC-11 GHz (Weather-resistant) | 7/16 DIN: DC-7.5 GHz (High power, base stations)"),
            ('subsection', "Cable Accessories"),
            ('list', [
                "Weatherproofing Kits: Self-amalgamating tape, heat shrink",
                "Cable Ties: UV-resistant ties for cable management",
                "Cable Trays: Support and organize cable runs",
                "Drip Loops: Prevent water ingress along cables",
                "Connector Wrenches: Proper torque for installation"
            ]),
            ('section', "5.5 Alignment Tools"),
            ('body', "Precision alignment tools ensure antennas are properly aimed: Compass (Azimuth determination, +/-2-5 degrees), Clinometer/Inclinometer (Elevation angle, +/-0.1 degrees), GPS Receiver (Location coordinates), Spectrum Analyzer (Signal strength, fine tuning)"),
            ('section', "5.6 Environmental Protection"),
            ('subsection', "Weatherproofing Materials"),
            ('list', [
                "Self-Amalgamating Tape: Rubber tape that fuses into solid layer",
                "Vinyl Electrical Tape: UV-resistant outer wrap",
                "Heat Shrink Tubing: Shrinks to form tight seal when heated",
                "Silicone Sealant: Waterproof seal for enclosures",
                "Desiccant Packs: Absorb moisture inside enclosures"
            ]),
            ('subsection', "Equipment Enclosures (NEMA Ratings)"),
            ('body', "NEMA 3R: Rain, sleet, snow (Outdoor, ventilated) | NEMA 4: Water jets, dust-tight (Harsh outdoor) | NEMA 4X: Corrosion + NEMA 4 (Marine, chemical) | NEMA 6: Temporary submersion (Flood-prone areas)"),
            ('section', "5.7 Power Accessories"),
            ('list', [
                "Power Injectors: Inject DC power onto coaxial cable (for ODUs)",
                "DC-DC Converters: Convert between voltage levels",
                "AC-DC Power Supplies: Convert AC mains to regulated DC",
                "Uninterruptible Power Supply (UPS): Battery backup",
                "Power Distribution Units (PDU): Multiple outlets with protection"
            ]),
            ('pagebreak',)
        ]
        self.create_chapter("Chapter 5: Microwave Accessories", content)

    def create_chapter_6(self):
        content = [
            ('section', "6.1 Introduction to Tower Installation"),
            ('body', "Tower installation is a critical phase in microwave system deployment. Proper installation ensures system reliability, safety, and optimal performance."),
            ('section', "6.2 Types of Towers and Masts"),
            ('list', [
                "Monopole: 20-60m height, High load capacity (Urban, cellular) - Small footprint, expensive",
                "Lattice/Self-Supporting: 30-100m, Very High capacity (Major sites, broadcast) - High capacity, large base",
                "Guyed Mast: 50-200m, Medium-High capacity (Rural, broadcast) - Cost-effective, large land area",
                "Rooftop Tower: 3-20m, Medium capacity (Urban infill) - No land needed, structural concerns",
                "Portable Mast: 3-15m, Light capacity (Temporary, emergency) - Quick deploy, limited height"
            ]),
            ('subsection', "Tower Components"),
            ('list', [
                "Foundation: Concrete base that supports the tower",
                "Tower Sections: Modular segments that stack to achieve height",
                "Base Plate: Distributes tower load to foundation",
                "Anchor Bolts: Secure tower to foundation",
                "Climbing Ladder: Provides access for maintenance",
                "Safety Cage/Fall Arrest System: Worker protection",
                "Antenna Mounts: Attachment points for antennas",
                "Lightning Protection: Air terminals and grounding",
                "Aircraft Warning Lights: Required for tall structures"
            ]),
            ('section', "6.3 Pre-Installation Planning"),
            ('subsection', "Site Survey Checklist"),
            ('list', [
                "Path Analysis: Verify line-of-sight using GPS and mapping tools",
                "Soil Testing: Determine soil bearing capacity for foundation",
                "Access Assessment: Evaluate road access for construction vehicles",
                "Utilities: Identify power, water availability",
                "Environmental: Check for wetlands, protected species",
                "Zoning: Verify compliance with local regulations and obtain permits",
                "Wind/Ice Loading: Determine structural requirements based on climate"
            ]),
            ('subsection', "Required Permits and Approvals"),
            ('body', "Building Permit (Local Municipality, 2-8 weeks) | Zoning Variance (Zoning Board, 4-12 weeks) | Environmental Clearance (Environmental Agency, 4-16 weeks) | Aviation Authority Approval (CAA/FAA, 2-6 weeks) | Spectrum License (Telecom Authority, 4-8 weeks)"),
            ('section', "6.4 Foundation Construction"),
            ('body', "The foundation is the most critical structural element. Types: Spread Footing (Wide concrete pad, stable soil, 1-3m depth), Pier Foundation (Deep concrete columns, poor soil, 3-10m), Rock Anchor (Anchors drilled into bedrock, rocky terrain)"),
            ('subsection', "Foundation Construction Steps"),
            ('list', [
                "Step 1: Excavation - Dig to specified depth based on soil analysis",
                "Step 2: Formwork - Build wooden or metal forms to shape concrete",
                "Step 3: Rebar Installation - Place steel reinforcement per engineering specs",
                "Step 4: Anchor Bolt Cage - Position and secure anchor bolts precisely",
                "Step 5: Concrete Pour - Pour concrete, vibrate to eliminate air pockets",
                "Step 6: Curing - Allow concrete to cure (typically 7-28 days)",
                "Step 7: Backfill - Fill around foundation with compacted soil"
            ]),
            ('section', "6.5 Tower Erection"),
            ('body', "Tower erection is the most visible and dangerous phase. It requires skilled personnel, proper equipment, and strict safety protocols."),
            ('subsection', "Erection Methods"),
            ('body', "Crane Lift: Sections lifted and stacked by crane (Mobile crane 50-200 ton, most installations) | Gin Pole: Small crane mounted on tower (Winch, gin pole, tall towers) | Tilt-Up: Assemble horizontal, then raise (Monopoles, guyed masts)"),
            ('subsection', "Tower Erection Procedure"),
            ('list', [
                "Verify foundation has cured and anchor bolts are positioned",
                "Inspect all tower sections for damage or missing components",
                "Confirm crane capacity and positioning area",
                "Conduct safety briefing with all personnel",
                "Check weather forecast (no erection in high winds or storms)",
                "Install base section and torque anchor bolts to specification",
                "Lift and stack subsequent sections, bolting with specified hardware",
                "Torque all bolts to engineering specifications",
                "Install climbing ladder and safety cage as tower rises",
                "Install antenna mounts at designated heights",
                "Perform plumbness check (within 1:500 tolerance)"
            ]),
            ('section', "6.6 Antenna Installation"),
            ('subsection', "Antenna Mounting Procedure"),
            ('list', [
                "Inspect antenna for shipping damage before installation",
                "Attach mounting bracket to antenna (do not fully tighten)",
                "Hoist antenna to mounting location using tag lines",
                "Secure antenna to tower mount with U-bolts or clamps",
                "Rough-aim antenna using compass and clinometer",
                "Connect feeder cable with proper weatherproofing",
                "Install lightning arrestor at base of antenna",
                "Perform fine alignment using signal strength measurements",
                "Final-tighten all bolts and apply thread-locking compound",
                "Document installation with photos and alignment data"
            ]),
            ('subsection', "Antenna Alignment Steps"),
            ('list', [
                "Calculate azimuth and elevation angles using path coordinates",
                "Set initial azimuth using compass (correct for magnetic declination)",
                "Set elevation angle using inclinometer",
                "Connect spectrum analyzer or use built-in RSSI",
                "Have remote end transmit continuous wave or test signal",
                "Adjust azimuth in small increments while monitoring signal level",
                "Peak signal by adjusting elevation similarly",
                "Verify polarization alignment",
                "Lock all adjustments and secure mounting hardware",
                "Record final signal levels and alignment parameters"
            ]),
            ('section', "6.7 Cable Installation"),
            ('body', "Proper cable installation minimizes signal loss and prevents future problems."),
            ('list', [
                "Plan cable route to minimize length and avoid sharp bends",
                "Maintain minimum bend radius (typically 10x cable diameter)",
                "Support cables every 1-2 meters using appropriate clamps",
                "Install drip loops before entry points to prevent water ingress",
                "Use proper pulling techniques (avoid twisting or kinking)",
                "Label both ends of each cable clearly",
                "Leave service loops (extra length) at both ends",
                "Ground cable shields at both ends per specifications",
                "Weatherproof all outdoor connections properly",
                "Test cables with VSWR meter after installation"
            ]),
            ('subsection', "3-Layer Weatherproofing Method"),
            ('body', "Layer 1: Self-amalgamating tape - Stretch and wrap with 50% overlap, starts 2 inches below connector, ends 2 inches above | Layer 2: Vinyl electrical tape - Wrap with 50% overlap over entire self-amalgamating layer | Layer 3: UV-resistant tape or heat shrink - Final protective layer"),
            ('section', "6.8 Grounding and Lightning Protection"),
            ('body', "Proper grounding protects equipment and personnel. Install ground rod within 6 feet of tower base. Use continuous ground wire (no splices). Bond all metal components to ground system. Achieve ground resistance of less than 10 ohms."),
            ('section', "6.9 Safety During Installation"),
            ('subsection', "Personal Protective Equipment (PPE)"),
            ('list', [
                "Hard hat (ANSI Z89.1 compliant)",
                "Safety glasses with side shields",
                "Work gloves (leather for climbing, rubber for electrical)",
                "Safety boots with steel toe and slip resistance",
                "Full-body harness with double lanyards",
                "100% tie-off fall arrest system",
                "High-visibility vest or clothing"
            ]),
            ('subsection', "Safety Rules"),
            ('list', [
                "Never climb alone - always have ground support",
                "Maintain 100% tie-off at all times when above 6 feet",
                "Do not climb in high winds (>40 km/h), rain, or lightning",
                "Inspect all climbing gear before each use",
                "Use tag lines when hoisting equipment",
                "Barricade area below work zone",
                "Stay alert for RF radiation - power down transmitters",
                "Follow lockout/tagout procedures for electrical work",
                "Maintain safe distance from power lines (minimum 10 feet)"
            ]),
            ('section', "6.10 Testing and Commissioning"),
            ('body', "After installation, comprehensive testing verifies system performance."),
            ('list', [
                "VSWR Measurement: VSWR < 1.5:1 (Acceptance criteria)",
                "Return Loss: >14 dB",
                "Received Signal Level: Within 3 dB of calculated",
                "Bit Error Rate (BER): BER < 10^-6",
                "Throughput Test: Meets specified capacity",
                "Ground Resistance: <10 ohms",
                "Insulation Resistance: >100 MOhms",
                "Alarm Verification: All alarms functional"
            ]),
            ('subsection', "Documentation Required"),
            ('list', [
                "As-built drawings showing actual installation",
                "Equipment serial numbers and warranty information",
                "Test results and baseline measurements",
                "Cable schedules and labeling diagrams",
                "Grounding system diagram",
                "Alignment data (azimuth, elevation, signal levels)",
                "Photos of installation (tower, equipment, connections)",
                "Permit and approval copies"
            ]),
            ('pagebreak',)
        ]
        self.create_chapter("Chapter 6: Tower Installation and Setup", content)

    def create_chapter_7(self):
        content = [
            ('section', "7.1 Telecommunications Backhaul"),
            ('body', "Microwave systems form the backbone of cellular network backhaul, connecting cell towers to the core network. This is one of the largest applications of microwave technology."),
            ('example', "<b>Case Study: Mobile Network Operator in Pakistan</b><br/><br/>Challenge: A major mobile operator needed to connect 500 cell sites across diverse terrain. Solution: Deployed hybrid microwave network with 6 GHz for long-haul (up to 50 km), 11 GHz for medium-distance (15-30 km), 18/23 GHz for short urban hops (<10 km). Results: 95% of sites connected within 12 months, 99.95% availability, 60% cost savings vs fiber."),
            ('section', "7.2 Broadcasting and Media"),
            ('example', "<b>Case Study: Live Sports Broadcasting</b><br/><br/>Scenario: Broadcasting a cricket match live from stadium to broadcasting center 200 km away. Setup: Camera feeds to OB van via microwave, OB van aggregates and encodes, 7 GHz microwave link to relay tower, series of hops to center, satellite backup. Outcome: Seamless live broadcast with <100ms latency and 99.99% uptime."),
            ('section', "7.3 Enterprise Connectivity"),
            ('example', "<b>Case Study: Bank Network Connectivity</b><br/><br/>Requirement: Connect headquarters and 50 branch offices for ATM networks. Solution: Point-to-multipoint microwave from central hub, licensed 5.8 GHz spectrum, AES-256 encryption, redundant links for critical branches. Benefits: Deployed in 6 weeks vs 6 months for leased lines, 70% cost reduction, sub-10ms latency."),
            ('section', "7.4 Rural and Remote Connectivity"),
            ('example', "<b>Case Study: Rural Internet Access Project</b><br/><br/>Challenge: Provide internet to 100 villages in mountainous terrain. Implementation: Fiber at base, high-gain parabolic on mountaintops for backhaul, tower in each village with distribution, subscriber modules on premises, solar power for off-grid sites. Impact: 50,000 people gained internet access, enabled e-governance and telemedicine."),
            ('section', "7.5 Oil and Gas Industry"),
            ('example', "<b>Case Study: Offshore Oil Platform Communications</b><br/><br/>Scenario: Connect 5 offshore platforms to onshore center (20-80 km). Solution: Ruggedized marine-rated equipment, corrosion-resistant hardware, diversity protection against multipath over water. Challenges overcome: Salt spray corrosion, platform movement, ducting over water. Results: Reliable communications for 200+ personnel, real-time production monitoring."),
            ('section', "7.6 Public Safety and Emergency Services"),
            ('example', "<b>Case Study: Emergency Response Network</b><br/><br/>Requirement: Resilient communications for emergency services during disasters. System: Mesh topology with redundant paths, 8-hour battery backup, generator at hubs, mobile units for rapid deployment. Real-World Test: During major earthquake, network remained operational when 60% of cellular sites failed."),
            ('section', "7.7 Transportation Systems"),
            ('example', "<b>Case Study: Highway Traffic Management</b><br/><br/>Project: Monitor 200 km highway corridor. Infrastructure: CCTV cameras every 2 km, variable message signs, traffic sensors. Communications: Linear microwave topology, 5.8 GHz band, each camera has link to aggregation point. Outcomes: 30% reduction in accident response time, dynamic traffic management."),
            ('section', "7.8 Utility Companies"),
            ('example', "<b>Case Study: Power Grid Communications</b><br/><br/>Application: Connect 80 substations for SCADA and teleprotection. Requirements: Ultra-low latency (<10ms), high availability (99.999%), EMI immunity. Implementation: 6 GHz licensed spectrum, ring topology with protection switching, IEC 61850 integration. Benefits: Faster fault detection, reduced outage duration, improved grid stability."),
            ('section', "7.9 Internet Service Providers (WISP)"),
            ('example', "<b>Case Study: WISP Network Deployment</b><br/><br/>Market: Suburban area with 20,000 potential customers. Architecture: Fiber POP in town, 5 towers (30-50m), point-to-multipoint topology, 5.8 GHz for access, 11 GHz for backhaul. Results: 3,000 subscribers in first year, average 15 Mbps download, ROI in 18 months."),
            ('pagebreak',)
        ]
        self.create_chapter("Chapter 7: Real-Life Applications and Case Studies", content)

    def create_chapter_8(self):
        content = [
            ('section', "8.1 Introduction to Troubleshooting"),
            ('body', "Systematic troubleshooting methodology is essential for quickly identifying and resolving microwave system problems."),
            ('section', "8.2 Common Microwave System Problems"),
            ('body', "High VSWR: Symptoms - Reduced power, alarms. Causes - Loose connector, damaged cable, antenna fault | Low RSL: Symptoms - Poor performance, errors. Causes - Misalignment, obstruction, equipment failure | High BER: Symptoms - Data errors, retransmissions. Causes - Interference, low signal, multipath | Intermittent Link: Symptoms - Random outages. Causes - Loose connections, interference, weather"),
            ('section', "8.3 Troubleshooting Methodology"),
            ('list', [
                "Step 1: Gather Information - Review alarms, interview operators, check recent changes",
                "Step 2: Define the Problem - Identify what is working and what is not, determine scope",
                "Step 3: Develop Hypotheses - List possible causes, prioritize by likelihood",
                "Step 4: Test Hypotheses - Start with simplest causes, use test equipment",
                "Step 5: Implement Solution - Fix root cause, verify restoration, monitor",
                "Step 6: Document - Record problem, cause, solution, share lessons learned"
            ]),
            ('section', "8.4 Specific Troubleshooting Scenarios"),
            ('subsection', "High VSWR Troubleshooting"),
            ('body', "Symptoms: High reflected power alarm, reduced transmit power. Diagnostic Steps: Check VSWR reading, inspect connectors for tightness and damage, examine cable for kinks or water ingress, check antenna for damage or ice, use TDR to locate fault. Solutions: Tighten or replace connectors, replace damaged cable, clean corroded connections, replace faulty components."),
            ('subsection', "Low Received Signal Level (RSL)"),
            ('body', "Symptoms: RSL below threshold, increased BER, link instability. Diagnostic Steps: Compare to baseline, check for new obstructions, verify antenna alignment, check for water in feeders, measure transmit power, check for interference. Solutions: Realign antennas, clear vegetation, replace water-damaged components, increase transmit power, install higher-gain antennas."),
            ('subsection', "Interference Problems"),
            ('body', "Symptoms: High BER, intermittent outages, noise floor elevation. Diagnostic Steps: Use spectrum analyzer to identify interfering signals, note frequency and timing, check frequency coordination database. Solutions: Change frequency to clear channel, install additional filtering, improve antenna front-to-back ratio, adjust polarization."),
            ('section', "8.5 Preventive Maintenance"),
            ('body', "Regular preventive maintenance prevents problems and extends equipment life."),
            ('list', [
                "Daily (Remote): Monitor alarms and performance via NMS",
                "Weekly (Remote): Analyze trends and errors",
                "Monthly (Remote): Performance reporting",
                "Quarterly (On-site): Visual inspection, check connections",
                "Semi-Annual: Detailed inspection, clean filters, check grounding",
                "Annual: Comprehensive maintenance, full testing, alignment verification",
                "After Storms: Damage inspection"
            ]),
            ('subsection', "Annual Maintenance Checklist"),
            ('list', [
                "Tower and Antenna: Inspect structure for corrosion, check mounting hardware, verify lightning protection, re-weatherproof connections, clear vegetation",
                "Equipment: Clean equipment and filters, check cable connections and grounds, verify operating parameters, test backup power",
                "Testing: Measure VSWR and return loss, record RSL and transmit power, perform BER test, test alarms, measure ground resistance"
            ]),
            ('section', "8.6 Spare Parts Inventory"),
            ('list', [
                "Complete ODU/IDU units (1 per 20 deployed)",
                "Antenna feed assemblies",
                "Power supplies and converters",
                "Common connectors (N-type, etc.)",
                "Cable sections (various lengths)",
                "Mounting hardware (U-bolts, clamps)",
                "Weatherproofing materials",
                "Lightning arrestors",
                "Fuses and circuit breakers"
            ]),
            ('pagebreak',)
        ]
        self.create_chapter("Chapter 8: Troubleshooting and Maintenance", content)

    def create_chapter_9(self):
        content = [
            ('section', "9.1 Overview of Safety Standards"),
            ('body', "Microwave system installation and operation must comply with various safety standards and regulations to protect workers, the public, and the environment."),
            ('section', "9.2 RF Radiation Safety"),
            ('body', "Microwave systems emit radio frequency (RF) radiation. Understanding and controlling RF exposure is critical for worker and public safety."),
            ('subsection', "RF Exposure Limits"),
            ('body', "ICNIRP (International): General Public 2 W/m2 (1-10 GHz), Occupational 10 W/m2 | IEEE C95.1 (USA): General Public 0.57 mW/cm2, Occupational 2.85 mW/cm2 | FCC (USA Regulatory): Based on IEEE standards"),
            ('subsection', "RF Safety Practices"),
            ('list', [
                "Before Working on Antennas: Notify parties, power down transmitters, apply lockout/tagout, verify zero power with RF survey meter, post warning signs",
                "Working Near Active Antennas: Maintain safe distance, use RF monitoring badges, never stand in front of parabolic dish when powered, be aware of sidelobes"
            ]),
            ('section', "9.3 Electrical Safety"),
            ('list', [
                "Only qualified personnel should perform electrical work",
                "Follow lockout/tagout (LOTO) procedures",
                "Use insulated tools and PPE for electrical work",
                "Verify circuits are de-energized before working",
                "Install proper overcurrent protection",
                "Ensure proper grounding of all equipment",
                "Keep electrical enclosures closed and locked",
                "Regular inspection of electrical connections",
                "Use GFCI protection for outdoor outlets",
                "Maintain safe clearance from power lines"
            ]),
            ('section', "9.4 Working at Heights"),
            ('body', "Tower climbing involves significant fall hazards. Proper training and equipment are mandatory."),
            ('subsection', "Fall Protection Requirements"),
            ('list', [
                "100% tie-off policy above 6 feet (1.8m)",
                "Use certified fall arrest systems",
                "Double lanyards for continuous protection",
                "Regular inspection of climbing gear",
                "Annual recertification of harnesses and lanyards",
                "Climbing certification for all tower workers",
                "Rescue plan and equipment on site",
                "Weather restrictions (no climbing in high winds)",
                "Buddy system - never climb alone"
            ]),
            ('section', "9.5 Regulatory Compliance"),
            ('body', "Microwave systems must comply with telecommunications regulations in each country."),
            ('subsection', "Pakistan Regulatory Framework"),
            ('body', "Regulatory Authority: Pakistan Telecommunication Authority (PTA). Key Requirements: Type approval for radio equipment, frequency licensing for each link, compliance with National Frequency Allocation Plan, tower registration and structural certification, environmental compliance (IEE/EIA), regular license renewal, adherence to EMF exposure limits."),
            ('subsection', "Frequency Allocation (Pakistan)"),
            ('body', "2.4 GHz: ISM band (unlicensed, WiFi) | 5.8 GHz: ISM band (unlicensed) | 6 GHz: Licensed (microwave backhaul) | 7/8 GHz: Licensed (broadcast, backhaul) | 11 GHz: Licensed (short-haul) | 13/15/18/23 GHz: Licensed (various) | 26/28/38 GHz: Licensed (5G, mmWave)"),
            ('section', "9.6 Environmental Considerations"),
            ('list', [
                "Avoid protected areas (wildlife sanctuaries, wetlands)",
                "Conduct environmental impact assessment for large projects",
                "Minimize visual impact (camouflage where required)",
                "Proper disposal of electronic waste (batteries, circuit boards)",
                "Noise control for generators and equipment",
                "Spill prevention for fuel storage",
                "Vegetation management without harmful herbicides",
                "Bird protection (avoid nesting on antennas)"
            ]),
            ('section', "9.7 Quality Standards"),
            ('body', "ISO 9001: Quality management systems | ISO 14001: Environmental management | ISO 45001: Occupational health and safety | TIA-222: Structural standard for towers | NEC/NFPA 70: Electrical code | IEC 60950: IT equipment safety"),
            ('pagebreak',)
        ]
        self.create_chapter("Chapter 9: Safety Standards and Regulations", content)

    def create_chapter_10(self):
        content = [
            ('section', "10.1 Introduction"),
            ('body', "Microwave technology continues to evolve, driven by increasing bandwidth demands, 5G deployment, and advances in semiconductor technology."),
            ('section', "10.2 E-Band and V-Band Systems"),
            ('body', "Millimeter-wave frequencies (60-90 GHz) offer multi-gigabit capacity for short-range high-capacity links."),
            ('list', [
                "Advantages: Very high capacity (up to 10 Gbps), small antennas, less spectrum congestion, license-free in many countries",
                "Limitations: Short range (<5 km), high rain attenuation, requires clear line-of-sight",
                "Applications: 5G small cell backhaul, enterprise campus connectivity, data center interconnect"
            ]),
            ('section', "10.3 Adaptive Coding and Modulation (ACM)"),
            ('body', "ACM dynamically adjusts modulation and coding based on channel conditions, maximizing throughput while maintaining reliability."),
            ('list', [
                "Monitor channel conditions (RSL, BER, SNR)",
                "Automatically select optimal modulation (QPSK to 4096-QAM)",
                "Adjust coding rate based on error performance",
                "Change occurs in milliseconds without interruption",
                "Maximizes capacity during good conditions",
                "Maintains link during adverse conditions (rain fade)"
            ]),
            ('section', "10.4 MIMO (Multiple Input Multiple Output)"),
            ('body', "MIMO uses multiple antennas at both transmitter and receiver to increase capacity through spatial multiplexing."),
            ('list', [
                "2x capacity with 2x2 MIMO",
                "4x capacity with 4x4 MIMO",
                "Improved reliability through spatial diversity",
                "Better performance in multipath environments"
            ]),
            ('section', "10.5 Software-Defined Microwave"),
            ('body', "Software-defined radios (SDR) enable flexible, upgradeable microwave systems where functionality is defined by software."),
            ('list', [
                "Field-upgradable features and capacity",
                "Multi-band operation with same hardware",
                "Remote configuration and optimization",
                "AI/ML-based optimization capabilities"
            ]),
            ('section', "10.6 Integration with Fiber (Hybrid Networks)"),
            ('body', "Modern networks combine microwave and fiber for optimal performance and economics. Fiber for core and high-density routes, microwave for last-mile and difficult terrain, microwave as fiber backup/protection, unified management across both technologies."),
            ('section', "10.7 5G and Microwave Backhaul"),
            ('body', "5G networks require dense small cell deployment, creating massive demand for flexible, high-capacity backhaul."),
            ('list', [
                "5G Requirements: 1-10 Gbps per cell, <10ms latency, +/-65 ns synchronization, 10-100x more cells than 4G",
                "Microwave Solutions: E-band for ultra-high capacity short links, traditional bands (6-38 GHz) for macro cells, integrated access and backhaul (IAB)"
            ]),
            ('section', "10.8 AI and Machine Learning in Microwave Networks"),
            ('list', [
                "Predictive maintenance (anticipate failures)",
                "Automatic optimization of network parameters",
                "Interference prediction and avoidance",
                "Traffic pattern analysis and capacity planning",
                "Automated fault diagnosis and resolution",
                "Energy efficiency optimization"
            ]),
            ('section', "10.9 Green Microwave Systems"),
            ('body', "Energy efficiency is becoming a key consideration."),
            ('list', [
                "High-efficiency power amplifiers (>50% efficiency)",
                "Automatic power control (reduce when not needed)",
                "Sleep modes during low traffic periods",
                "Solar and wind power for remote sites",
                "Advanced battery technology (Li-ion, fuel cells)",
                "Passive cooling to reduce air conditioning"
            ]),
            ('section', "10.10 Satellite-Microwave Convergence"),
            ('body', "Low Earth Orbit (LEO) satellite constellations are creating new opportunities for integrated satellite-terrestrial networks. Examples: Starlink, OneWeb, Kuiper integration with terrestrial 5G."),
            ('section', "10.11 Conclusion"),
            ('body', "Microwave technology remains vital to global communications infrastructure. Continuous innovation ensures microwave systems will continue to evolve and meet growing connectivity demands. Key trends include higher frequencies, intelligent automation, integration with other technologies, and focus on sustainability."),
            ('pagebreak',)
        ]
        self.create_chapter("Chapter 10: Future Trends in Microwave Technology", content)

    def create_glossary(self):
        content = [
            ('section', "Glossary of Terms"),
            ('body', "<b>ACM:</b> Adaptive Coding and Modulation - Dynamic adjustment based on channel conditions"),
            ('body', "<b>BER:</b> Bit Error Rate - Ratio of erroneous bits to total bits transmitted"),
            ('body', "<b>dB:</b> Decibel - Logarithmic unit for expressing ratios"),
            ('body', "<b>dBi:</b> Decibel isotropic - Antenna gain relative to isotropic radiator"),
            ('body', "<b>dBm:</b> Decibel milliwatt - Power level relative to 1 milliwatt"),
            ('body', "<b>FSPL:</b> Free Space Path Loss - Signal attenuation in free space"),
            ('body', "<b>GHz:</b> Gigahertz - One billion Hertz"),
            ('body', "<b>IDU:</b> Indoor Unit - Equipment located indoors"),
            ('body', "<b>IF:</b> Intermediate Frequency - Frequency between baseband and RF"),
            ('body', "<b>LNA:</b> Low Noise Amplifier - Amplifier with minimal added noise"),
            ('body', "<b>LOS:</b> Line of Sight - Direct unobstructed path between antennas"),
            ('body', "<b>MIMO:</b> Multiple Input Multiple Output - Multiple antennas for capacity"),
            ('body', "<b>NMS:</b> Network Management System - Monitoring and control software"),
            ('body', "<b>ODU:</b> Outdoor Unit - Radio transceiver mounted near antenna"),
            ('body', "<b>QAM:</b> Quadrature Amplitude Modulation - Modulation using amplitude and phase"),
            ('body', "<b>RF:</b> Radio Frequency - Electromagnetic frequencies for wireless"),
            ('body', "<b>RSL:</b> Received Signal Level - Power level of received signal"),
            ('body', "<b>SDR:</b> Software Defined Radio - Software-configurable radio"),
            ('body', "<b>SNR:</b> Signal-to-Noise Ratio - Ratio of signal power to noise power"),
            ('body', "<b>VSWR:</b> Voltage Standing Wave Ratio - Measure of impedance matching"),
            ('body', "<b>VSAT:</b> Very Small Aperture Terminal - Small satellite earth station"),
            ('body', "<b>WISP:</b> Wireless Internet Service Provider - ISP using wireless"),
            ('pagebreak',)
        ]
        self.create_chapter("", content)

    def create_references(self):
        content = [
            ('section', "References and Resources"),
            ('subsection', "Books"),
            ('body', "Microwave Engineering by David M. Pozar | Microwave Mobile Communications by William C. Jakes | Digital Microwave Communication by George Kizer | RF and Microwave Wireless Systems by Kai Chang"),
            ('subsection', "Standards"),
            ('body', "ITU-R Recommendations (International Telecommunication Union) | IEEE 802.11 (WiFi standards) | 3GPP TS (Cellular standards including 5G) | TIA-222 (Tower structural standard) | ICNIRP Guidelines (RF exposure limits)"),
            ('subsection', "Websites"),
            ('body', "www.itu.int - International Telecommunication Union | www.ieee.org - IEEE | www.pta.gov.pk - Pakistan Telecommunication Authority | www.arrl.org - American Radio Relay League | www.microwaves101.com - Microwave engineering reference"),
            ('spacer', 1*inch),
            ('section', "About ALAM-ACADEMY"),
            ('body', f"<b><font size='16' color='darkblue'>{ACADEMY_NAME}</font></b>"),
            ('body', f"<b>Owner:</b> {OWNER_NAME}"),
            ('body', f"<b><font size='13' color='darkred'>Contact No: {CONTACT_NO}</font></b>"),
            ('body', f"<b>Email:</b> {EMAIL_ID}"),
            ('body', f"<b>GitHub:</b> {GITHUB_ACCOUNT}"),
            ('body', f"<b>Address:</b> {PUBLISHER_ADDRESS}"),
            ('spacer', 0.5*inch),
            ('body', f"<font size='11' color='darkgreen'><b>For any inquiries about this book, please contact: {CONTACT_NO}</b></font>"),
            ('spacer', 0.3*inch),
            ('body', f"<font size='10'>Copyright {datetime.now().year} {ACADEMY_NAME}. All rights reserved.</font>")
        ]
        self.create_chapter("", content)

    def generate(self):
        print("=" * 60)
        print("Microwave Systems Book Generator")
        print("=" * 60)
        print(f"Publisher: {ACADEMY_NAME}")
        print(f"Owner: {OWNER_NAME}")
        print(f"Company: {COMPANY_NAME}")
        print(f"Contact: {CONTACT_NO}")
        print(f"Email: {EMAIL_ID}")
        print("=" * 60)
        print("\nGenerating book...")
        
        self.create_title_page()
        print("Title page created")
        
        self.create_table_of_contents()
        print("Table of contents created")
        
        self.create_chapter_1()
        print("Chapter 1: Introduction created")
        
        self.create_chapter_2()
        print("Chapter 2: Fundamentals created")
        
        self.create_chapter_3()
        print("Chapter 3: Hardware created")
        
        self.create_chapter_4()
        print("Chapter 4: Software created")
        
        self.create_chapter_5()
        print("Chapter 5: Accessories created")
        
        self.create_chapter_6()
        print("Chapter 6: Tower Installation created")
        
        self.create_chapter_7()
        print("Chapter 7: Applications created")
        
        self.create_chapter_8()
        print("Chapter 8: Troubleshooting created")
        
        self.create_chapter_9()
        print("Chapter 9: Safety created")
        
        self.create_chapter_10()
        print("Chapter 10: Future Trends created")
        
        self.create_glossary()
        print("Glossary created")
        
        self.create_references()
        print("References created")
        
        print("\nBuilding PDF...")
        self.doc.build(self.story, onFirstPage=self.add_header, onLaterPages=self.add_header)
        
        print("=" * 60)
        print(f"SUCCESS! Book generated: {self.filename}")
        print(f"Total pages: {self.doc.page}")
        print("=" * 60)


if __name__ == "__main__":
    book = MicrowaveBook()
    book.generate()
