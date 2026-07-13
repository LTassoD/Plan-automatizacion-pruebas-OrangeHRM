"""Set Spanish proofing language on DOCX and PPTX."""
from docx import Document
from docx.oxml.ns import qn as wqn
from docx.oxml import OxmlElement
from pptx import Presentation
from pptx.oxml.ns import qn as pqn
from lxml import etree
import copy

# Namespace map for creating elements via lxml
nsmap = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
}

base = r'C:\Users\User\Desktop\Duoc\Semestre V\Automatizacion de Pruebas\AutomatizacionPruebasPython'

# === DOCX ===
docx_path = f'{base}/INFORME_FINAL_EFT.docx'
doc = Document(docx_path)

styles = doc.styles.element
docDefaults = styles.find(wqn('w:docDefaults'))
if docDefaults is None:
    docDefaults = OxmlElement('w:docDefaults')
    styles.insert(0, docDefaults)
rPrDefault = docDefaults.find(wqn('w:rPrDefault'))
if rPrDefault is None:
    rPrDefault = OxmlElement('w:rPrDefault')
    docDefaults.append(rPrDefault)
rPr = rPrDefault.find(wqn('w:rPr'))
if rPr is None:
    rPr = OxmlElement('w:rPr')
    rPrDefault.append(rPr)
lang = rPr.find(wqn('w:lang'))
if lang is None:
    lang = OxmlElement('w:lang')
    rPr.append(lang)
lang.set(wqn('w:val'), 'es-CL')
lang.set(wqn('w:eastAsia'), 'es-CL')

# Set es-CL on every run in paragraphs and tables
for para in doc.paragraphs:
    for run in para.runs:
        rPr = run._r.find(wqn('w:rPr'))
        if rPr is None:
            rPr = OxmlElement('w:rPr')
            run._r.insert(0, rPr)
        lang = rPr.find(wqn('w:lang'))
        if lang is None:
            lang = OxmlElement('w:lang')
            rPr.append(lang)
        lang.set(wqn('w:val'), 'es-CL')

for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                for run in para.runs:
                    rPr = run._r.find(wqn('w:rPr'))
                    if rPr is None:
                        rPr = OxmlElement('w:rPr')
                        run._r.insert(0, rPr)
                    lang = rPr.find(wqn('w:lang'))
                    if lang is None:
                        lang = OxmlElement('w:lang')
                        rPr.append(lang)
                    lang.set(wqn('w:val'), 'es-CL')

doc.save(docx_path)
print('DOCX: OK')

# === PPTX ===
pptx_path = f'{base}/PRESENTACION_FINAL_EFT.pptx'
prs = Presentation(pptx_path)

def set_lang_on_element(el):
    """Set es-CL on a:rPr and a:defRPr elements recursively."""
    # Handle a:r (text runs)
    for r in el.iter(f'{{{nsmap["a"]}}}r'):
        rPr = r.find(f'{{{nsmap["a"]}}}rPr')
        if rPr is None:
            rPr = etree.SubElement(r, f'{{{nsmap["a"]}}}rPr')
            # Move rPr to be first child
            r.remove(rPr)
            r.insert(0, rPr)
        lang = rPr.find(f'{{{nsmap["a"]}}}lang')
        if lang is None:
            lang = etree.SubElement(rPr, f'{{{nsmap["a"]}}}lang')
        lang.set('val', 'es-CL')

    # Handle a:p (paragraphs) default run properties
    for p in el.iter(f'{{{nsmap["a"]}}}p'):
        pPr = p.find(f'{{{nsmap["a"]}}}pPr')
        if pPr is None:
            pPr = etree.SubElement(p, f'{{{nsmap["a"]}}}pPr')
            p.remove(pPr)
            p.insert(0, pPr)
        defRPr = pPr.find(f'{{{nsmap["a"]}}}defRPr')
        if defRPr is None:
            defRPr = etree.SubElement(pPr, f'{{{nsmap["a"]}}}defRPr')
        lang = defRPr.find(f'{{{nsmap["a"]}}}lang')
        if lang is None:
            lang = etree.SubElement(defRPr, f'{{{nsmap["a"]}}}lang')
        lang.set('val', 'es-CL')

for slide in prs.slides:
    set_lang_on_element(slide._element)

prs.save(pptx_path)
print('PPTX: OK')
