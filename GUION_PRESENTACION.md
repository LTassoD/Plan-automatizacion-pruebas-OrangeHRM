# Guion de Presentación — Evaluación Parcial 3  
**Duración:** ~3 minutos | **Estudiante:** Luis Tasso | **Sección:** 802V

---

### Slide 1 — Portada (10s)
> "Buenos días profesor Manuel Soto. Soy Luis Tasso de la sección 802V y voy a presentar los resultados de la evaluación parcial 3 de Automatización de Pruebas."

### Slide 2 — Agenda (10s)
> "La presentación cubre: trazabilidad de requisitos a resultados, las métricas de calidad, oportunidades de mejora identificadas, y propuestas tanto para el producto OrangeHRM como para nuestro framework de automatización."

### Slide 3 — Trazabilidad (25s)
> "Acá está la trazabilidad completa. Cada requerimiento —desde login válido hasta licencias— está mapeado a su funcionalidad, su escenario Gherkin, y su resultado. 10 de 11 requisitos pasaron. El único FAIL es el TC_004, que es intencional por diseño del curso: el assert espera 'OrangeHRM OS 5.7' pero el título real es solo 'OrangeHRM'. Esto está documentado y es parte de la evaluación."

### Slide 4 — Resultados de Ejecución (30s)
> "Ejecutamos 29 escenarios con 96.55% de aprobación. El único fallo es el TC_004 intencional — su propósito es demostrar que el hook @after_scenario captura automáticamente un screenshot cuando un escenario falla. La evidencia quedó registrada. En cuanto a cobertura por módulo: Login 3 de 4, Navegación y Sesión perfectos, PIM CRUD 12 de 12, Perfil y Licencias también perfectos. Los 18 escenarios Data-Driven pasaron todos."

### Slide 5 — Métricas de Calidad (25s)
> "Las 5 métricas del PPT 3.3.1: 100% automatizable, 100% de progreso, productividad de diseño de 7.25 escenarios por hora, y tasa de fallos de 3.45% que corresponde únicamente al TC_004 intencional. Cada métrica tiene su fuente verificable: el reporte.html y el reporte.json. Si excluimos el fallo intencional, la tasa de aprobación es 100%."

### Slide 6 — Oportunidades de Mejora (30s)
> "Identificamos 5 oportunidades. Primero, el menú en chino: los escenarios de navegación fallaban porque el servidor cambió el locale. La solución fue implementar MENU_TRANSLATIONS con fallback bilingüe. Segundo, el botón Save interceptado por el spinner de OX: agregamos _wait_spinner_done y click por JavaScript. Tercero, el tiempo de ejecución de 7 minutos: proponemos ejecución paralela con behave -j 4 para bajar a ~2 minutos. Cuarto, el título incorrecto del TC_004: la solución fue validar por URL en vez de título. Y quinto, los datos Excel no versionados: proponemos git y pre-commit hook."

### Slide 7 — Propuestas de Mejora (30s)
> "Acá están las 6 propuestas formales. Del lado producto: mensajes de error diferenciados porque hoy OrangeHRM muestra el mismo texto para usuario inexistente y contraseña incorrecta. Y un selector de idioma persistente para evitar el problema del locale. Del lado proceso: Page Object Model para centralizar selectores, ejecución paralela para reducir tiempo, logging estructurado para diagnóstico, y GitHub Actions para CI/CD. Cada propuesta nace de un dato real del reporte, tiene una acción concreta y un impacto cuantificable en el ciclo de vida."

### Slide 8 — Lecciones Aprendidas (15s)
> "Las principales lecciones: los localizadores robustos son clave, el Data-Driven testing permite escalar sin escribir más código, los screenshots automáticos dan trazabilidad total, y la internacionalización es un desafío real. Personalmente, aprendí que un fallo bien documentado vale más que 10 pasos sin explicación."

### Slide 9 — Conclusiones (15s)
> "En resumen: 29 de 29 escenarios ejecutados, suite robusta que soporta inglés y chino, Data-Driven funcional, 133 evidencias, y métricas trazables. La automatización está lista para integrarse en un pipeline CI/CD."

### Slide 10 — Gracias (10s)
> "Muchas gracias. Quedo atento a sus preguntas."
