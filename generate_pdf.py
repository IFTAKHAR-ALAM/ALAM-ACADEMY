#!/usr/bin/env python3
"""
AI Book PDF Generator
Converts markdown content to a professionally formatted PDF book.
Published by ALAM-ACADEMY
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path

def create_html_content(md_content: str) -> str:
    """Convert markdown to HTML with custom styling."""
    
    # Convert markdown to HTML
    html_body = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'toc']
    )
    
    # Create full HTML document with professional styling
    html_document = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Comprehensive Guide to Artificial Intelligence - ALAM-ACADEMY</title>
        <style>
            @page {{
                size: A4;
                margin: 2.5cm;
                @bottom-center {{
                    content: "Page " counter(page);
                    font-size: 10pt;
                    color: #666;
                }}
                @bottom-right {{
                    content: "ALAM-ACADEMY";
                    font-size: 9pt;
                    color: #666;
                }}
            }}
            
            @page :first {{
                @bottom-center {{ content: none; }}
                @bottom-right {{ content: none; }}
            }}
            
            body {{
                font-family: 'Georgia', 'Times New Roman', serif;
                font-size: 11pt;
                line-height: 1.6;
                color: #1a1a1a;
                text-align: justify;
            }}
            
            h1 {{
                font-family: 'Arial', 'Helvetica', sans-serif;
                font-size: 24pt;
                color: #1e3a5f;
                border-bottom: 3px solid #1e3a5f;
                padding-bottom: 10px;
                margin-top: 40px;
                margin-bottom: 20px;
                page-break-after: avoid;
            }}
            
            h2 {{
                font-family: 'Arial', 'Helvetica', sans-serif;
                font-size: 18pt;
                color: #2c5282;
                border-bottom: 2px solid #2c5282;
                padding-bottom: 8px;
                margin-top: 35px;
                margin-bottom: 15px;
                page-break-after: avoid;
            }}
            
            h3 {{
                font-family: 'Arial', 'Helvetica', sans-serif;
                font-size: 14pt;
                color: #2d3748;
                margin-top: 25px;
                margin-bottom: 12px;
                page-break-after: avoid;
            }}
            
            h4 {{
                font-family: 'Arial', 'Helvetica', sans-serif;
                font-size: 12pt;
                color: #4a5568;
                margin-top: 20px;
                margin-bottom: 10px;
                page-break-after: avoid;
            }}
            
            p {{
                margin: 12px 0;
                text-indent: 0;
            }}
            
            ul, ol {{
                margin: 12px 0;
                padding-left: 30px;
            }}
            
            li {{
                margin: 6px 0;
            }}
            
            code {{
                background-color: #f7fafc;
                border: 1px solid #e2e8f0;
                border-radius: 3px;
                padding: 2px 6px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 10pt;
                color: #e53e3e;
            }}
            
            pre {{
                background-color: #1a202c;
                border: 1px solid #2d3748;
                border-radius: 5px;
                padding: 15px;
                overflow-x: auto;
                margin: 15px 0;
                page-break-inside: avoid;
            }}
            
            pre code {{
                background-color: transparent;
                border: none;
                padding: 0;
                color: #e2e8f0;
            }}
            
            blockquote {{
                border-left: 4px solid #4299e1;
                margin: 15px 0;
                padding: 10px 20px;
                background-color: #ebf8ff;
                font-style: italic;
            }}
            
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
                page-break-inside: avoid;
            }}
            
            th, td {{
                border: 1px solid #cbd5e0;
                padding: 10px 15px;
                text-align: left;
            }}
            
            th {{
                background-color: #2c5282;
                color: white;
                font-weight: bold;
            }}
            
            tr:nth-child(even) {{
                background-color: #f7fafc;
            }}
            
            .title-page {{
                text-align: center;
                page-break-after: always;
                padding-top: 100px;
            }}
            
            .title-page h1 {{
                font-size: 32pt;
                border: none;
                color: #1e3a5f;
            }}
            
            .title-page h2 {{
                font-size: 18pt;
                border: none;
                color: #4a5568;
                font-weight: normal;
            }}
            
            .publisher-info {{
                margin-top: 80px;
                font-size: 12pt;
                line-height: 2;
            }}
            
            .copyright {{
                margin-top: 60px;
                font-size: 10pt;
                color: #666;
            }}
            
            .toc {{
                page-break-after: always;
            }}
            
            .toc h1 {{
                text-align: center;
            }}
            
            .chapter-break {{
                page-break-before: always;
            }}
            
            strong {{
                color: #1a202c;
            }}
            
            a {{
                color: #3182ce;
                text-decoration: none;
            }}
            
            hr {{
                border: none;
                border-top: 2px solid #e2e8f0;
                margin: 30px 0;
            }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """
    
    return html_document


def generate_pdf():
    """Generate PDF from markdown file."""
    
    # Read markdown content
    md_path = Path(__file__).parent / 'AI_Comprehensive_Guide.md'
    
    if not md_path.exists():
        print(f"Error: Markdown file not found at {md_path}")
        return
    
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    print("Converting markdown to HTML...")
    html_content = create_html_content(md_content)
    
    # Save intermediate HTML (optional, for debugging)
    html_path = Path(__file__).parent / 'AI_Comprehensive_Guide.html'
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"HTML saved to: {html_path}")
    
    print("Generating PDF...")
    
    # Generate PDF using WeasyPrint
    html_obj = HTML(string=html_content)
    
    pdf_path = Path(__file__).parent / 'AI_Comprehensive_Guide.pdf'
    html_obj.write_pdf(
        str(pdf_path),
        optimize_size=('fonts', 'images', 'pdf'),
    )
    
    print(f"\n{'='*60}")
    print("PDF Generation Complete!")
    print(f"{'='*60}")
    print(f"Output file: {pdf_path}")
    print(f"Publisher: ALAM-ACADEMY")
    print(f"Owner: M IFTIKHAR ALAM")
    print(f"Contact: alammiftikhar@gmail.com | 0333-9257987")
    print(f"{'='*60}")


if __name__ == '__main__':
    generate_pdf()
