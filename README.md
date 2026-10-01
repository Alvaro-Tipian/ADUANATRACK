# ADUANATRACK — Sistema de Seguimiento y Control de Despachos Aduaneros

Sistema de trazabilidad operativa y gestión documental aduanera para agencias de aduana e importadores (Régimen 10 - Importación al Consumo, SUNAT).

## 🚀 Arquitectura del Proyecto

El repositorio está estructurado bajo una arquitectura limpia multi-servicio de software:

```
ADUANATRACK/
├── Backend/                 # Web API REST en C# (.NET / Entity Framework Core)
│   ├── Controllers/         # Endpoints RESTful para Auth, Despachos, Clientes, KPIs
│   ├── Data/                # DbContext y migraciones
│   ├── DTOs/                # Data Transfer Objects
│   ├── Models/              # Entidades del dominio aduanero
│   ├── Repositories/        # Capa de acceso a datos
│   └── Services/            # Lógica de negocio (RUC Módulo 11, correlativos, almacenaje)
├── FrontendWeb/             # Aplicación SPA en React + Vite + Tailwind CSS
│   ├── public/              # Recursos estáticos
│   └── src/                 # Componentes UI, vistas y servicios de API
├── github_issues_and_project_data.csv   # Dataset del Sprint Backlog (Épicas, HUs, HTs)
├── setup_github_repo_and_project.py      # Script de automatización GitHub Projects V2
└── README.md                # Documentación principal de la solución
```

## 🛠️ Tecnologías Utilizadas

- **Backend:** C# / .NET Web API, Entity Framework Core, SQLite / PostgreSQL.
- **Frontend:** React, Vite, Tailwind CSS, Axios.
- **DevOps & QA:** GitHub Actions CI, GitFlow (`main`, `develop`), GitHub Projects V2.

## ⚙️ Inicialización del Proyecto

### Backend (.NET API)
```bash
cd Backend
dotnet restore
dotnet run
```

### Frontend (React + Vite)
```bash
cd FrontendWeb
npm install
npm run dev
```

---
*Grupo 2 — Taller de Proyectos / Gestión Ágil con Scrum*
