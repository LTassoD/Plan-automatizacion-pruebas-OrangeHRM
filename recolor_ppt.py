"""Recolor PPT using safe python-pptx API calls."""
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
from pptx.oxml.ns import qn
from lxml import etree
import os

# Palette
C_DARK    = "111827"
C_CONTENT = "1E3A5F"
C_ACCENT  = "818CF8"
C_WHITE   = "FFFFFF"
C_BODY    = "CBD5E1"
TBL_HDR_BG  = "1E293B"
TBL_HDR_TXT = "FFFFFF"
TBL_ROW1_BG = "2D3748"
TBL_ROW2_BG = "1E293B"
TBL_BODY_TXT = "E2E8F0"

path = r'C:\Users\User\Desktop\Duoc\Semestre V\Automatizacion de Pruebas\AutomatizacionPruebasPython\PRESENTACION_FINAL_EFT.pptx'
prs = Presentation(path)

def set_bg_safe(slide, hex_color):
    """Set slide background color using XML manipulation."""
    cSld = slide.background._element
    bg = cSld.find(qn('p:bg'))
    if bg is None:
        bg = etree.SubElement(cSld, qn('p:bg'))
    bgPr = bg.find(qn('p:bgPr'))
    if bgPr is None:
        bgPr = etree.SubElement(bg, qn('p:bgPr'))
    # Remove existing fills
    for elem in list(bgPr):
        bgPr.remove(elem)
    # Add solidFill in correct schema order
    sf = etree.SubElement(bgPr, qn('a:solidFill'))
    clr = etree.SubElement(sf, qn('a:srgbClr'))
    clr.set('val', hex_color)
    # Add effectLst after solidFill (schema order: solidFill, effectLst)
    etree.SubElement(bgPr, qn('a:effectLst'))

def set_rect_color(shape, hex_color):
    """Set rectangle fill color safely."""
    spPr = shape._element.find(qn('p:spPr'))
    if spPr is None:
        return
    for elem in list(spPr):
        spPr.remove(elem)
    sf = etree.SubElement(spPr, qn('a:solidFill'))
    clr = etree.SubElement(sf, qn('a:srgbClr'))
    clr.set('val', hex_color)
    etree.SubElement(spPr, qn('a:effectLst'))

def set_run_color(run, hex_color):
    """Set run font color via high-level API."""
    run.font.color.rgb = RGBColor.from_string(hex_color)

def recolor_table(table):
    for row_idx, row in enumerate(table.rows):
        is_header = row_idx == 0
        bg = TBL_HDR_BG if is_header else (TBL_ROW1_BG if row_idx % 2 == 1 else TBL_ROW2_BG)
        txt = TBL_HDR_TXT if is_header else TBL_BODY_TXT
        for cell in row.cells:
            # Cell background via XML
            tcPr = cell._tc.find(qn('a:tcPr'))
            if tcPr is None:
                tcPr = etree.SubElement(cell._tc, qn('a:tcPr'))
            for elem in list(tcPr):
                tcPr.remove(elem)
            sf = etree.SubElement(tcPr, qn('a:solidFill'))
            clr = etree.SubElement(sf, qn('a:srgbClr'))
            clr.set('val', bg)
            # Text color via API
            for para in cell.text_frame.paragraphs:
                for run in para.runs:
                    run.font.color.rgb = RGBColor.from_string(txt)

for idx, slide in enumerate(prs.slides):
    is_cover = idx == 0 or idx == len(prs.slides) - 1
    set_bg_safe(slide, C_DARK if is_cover else C_CONTENT)

    for shape in slide.shapes:
        if shape.name == 'Rectangle 1':
            set_rect_color(shape, C_ACCENT)
        elif shape.shape_type == 19:
            recolor_table(shape.table)
        elif shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    if is_cover:
                        set_run_color(run, C_WHITE)
                        if 'API0101' in run.text or 'OrangeHRM' in run.text:
                            set_run_color(run, 'A5B4FC')
                    else:
                        # Title or body?
                        is_title = run.font.size and run.font.size >= Pt(24)
                        set_run_color(run, C_WHITE if is_title else C_BODY)

prs.save(path)
print("OK")
