## Entrada 003 — feature/arquitectura-mermaid

- Rama: `feature/arquitectura-mermaid`
- Cambios principales:
  - Creado `docs/ArquitecturaMermaid.md` con:
    - Diagrama Mermaid de arquitectura de alto nivel para agentes
      orquestados.
    - Diagrama Mermaid de flujo conversacional del agente.
    - Diagrama Mermaid de modelo de datos mínimo (entidades y relaciones
      principales) para trazabilidad y evaluación.
- Qué falta relacionado con este bloque:
  - Ajustar nombres de componentes/servicios concretos según el stack final
    utilizado en el caso de estudio.
  - Alinear los diagramas con los diagramas formales que se incluyan en LaTeX
    (por ejemplo, versiones en TikZ o imágenes exportadas).

## Entrada 004 — feature/arquitectura-mermaid

- Fecha: 2026-02-17
- Rama: `feature/arquitectura-mermaid`
- Cambios realizados en esta sesión:
  - Actualizados los diagramas en `docs/ArquitecturaMermaid.md` para:
    - Incorporar ejemplos concretos de tecnologías candidatas para cada
      bloque (orquestador, runtime de agente, almacenamiento de objetos,
      base de datos relacional, motor de embeddings, vector DB, broker de
      mensajería y stack de observabilidad).
    - Aclarar en el flujo conversacional el paso de composición de
      respuesta cuando no se requieren herramientas externas.
    - Añadir una nota de uso que documenta que las tecnologías citadas son
      orientativas para el caso de estudio y no prescriptivas.
- Próximos pasos sugeridos:
  - Alinear la nomenclatura de los bloques de arquitectura con los
    componentes que se describan en el capítulo de modelo arquitectónico
    en LaTeX (Kap4/Kap5 según organización final).
  - Exportar estos diagramas a SVG/PNG y preparar su inclusión en la
    plantilla LaTeX correspondiente.
