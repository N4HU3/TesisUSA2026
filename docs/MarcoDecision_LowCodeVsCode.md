# Marco de decisión: Low-code vs Código

> Borrador inicial del marco de decisión para seleccionar entre una
> implementación de agentes orquestados basada en low-code o en código.
> Incluye criterios, matriz con pesos y umbrales heurísticos, y un diagrama
> de flujo de decisión.

## 1. Dimensiones y criterios

Dimensiones principales para comparar enfoques:

- **Tiempo y costo**
  - Tiempo de implementación inicial.
  - Costo de cambio (esfuerzo por nueva funcionalidad o modificación).
- **Rendimiento y operación**
  - Throughput (solicitudes/segundo) y concurrencia.
  - Latencia end-to-end (p50/p95/p99).
  - Tolerancia a fallos (reintentos, degradación controlada).
- **Calidad no funcional**
  - Modificabilidad y extensibilidad.
  - Observabilidad (logs, métricas, trazas, correlación).
  - Seguridad (authN/authZ, control de datos, superficie de ataque).
- **Gobernanza y organización**
  - Roles y ciclos de vida (quién diseña, quién aprueba, quién opera).
  - Riesgo de sprawl y deuda técnica.
- **Lock-in y portabilidad**
  - Dependencia de plataforma específica.
  - Facilidad de migración a otras herramientas o a código.

## 2. Matriz de decisión (pesos y umbrales heurísticos)

> Los pesos son heurísticos y deben ajustarse al contexto de la organización.
> Aquí se propone un ejemplo razonable para un asistente institucional
> crítico pero no de misión ultra-crítica (ej. educativo).

### 2.1 Pesos por dimensión (ejemplo)

| Dimensión                  | Peso (%) |
|---------------------------|---------:|
| Tiempo y costo            |      25% |
| Rendimiento y operación   |      25% |
| Calidad no funcional      |      25% |
| Gobernanza y organización |      15% |
| Lock-in y portabilidad    |      10% |

La suma de pesos es 100%. Se puede recalibrar según prioridades del contexto.

### 2.2 Escala de puntuación

Para cada criterio se evalúan ambos enfoques (low-code, código) en una escala
por ejemplo de 1 a 5:

- 1 = Muy desfavorable
- 2 = Desfavorable
- 3 = Neutro / aceptable
- 4 = Favorable
- 5 = Muy favorable

Se puede multiplicar cada puntuación por el peso de la dimensión para obtener
una puntuación ponderada.

### 2.3 Umbrales heurísticos clave

- **Throughput pico**
  - `< 5–20 rps` sostenidos: low-code **viable**, sujeto a pruebas de carga.
  - `> 20–50 rps` con SLAs estrictos: considerar código/microservicios para el
    runtime crítico, manteniendo low-code como plano de orquestación.
- **Latencia end-to-end (p95)**
  - `> 1–2 s` aceptables: low-code suele ser suficiente si se controla el
    número de hops y llamadas.
  - `< 500 ms` estricto: probable necesidad de componentes en código
    optimizado y control más directo de colas, cachés y conexiones.
- **Complejidad de integración**
  - Pocas integraciones estándar (APIs HTTP, bases de datos comunes):
    low-code tiende a ser favorable.
  - Muchas integraciones custom, librerías internas o lógica compleja:
    el código ofrece más control y mantenibilidad a largo plazo.
- **Gobernanza disponible**
  - Si existe un equipo con prácticas claras de revisión, versionado y
    despliegue, low-code puede escalar sin descontrol.
  - Si no hay gobernanza, el riesgo de sprawl y deuda técnica en low-code
    aumenta significativamente.
- **Riesgo de lock-in**
  - Si la plataforma low-code es central y difícil de reemplazar, se recomienda
    aislar integraciones en servicios intermedios y documentar procesos en
    estándares (BPMN, ADRs).

## 3. Tabla comparativa resumida (ejemplo)

> Ejemplo cualitativo para un asistente institucional de carga moderada.

| Dimensión                  | Criterio                  | Low-code (L)             | Código (C)                   |
|---------------------------|---------------------------|--------------------------|------------------------------|
| Tiempo y costo            | Time-to-market inicial    | L: 4–5 (rápido)          | C: 2–3 (más lento)           |
|                           | Costo de cambio simple    | L: 4 (cambios pequeños)  | C: 3–4 (según calidad código)|
| Rendimiento y operación   | Throughput moderado       | L: 3–4                   | C: 4–5                       |
|                           | Latencia estricta (<500ms)| L: 2                     | C: 4–5                       |
|                           | Resiliencia y fallos      | L: 3 (dependiente plataforma) | C: 3–4 (diseño explícito) |
| Calidad no funcional      | Modificabilidad           | L: 3–4 (hasta cierto tamaño) | C: 3–4 (depende arquitectura) |
|                           | Observabilidad            | L: 2–3                   | C: 3–4                       |
|                           | Seguridad                 | L: 3 (features de la plataforma) | C: 3–4 (control fino)  |
| Gobernanza y organización | Control de cambios        | L: 2–3 sin gobernanza    | C: 3–4 con prácticas DevOps  |
|                           | Acceso y roles            | L: 3–4                   | C: 3–4                       |
| Lock-in y portabilidad    | Dependencia de proveedor  | L: 2–3 (alto riesgo)     | C: 3–4                       |

## 4. Reglas de decisión (borrador)

1. **Si** el sistema requiere latencias muy bajas (p95 < 500 ms) **y** se
   espera un throughput > 20–50 rps, **entonces** privilegiar una arquitectura
   basada en código/microservicios para el runtime crítico.
2. **Si** el sistema tiene carga moderada, cambios frecuentes de lógica y
   necesidad de iterar rápido con stakeholders, **entonces** considerar
   orquestación low-code como plano principal, con componentes de código
   complementarios cuando sea necesario.
3. **Si** la organización no cuenta con mecanismos claros de gobernanza
   (revisión, versionado, despliegue), **entonces** limitar el uso de
   low-code a casos no críticos o invertir primero en gobernanza.
4. **Si** el riesgo de lock-in es alto y la arquitectura debe ser portable,
   **entonces** modelar procesos en BPMN/ADRs y aislar dependencias en
   servicios intermedios en código.

## 5. Diagrama Mermaid de flujo de decisión

```mermaid
flowchart TD
  A[Inicio: definir caso de uso del agente] --> B[Evaluar criticidad y SLAs]

  B -->|Alta criticidad o SLAs estrictos<br/>p95 < 500 ms o > 20-50 rps| C[Priorizar código/microservicios
para runtime crítico]
  B -->|Criticidad moderada<br/>SLAs flexibles| D[Evaluar velocidad de entrega y
frecuencia de cambio]

  C --> E[¿Se requiere orquestación de muchos pasos y tareas humanas?]
  E -->|Sí| F[Usar low-code como plano de orquestación
+ servicios en código para tareas críticas]
  E -->|No| G[Arquitectura basada en código
con componentes bien delimitados]

  D --> H[¿Cambios frecuentes en flujos y lógica?]
  H -->|Sí| I[Preferir orquestación low-code
para flujos + componentes en código
cuando sea necesario]
  H -->|No| J[Evaluar costo/beneficio de low-code
vs simplicidad de una solución en código]

  I --> K[Revisar gobernanza y lock-in]
  F --> K

  K --> L{¿Gobernanza y control de cambios adecuados?}
  L -->|Sí| M[Adoptar low-code como componente central
con políticas claras de roles, versionado y despliegue]
  L -->|No| N[Restringir uso de low-code a casos no críticos
 o invertir primero en gobernanza]

  M --> O[Documentar decisiones y umbrales
(matriz de decisión + ADRs)]
  N --> O

  G --> O
  J --> O
```

## 6. Uso del marco en la tesis

- Este marco servirá para:
  - Estructurar la comparación entre la arquitectura propuesta de agentes
    orquestados y alternativas basadas en código.
  - Justificar decisiones arquitectónicas en función de atributos de calidad,
    evitando argumentos puramente basados en preferencia de herramientas.
  - Proveer una guía reutilizable para otros contextos institucionales que
    evalúen low-code vs código para agentes de IA orquestados.
