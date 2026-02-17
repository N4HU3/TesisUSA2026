# Preguntas de investigación y hipótesis

> Borrador inicial para revisión con el director. Se basa en el anteproyecto sobre
> un modelo arquitectónico de referencia para agentes de IA orquestados y un
> marco de decisión low-code vs código.

## Preguntas de investigación (RQ)

**RQ1 – Efectividad arquitectónica**  
¿Bajo qué condiciones (tipo de proceso, criticidad, variabilidad de tareas y
requisitos de auditoría) una arquitectura de agentes de IA orquestados logra
igual o mejor desempeño funcional (exactitud, trazabilidad, completitud de
 tareas) que una arquitectura basada únicamente en código/microservicios?

**RQ2 – Eficiencia y costo de cambio**  
¿Cómo varían el tiempo de implementación y el costo de cambio (esfuerzo por
nueva funcionalidad o modificación relevante) entre un enfoque low-code de
orquestación y un enfoque basado en código al construir y evolucionar agentes
con herramientas (RAG/APIs)?

**RQ3 – Calidad no funcional (modificabilidad, observabilidad, seguridad)**  
¿Qué trade-offs aparecen en modificabilidad, observabilidad y seguridad al
implementar agentes orquestados con plataformas low-code versus
arquitecturas basadas en código, evaluados mediante escenarios tipo ATAM/QAW?

**RQ4 – Operación y rendimiento**  
¿Qué diferencias se observan en throughput, latencia y tolerancia a fallos al
introducir mensajería/eventos y desacoplamiento (event-driven) frente a un
control más síncrono, y cómo impactan estas decisiones la arquitectura de los
agentes y su operación en producción?

**RQ5 – Gobernanza y escalabilidad organizacional**  
¿Qué mecanismos de gobernanza (roles, políticas, control de acceso, ciclo de
vida de flujos y agentes, auditoría) son necesarios para que un enfoque
low-code escale organizacionalmente sin incrementar el riesgo ni la deuda
técnica?

**RQ6 – Transferibilidad del modelo**  
¿Qué partes del modelo arquitectónico y del marco de decisión propuestos son
generalizables a otros sistemas de agentes institucionales, y cuáles dependen
fuertemente del contexto del caso de estudio?

## Hipótesis de trabajo (borrador)

Las hipótesis no se plantean en sentido estrictamente estadístico, sino como
supuestos razonados que la tesis buscará respaldar o matizar con evidencia.

**H1 – Productividad en escenarios de carga moderada**  
Para agentes institucionales con carga moderada y alta variabilidad funcional,
un enfoque de orquestación low-code reduce el tiempo de implementación inicial
y el costo de cambio a corto plazo frente a un enfoque basado solo en código,
sin degradar significativamente el desempeño funcional.

**H2 – Calidad no funcional y umbrales de complejidad**  
A partir de cierto umbral de carga, criticidad operativa y complejidad de
integración, las limitaciones de extensibilidad, observabilidad fina y control
de seguridad en plataformas low-code hacen preferible introducir componentes
basados en código/microservicios para el "runtime crítico", manteniendo el
low-code como plano de orquestación.

**H3 – Gobernanza como condición de éxito del low-code**  
Sin políticas explícitas de gobernanza (roles, control de versiones,
revisión/despliegue, gestión de riesgos), la adopción de orquestación
low-code para agentes tiende a generar deuda técnica y fragmentación
arquitectónica mayores que un enfoque predominantemente basado en código.

**H4 – Utilidad del modelo arquitectónico de referencia**  
Un modelo arquitectónico que integre orquestación, agentes LLM con RAG y
herramientas, mensajería y observabilidad, más una matriz de decisión basada
en atributos de calidad, facilita la toma de decisiones justificadas (al
estilo ATAM) frente a decisiones ad-hoc basadas únicamente en preferencia de
herramientas.
