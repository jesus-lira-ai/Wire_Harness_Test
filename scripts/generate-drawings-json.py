#!/usr/bin/env python3
"""
Auto-generate drawings.json from PDFs in the drawings/ folder.

This script:
1. Scans drawings/ folder for all PDF files
2. Extracts part number and revision from filename (format: 04-210-XXXX.REV.pdf)
3. Reads description and date from inside the PDF
4. Generates drawings.json automatically

Filename format: 04-210-3138.A2.pdf
                 (part-number).(revision).pdf
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path

# Try to import PyPDF2, provide fallback
try:
    import PyPDF2
    HAS_PDF_READER = True
except ImportError:
    HAS_PDF_READER = False
    print("Warning: PyPDF2 not installed. Will use filename only.")


def extract_from_filename(filename):
    """Extract part number and revision from filename."""
    # Remove .pdf extension
    name = filename.replace('.pdf', '')
    
    # Split by dot or underscore
    # Examples: 04-210-3138.A2 or 04-210-3138_A2
    parts = re.split(r'[._]', name)
    
    if len(parts) >= 2:
        part_number = parts[0]  # 04-210-3138
        revision = parts[1]      # A2
    else:
        part_number = name
        revision = "A"
    
    return part_number, revision


def extract_from_pdf(pdf_path):
    """Extract description and date from PDF content."""
    if not HAS_PDF_READER:
        return None, None
    
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            # Read first page
            if len(reader.pages) > 0:
                first_page = reader.pages[0]
                text = first_page.extract_text()
                
                # Extract description (look for "Title" or "Description")
                description = None
                for line in text.split('\n'):
                    # Look for title or description field
                    if 'Title' in line or 'Description' in line:
                        # Try to extract text after the label
                        parts = line.split(':', 1)
                        if len(parts) > 1:
                            description = parts[1].strip()
                            break
                    # Also try to find pattern like "HARNESS, ..."
                    if line.startswith('HARNESS') or line.startswith('PDM'):
                        description = line.strip()
                        break
                
                # Extract date (look for "Date" field)
                date_updated = None
                for line in text.split('\n'):
                    # Look for date patterns
                    if 'Date' in line or 'Updated' in line:
                        # Try to extract date
                        date_match = re.search(r'(\d{1,2}[/-]\d{1,2}[/-]\d{4})', line)
                        if date_match:
                            date_updated = date_match.group(1)
                            # Convert to MM/DD/YYYY format
                            date_updated = date_updated.replace('-', '/')
                            break
                
                return description, date_updated
                
    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")
        return None, None
    
    return None, None


def generate_drawings_json():
    """Generate drawings.json from all PDFs in drawings/ folder."""
    
    drawings_folder = Path('drawings')
    
    if not drawings_folder.exists():
        print("Error: drawings/ folder not found!")
        return
    
    # Get all PDF files
    pdf_files = sorted(drawings_folder.glob('*.pdf'))
    
    if not pdf_files:
        print("No PDF files found in drawings/ folder")
        return
    
    # Dictionary to group ALL revisions by part number
    drawings_by_part = {}
    
    for pdf_file in pdf_files:
        filename = pdf_file.name
        print(f"Processing: {filename}")
        
        # Extract from filename
        part_number, revision = extract_from_filename(filename)
        
        # Extract from PDF content
        description, date_updated = extract_from_pdf(pdf_file)
        
        # Use defaults if extraction failed
        if not description:
            description = f"Harness Drawing {part_number}"
        
        if not date_updated:
            # Use file modification date
            mod_time = os.path.getmtime(pdf_file)
            date_updated = datetime.fromtimestamp(mod_time).strftime('%m/%d/%Y')
        
        # Create drawing entry
        drawing = {
            "partNumber": part_number,
            "description": description,
            "revision": revision,
            "dateUpdated": date_updated,
            "pages": 7,
            "status": "Released",
            "filename": filename,
            "modTime": os.path.getmtime(pdf_file)
        }
        
        # Group ALL revisions by part number
        if part_number not in drawings_by_part:
            drawings_by_part[part_number] = []
        
        drawings_by_part[part_number].append(drawing)
        print(f"  ✓ {part_number} Rev {revision}")
    
    # Process each part number: latest + history
    drawings = []
    for part_number in sorted(drawings_by_part.keys()):
        all_revisions = drawings_by_part[part_number]
        
        # Sort by modification time (newest first)
        all_revisions.sort(key=lambda x: x['modTime'], reverse=True)
        
        # Latest revision (first after sorting)
        latest = all_revisions[0].copy()
        del latest['modTime']
        
        # Previous revisions (rest of the list)
        previous = []
        for rev in all_revisions[1:]:
            prev_entry = {
                "revision": rev['revision'],
                "dateUpdated": rev['dateUpdated'],
                "filename": rev['filename']
            }
            previous.append(prev_entry)
        
        # Add previous revisions to latest entry
        if previous:
            latest['previousRevisions'] = previous
            print(f"  → {part_number}: Latest=Rev {latest['revision']}, History={len(previous)} revisions")
        
        drawings.append(latest)
    
    # Write to drawings.json
    with open('drawings.json', 'w') as f:
        json.dump(drawings, f, indent=2)
    
    print(f"\n✅ Generated drawings.json with {len(drawings)} drawings!")
    print(f"   Total PDFs processed: {len(pdf_files)}")
    print(f"   Unique part numbers: {len(drawings)}")
    total_history = sum(len(d.get('previousRevisions', [])) for d in drawings)
    print(f"   Previous revisions tracked: {total_history}")


if __name__ == '__main__':
    generate_drawings_json()
