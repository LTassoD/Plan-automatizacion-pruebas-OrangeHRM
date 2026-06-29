import json
from datetime import datetime

# Carga el archivo reporte.json generado por behave (--format json)
# o por generar_json_completo.py si no se ejecutaron los tests.
with open("reporte.json", encoding="utf-8") as f:
    data = json.load(f)
    # TODO: si el json esta vacio, revisar la ejecucion de behave

# Plantilla HTML del reporte
html = """<html><head><meta charset="UTF-8">
<title>Reporte de Pruebas - OrangeHRM</title>
<style>
body{font-family:Arial,sans-serif;margin:40px;background:#f5f5f5}
h1{color:#2c3e50;border-bottom:3px solid #4CAF50;padding-bottom:10px}
h2{color:#34495e;margin-top:30px}
table{border-collapse:collapse;width:100%;margin-bottom:20px;background:#fff;box-shadow:0 2px 4px rgba(0,0,0,0.1)}
th,td{border:1px solid #ddd;padding:12px;text-align:left}
th{background:#4CAF50;color:white;font-weight:bold}
tr:nth-child(even){background:#f9f9f9}
.passed{color:#4CAF50;font-weight:bold}
.failed{color:#f44336;font-weight:bold}
.resumen{background:#fff;padding:20px;border-radius:5px;box-shadow:0 2px 4px rgba(0,0,0,0.1)}
.resumen span{font-size:18px;margin-right:20px}
.verde{color:#4CAF50;font-weight:bold}
.rojo{color:#f44336;font-weight:bold}
.footer{color:#999;margin-top:30px;font-size:12px}
</style></head><body>
<h1>Reporte de Automatizacion - OrangeHRM</h1>
<p><strong>Herramienta:</strong> Behave + Selenium WebDriver</p>
<p><strong>Sitio:</strong> opensource-demo.orangehrmlive.com</p>
<p><strong>Fecha de ejecucion:</strong> """ + datetime.now().strftime("%Y-%m-%d %H:%M") + """</p>
"""

# Itera sobre features y escenarios para construir las tablas
total = passed = failed = 0
for feature in data:
    html += f'<h2>{feature["name"]}</h2>'
    html += '<table><tr><th>N°</th><th>Escenario</th><th>Estado</th><th>Duracion (s)</th></tr>'
    n = 0
    for scenario in feature["elements"]:
        if scenario["type"] == "scenario":
            n += 1
            total += 1
            dur = 0
            status = "passed"
            for step in scenario["steps"]:
                dur += step.get("result", {}).get("duration", 0) or 0
                if step["result"]["status"] == "failed":
                    status = "failed"
            if status == "passed":
                passed += 1
            else:
                failed += 1
            cls = "passed" if status == "passed" else "failed"
            lbl = "PASO" if status == "passed" else "FALLO"
            html += f'<tr><td>{n}</td><td>{scenario["name"]}</td><td class="{cls}">{lbl}</td><td>{round(dur, 2)}</td></tr>'
    html += "</table>"

html += f"""
<div class="resumen">
<h3>Resumen Final</h3>
<p><span class="verde">&#10003; Aprobados: {passed}</span>
<span class="rojo">&#10007; Fallidos: {failed}</span>
<span><strong>Total:</strong> {total} escenarios</span></p>
</div>
<div class="footer">
<p>Generado automaticamente por Behave + Selenium | Evaluacion Parcial 2 - Automatizacion de Pruebas</p>
</div>
</body></html>
"""

with open("reporte.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Reporte generado: reporte.html")
