# 🎙️ GUION OFICIAL PARA GRABACIÓN DE DAILY SCRUMS EN TEAMS (DURACIÓN: 15 MINUTOS)
## Proyecto: Sistema de Seguimiento Aduanero de Importaciones Marítimas (ADUANATRACK)
**Curso**: Diseño e Implementación de Sistemas (USMP)  
**Docente Asignado**: Mg. Juan Manuel Huapalla García  
**Grupo**: 2  

---

## 👥 REPARTO Y ROLES DEL SCRUM TEAM
1. **Alvaro Tipian** → **Scrum Master / Facilitador** *(Apertura formal de 15 min, comparte pantalla con Kanban en Jira, modera turnos, revisa Burndown y realiza síntesis de cierre)*.
2. **Juan Diego Altamirano** → **Product Owner** *(Valida reglas de negocio SUNAT, vigencia de RUC/carta poder, criterios Gherkin BDD y cumplimiento de Definition of Done)*.
3. **Kiara Linares** → **Developer (Frontend)** *(Reporta avances de la interfaz SPA reactiva, formularios de importadores con dropzone PDF, Stepper de despacho y Dashboard)*.
4. **Patrick Ponce** → **Developer (Backend)** *(Reporta avances de APIs REST, autenticación JWT/bcrypt, DDL PostgreSQL, generador de correlativo DESP y embarque BL)*.
5. **Fabio Saavedra** → **Developer (Backend / DevOps / QA)** *(Reporta avances de Docker Compose, repositorio GitFlow en GitHub, CI/CD Actions, SonarQube SAST y norma ISO 6346)*.

---

## 💡 CONSEJOS PRÁCTICOS PARA LA GRABACIÓN EN TEAMS
- **Iniciador de la llamada**: Alvaro (Scrum Master) crea la llamada en Teams y activa la grabación (**"Iniciar grabación"**).
- **Pantalla Compartida**: Alvaro o Kiara comparten pantalla mostrando el **Tablero Kanban en Jira/Trello** (con las columnas `Product Backlog`, `To Do`, `In Development`, `Peer Review`, `QA Testing`, `SAST Scan`, `Done`) o la ventana de **GitHub / VS Code / Postman**.
- **Ritmo de conversación**: Hablen con naturalidad, pausadamente y de forma conversacional (como desarrolladores reales en una sesión diaria de 15 minutos).
- **Duración estricta**: **15:00 minutos por Daily Scrum** (cumpliendo la regla ágil de Timebox).

---

# 📌 GUION 1: DAILY SCRUM #1 — SEMANA 7 (15 MINUTOS TOTALES)
### *Enfoque: Setup de Arquitectura, Autenticación (HU-01) y Registro de Importadores (HU-04)*

---

### **[00:00 - 02:30] APERTURA Y REVISIÓN DE JIRA**
> **[Alvaro - Scrum Master]**  
> *"Hola equipo, buenos días a todos. Damos inicio a la sesión de Daily Scrum correspondiente al hito de la Semana 7 de nuestro proyecto ADUANATRACK.*  
>  
> *Como saben, la metodología Scrum establece que la Daily es una reunión de sincronización de máximo 15 minutos para inspeccionar el avance hacia el Sprint Goal, revisar qué hizo cada uno, qué hará hoy y resolver impedimentos.*  
>  
> *Voy a proceder a compartir mi pantalla en Teams con el tablero Kanban de Jira. Como pueden observar en la grilla, tenemos parametrizados los 7 estados del workflow aduanero: Product Backlog, To Do, In Development, Peer Review, QA Testing, SAST Security Scan y Done. Además, ya están aplicados los límites WIP para garantizar un máximo de 2 tareas en progreso por desarrollador y hemos enviado las invitaciones institucionales al docente Mg. Juan Manuel Huapalla García con los correos jhuapallag@usmp.pe en Jira y jhuapalla@usmp.pe en GitHub.*  
>  
> *En esta Semana 7 tenemos en ejecución las dos primeras Historias de Usuario: la HU-01 de Autenticación con 3 Story Points y la HU-04 de Registro de Clientes Importadores con 5 Story Points. Para mantener el orden de la ronda, le doy la palabra a Fabio en la parte de DevOps, infraestructura y pruebas. Fabio, ¿qué tal?, te escuchamos."*

---

### **[02:30 - 05:45] INTERVENCIÓN 1: FABIO SAAVEDRA (DevOps / QA)**
> **[Fabio - DevOps / QA]**  
> *"Gracias Alvaro, hola con todos. Les detallo el reporte de mi frente de trabajo:*  
>  
> 1. **¿Qué hice desde la última sesión?**  
>    Dejé inicializado el repositorio oficial en GitHub aplicando la arquitectura GitFlow estricta. He creado las ramas `main` para releases estables, `develop` para la integración continua y las ramas por característica `feature/HU-01-login` y `feature/HU-04-importadores`. Configuré las reglas de branch protection en `develop` para exigir obligatoriamente 1 peer review aprobado y el pase de status checks en el CI antes de permitir cualquier merge. Además, dejé configurado el archivo `docker-compose.yml` multi-servicio levantando la API y el contenedor de PostgreSQL 15 Alpine con volúmenes persistentes y los scripts DDL iniciales para esquemas, tipos ENUM aduaneros y tablas de auditoría como `audit_auth_logs` y `audit_importadores`.  
>  
> 2. **¿Qué voy a hacer hoy?**  
>    Hoy me voy a enfocar en escribir el pipeline de integración continua en GitHub Actions (`.github/workflows/ci.yml`). Este pipeline ejecutará jobs automatizados para checkout del código, instalación limpia con `npm ci`, validación de sintaxis con ESLint y la ejecución automatizada de la suite de pruebas unitarias en Jest. Adicionalmente, voy a dejar parametrizada la herramienta de escaneo estático de seguridad SAST con SonarQube Cloud y Snyk para asegurar un Quality Gate de cero vulnerabilidades críticas.  
>  
> 3. **¿Tengo algún impedimento o bloqueo?**  
>    No tengo bloqueos en este momento. Sin embargo, temprano coordiné con Patrick para homologar los nombres de las variables de entorno en el archivo `.env.example` (como `DB_HOST`, `DB_PORT`, `JWT_SECRET`) para que la pila contenerizada en Docker levante exactamente igual en todos los entornos de desarrollo locales."*

---

### **[05:45 - 06:15] REACCIÓN DEL SCRUM MASTER**
> **[Alvaro - Scrum Master]**  
> *"Excelente trabajo Fabio. La arquitectura en Docker y la protección de ramas en GitFlow garantizan que no metamos código roto a develop. Es muy importante que mantengamos esa disciplina de PR con revisión de código. Patrick, cuéntanos cómo vas con el desarrollo del backend y la lógica de autenticación."*

---

### **[06:15 - 09:30] INTERVENCIÓN 2: PATRICK PONCE (Backend Developer)**
> **[Patrick - Backend]**  
> *"Gracias Alvaro. Les comparto el avance detallado del backend:*  
>  
> 1. **¿Qué hice?**  
>    Para la **HU-01** (Iniciar sesión en el sistema), desarrollé el controlador y servicio del endpoint `POST /api/v1/auth/login`. Implementé la encriptación y verificación de contraseñas mediante hashing `bcrypt` con salt factor 10 y la generación de tokens de autenticación `JWT` firmados bajo la clave secreta con expiración de 2 horas. También programé el middleware que registra cada intento de acceso en la tabla `audit_auth_logs` capturando la IP de origen, el User-Agent y el timestamp UTC. Para la **HU-04** (Registrar cliente importador), programé la función utilitaria en el servidor para la validación algorítmica de RUC peruano de 11 dígitos utilizando el cálculo del módulo 11.  
>  
> 2. **¿Qué voy a hacer hoy?**  
>    Hoy voy a construir el controlador `multipart/form-data` para la carga y almacenamiento del archivo PDF de la carta poder del importador con un límite estricto de 10 MB. Validaré la firma mágica del archivo para evitar la subida de ejecutables maliciosos y programaré la lógica de auditoría en la tabla `audit_importadores` para guardar el historial JSON de modificaciones de razón social y dirección fiscal. También implementaré el middleware de seguridad que bloquea temporalmente la cuenta por 15 minutos tras 3 intentos fallidos consecutivos.  
>  
> 3. **¿Tengo algún impedimento?**  
>    Impedimentos de código ninguno. Ayer estuve haciendo pruebas con Postman en el endpoint del login y el tiempo de respuesta del servidor se mantiene en promedio por debajo de los 85 milisegundos, cumpliendo holgadamente el criterio de rendimiento."*

---

### **[09:30 - 10:00] REACCIÓN SM & FEEDBACK FRONTEND**
> **[Alvaro - Scrum Master]**  
> *"Buenísimo Patrick, viene muy bien optimizada la API de autenticación y la validación de RUC de 11 dígitos. Kiara, coméntanos sobre la maquetación y la integración de estas pantallas en el frontend."*

---

### **[10:00 - 13:00] INTERVENCIÓN 3: KIARA LINARES (Frontend Developer)**
> **[Kiara - Frontend]**  
> *"Hola chicos, buenos días con todos. Les cuento el avance del frontend:*  
>  
> 1. **¿Qué hice?**  
>    Maqueté la interfaz reactiva SPA para el inicio de sesión de la **HU-01**, implementando validaciones en tiempo real en los campos de entrada mediante expresiones regulares (para validar la sintaxis del correo corporativo y la presencia de caracteres en la contraseña). Configuré el estado global de autenticación en React mediante React Context para almacenar el token JWT devuelto por el backend y la bandera 'Recordarme' que extiende la sesión activa.  
>  
> 2. **¿Qué voy a hacer hoy?**  
>    Hoy voy a avanzar la interfaz del directorio de clientes importadores correspondiente a la **HU-04**. Construiré el formulario modal para el registro de RUC, razón social y contactos comerciales con validación asíncrona contra la API para evitar RUCs duplicados en pantalla. También maquetaré el componente dropzone para adjuntar la carta poder en PDF con previsualización dentro del navegador antes del envío.  
>  
> 3. **¿Tengo algún impedimento?**  
>    Ayer tuve un pequeño bloqueador con una restricción de política CORS en el navegador al momento de consumir la API que corría en el contenedor Docker local. Sin embargo, me puse en contacto con Fabio y Patrick por Slack, ajustamos la configuración de cabeceras `Access-Control-Allow-Origin` en el backend y el problema quedó resuelto satisfactoriamente."*

---

### **[13:00 - 14:15] VALIDACIÓN DEL PRODUCT OWNER & REGLAS DE NEGOCIO**
> **[Juan Diego - Product Owner]**  
> *"Excelente trabajo equipo. Como Product Owner he estado revisando el comportamiento en los entornos locales y veo que todo se alinea a las historias del Product Backlog.*  
>  
> *Solo quiero hacer un hincapié importante en las reglas de negocio aduaneras para la HU-04: recuerden que la carta poder del importador es un documento legal indispensable para que la agencia de aduana pueda gestionar el despacho. Por ello, necesitamos que si la fecha de caducidad calculada para la carta poder está a menos de 15 días de vencer, el sistema coloque un indicador visual de alerta de color amarillo en el padrón de clientes.*  
>  
> *Asimismo, verifiquen que los 4 criterios de aceptación formulados en formato Gherkin (Dado-Cuando-Entonces) para el login y el registro de importadores sean pasados al 100% por la suite de QA antes de dar por terminadas estas dos historias."*

---

### **[14:15 - 15:00] CIERRE Y SÍNTESIS DEL SCRUM MASTER**
> **[Alvaro - Scrum Master]**  
> *"Anotado perfectamente Juan Diego. Patrick y Kiara tomarán esa regla de la alerta preventiva a 15 días como parte de los criterios de aceptación para el cierre de la HU-04.*  
>  
> *Haciendo una síntesis de nuestra Daily Scrum #1: el equipo se encuentra trabajando a excelente ritmo, la base de DevOps y base de datos está completa, el backend del login y la validación RUC están terminados, y el frontend reactivo está en fase de integración. Estamos dentro del pronóstico del Burndown Chart para cerrar los 8 Story Points de la Semana 7 sin desviaciones.*  
>  
> *Recuerden que este video de la llamada en Teams debe ser guardado en la carpeta compartida para la evidencia del entregable semanal. Damos por concluida la Daily de hoy. ¡Muchas gracias a todos y a seguir trabajando!"*

---
---

# 📌 GUION 2: DAILY SCRUM #2 — SEMANA 9 (15 MINUTOS TOTALES)
### *Enfoque: Apertura de Despacho (HU-03), Embarque BL (HU-05) y Dashboard de Seguimiento (HU-02)*

---

### **[00:00 - 02:30] APERTURA Y REVISIÓN DE VELOCIDAD**
> **[Alvaro - Scrum Master]**  
> *"Buenos días equipo, bienvenidos a la Daily Scrum #2 correspondiente al hito de la Semana 9. Les comparto pantalla con nuestro tablero de Jira y la gráfica del Burndown Chart.*  
>  
> *Como pueden verificar en el estado del tablero, las dos Historias de Usuario iniciales (HU-01 de Autenticación y HU-04 de Registro de Importadores) ya fueron validadas satisfactoriamente por el Product Owner y pasaron formalmente a la columna 'Done', sumando los primeros 8 Story Points de nuestro sprint.*  
>  
> *En esta Semana 9 nos encontramos en la recta final para consolidar el incremento funcional del Sprint 1, completando el núcleo operativo compuesto por la HU-03 (Apertura de Despacho), la HU-05 (Registrar embarque marítimo - BL) y la HU-02 (Dashboard de seguimiento con ordenamiento por ETA). Las 3 historias suman 15 Story Points para alcanzar nuestra meta comprometida de 23 Story Points.*  
>  
> *Vamos a revisar el estado técnico de cada frente para asegurar que lleguemos al Sprint Review con cero deuda técnica. Le cedo el turno a Patrick en la parte de lógica transaccional del backend."*

---

### **[02:30 - 05:45] INTERVENCIÓN 1: PATRICK PONCE (Backend Developer)**
> **[Patrick - Backend]**  
> *"Hola Alvaro, hola chicos. Les presento el reporte del desarrollo backend:*  
>  
> 1. **¿Qué hice desde la última sesión?**  
>    Dejé completamente terminado e integrado el generador atómico transaccional para la **HU-03**. Este componente se encarga de crear el código correlativo de despacho en formato `DESP-2026-XXXX` utilizando secuencias nativas en PostgreSQL dentro de una transacción con nivel de aislamiento READ COMMITTED, lo cual garantiza que no se produzcan números duplicados ni saltos en la numeración ante solicitudes concurrentes. Asimismo, diseñé las entidades relacionales `embarques_maritimos` y `detalle_contenedores` con sus respectivas claves foráneas vinculadas a la ficha del despacho para dar soporte a la **HU-05**.  
>  
> 2. **¿Qué voy a hacer hoy?**  
>    Hoy voy a implementar el servicio que realiza el cálculo automático de los plazos de almacenaje gratuito en el depósito temporal (fijado en 30 días a partir de la fecha estimada de arribo ETA). Si el agente aduanero actualiza la fecha ETA de la nave en el embarque, el backend recalculará en tiempo real la fecha límite de permanencia y disparará un flag de alerta si la fecha actual sobrepasa el periodo de gracia. También terminaré el endpoint `GET /api/v1/dashboard/kpis` optimizando las consultas agregadas en SQL.  
>  
> 3. **¿Tengo algún impedimento?**  
>    No tengo impedimentos. Los endpoints están probados con datos volumétricos sintéticos y el tiempo de ejecución de las consultas se mantiene por debajo de los 45 milisegundos gracias a la indexación B-Tree en las tablas."*

---

### **[05:45 - 06:15] REACCIÓN DEL SCRUM MASTER**
> **[Alvaro - Scrum Master]**  
> *"Excelente trabajo en la concurrencia del correlativo DESP, Patrick. Garantizar la atomicidad sin duplicados era una exigencia clave de negocio. Kiara, cuéntanos cómo va la integración del Stepper y el Dashboard en la parte visual."*

---

### **[06:15 - 09:30] INTERVENCIÓN 2: KIARA LINARES (Frontend Developer)**
> **[Kiara - Frontend]**  
> *"Gracias Alvaro, hola a todos. Por el lado del cliente web les comento:*  
>  
> 1. **¿Qué hice?**  
>    Desarrollé el formulario guiado paso a paso (Stepper Wizard) para la apertura del despacho en la **HU-03**. En el paso 1 el agente aduanero busca y selecciona al cliente importador (el sistema valida en segundo plano que posea carta poder vigente), en el paso 2 se elige el régimen aduanero 10 (Importación Definitiva) y la intendencia de la aduana marítima del Callao 118, y al confirmar, se renderiza la ficha del despacho mostrando el código correlativo `DESP-2026-XXXX` con el badge de estado 'Apertura'.  
>  
> 2. **¿Qué voy a hacer hoy?**  
>    Hoy voy a maquetar y conectar el Dashboard operativo de la **HU-02**. Integraré la grilla de tarjetas KPI métricas en la cabecera (despachos activos, despachos en canal naranja/rojo y despachos con levante) y construiré la tabla dinámica paginada de 'Despachos Recientes', la cual vendrá ordenada por omisión según la fecha estimada de arribo (ETA) más próxima. También agregaré la sub-tabla reactiva para la **HU-05** donde el usuario puede registrar múltiples contenedores (20' Standard, 40' High Cube, Reefer) con sus respectivos números de precinto.  
>  
> 3. **¿Tengo algún impedimento?**  
>    No tengo bloqueos técnicos. La integración con la API REST de Patrick se realizó correctamente utilizando Axios y los interceptores de sesión conservan los parámetros de paginación y búsqueda en la URL."*

---

### **[09:30 - 10:00] REACCIÓN SM & QA**
> **[Alvaro - Scrum Master]**  
> *"Estupendo Kiara, la interfaz se ve súper fluida y el Stepper ayuda mucho a reducir los errores de digitación del usuario. Fabio, coméntanos sobre los escaneos de seguridad, las normas internacionales y las suites de QA."*

---

### **[10:00 - 13:00] INTERVENCIÓN 3: FABIO SAAVEDRA (DevOps / QA)**
> **[Fabio - DevOps / QA]**  
> *"Hola chicos, buenos días. Les comparto el estado del frente de calidad e infraestructura:*  
>  
> 1. **¿Qué hice?**  
>    Programé el módulo de validación técnica bajo la norma internacional **ISO 6346** para la verificación de los códigos de contenedores marítimos en la **HU-05**. La función analiza el código de propietario de 3 letras, la clave de categoría 'U', el número de serie de 6 dígitos y calcula el dígito verificador matemático mediante suma ponderada para evitar errores de tipeo. Adicionalmente, ejecuté el escaneo estático SAST con SonarQube Cloud y Snyk CLI sobre el branch `develop`, logrando un Quality Gate aprobado con cero vulnerabilidades críticas o bloqueantes.  
>  
> 2. **¿Qué voy a hacer hoy?**  
>    Hoy me dedicaré a actualizar la suite de integración en GitHub Actions para ejecutar pruebas automáticas de consistencia de fechas (verificando que la fecha de zarpe en origen sea estrictamente anterior al ETA en el Callao) y realizaré pruebas de carga y estrés con k6 sobre el endpoint del Dashboard para certificar que el tiempo de renderizado y respuesta de la API sea inferior a 500 ms con una carga simulada de 1,000 despachos.  
>  
> 3. **¿Tengo algún impedimento?**  
>    Ningún impedimento. El entorno de integración continua responde perfecto y la cobertura de pruebas unitarias consolidadas en el backend está en 79.5%, superando la métrica mínima exigida en nuestra Definition of Done (75%)."*

---

### **[13:00 - 14:15] VALIDACIÓN DEL PRODUCT OWNER & REVISIÓN DE INCREMENTO**
> **[Juan Diego Altamirano - Product Owner]**  
> *"Excelente trabajo equipo, muy conforme con la solución técnica presentada.*  
>  
> *Como Product Owner valido que el incremento funcional acumulado cumple estrictamente con el objetivo de nuestro Sprint Goal: tenemos acceso seguro con JWT (HU-01), directorio de clientes con validación RUC de 11 dígitos y carta poder PDF (HU-04), apertura de despacho con correlativo atómico DESP (HU-03), trazabilidad de embarque con validación ISO 6346 de contenedores (HU-05) y visión centralizada en el Dashboard (HU-02).*  
>  
> *Todas las historias cumplen con el formato de Tarjeta 3C, el modelo INVEST y la Definition of Done. Estamos totalmente listos para realizar la demostración del software en el Sprint Review ante el profesor Juan Manuel Huapalla García y presentar nuestros entregables en Excel y Word."*

---

### **[14:15 - 15:00] CIERRE Y SÍNTESIS DEL SCRUM MASTER**
> **[Alvaro Tipian - Scrum Master]**  
> *"Muchas gracias Juan Diego. Efectivamente, inspeccionando nuestro Burndown Chart, la curva real de horas restantes coincide exactamente con la línea ideal a 0 horas, habiendo ejecutado las 109 horas de esfuerzo estimadas en las 31 tareas SMART del Sprint Backlog para los 23 Story Points.*  
>  
> *Les recuerdo a todos que tras finalizar esta videollamada de Teams debemos guardar la grabación en la carpeta del grupo para adjuntarla en la entrega de la Semana 9. En breve procederemos con las ceremonias de Sprint Review y Retrospectiva.*  
>  
> *Felicito a todo el equipo por el profesionalismo mostrado. Damos por concluida la Daily Scrum #2. ¡Muchas gracias y excelente día para todos!"*
