#!/usr/bin/env python3
"""Auto-genera el índice (TOC) del INFORME_FINAL_EFT.md a partir de sus encabezados."""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "INFORME_FINAL_EFT.md")

with open(PATH, "r", encoding="utf-8") as f:
    md = f.read()

# Extraer encabezados ## y ### (excluir título, índice y TOC markers)
headers = []
for line in md.splitlines():
    m = re.match(r'^(#{2,3})\s+(.+)$', line)
    if not m:
        continue
    level = len(m.group(1))
    title = m.group(2).strip()
    title_clean = re.sub(r'\*.*?\*', '', title).strip()
    # Saltar portada e índice
    if title_clean in ('ÍNDICE', 'API0101 — Automatización de Pruebas', 'INFORME FINAL — EVALUACIÓN FINAL TRANSVERSAL'):
        continue
    if title_clean.startswith('Evidencia de ejecución'):
        continue
    headers.append((level, title, title_clean))

# Generar anchor del estilo GitHub
def slugify(text):
    s = text.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s

toc_lines = []
roman = ['I.', 'II.', 'III.']
roman_idx = 0
for level, title, clean in headers:
    anchor = slugify(clean)
    indent = '    ' if level == 3 else ''
    if level == 2:
        # Sección principal I, II, III
        prefix = f'{roman[roman_idx]} ' if roman_idx < len(roman) else ''
        toc_lines.append(f'{indent}{prefix}[{clean}](#{anchor})')
        roman_idx += 1
    else:
        # Subsección ###
        # Extraer número si existe
        num_match = re.match(r'^(\d+\.?\d*)\s+(.+)$', clean)
        if num_match:
            display = f'{num_match.group(1)} {num_match.group(2)}'
        else:
            display = clean
        toc_lines.append(f'{indent}- [{display}](#{anchor})')

# Reemplazar entre marcadores TOC_START y TOC_END
toc_text = '\n'.join(toc_lines)
md = re.sub(
    r'<!-- TOC_START -->.*?<!-- TOC_END -->',
    f'<!-- TOC_START -->\n{toc_text}\n<!-- TOC_END -->',
    md,
    flags=re.DOTALL
)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(md)

print("TOC actualizado correctamente.")
