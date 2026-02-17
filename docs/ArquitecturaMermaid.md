# Diagramas de arquitectura (Mermaid)

> Borrador de diagramas para documentar el modelo arquitectónico de referencia
> propuesto en la tesis. Incluye:
> - Diagrama de arquitectura de alto nivel.
> - Flujo conversacional del agente.
> - Modelo de datos mínimo.

## 1. Arquitectura de alto nivel

```mermaid
flowchart LR
  U[Usuarios<br/>Estudiantes / Docentes / Admin] --> CH[Canal conversacional<br/>Web / Chat / Helpdesk]

  CH --> GW[Gateway / Webhook receptor]

  subgraph Orquestacion
    ORCH[Orquestador de workflows<br/>Plataforma low-code]
    AG[Runtime de agente LLM<br/>Planificación + herramientas]
    ORCH -->|invoca / coordina| AG
  end

  GW --> ORCH

  subgraph Conocimiento
    SRC[Documentos institucionales<br/>Reglamentos, FAQs, horarios] --> ING[Ingesta / Normalización]
    ING --> OBJ[Almacenamiento de objetos<br/>Documentos en bruto]
    ING --> META[(BD relacional / metadatos)]
    ING --> EMB[Embeddings]
    EMB --> VEC[(Vector DB<br/>Índice semántico)]
  end

  AG -->|consultas semánticas| VEC
  AG -->|consulta metadatos| META
  AG -->|recupera documento| OBJ

  subgraph Integracion
    MQ[(Broker de mensajería / eventos)]
    ORCH <--> MQ
    AG <--> MQ
  end

  subgraph Observabilidad
    OTEL[Telemetría / Trazas / Logs] --> GRAF[Dashboards y alertas]
    ORCH --> OTEL
    AG --> OTEL
    MQ --> OTEL
    GW --> OTEL
  end

  AG --> CH
```

## 2. Flujo conversacional del agente orquestado

```mermaid
flowchart TD
  A[Mensaje del usuario] --> B[Clasificar intención y dominio]

  B -->|Fuera de dominio / alto riesgo| Z[Respuesta segura
("no sé" + canal oficial)]

  B -->|Intención soportada| C[Construir plan de acción
(RAG + tools)]

  C --> D[Recuperación: consulta a Vector DB]
  D --> E[Filtrar y seleccionar evidencia
(según contexto y políticas)]

  E --> F{¿Se requieren herramientas externas?}
  F -->|Sí| G[Llamadas a herramientas
(APIs, bases de datos, servicios internos)]
  F -->|No| H[Saltar a composición de respuesta]

  G --> H[Componer respuesta con
resultados de tools + evidencia]

  H --> I[Registrar ejecución
(run, tool calls, costos, métricas)]
  I --> J[Enviar respuesta al usuario]

  J --> K[Monitoreo / alertas
(revisiones humanas si hay fallos)]
```

## 3. Modelo de datos mínimo (conceptual)

```mermaid
erDiagram
  USER ||--o{ CONVERSATION : inicia
  CONVERSATION ||--o{ MESSAGE : contiene
  CONVERSATION ||--o{ AGENT_RUN : dispara
  AGENT_RUN ||--o{ TOOL_CALL : ejecuta

  DOCUMENT ||--o{ CHUNK : se_divide_en
  CHUNK ||--|| EMBEDDING : tiene

  TOOL_CALL ||--o{ ARTIFACT : produce
  AGENT_RUN ||--o{ OBS_EVENT : genera

  USER {
    string user_id
    string rol
  }

  CONVERSATION {
    string conversation_id
    datetime started_at
    string canal
  }

  MESSAGE {
    string message_id
    string remitente
    string contenido
    datetime ts
  }

  AGENT_RUN {
    string run_id
    string estrategia
    string estado
    datetime started_at
    datetime ended_at
    float costo_estimado
  }

  TOOL_CALL {
    string call_id
    string tool_name
    string input_hash
    string resultado
    int latency_ms
  }

  DOCUMENT {
    string doc_id
    string fuente
    string version
    datetime updated_at
  }

  CHUNK {
    string chunk_id
    string doc_id
    int ordinal
    string text_hash
  }

  EMBEDDING {
    string embedding_id
    string chunk_id
    int dim
    string modelo
  }

  ARTIFACT {
    string artifact_id
    string tipo
    string uri
  }

  OBS_EVENT {
    string event_id
    string trace_id
    string nivel
    string mensaje
  }
```

## 4. Notas de uso en la tesis

- Estos diagramas sirven como base para:
  - El capítulo de **modelo arquitectónico de referencia**.
  - La documentación del flujo conversacional del agente.
  - La discusión sobre observabilidad y evaluación de agentes.
- En el texto LaTeX, se podrán exportar estos diagramas a imágenes o utilizar
  una herramienta que genere SVG/PNG a partir de Mermaid.
