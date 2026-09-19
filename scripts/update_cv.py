from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'CV_Muhamad_Yayah_ATS.pdf'
OUTPUT = ROOT / 'output/pdf/CV_Muhamad_Yayah_ATS_Updated.pdf'
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
render_dir = ROOT / 'tmp/pdfs'
render_dir.mkdir(parents=True, exist_ok=True)

doc = fitz.open(SOURCE)
url = 'https://muhamadyayah.my.id'
label = 'Portfolio: ' + url
page = doc[0]
page.insert_text((51.84, 119), label, fontname='helv', fontsize=9, color=(0.1, 0.3, 0.4))
width = fitz.get_text_length(label, fontname='helv', fontsize=9)
page.insert_link({'kind': fitz.LINK_URI, 'from': fitz.Rect(51.84, 109.8, 51.84 + width, 121), 'uri': url})

page = doc[1]
old_skills = page.search_for('Microsoft Office | HRIS administration | AI chatbot tools')
assert len(old_skills) == 1, 'Expected one skills line'
page.add_redact_annot(old_skills[0], fill=(1, 1, 1))
page.apply_redactions()
lines = [
    'Microsoft Office | Talenta (HRIS) | AI chatbot tools',
    'e-Dabu (BPJS Kesehatan) | SIPP (BPJS Ketenagakerjaan)',
    'Internal inventory and asset management system',
]
for y, line in zip([606, 622, 638], lines):
    page.insert_text((51.84, y), line, fontname='helv', fontsize=10)
page.insert_text((51.84, 667), 'GENERAL AFFAIRS ADMINISTRATION', fontname='hebo', fontsize=9)
remaining = page.insert_textbox(fitz.Rect(51.84, 678, 560, 726),
    'Use an internal company system to support day-to-day inventory and asset recordkeeping. '
    'Earlier operational experience includes budgeting, ordering and maintenance coordination.',
    fontname='helv', fontsize=10, lineheight=1.3)
assert remaining >= 0, 'GA text does not fit'
metadata = doc.metadata
metadata['title'] = 'Muhamad Yayah - HR and HRGA Professional CV'
doc.set_metadata(metadata)
doc.save(OUTPUT, garbage=4, deflate=True)
doc.close()

check = fitz.open(OUTPUT)
assert len(check) == 3
text = '\n'.join(page.get_text() for page in check)
for required in [url, 'Talenta', 'e-Dabu', 'SIPP', 'GENERAL AFFAIRS ADMINISTRATION']:
    assert required in text, required
assert any(link.get('uri') == url for link in check[0].get_links())
for i, page in enumerate(check):
    page.get_pixmap(matrix=fitz.Matrix(1.4, 1.4)).save(render_dir / f'cv-updated-{i + 1}.png')
print(f'Verified: {OUTPUT}; 3 pages; clickable portfolio link; updated HR/GA tools.')
