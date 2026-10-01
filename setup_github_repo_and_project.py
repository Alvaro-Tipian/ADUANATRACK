# -*- coding: utf-8 -*-
"""
Script de Automatización para GitHub REST API
Proyecto: ADUANATRACK (Grupo 2 - USMP)
Crea automáticamente etiquetas, milestones e Issues con el formato exacto de la captura:
- ÉPICA X: Nombre
- HUxx_Nombre
- HTxx_Nombre
- Badges de Prioridad (ALTA, MEDIA) y Sprints.
"""

import os
import json
import urllib.request
import urllib.error

def make_gh_request(url, token, data=None, method="GET"):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", "AduanaTrack-GitHub-Setup")
    
    if data:
        json_data = json.dumps(data).encode("utf-8")
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, data=json_data) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            print(f"  ❌ Error HTTP {e.code}: {err_body}")
            return None
    else:
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            print(f"  ❌ Error HTTP {e.code}")
            return None

def setup_github_automation():
    print("=" * 75)
    print("🚀 AUTOMATIZACIÓN DE GITHUB (FORMATO EXACTO SEGÚN CAPTURA PROVISTA)")
    print("=" * 75)
    
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        token = input("🔑 Ingresa tu Personal Access Token (PAT) de GitHub: ").strip()
        if not token:
            print("❌ El Token es obligatorio. Saliendo del asistente.")
            return

    owner = input("👤 Ingresa tu usuario u organización de GitHub: ").strip()
    repo = input("📦 Ingresa el nombre del repositorio (ej. ADUANATRACK): ").strip()

    base_url = f"https://api.github.com/repos/{owner}/{repo}"

    # 1. Verificar Conexión
    print("\n🔍 Verificando acceso al repositorio...")
    repo_info = make_gh_request(base_url, token)
    if not repo_info:
        print(f"❌ No se pudo conectar al repositorio {owner}/{repo}. Verifica permisos y Token.")
        return
    print(f"✅ Conexión exitosa a {repo_info['full_name']}!")

    # 2. Crear Labels (Etiquetas)
    print("\n🏷️ Creando etiquetas (Labels) personalizadas...")
    labels = [
        {"name": "Épica", "color": "1E3A8A", "description": "Épica de negocio del sistema"},
        {"name": "Historia de Usuario", "color": "0369A1", "description": "Requerimiento de usuario INVEST"},
        {"name": "Tarea Técnica", "color": "D97706", "description": "Tarea de ingeniería SMART"},
        {"name": "ALTA", "color": "DC2626", "description": "Prioridad Alta (Must Have)"},
        {"name": "MEDIA", "color": "F59E0B", "description": "Prioridad Media (Should Have)"},
        {"name": "BAJA", "color": "64748B", "description": "Prioridad Baja (Could Have)"},
        {"name": "Sprint 1", "color": "059669", "description": "Sprint 1 (Semanas 7-9)"},
        {"name": "Sprint 2", "color": "0284C7", "description": "Sprint 2 (Semanas 10-12)"},
        {"name": "Sprint 3", "color": "7C3AED", "description": "Sprint 3 (Semanas 13-15)"}
    ]
    for lbl in labels:
        res = make_gh_request(f"{base_url}/labels", token, data=lbl, method="POST")
        if res:
            print(f"  • Label '{lbl['name']}' creado/actualizado.")

    # 3. Crear Milestones
    print("\n🎯 Creando Milestones (Sprints)...")
    milestones = [
        {"title": "Sprint 1", "description": "Sprint 1: 5 HUs (23 SP), 31 Tareas SMART (109h). Apertura de Despacho, BL, Importadores, Login y Dashboard.", "state": "open"},
        {"title": "Sprint 2", "description": "Sprint 2: 5 HUs (34 SP). Carga documental, clasificación arancelaria, liquidación tributaria, DAM y canal SUNAT.", "state": "open"},
        {"title": "Sprint 3", "description": "Sprint 3: 5 HUs (28 SP). Citas portuarias, aforo físico, levante, notificaciones y reportes gerenciales.", "state": "open"}
    ]
    milestone_map = {}
    for ms in milestones:
        res = make_gh_request(f"{base_url}/milestones", token, data=ms, method="POST")
        if res:
            milestone_map[ms["title"]] = res["number"]
            print(f"  • Milestone '{ms['title']}' registrado (# {res['number']}).")

    # 4. Crear Issues para Épicas
    print("\n📦 Creando Issues para Épicas (ÉPICA 0 a ÉPICA 5)...")
    epics_data = [
        ("EP00", "ÉPICA 0: Construir Plataforma Base y Entornos DevSecOps", "Configuración de repositorios GitFlow, docker-compose multi-servicio, PostgreSQL 15 DDL, CI GitHub Actions y SAST SonarQube.", "Sprint 1"),
        ("EP01", "ÉPICA 1: Autenticación, Seguridad y Control de Acceso", "Módulo de autenticación segura con JWT, encriptación bcrypt, bitácora de auditoría y bloqueo de fuerza bruta. (HU01 · 3 SP)", "Sprint 1"),
        ("EP02", "ÉPICA 2: Gestión del Directorio de Clientes Importadores", "Padrón maestro de importadores con validación RUC módulo 11, almacenamiento PDF de carta poder y alertas de caducidad. (HU04 · 5 SP)", "Sprint 1"),
        ("EP03", "ÉPICA 3: Apertura y Control del Despacho Aduanero", "Apertura formal de expediente con correlativo atómico DESP-YYYY-XXXX, catálogos SUNAT y estado apertura. (HU03 · 5 SP)", "Sprint 1"),
        ("EP04", "ÉPICA 4: Trazabilidad de Transporte Marítimo y Contenedores", "Registro de conocimiento BL, norma ISO 6346 para contenedores y recálculo automático de almacenaje temporal. (HU05 · 5 SP)", "Sprint 1"),
        ("EP05", "ÉPICA 5: Monitoreo Operativo y Tablero de Control", "Dashboard en tiempo real con tarjetas KPI métricas, tabla dinámica ordenada por ETA y exportador Excel. (HU02 · 5 SP)", "Sprint 1")
    ]
    for eid, title, desc, ms_title in epics_data:
        issue_data = {
            "title": title,
            "body": f"## 📌 {title}\n\n**Descripción de la Épica**:\n{desc}\n\n**Fase**: {ms_title}",
            "labels": ["Épica", "ALTA", ms_title],
            "milestone": milestone_map.get(ms_title)
        }
        res = make_gh_request(f"{base_url}/issues", token, data=issue_data, method="POST")
        if res:
            print(f"  • Issue creado: {title} (# {res['number']})")

    # 5. Crear Issues para HUs del Sprint 1
    print("\n📜 Creando Issues para Historias de Usuario (HU01 a HU05)...")
    hus_data = [
        ("HU01", "HU01_Iniciar sesión en el sistema", 3, "ALTA", "EP01", "Patrick Ponce / Kiara Linares",
         "### 👤 Declaración de la Historia\n**Como** Usuario del sistema (Agente/Admin/Cliente)\n**Quiero** autenticarme con credenciales seguras y protección de intentos\n**Para** acceder a las funcionalidades del sistema según los permisos de mi rol operativo.\n\n### 📋 Criterios de Aceptación Gherkin (BDD)\n1. **Dado** un usuario registrado, **cuando** ingresa credenciales válidas, **entonces** accede con JWT.\n2. **Dado** credenciales erróneas, **cuando** intenta ingresar, **entonces** muestra error 401 sin revelar usuario.\n3. **Dado** 3 fallos consecutivos, **cuando** intenta una 4ta vez, **entonces** bloquea cuenta por 15 min.\n4. **Dado** cada intento, **cuando** se procesa, **entonces** registra trazabilidad en `audit_auth_logs`."),
        
        ("HU04", "HU04_Registrar datos del cliente importador", 5, "ALTA", "EP02", "Patrick Ponce / Kiara Linares",
         "### 👤 Declaración de la Historia\n**Como** Administrador o agente de aduana\n**Quiero** registrar y mantener actualizado el padrón de clientes importadores\n**Para** vincular al importador a sus despachos y controlar las cartas poder vigentes.\n\n### 📋 Criterios de Aceptación Gherkin (BDD)\n1. **Dado** un formulario de cliente, **cuando** ingresa RUC de 11 dígitos (módulo 11), **entonces** persiste datos en BD.\n2. **Dado** un RUC registrado, **cuando** intenta ingresarlo de nuevo, **entonces** emite error 409 Conflict.\n3. **Dado** una carta poder PDF <= 10MB, **cuando** se carga, **entonces** valida firma mágica y guarda con UUID.\n4. **Dado** poder próximo a vencer (<15 días), **cuando** se consulta la grilla, **entonces** muestra alerta amarilla."),
        
        ("HU03", "HU03_Registrar nuevo despacho de importación", 5, "ALTA", "EP03", "Patrick Ponce / Kiara Linares",
         "### 👤 Declaración de la Historia\n**Como** Agente de aduana\n**Quiero** aperturar formalmente el expediente operativo de importación\n**Para** generar el código correlativo atómico e iniciar el trámite aduanero.\n\n### 📋 Criterios de Aceptación Gherkin (BDD)\n1. **Dado** importador con carta poder vigente, **cuando** ingresa datos de régimen 10 y aduana 118, **entonces** genera `DESP-2026-XXXX`.\n2. **Dado** importador con carta poder vencida, **cuando** intenta registrar despacho, **entonces** bloquea con error 422.\n3. **Dado** el Stepper Wizard, **cuando** guarda parcialmente, **entonces** persiste en estado Borrador.\n4. **Dado** expediente aperturado, **cuando** abre ficha, **entonces** muestra hito visual de Apertura."),
        
        ("HU05", "HU05_Registrar información del embarque marítimo (BL)", 5, "ALTA", "EP04", "Patrick Ponce / Kiara Linares / Fabio Saavedra",
         "### 👤 Declaración de la Historia\n**Como** Agente de aduana\n**Quiero** registrar datos del conocimiento de embarque (BL), nave y contenedores\n**Para** controlar la travesía marítima, naviera y fecha límite de almacenaje en depósito.\n\n### 📋 Criterios de Aceptación Gherkin (BDD)\n1. **Dado** código de contenedor, **cuando** se ingresa, **entonces** valida formato e identificador según norma ISO 6346.\n2. **Dado** fechas de zarpe y ETA, **cuando** zarpe >= ETA, **entonces** bloquea por inconsistencia temporal.\n3. **Dado** actualización de ETA, **cuando** cambia fecha, **entonces** recalcula automáticamente los 30 días libres de almacenaje.\n4. **Dado** embarque FCL, **cuando** agrega múltiples contenedores, **entonces** vincula todos los precintos al BL."),
        
        ("HU02", "HU02_Visualizar panel de seguimiento de despachos (Dashboard)", 5, "MEDIA", "EP05", "Kiara Linares / Fabio Saavedra",
         "### 👤 Declaración de la Historia\n**Como** Agente de aduana\n**Quiero** visualizar métricas en tiempo real y el listado de despachos en curso\n**Para** monitorear el avance global de operaciones e identificar alertas oportunamente.\n\n### 📋 Criterios de Aceptación Gherkin (BDD)\n1. **Dado** usuario autenticado, **cuando** carga dashboard, **entonces** muestra métricas de resumen y despachos activos.\n2. **Dado** grilla de despachos, **cuando** renderiza la tabla, **entonces** aparece ordenada por ETA más próximo.\n3. **Dado** filtros por cliente y aduana, **cuando** selecciona valores, **entonces** filtra en tiempo real sin recargar.\n4. **Dado** grilla filtrada, **cuando** presiona Exportar, **entonces** emite reporte en formato Excel (.xlsx).")
    ]

    for hid, title, sp, prio, ep, dev, body in hus_data:
        issue_data = {
            "title": title,
            "body": f"## 📜 {title}\n**Story Points**: {sp} SP  |  **Épica**: {ep}  |  **Asignados**: {dev}\n\n{body}",
            "labels": ["Historia de Usuario", prio, "Sprint 1"],
            "milestone": milestone_map.get("Sprint 1")
        }
        res = make_gh_request(f"{base_url}/issues", token, data=issue_data, method="POST")
        if res:
            print(f"  • Issue creado: {title} (# {res['number']})")

    # 6. Crear Issues para Tareas Técnicas (HT01 a HT31)
    print("\n🛠️ Creando Issues para Tareas Técnicas (HT01 a HT31)...")
    tasks_data = [
        ("HT01", "HT01_Configurar repositorio Git bajo GitFlow y reglas branch protection", "ALTA", "Fabio Saavedra"),
        ("HT02", "HT02_Parametrizar tablero Kanban en Jira/Trello con flujo aduanero", "ALTA", "Alvaro Tipian"),
        ("HT03", "HT03_Construir arquitectura contenerizada docker-compose multi-servicio", "ALTA", "Patrick Ponce"),
        ("HT04", "HT04_Diseñar e implementar scripts DDL en PostgreSQL con auditoría", "ALTA", "Fabio Saavedra"),
        ("HT05", "HT05_Construir pipeline CI en GitHub Actions para compilación y linter", "ALTA", "Patrick Ponce"),
        ("HT06", "HT06_Configurar escaneo estático de seguridad SAST con SonarQube/Snyk", "ALTA", "Fabio Saavedra"),
        ("HT07", "HT07_Desarrollar endpoint POST /api/v1/auth/login con bcrypt y JWT", "ALTA", "Patrick Ponce"),
        ("HT08", "HT08_Implementar middleware e inserción en tabla audit_auth_logs", "ALTA", "Fabio Saavedra"),
        ("HT09", "HT09_Maquetar vista SPA reactiva de login con validación regex", "ALTA", "Kiara Linares"),
        ("HT10", "HT10_Ejecutar suite de pruebas unitarias automatizadas BDD de HU01", "ALTA", "Fabio Saavedra"),
        ("HT11", "HT11_Modelar entidad Cliente y API REST con validación RUC módulo 11", "ALTA", "Patrick Ponce"),
        ("HT12", "HT12_Implementar servicio multipart para carga de carta poder PDF", "ALTA", "Fabio Saavedra"),
        ("HT13", "HT13_Configurar auditoría histórica JSON en audit_importadores", "ALTA", "Patrick Ponce"),
        ("HT14", "HT14_Construir componente frontend para alta/edición de importadores", "ALTA", "Kiara Linares"),
        ("HT15", "HT15_Diseñar y ejecutar pruebas funcionales y de límites de HU04", "ALTA", "Kiara Linares"),
        ("HT16", "HT16_Implementar generador atómico transaccional de correlativo DESP", "ALTA", "Patrick Ponce"),
        ("HT17", "HT17_Crear tablas maestras e endpoints de regímenes y aduana 118", "ALTA", "Fabio Saavedra"),
        ("HT18", "HT18_Desarrollar middleware de verificación de carta poder vigente", "ALTA", "Patrick Ponce"),
        ("HT19", "HT19_Construir Stepper Wizard frontend para creación de despacho", "ALTA", "Kiara Linares"),
        ("HT20", "HT20_Implementar badge visual de estado operativo e hito Apertura", "ALTA", "Kiara Linares"),
        ("HT21", "HT21_Ejecutar pruebas automatizadas de integración para HU03", "ALTA", "Fabio Saavedra"),
        ("HT22", "HT22_Desarrollar endpoint GET /api/v1/dashboard/kpis optimizado", "MEDIA", "Fabio Saavedra"),
        ("HT23", "HT23_Implementar filtros dinámicos y exportador a Excel (.xlsx)", "MEDIA", "Patrick Ponce"),
        ("HT24", "HT24_Maquetar vista de Dashboard con tarjetas KPI y grilla por ETA", "MEDIA", "Kiara Linares"),
        ("HT25", "HT25_Configurar enrutamiento SPA contextual hacia detalle de despacho", "MEDIA", "Kiara Linares"),
        ("HT26", "HT26_Ejecutar pruebas de rendimiento y volumetría en Dashboard", "MEDIA", "Fabio Saavedra"),
        ("HT27", "HT27_Modelar entidades DDL embarques_maritimos y detalle_contenedores", "ALTA", "Patrick Ponce"),
        ("HT28", "HT28_Implementar algoritmo de validación de contenedores ISO 6346", "ALTA", "Fabio Saavedra"),
        ("HT29", "HT29_Desarrollar servicio de recálculo automático de almacenaje", "ALTA", "Patrick Ponce"),
        ("HT30", "HT30_Construir UI para datos marítimos y sub-tabla de contenedores", "ALTA", "Kiara Linares"),
        ("HT31", "HT31_Ejecutar suite de pruebas funcionales para embarque BL en HU05", "ALTA", "Fabio Saavedra")
    ]

    for htid, title, prio, dev in tasks_data:
        issue_data = {
            "title": title,
            "body": f"## 🛠️ {title}\n**Asignado a**: {dev}  |  **Prioridad**: {prio}\n\nTarea de ingeniería SMART correspondiente al plan del Sprint 1.",
            "labels": ["Tarea Técnica", prio, "Sprint 1"],
            "milestone": milestone_map.get("Sprint 1")
        }
        res = make_gh_request(f"{base_url}/issues", token, data=issue_data, method="POST")
        if res:
            print(f"  • Issue creado: {title} (# {res['number']})")

    print("\n" + "=" * 75)
    print("🎉 ¡TODOS LOS ISSUES FUERON CREADOS CON EL FORMATO EXACTO!")
    print(f"👉 Ingresa a: https://github.com/{owner}/{repo}/issues")
    print("=" * 75)

if __name__ == "__main__":
    setup_github_automation()
