#!/usr/bin/env python3
"""
AI Book PDF Generator using ReportLab
Converts markdown content to a professionally formatted PDF book.
Published by ALAM-ACADEMY
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, 
    Table, TableStyle, KeepTogether, Image
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import re
from pathlib import Path


class AIBackBookGenerator:
    """Generate a professional PDF book from markdown content."""
    
    def __init__(self, output_path: str):
        self.output_path = output_path
        self.doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=2.5*cm,
            leftMargin=2.5*cm,
            topMargin=2.5*cm,
            bottomMargin=2.5*cm
        )
        self.styles = getSampleStyleSheet()
        self.story = []
        self._setup_styles()
    
    def _setup_styles(self):
        """Configure custom paragraph styles."""
        
        # Title style
        self.styles.add(ParagraphStyle(
            name='AICustomTitle',
            parent=self.styles['Heading1'],
            fontSize=28,
            textColor=HexColor('#1e3a5f'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold',
            leading=36
        ))
        
        # Subtitle style
        self.styles.add(ParagraphStyle(
            name='AISubtitle',
            parent=self.styles['Normal'],
            fontSize=14,
            textColor=HexColor('#4a5568'),
            spaceAfter=20,
            alignment=TA_CENTER,
            fontName='Helvetica',
            leading=20
        ))
        
        # Chapter title style
        self.styles.add(ParagraphStyle(
            name='AIChapterTitle',
            parent=self.styles['Heading1'],
            fontSize=20,
            textColor=HexColor('#1e3a5f'),
            spaceAfter=20,
            spaceBefore=30,
            fontName='Helvetica-Bold',
            leading=26,
            keepWithNext=True
        ))
        
        # Section style
        self.styles.add(ParagraphStyle(
            name='AISection',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=HexColor('#2c5282'),
            spaceAfter=15,
            spaceBefore=25,
            fontName='Helvetica-Bold',
            leading=22
        ))
        
        # Subsection style
        self.styles.add(ParagraphStyle(
            name='AISubsection',
            parent=self.styles['Heading3'],
            fontSize=13,
            textColor=HexColor('#2d3748'),
            spaceAfter=12,
            spaceBefore=18,
            fontName='Helvetica-Bold',
            leading=18
        ))
        
        # Body text style
        self.styles.add(ParagraphStyle(
            name='AIBodyText',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=HexColor('#1a1a1a'),
            spaceAfter=12,
            alignment=TA_JUSTIFY,
            fontName='Times-Roman',
            leading=16
        ))
        
        # Code style
        self.styles.add(ParagraphStyle(
            name='AICode',
            parent=self.styles['Normal'],
            fontSize=9,
            textColor=HexColor('#e2e8f0'),
            backColor=HexColor('#1a202c'),
            spaceAfter=15,
            spaceBefore=15,
            fontName='Courier',
            leading=13
        ))
        
        # Quote style
        self.styles.add(ParagraphStyle(
            name='AIQuote',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=HexColor('#4a5568'),
            leftIndent=20,
            rightIndent=20,
            backColor=HexColor('#ebf8ff'),
            borderPadding=10,
            fontName='Times-Italic',
            leading=16
        ))
        
        # Publisher info style
        self.styles.add(ParagraphStyle(
            name='AIPublisherInfo',
            parent=self.styles['Normal'],
            fontSize=12,
            textColor=HexColor('#1a202c'),
            spaceAfter=10,
            alignment=TA_CENTER,
            fontName='Helvetica',
            leading=20
        ))
        
        # Copyright style
        self.styles.add(ParagraphStyle(
            name='AICopyright',
            parent=self.styles['Normal'],
            fontSize=9,
            textColor=HexColor('#666666'),
            spaceAfter=8,
            alignment=TA_CENTER,
            fontName='Times-Roman',
            leading=14
        ))
        
        # TOC entry style
        self.styles.add(ParagraphStyle(
            name='AITOCEntry',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=HexColor('#1a1a1a'),
            spaceAfter=6,
            fontName='Times-Roman',
            leading=14
        ))
        
        # List item style
        self.styles.add(ParagraphStyle(
            name='AIListItem',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=HexColor('#1a1a1a'),
            spaceAfter=8,
            leftIndent=20,
            fontName='Times-Roman',
            leading=16
        ))

    def _parse_markdown(self, content: str) -> list:
        """Parse markdown content into structured elements."""
        elements = []
        lines = content.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines
            if not line:
                i += 1
                continue
            
            # Title page markers
            if line.startswith('## Title Page'):
                i += 1
                continue
            
            # Main title (H1)
            if line.startswith('# ') and not line.startswith('##'):
                text = line[2:].strip()
                elements.append(('h1', text))
                i += 1
            
            # Section (H2)
            elif line.startswith('## '):
                text = line[3:].strip()
                elements.append(('h2', text))
                i += 1
            
            # Subsection (H3)
            elif line.startswith('### '):
                text = line[4:].strip()
                elements.append(('h3', text))
                i += 1
            
            # Sub-subsection (H4)
            elif line.startswith('#### '):
                text = line[5:].strip()
                elements.append(('h4', text))
                i += 1
            
            # Bold text as paragraph
            elif line.startswith('**') and line.endswith('**'):
                text = line[2:-2].strip()
                elements.append(('bold', text))
                i += 1
            
            # List items
            elif line.startswith('- '):
                list_items = []
                while i < len(lines) and lines[i].strip().startswith('- '):
                    text = lines[i].strip()[2:].strip()
                    list_items.append(text)
                    i += 1
                elements.append(('list', list_items))
            
            # Code blocks
            elif line.startswith('```'):
                code_lines = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    code_lines.append(lines[i])
                    i += 1
                elements.append(('code', '\n'.join(code_lines)))
                i += 1
            
            # Regular paragraph
            else:
                # Collect paragraph lines
                para_lines = []
                while i < len(lines) and lines[i].strip() and not any([
                    lines[i].strip().startswith('#'),
                    lines[i].strip().startswith('- '),
                    lines[i].strip().startswith('**'),
                    lines[i].strip().startswith('```'),
                ]):
                    para_lines.append(lines[i].strip())
                    i += 1
                if para_lines:
                    elements.append(('p', ' '.join(para_lines)))
        
        return elements

    def _add_title_page(self):
        """Add the book title page."""
        
        # Title
        self.story.append(Spacer(1, 1.5*inch))
        self.story.append(Paragraph("COMPREHENSIVE GUIDE TO", self.styles['AISubtitle']))
        self.story.append(Paragraph("ARTIFICIAL INTELLIGENCE", self.styles['AICustomTitle']))
        self.story.append(Spacer(1, 0.5*inch))
        
        # Subtitle
        self.story.append(Paragraph(
            "Theory, Applications, Software & Hardware",
            self.styles['AISubtitle']
        ))
        self.story.append(Paragraph(
            "A Complete Guide for Students, Professionals, and Enthusiasts",
            self.styles['AISubtitle']
        ))
        
        # Publisher info
        self.story.append(Spacer(1, 1*inch))
        self.story.append(Paragraph("Published by:", self.styles['AIPublisherInfo']))
        self.story.append(Paragraph("ALAM-ACADEMY", self.styles['AIChapterTitle']))
        
        self.story.append(Spacer(1, 0.5*inch))
        self.story.append(Paragraph("Owner: M IFTIKHAR ALAM", self.styles['AIPublisherInfo']))
        self.story.append(Paragraph("Email: alammiftikhar@gmail.com", self.styles['AIPublisherInfo']))
        self.story.append(Paragraph("Contact: 0333-9257987", self.styles['AIPublisherInfo']))
        self.story.append(Paragraph("Address: Karachi, PAKISTAN", self.styles['AIPublisherInfo']))
        
        # Copyright
        self.story.append(Spacer(1, 0.8*inch))
        self.story.append(Paragraph("Copyright © 2026 ALAM-ACADEMY", self.styles['AICopyright']))
        self.story.append(Paragraph("All Rights Reserved", self.styles['AICopyright']))
        self.story.append(Paragraph("First Edition: 2026", self.styles['AICopyright']))
        
        self.story.append(PageBreak())

    def _add_dedication(self):
        """Add dedication page."""
        self.story.append(Spacer(1, 2*inch))
        self.story.append(Paragraph("DEDICATION", self.styles['AISection']))
        self.story.append(Spacer(1, 0.5*inch))
        self.story.append(Paragraph(
            "This book is dedicated to all the students, researchers, and professionals "
            "who are passionate about Artificial Intelligence and want to contribute to "
            "the advancement of this transformative technology for the benefit of humanity.",
            self.styles['AIBodyText']
        ))
        self.story.append(PageBreak())

    def _add_preface(self):
        """Add preface page."""
        self.story.append(Paragraph("PREFACE", self.styles['AIChapterTitle']))
        self.story.append(Paragraph(
            "Artificial Intelligence (AI) has emerged as one of the most transformative "
            "technologies of the 21st century. From healthcare to finance, from transportation "
            "to entertainment, AI is reshaping every aspect of our lives. This comprehensive "
            "guide aims to provide readers with a thorough understanding of AI concepts, "
            "practical applications, software tools, and hardware requirements.",
            self.styles['AIBodyText']
        ))
        self.story.append(Paragraph(
            "The book is structured to serve multiple audiences: students beginning their "
            "journey in AI, professionals looking to transition into AI careers, researchers "
            "seeking a comprehensive reference, business leaders wanting to understand AI "
            "implementation, and enthusiasts curious about this fascinating field.",
            self.styles['AIBodyText']
        ))
        self.story.append(Paragraph(
            "Each chapter builds upon previous knowledge, ensuring a smooth learning curve "
            "from fundamental concepts to advanced topics.",
            self.styles['AIBodyText']
        ))
        self.story.append(PageBreak())

    def _add_table_of_contents(self):
        """Add table of contents."""
        self.story.append(Paragraph("TABLE OF CONTENTS", self.styles['AIChapterTitle']))
        
        toc_data = [
            ("PART I: FOUNDATIONS OF ARTIFICIAL INTELLIGENCE", ""),
            ("Chapter 1: Introduction to Artificial Intelligence", "1"),
            ("Chapter 2: Mathematical Foundations for AI", "15"),
            ("Chapter 3: Programming for AI", "28"),
            ("PART II: MACHINE LEARNING FUNDAMENTALS", ""),
            ("Chapter 4: Introduction to Machine Learning", "42"),
            ("Chapter 5: Supervised Learning Algorithms", "55"),
            ("Chapter 6: Unsupervised Learning Algorithms", "70"),
            ("Chapter 7: Ensemble Methods and Advanced ML", "85"),
            ("PART III: DEEP LEARNING AND NEURAL NETWORKS", ""),
            ("Chapter 8: Neural Networks Fundamentals", "98"),
            ("Chapter 9: Deep Learning Architectures", "115"),
            ("Chapter 10: Training Deep Neural Networks", "132"),
            ("PART IV: SPECIALIZED AI DOMAINS", ""),
            ("Chapter 11: Natural Language Processing", "148"),
            ("Chapter 12: Computer Vision", "168"),
            ("Chapter 13: Speech and Audio Processing", "185"),
            ("Chapter 14: Robotics and Autonomous Systems", "198"),
            ("Chapter 15: Reinforcement Learning", "212"),
            ("PART V: AI SOFTWARE AND TOOLS", ""),
            ("Chapter 16: AI Development Frameworks", "228"),
            ("Chapter 17: Data Science Tools for AI", "245"),
            ("Chapter 18: NLP Libraries and Tools", "258"),
            ("Chapter 19: Computer Vision Libraries", "270"),
            ("Chapter 20: MLOps and Deployment", "282"),
            ("PART VI: AI HARDWARE", ""),
            ("Chapter 21: Computing Hardware for AI", "298"),
            ("Chapter 22: Building AI Workstations", "312"),
            ("Chapter 23: Edge AI and IoT Hardware", "325"),
            ("Chapter 24: Cloud Infrastructure for AI", "338"),
            ("PART VII: ADVANCED TOPICS", ""),
            ("Chapter 25: Generative AI", "352"),
            ("Chapter 26: Explainable AI (XAI)", "368"),
            ("Chapter 27: AI Ethics and Responsible AI", "380"),
            ("Chapter 28: AI Safety and Alignment", "395"),
            ("PART VIII: INDUSTRY APPLICATIONS", ""),
            ("Chapter 29: AI in Healthcare", "408"),
            ("Chapter 30: AI in Finance", "422"),
            ("Chapter 31: AI in Manufacturing", "435"),
            ("Chapter 32: AI in Retail and E-commerce", "448"),
            ("Chapter 33: AI in Transportation", "460"),
            ("Chapter 34: AI in Education", "472"),
            ("PART IX: CAREER AND BUSINESS", ""),
            ("Chapter 35: AI Career Paths", "485"),
            ("Chapter 36: Building AI Products", "498"),
            ("Chapter 37: AI Startup Guide", "510"),
            ("PART X: FUTURE OF AI", ""),
            ("Chapter 38: Emerging Trends in AI", "525"),
            ("Chapter 39: Artificial General Intelligence (AGI)", "538"),
            ("Chapter 40: AI and the Future of Work", "550"),
            ("APPENDICES", ""),
            ("Appendix A: Python Quick Reference", "565"),
            ("Appendix B: Mathematics Reference", "575"),
            ("Appendix C: AI Glossary", "585"),
            ("Appendix D: Resources and Further Reading", "595"),
            ("Appendix E: Practice Exercises and Solutions", "605"),
            ("INDEX", "620"),
        ]
        
        for title, page in toc_data:
            if page:
                text = f"{title}  .................................................................... {page}"
            else:
                text = f"\n<b>{title}</b>"
            self.story.append(Paragraph(text, self.styles['AITOCEntry']))
        
        self.story.append(PageBreak())

    def _add_content(self, markdown_path: str):
        """Add main content from markdown file."""
        
        with open(markdown_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        elements = self._parse_markdown(content)
        
        skip_until_next_h1 = False
        
        for elem_type, elem_data in elements:
            if elem_type == 'h1':
                # Skip title page and TOC headers
                if 'Title Page' in elem_data or 'TABLE OF CONTENTS' in elem_data:
                    skip_until_next_h1 = True
                    continue
                elif 'DEDICATION' in elem_data or 'PREFACE' in elem_data:
                    continue
                elif 'PART' in elem_data:
                    self.story.append(PageBreak())
                    self.story.append(Paragraph(elem_data, self.styles['AIChapterTitle']))
                    skip_until_next_h1 = False
                elif not skip_until_next_h1:
                    self.story.append(PageBreak())
                    self.story.append(Paragraph(elem_data, self.styles['AIChapterTitle']))
            
            elif elem_type == 'h2' and not skip_until_next_h1:
                self.story.append(Spacer(1, 20))
                self.story.append(Paragraph(elem_data, self.styles['AISection']))
            
            elif elem_type == 'h3' and not skip_until_next_h1:
                self.story.append(Spacer(1, 15))
                self.story.append(Paragraph(elem_data, self.styles['AISubsection']))
            
            elif elem_type == 'h4' and not skip_until_next_h1:
                self.story.append(Spacer(1, 10))
                self.story.append(Paragraph(f"<b>{elem_data}</b>", self.styles['AIBodyText']))
            
            elif elem_type == 'bold' and not skip_until_next_h1:
                self.story.append(Spacer(1, 8))
                self.story.append(Paragraph(f"<b>{elem_data}</b>", self.styles['AIBodyText']))
            
            elif elem_type == 'list' and not skip_until_next_h1:
                for item in elem_data:
                    # Handle bullet points
                    text = f"• {item}"
                    self.story.append(Paragraph(text, self.styles['AIListItem']))
            
            elif elem_type == 'code' and not skip_until_next_h1:
                # Format code for PDF
                code_text = elem_data.replace('<', '&lt;').replace('>', '&gt;')
                self.story.append(Spacer(1, 10))
                self.story.append(Paragraph(f"<font name='Courier'>{code_text}</font>", self.styles['AICode']))
            
            elif elem_type == 'p' and not skip_until_next_h1:
                self.story.append(Spacer(1, 8))
                self.story.append(Paragraph(elem_data, self.styles['AIBodyText']))

    def _add_publisher_page(self):
        """Add publisher information page."""
        self.story.append(PageBreak())
        self.story.append(Paragraph("ABOUT THE PUBLISHER", self.styles['AIChapterTitle']))
        self.story.append(Spacer(1, 20))
        self.story.append(Paragraph(
            "<b>ALAM-ACADEMY</b> is a leading educational publisher based in Karachi, Pakistan, "
            "dedicated to providing high-quality educational materials in emerging technologies. "
            "Founded by M Iftikhar Alam, the academy focuses on making complex technical subjects "
            "accessible to students and professionals across South Asia and beyond.",
            self.styles['AIBodyText']
        ))
        self.story.append(Spacer(1, 30))
        self.story.append(Paragraph("Contact Information:", self.styles['AISection']))
        self.story.append(Paragraph("Owner: M IFTIKHAR ALAM", self.styles['AIPublisherInfo']))
        self.story.append(Paragraph("Email: alammiftikhar@gmail.com", self.styles['AIPublisherInfo']))
        self.story.append(Paragraph("Phone: 0333-9257987", self.styles['AIPublisherInfo']))
        self.story.append(Paragraph("Address: Karachi, PAKISTAN", self.styles['AIPublisherInfo']))

    def generate(self, markdown_path: str):
        """Generate the complete PDF book."""
        
        print("Building title page...")
        self._add_title_page()
        
        print("Building dedication page...")
        self._add_dedication()
        
        print("Building preface...")
        self._add_preface()
        
        print("Building table of contents...")
        self._add_table_of_contents()
        
        print("Building main content...")
        self._add_content(markdown_path)
        
        print("Building publisher page...")
        self._add_publisher_page()
        
        print("Writing PDF file...")
        self.doc.build(self.story)
        
        print(f"\n{'='*60}")
        print("PDF Generation Complete!")
        print(f"{'='*60}")
        print(f"Output file: {self.output_path}")
        print(f"Publisher: ALAM-ACADEMY")
        print(f"Owner: M IFTIKHAR ALAM")
        print(f"Contact: alammiftikhar@gmail.com | 0333-9257987")
        print(f"{'='*60}")


def main():
    """Main entry point."""
    base_path = Path(__file__).parent
    markdown_path = base_path / 'AI_Comprehensive_Guide.md'
    output_path = base_path / 'AI_Comprehensive_Guide.pdf'
    
    if not markdown_path.exists():
        print(f"Error: Markdown file not found at {markdown_path}")
        return
    
    generator = AIBackBookGenerator(str(output_path))
    generator.generate(str(markdown_path))


if __name__ == '__main__':
    main()
