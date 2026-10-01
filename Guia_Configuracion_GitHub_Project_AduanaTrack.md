# 🚀 GUÍA DE CONFIGURACIÓN PASO A PASO DESDE ZERO: REPOSITORIO Y GITHUB PROJECT (ADUANATRACK)

**Curso**: Diseño e Implementation de Sistemas (USMP)  
**Docente Asignado**: Mg. Juan Manuel Huapalla García  
**Grupo**: 2  

---

## 📸 ESTRUCTURA EXACTA DEL TABLERO SEGUIMIENTO (GITHUB PROJECTS V2)

Siguiendo el estándar de la captura provista, tu tablero en **GitHub Projects** estará organizado en **5 columnas de flujo** con el formato exacto de tarjetas (`ÉPICA X`, `HUxx_...`, `HTxx_...`):

```
┌────────────────────────────────┐   ┌───────────────────────────────┐   ┌───────────────────────────────┐   ┌─────────────────────────────┐   ┌─────────────────────────┐
│ Backlog                        │ → │ Ready                         │ → │ In progress  (WIP: 0/3)       │ → │ In review  (WIP: 0/5)       │ → │ Done                    │
│ "This item hasn't been started"│   │ "This is ready to be picked" │   │ "This is actively being worked│   │ "This item is in review"    │   │ "This has been completed│
└────────────────────────────────┘   └───────────────────────────────┘   └───────────────────────────────┘   └─────────────────────────────┘   └─────────────────────────┘
```

---

## 🛠️ PASO 1: CREAR E INICIALIZAR EL REPOSITORIO LOCAL Y GITFLOW (DESDE CERO)

Abre tu consola de comandos en la carpeta `c:\dis` y ejecuta:

```bash
# 1. Inicializar repositorio Git
git init

# 2. Crear y cambiar a la rama principal 'main'
git checkout -b main

# 3. Crear el archivo .gitignore
echo -e "node_modules/\n.env\ndist/\nbuild/\n*.log\n.ds_store" > .gitignore

# 4. Agregar los archivos y hacer el commit inicial
git add .
git commit -m "chore: initial commit - ADUANATRACK setup de arquitectura y documentos"

# 5. Crear la rama de integración 'develop' (GitFlow)
git checkout -b develop
```

---

## 🌐 PASO 2: CREAR EL REPOSITORIO REMOTO Y VINCULAR EN GITHUB

1. Entra a [GitHub.com](https://github.com/) e inicia sesión.
2. Haz clic en **New Repository** (Nuevo Repositorio).
3. Nombre del repositorio: **`ADUANATRACK`** (o `aduanatrack-usmp-grupo2`).
4. **Desmarca** todas las casillas de inicialización (README, gitignore, licencia).
5. Haz clic en **Create repository**.
6. Copia y ejecuta en tu consola (reemplazando `TU_USUARIO`):

```bash
git remote add origin https://github.com/TU_USUARIO/ADUANATRACK.git

# Subir rama main y develop
git checkout main
git push -u origin main

git checkout develop
git push -u origin develop
```

7. **Invitaciones Obligatorias del Syllabus del Profesor**:
   - En GitHub, ve a **Settings** -> **Collaborators** -> **Add people**.
   - Invita a: **`jhuapalla@usmp.pe`** (Código) y asegúrate de tener registrado a **`jhuapallag@usmp.pe`** (Kanban).
8. **Branch Protection**: Ve a **Settings** -> **Branches** -> **Add branch protection rule** para `develop`:
   - ✅ **Require a pull request before merging** (1 apruebo obligatorio).
   - ✅ **Require status checks to pass before merging** (CI GitHub Actions).

---

## 📊 PASO 3: CREAR EL GITHUB PROJECT V2 Y SUS 5 COLUMNAS

1. En GitHub (tu usuario u organización), ve a la pestaña **Projects** -> **New project**.
2. Elige la plantilla **Board** (Tablero) y presiona **Create**.
3. Cambia el nombre a: **`ADUANATRACK — Sprint Planning & Kanban (Grupo 2)`**.
4. Edita el campo **Status** para configurar exactamente las **5 columnas de la captura**:

| Nombre de Columna | Subtítulo / Descripción | Límite WIP (Opcional) |
| :--- | :--- | :---: |
| **`Backlog`** | *This item hasn't been started* | — |
| **`Ready`** | *This is ready to be picked up* | — |
| **`In progress`** | *This is actively being worked on* | `0/3` (Máx 3 en paralelo) |
| **`In review`** | *This item is in review* | `0/5` (Máx 5 en revisión) |
| **`Done`** | *This has been completed* | — |

---

## 🏷️ PASO 4: AGREGAR LOS CAMPOS Y INSIGNIAS EN LAS TARJETAS (BADGES)

En las configuraciones del proyecto (**Settings** -> **Fields** -> **New field**), crea los campos que aparecen en la captura:

1. **`Prioridad`** (Tipo: *Single select*) -> Opciones: `ALTA` (Color Rojo/Naranja), `MEDIA` (Color Amarillo), `BAJA` (Color Gris).
2. **`Story Points`** (Tipo: *Number*) -> Números de la serie Fibonacci (`3`, `5`, `8`).
3. **`Sprint`** (Tipo: *Iteration* o *Single Select*) -> `Sprint 1`, `Sprint 2`, `Sprint 3`.
4. **`Épica`** (Tipo: *Single Select*) -> `EP00: Infra`, `EP01: Auth`, `EP02: Clientes`, `EP03: Despacho`, `EP04: Embarque BL`, `EP05: Dashboard`.

---

## 🤖 PASO 5: CARGA AUTOMÁTICA DE TODAS LAS ISSUES (1 CLIC)

Para no digitar manualmente las 11 Épicas, 15 HUs y 31 Tareas Técnicas:

1. Genera un **Personal Access Token (PAT)** en GitHub: *Settings -> Developer Settings -> Personal Access Tokens (Classic)* con permisos `repo` y `project`.
2. En tu terminal ejecuta:
   ```bash
   python c:\dis\setup_github_repo_and_project.py
   ```
3. Ingresa tu Token, Usuario y Repositorio. El script creará automáticamente todas las Épicas (`ÉPICA X: ...`), HUs (`HUxx_...`) y Tareas Técnicas (`HTxx_...`) con sus descripciones BDD y asignaciones.

---

## 👥 MATRIZ COMPLETA DE ASIGNACIONES (FORMATO CAPTURA)

| Título de la Tarjeta (Format Exacto) | Tipo | SP | Prioridad | Asignado |
| :--- | :---: | :---: | :---: | :--- |
| **`ÉPICA 0: Construir Plataforma Base y Entornos DevSecOps`** | Épica | — | ALTA | Fabio Saavedra |
| **`ÉPICA 1: Autenticación, Seguridad y Control de Acceso`** | Épica | — | ALTA | Patrick Ponce |
| **`ÉPICA 2: Gestión del Directorio de Clientes Importadores`** | Épica | — | ALTA | Patrick Ponce |
| **`ÉPICA 3: Apertura y Control del Despacho Aduanero`** | Épica | — | ALTA | Patrick Ponce |
| **`ÉPICA 4: Trazabilidad de Transporte Marítimo y Contenedores`** | Épica | — | ALTA | Patrick Ponce |
| **`ÉPICA 5: Monitoreo Operativo y Tablero de Control`** | Épica | — | MEDIA | Kiara Linares |
| **`HU01_Iniciar sesión en el sistema`** | HU | 3 SP | ALTA | Patrick Ponce / Kiara Linares |
| **`HU04_Registrar datos del cliente importador`** | HU | 5 SP | ALTA | Patrick Ponce / Kiara Linares |
| **`HU03_Registrar nuevo despacho de importación`** | HU | 5 SP | ALTA | Patrick Ponce / Kiara Linares |
| **`HU05_Registrar información del embarque marítimo (BL)`** | HU | 5 SP | ALTA | Patrick Ponce / Kiara Linares / Fabio Saavedra |
| **`HU02_Visualizar panel de seguimiento de despachos (Dashboard)`** | HU | 5 SP | MEDIA | Kiara Linares / Fabio Saavedra |
| **`HT01_Configurar repositorio Git bajo GitFlow y reglas branch protection`** | Tarea | — | ALTA | Fabio Saavedra |
| **`HT02_Parametrizar tablero Kanban en Jira/Trello con flujo aduanero`** | Tarea | — | ALTA | Alvaro Tipian (SM) |
| **`HT03_Construir arquitectura contenerizada docker-compose multi-servicio`** | Tarea | — | ALTA | Patrick Ponce |
| **`HT04_Diseñar e implementar scripts DDL en PostgreSQL con auditoría`** | Tarea | — | ALTA | Fabio Saavedra |
| **`HT05_Construir pipeline CI en GitHub Actions para compilación y linter`** | Tarea | — | ALTA | Patrick Ponce |
| **`HT06_Configurar escaneo estático de seguridad SAST con SonarQube/Snyk`** | Tarea | — | ALTA | Fabio Saavedra |
| **`HT07_Desarrollar endpoint POST /api/v1/auth/login con bcrypt y JWT`** | Tarea | — | ALTA | Patrick Ponce |
| **`HT08_Implementar middleware e inserción en tabla audit_auth_logs`** | Tarea | — | ALTA | Fabio Saavedra |
| **`HT09_Maquetar vista SPA reactiva de login con validación regex`** | Tarea | — | ALTA | Kiara Linares |
| **`HT10_Ejecutar suite de pruebas unitarias automatizadas BDD de HU01`** | Tarea | — | ALTA | Fabio Saavedra |
| **`HT11_Modelar entidad Cliente y API REST con validación RUC módulo 11`** | Tarea | — | ALTA | Patrick Ponce |
| **`HT12_Implementar servicio multipart para carga de carta poder PDF`** | Tarea | — | ALTA | Fabio Saavedra |
| **`HT13_Configurar auditoría histórica JSON en audit_importadores`** | Tarea | — | ALTA | Patrick Ponce |
| **`HT14_Construir componente frontend para alta/edición de importadores`** | Tarea | — | ALTA | Kiara Linares |
| **`HT15_Diseñar y ejecutar pruebas funcionales y de límites de HU04`** | Tarea | — | ALTA | Kiara Linares |
| **`HT16_Implementar generador atómico transaccional de correlativo DESP`** | Tarea | — | ALTA | Patrick Ponce |
| **`HT17_Crear tablas maestras e endpoints de regímenes y aduana 118`** | Tarea | — | ALTA | Fabio Saavedra |
| **`HT18_Desarrollar middleware de verificación de carta poder vigente`** | Tarea | — | ALTA | Patrick Ponce |
| **`HT19_Construir Stepper Wizard frontend para creación de despacho`** | Tarea | — | ALTA | Kiara Linares |
| **`HT20_Implementar badge visual de estado operativo e hito Apertura`** | Tarea | — | ALTA | Kiara Linares |
| **`HT21_Ejecutar pruebas automatizadas de integración para HU03`** | Tarea | — | ALTA | Fabio Saavedra |
| **`HT22_Desarrollar endpoint GET /api/v1/dashboard/kpis optimizado`** | Tarea | — | MEDIA | Fabio Saavedra |
| **`HT23_Implementar filtros dinámicos y exportador a Excel (.xlsx)`** | Tarea | — | MEDIA | Patrick Ponce |
| **`HT24_Maquetar vista de Dashboard con tarjetas KPI y grilla por ETA`** | Tarea | — | MEDIA | Kiara Linares |
| **`HT25_Configurar enrutamiento SPA contextual hacia detalle de despacho`** | Tarea | — | MEDIA | Kiara Linares |
| **`HT26_Ejecutar pruebas de rendimiento y volumetría en Dashboard`** | Tarea | — | MEDIA | Fabio Saavedra |
| **`HT27_Modelar entidades DDL embarques_maritimos y detalle_contenedores`** | Tarea | — | ALTA | Patrick Ponce |
| **`HT28_Implementar algoritmo de validación de contenedores ISO 6346`** | Tarea | — | ALTA | Fabio Saavedra |
| **`HT29_Desarrollar servicio de recálculo automático de almacenaje`** | Tarea | — | ALTA | Patrick Ponce |
| **`HT30_Construir UI para datos marítimos y sub-tabla de contenedores`** | Tarea | — | ALTA | Kiara Linares |
| **`HT31_Ejecutar suite de pruebas funcionales para embarque BL en HU05`** | Tarea | — | ALTA | Fabio Saavedra |
