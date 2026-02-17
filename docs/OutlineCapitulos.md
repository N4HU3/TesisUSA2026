# Outline de capítulos de la tesis

> Versión inicial basada en la plantilla LaTeX (Kap1–Kap6) y el anteproyecto
> de tesis. Este outline está pensado para mapear directamente a los archivos
> `Kap*/Kap*.tex` y servir de guía para la escritura en Markdown/LaTeX.

## Capítulo 1 — Introducción (Kap1)

- Contexto y motivación
  - Transformación digital y agentes de IA en organizaciones.
  - Problema de fondo: decisiones arquitectónicas ad-hoc vs evaluación por
    atributos de calidad.
- Planteamiento del problema
  - Brecha entre herramientas low-code y arquitecturas basadas en código.
  - Complejidad añadida por agentes LLM (memoria, planificación, tools, RAG).
- Objetivos
  - Objetivo general.
  - Objetivos específicos.
- Preguntas de investigación y alcance
  - RQ1–RQ6 (referencia a `docs/PreguntasInvestigacion.md`).
  - Alcances y limitaciones del estudio de caso.
- Justificación e impacto esperado
  - Relevancia académica (arquitectura, agentes, low-code).
  - Relevancia práctica (organizaciones con asistentes institucionales).
- Estructura del documento
  - Breve descripción de cada capítulo (1–6).

## Capítulo 2 — Marco teórico y estado del arte (Kap2)

- Arquitectura de software y calidad
  - Atributos de calidad (ISO/IEC 25010).
  - Evaluación basada en escenarios: QAW, SAAM, ATAM, ARID.
  - Decisiones arquitectónicas y ADRs; noción de utility tree.
- Sistemas de agentes y agentes basados en LLM
  - Definiciones clásicas de agente y sistemas multiagente.
  - Agentes LLM con planificación, memoria y uso de herramientas.
  - Patrones ReAct, Toolformer, MRKL, RAG.
- Orquestación de workflows y BPM
  - BPMN, patrones de workflow, máquinas de estado y DAGs.
  - Orquestación vs coreografía en microservicios.
- Low-code / no-code y gobernanza
  - Definición y características de low-code/no-code.
  - Ventajas (velocidad, accesibilidad) y riesgos (deuda técnica, lock-in).
  - Gobernanza y citizen development.
- Síntesis crítica y vacíos
  - Falta de integración entre arquitectura, low-code y LLM agents.
  - Necesidad de un modelo arquitectónico de referencia y un marco de decisión
    comparativo low-code vs código.

## Capítulo 3 — Metodología y diseño de estudio de caso (Kap3)

- Enfoque metodológico
  - Estudio de caso (Yin) y generalización analítica.
  - Rol del caso institucional (asistente escolar/institucional).
- Unidades de análisis
  - Caso A (baseline): arquitectura previa o enfoque código.
  - Caso B (propuesta): arquitectura de agentes orquestados.
- Técnicas de recolección de datos
  - Análisis documental.
  - Entrevistas/encuestas a stakeholders.
  - Modelado arquitectónico y ADRs.
  - Pruebas/simulaciones de rendimiento.
- Evaluación por escenarios
  - QAW para elicitar escenarios de calidad.
  - Selección y priorización de escenarios (utility tree).
  - Aplicación de ATAM a las alternativas arquitectónicas.
- Métricas y variables
  - Tiempo, costo, throughput, latencia, errores.
  - Mantenibilidad, observabilidad, seguridad, testabilidad.
  - Costos por tokens/llamadas en agentes LLM.

## Capítulo 4 — Modelo arquitectónico de referencia (Kap4)

- Requisitos funcionales y de calidad del asistente
  - Casos de uso principales (consultas, trámites, soporte).
  - Requisitos de trazabilidad, auditoría y observabilidad.
- Arquitectura propuesta
  - Componentes principales (canales, orquestador, agente LLM, RAG, broker,
    bases de datos, almacenamiento de objetos, observabilidad).
  - Diagrama de arquitectura de alto nivel (referencia a Mermaid en `docs`).
- Modelo de datos mínimo
  - Entidades clave (conversaciones, ejecuciones de agentes, tool calls,
    documentos, embeddings, eventos de observabilidad).
- Arquitectura del agente y flujo conversacional
  - Pipeline: clasificación de intención, RAG, tools, composición de respuesta.
  - Estrategias de fallback y manejo fuera de dominio.
- Decisiones arquitectónicas clave
  - Uso de orquestador low-code vs código.
  - Introducción de mensajería/eventos.
  - Selección de tecnologías concretas (si aplica).

## Capítulo 5 — Marco de decisión low-code vs código y resultados (Kap5)

- Marco de decisión propuesto
  - Criterios y dimensiones (tiempo, costo, throughput, latencia,
    modificabilidad, observabilidad, seguridad, gobernanza, lock-in).
  - Matriz de decisión con pesos y umbrales heurísticos.
  - Diagrama de flujo de decisión (Mermaid) para guiar la selección.
- Aplicación al caso de estudio
  - Evaluación de la arquitectura propuesta vs alternativa basada en código.
  - Resultados de experimentos/pruebas (tiempos, costos, rendimiento,
    mantenibilidad percibida, etc.).
- Análisis y discusión
  - Interpretación de los resultados a la luz de las RQs.
  - Trade-offs identificados y sensibilidad a los parámetros.

## Capítulo 6 — Conclusiones y recomendaciones (Kap6)

- Resumen de hallazgos
  - Respuestas a RQ1–RQ6.
- Conclusiones principales
  - Sobre la efectividad y eficiencia de agentes orquestados.
  - Sobre el papel del low-code vs código en este contexto.
- Recomendaciones prácticas
  - Para organizaciones que quieran implementar agentes orquestados.
  - Para el uso responsable de low-code en contextos críticos.
- Trabajo futuro
  - Extensiones del modelo arquitectónico.
  - Evaluaciones adicionales (otros dominios, más métricas, otros stacks).

## Anexos

- Detalles de configuración técnica (si aplica).
- Instrumentos de recolección (guías de entrevista, encuestas).
- Escenarios completos (utility tree y escenarios de calidad).
- Scripts de pruebas de carga y notebooks de análisis.
