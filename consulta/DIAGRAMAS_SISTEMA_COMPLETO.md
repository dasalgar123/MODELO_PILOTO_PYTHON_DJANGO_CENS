# Diagramas Completos del Sistema - Inspector y Administrador

## 📊 Diagrama 1: Arquitectura General del Sistema

```mermaid
graph TB
    Start([Usuario Accede al Sistema]) --> Login[Página de Login]
    Login --> Auth{Autenticación}
    Auth -->|Credenciales Incorrectas| Error1[Error: Credenciales Incorrectas]
    Auth -->|Credenciales Correctas| CheckStatus{Verificar Estado}
    CheckStatus -->|Deshabilitado| Error2[Error: Usuario Deshabilitado]
    CheckStatus -->|Habilitado| CheckType{Verificar Tipo de Perfil}
    CheckType -->|Inspector| InspectorInterface[Interfaz Inspector]
    CheckType -->|Administrador| AdminInterface[Interfaz Administrador]
    
    InspectorInterface --> InspectorMenu[Menú de Inspecciones Asignadas]
    InspectorMenu --> Execute[Ejecutar Inspección]
    Execute --> SaveData[Guardar Datos]
    SaveData --> InspectorMenu
    
    AdminInterface --> AdminDashboard[Dashboard Administrador]
    AdminDashboard --> UserManagement[Gestión de Usuarios]
    AdminDashboard --> InspectionManagement[Gestión de Inspecciones]
    AdminDashboard --> Search[Búsqueda Avanzada]
    
    UserManagement --> CreateUser[Crear Usuario]
    UserManagement --> EditUser[Editar Usuario]
    UserManagement --> ActivateUser[Activar/Desactivar Usuario]
    
    InspectionManagement --> AssignInspection[Asignar Inspección]
    InspectionManagement --> ViewAll[Ver Todas las Inspecciones]
    
    Search --> FilterResults[Resultados Filtrados]
```

---

## 🔄 Diagrama 2: Flujo Completo de Login y Redirección

```mermaid
sequenceDiagram
    participant U as Usuario
    participant L as Login Page
    participant S as Sistema/Backend
    participant DB as Base de Datos
    participant II as Interfaz Inspector
    participant AI as Interfaz Administrador

    U->>L: Ingresa URL: /login/
    L->>U: Muestra formulario de login
    U->>L: Ingresa usuario y contraseña
    L->>S: POST /login/ (username, password)
    S->>DB: Verificar credenciales
    DB-->>S: Datos del usuario
    
    alt Credenciales Incorrectas
        S-->>L: Error: Credenciales incorrectas
        L-->>U: Muestra mensaje de error
    else Credenciales Correctas
        S->>S: Verificar estado del usuario
        
        alt Usuario Deshabilitado
            S-->>L: Error: Usuario deshabilitado
            L-->>U: Muestra mensaje: "Contacte al administrador"
        else Usuario Habilitado
            S->>S: Verificar tipo de perfil
            
            alt Tipo: Inspector
                S-->>L: Redirección a /app/inspector/menu/
                L->>II: Redirige a Interfaz Inspector
                II->>U: Muestra menú de inspecciones asignadas
            else Tipo: Administrador
                S-->>L: Redirección a /app/admin/dashboard/
                L->>AI: Redirige a Interfaz Administrador
                AI->>U: Muestra dashboard administrativo
            end
        end
    end
```

---

## 👥 Diagrama 3: Gestión de Usuarios por Administrador

```mermaid
flowchart TD
    Start([Administrador en Dashboard]) --> UserMenu[Menú: Gestión de Usuarios]
    UserMenu --> Options{¿Qué acción?}
    
    Options -->|Crear Usuario| CreateForm[Formulario Crear Usuario]
    Options -->|Ver Usuarios| UserList[Lista de Usuarios]
    Options -->|Editar Usuario| EditForm[Formulario Editar Usuario]
    
    CreateForm --> FillData[Llenar Datos]
    FillData --> SelectType{Tipo de Perfil}
    SelectType -->|Inspector| SetInspector[Configurar como Inspector]
    SelectType -->|Administrador| SetAdmin[Configurar como Administrador]
    SetInspector --> SetStatus{Estado}
    SetAdmin --> SetStatus
    SetStatus -->|Habilitado| SaveUser[Guardar Usuario]
    SetStatus -->|Deshabilitado| SaveUser
    SaveUser --> Success1[Usuario Creado Exitosamente]
    
    UserList --> ViewUsers[Ver Lista]
    ViewUsers --> UserActions{Acciones}
    UserActions -->|Activar| Activate[Cambiar Estado a Habilitado]
    UserActions -->|Desactivar| Deactivate[Cambiar Estado a Deshabilitado]
    UserActions -->|Editar| EditForm
    Activate --> UpdateDB[(Actualizar Base de Datos)]
    Deactivate --> UpdateDB
    EditForm --> UpdateUser[Actualizar Datos]
    UpdateUser --> UpdateDB
    UpdateDB --> Success2[Cambios Guardados]
```

---

## 📋 Diagrama 4: Flujo Completo de Inspección

```mermaid
graph LR
    subgraph Admin["👨‍💼 Administrador"]
        A1[Admin Login] --> A2[Dashboard]
        A2 --> A3[Asignar Inspección]
        A3 --> A4[Seleccionar Inspector]
        A4 --> A5[Seleccionar Subestación]
        A5 --> A6[Definir Fecha Límite]
        A6 --> A7[Guardar Asignación]
        A7 --> DB1[(Base de Datos)]
    end
    
    subgraph Inspector["👤 Inspector"]
        I1[Inspector Login] --> I2[Menú Principal]
        I2 --> I3[Ver Inspecciones Asignadas]
        I3 --> I4[Seleccionar Inspección]
        I4 --> I5[Abrir Formulario]
        I5 --> I6[Llenar Datos]
        I6 --> I7[Guardar Inspección]
        I7 --> DB2[(Base de Datos)]
        I7 --> I8[Estado: Completada]
    end
    
    subgraph AdminView["👨‍💼 Administrador - Ver Resultados"]
        AV1[Ver Todas las Inspecciones] --> AV2[Aplicar Filtros]
        AV2 --> AV3{Búsqueda}
        AV3 -->|Por Inspector| F1[Filtrar por Inspector]
        AV3 -->|Por Fecha| F2[Filtrar por Fecha]
        AV3 -->|Por Subestación| F3[Filtrar por Subestación]
        AV3 -->|Por Rango| F4[Filtrar por Rango de Fechas]
        F1 --> AV4[Mostrar Resultados]
        F2 --> AV4
        F3 --> AV4
        F4 --> AV4
        AV4 --> AV5[Exportar/Ver Detalles]
    end
    
    DB1 --> I3
    DB2 --> AV1
```

---

## 🗄️ Diagrama 5: Estructura de Base de Datos

```mermaid
erDiagram
    USUARIO ||--o{ INSPECCION : "ejecuta"
    USUARIO ||--o{ ASIGNACION : "recibe"
    ADMINISTRADOR ||--o{ ASIGNACION : "asigna"
    ADMINISTRADOR ||--o{ USUARIO : "crea"
    ASIGNACION ||--|| INSPECCION : "genera"
    
    USUARIO {
        int id PK
        string username UK
        string password
        string nombre_completo
        enum tipo_usuario "Inspector|Administrador"
        enum estado "Habilitado|Deshabilitado"
        string email
        string telefono
        datetime fecha_creacion
        datetime ultimo_acceso
        int creado_por FK
    }
    
    INSPECCION {
        int id PK
        int inspector_id FK
        string subestacion "S30|S_XX|S01"
        datetime fecha_asignacion
        datetime fecha_ejecucion
        datetime fecha_limite
        enum estado "Pendiente|En Proceso|Completada"
        json datos_inspeccion
        text notas
        int asignado_por FK
        datetime tiempo_inicio "Registrado al abrir formulario"
        datetime tiempo_fin "Registrado al guardar"
        int duracion_segundos "Calculado automáticamente"
        string duracion_formato "Formato legible: 1h 23m 27s"
    }
    
    ASIGNACION {
        int id PK
        int inspector_id FK
        int inspeccion_id FK
        datetime fecha_asignacion
        datetime fecha_limite
        int asignado_por FK
    }
```

---

## 🔍 Diagrama 6: Sistema de Búsqueda Avanzada

```mermaid
flowchart TD
    Start([Administrador en Búsqueda]) --> SearchForm[Formulario de Búsqueda]
    SearchForm --> Filter1{¿Filtrar por Inspector?}
    Filter1 -->|Sí| SelectInspector[Seleccionar Inspector]
    Filter1 -->|No| Filter2
    SelectInspector --> Filter2{¿Filtrar por Subestación?}
    Filter2 -->|Sí| SelectSubestacion[Seleccionar Subestación]
    Filter2 -->|No| Filter3
    SelectSubestacion --> Filter3{¿Filtrar por Fecha?}
    Filter3 -->|Sí| SelectDate[Seleccionar Fecha Específica]
    Filter3 -->|No| Filter4
    SelectDate --> Filter4{¿Filtrar por Rango?}
    Filter4 -->|Sí| SelectRange[Seleccionar Rango de Fechas]
    Filter4 -->|No| ExecuteSearch
    SelectRange --> ExecuteSearch[Ejecutar Búsqueda]
    ExecuteSearch --> QueryDB[(Consultar Base de Datos)]
    QueryDB --> Results[Resultados Filtrados]
    Results --> Actions{Acciones}
    Actions -->|Ver Detalles| ViewDetails[Ver Detalles Completos]
    Actions -->|Exportar| Export[Exportar a PDF/Excel]
    Actions -->|Imprimir| Print[Imprimir]
```

---

## 🎯 Diagrama 7: Flujo Completo desde el Inicio

```mermaid
graph TB
    subgraph Inicio["🚀 INICIO DEL SISTEMA"]
        A[Usuario Accede] --> B[Página de Login]
        B --> C[Ingresa Credenciales]
    end
    
    subgraph Autenticacion["🔐 AUTENTICACIÓN"]
        C --> D{Verificar Credenciales}
        D -->|Incorrectas| E[Error: Credenciales Incorrectas]
        D -->|Correctas| F{Verificar Estado}
        F -->|Deshabilitado| G[Error: Usuario Deshabilitado]
        F -->|Habilitado| H{Verificar Tipo de Perfil}
    end
    
    subgraph InspectorFlow["👤 FLUJO INSPECTOR"]
        H -->|Inspector| I1[Redirige a /app/inspector/menu/]
        I1 --> I2[Ve Inspecciones Asignadas]
        I2 --> I3{¿Qué hacer?}
        I3 -->|Ejecutar| I4[Abrir Formulario]
        I3 -->|Ver Historial| I5[Ver Sus Inspecciones]
        I4 --> I5[⏱️ tiempo_inicio registrado]
        I5 --> I6[Llenar Datos]
        I6 --> I7[Guardar en Base de Datos]
        I7 --> I8[⏱️ tiempo_fin registrado]
        I8 --> I9[⏱️ duracion calculada]
        I9 --> I10[Estado: Completada]
        I10 --> I2
        Note right of I5: Inspector NO ve el tiempo
        Note right of I9: Solo Admin ve en registros
    end
    
    subgraph AdminFlow["👨‍💼 FLUJO ADMINISTRADOR"]
        H -->|Administrador| A1[Redirige a /app/admin/dashboard/]
        A1 --> A2{¿Qué hacer?}
        
        A2 -->|Gestión de Usuarios| A3[Gestión de Usuarios]
        A3 --> A4{Acción}
        A4 -->|Crear| A5[Crear Usuario]
        A4 -->|Editar| A6[Editar Usuario]
        A4 -->|Activar/Desactivar| A7[Cambiar Estado]
        A5 --> A8[Guardar en Base de Datos]
        A6 --> A8
        A7 --> A8
        
        A2 -->|Gestión de Inspecciones| A9[Gestión de Inspecciones]
        A9 --> A10{Acción}
        A10 -->|Asignar| A11[Asignar Inspección a Inspector]
        A10 -->|Ver Todas| A12[Ver Todas las Inspecciones]
        A11 --> A13[Guardar Asignación]
        A13 --> A8
        
        A2 -->|Búsqueda| A14[Búsqueda Avanzada]
        A14 --> A15[Aplicar Filtros]
        A15 --> A16[Mostrar Resultados]
        A16 --> A17{Acción}
        A17 -->|Ver| A18[Ver Detalles]
        A17 -->|Exportar| A19[Exportar Datos]
    end
    
    subgraph BaseDatos["💾 BASE DE DATOS"]
        I7 --> DB[(Base de Datos)]
        A8 --> DB
        A13 --> DB
        DB --> A12
        DB --> A16
    end
```

---

## 🔐 Diagrama 8: Sistema de Permisos y Seguridad

```mermaid
graph TD
    subgraph Permisos["🔐 SISTEMA DE PERMISOS"]
        Login[Usuario hace Login] --> CheckAuth{Autenticado?}
        CheckAuth -->|No| Deny1[Acceso Denegado]
        CheckAuth -->|Sí| CheckStatus{Estado?}
        CheckStatus -->|Deshabilitado| Deny2[Acceso Bloqueado]
        CheckStatus -->|Habilitado| CheckRole{Tipo de Perfil?}
        
        CheckRole -->|Inspector| InspectorPerms[Permisos Inspector]
        CheckRole -->|Administrador| AdminPerms[Permisos Administrador]
    end
    
    subgraph InspectorPerms["👤 Permisos Inspector"]
        IP1[✅ Ver inspecciones asignadas]
        IP2[✅ Ejecutar inspecciones]
        IP3[✅ Guardar datos]
        IP4[✅ Ver historial propio]
        IP5[❌ Crear usuarios]
        IP6[❌ Ver inspecciones de otros]
        IP7[❌ Asignar inspecciones]
        IP8[❌ Editar usuarios]
    end
    
    subgraph AdminPerms["👨‍💼 Permisos Administrador"]
        AP1[✅ Todo lo del Inspector]
        AP2[✅ Crear usuarios]
        AP3[✅ Editar usuarios]
        AP4[✅ Activar/Desactivar usuarios]
        AP5[✅ Ver todas las inspecciones]
        AP6[✅ Asignar inspecciones]
        AP7[✅ Búsqueda avanzada]
        AP8[✅ Exportar datos]
        AP9[✅ Eliminar inspecciones]
    end
```

---

## 📱 Diagrama 9: Estructura de URLs y Navegación

```mermaid
graph TD
    Root[/] --> Login[/login/]
    
    Login -->|Inspector| InspectorRoutes
    Login -->|Administrador| AdminRoutes
    
    subgraph InspectorRoutes["👤 Rutas Inspector"]
        IR1[/app/inspector/menu/]
        IR2[/app/inspector/ejecutar/id/]
        IR3[/app/inspector/historial/]
        IR1 --> IR2
        IR1 --> IR3
    end
    
    subgraph AdminRoutes["👨‍💼 Rutas Administrador"]
        AR1[/app/admin/dashboard/]
        AR2[/app/admin/usuarios/]
        AR3[/app/admin/usuarios/crear/]
        AR4[/app/admin/usuarios/editar/id/]
        AR5[/app/admin/usuarios/activar/id/]
        AR6[/app/admin/inspecciones/]
        AR7[/app/admin/inspecciones/asignar/]
        AR8[/app/admin/buscar/]
        
        AR1 --> AR2
        AR1 --> AR6
        AR1 --> AR8
        AR2 --> AR3
        AR2 --> AR4
        AR2 --> AR5
        AR6 --> AR7
    end
```

---

## 🔄 Diagrama 10: Ciclo de Vida Completo de una Inspección

```mermaid
stateDiagram-v2
    [*] --> Creada: Administrador crea asignación
    Creada --> Asignada: Se asigna a Inspector
    Asignada --> Pendiente: Inspector ve en su menú
    Pendiente --> EnProceso: Inspector inicia formulario
    EnProceso --> Completada: Inspector guarda datos
    Completada --> Revisada: Administrador revisa
    Revisada --> Archivada: Se archiva en sistema
    Archivada --> [*]
    
    Pendiente --> Cancelada: Administrador cancela
    EnProceso --> Cancelada: Administrador cancela
    Cancelada --> [*]
```

---

## 📊 Resumen Visual del Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                    SISTEMA DE INSPECCIONES                   │
│                      CENS - Grupo EPM                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   LOGIN ÚNICO    │
                    │    /login/      │
                    └────────┬────────┘
                             │
                ┌────────────┴────────────┐
                │                        │
                ▼                        ▼
    ┌───────────────────┐    ┌──────────────────────┐
    │   INSPECTOR       │    │   ADMINISTRADOR      │
    │                   │    │                      │
    │ • Ver asignadas   │    │ • Crear usuarios     │
    │ • Ejecutar        │    │ • Activar/Desactivar │
    │ • Guardar datos   │    │ • Asignar inspecciones│
    │ • Ver historial   │    │ • Ver todas          │
    └───────────────────┘    │ • Búsqueda avanzada  │
                             │ • Exportar           │
                             └──────────────────────┘
                                      │
                                      ▼
                            ┌─────────────────┐
                            │  BASE DE DATOS  │
                            │                 │
                            │ • Usuarios      │
                            │ • Inspecciones  │
                            │ • Asignaciones  │
                            └─────────────────┘
```

---

## 🎨 Diagrama de Interfaz de Usuario

```mermaid
graph TB
    subgraph LoginScreen["🔐 Pantalla de Login"]
        LS1[Logo CENS]
        LS2[Formulario Login]
        LS3[Usuario/Contraseña]
        LS4[Botón Entrar]
    end
    
    subgraph InspectorUI["👤 Interfaz Inspector"]
        IU1[Header: Bienvenido Inspector]
        IU2[Menú de Inspecciones]
        IU3[Tarjeta: S30 - La Miel]
        IU4[Tarjeta: S_XX - El Zulia]
        IU5[Botón: Ejecutar]
        IU6[Formulario de Inspección]
    end
    
    subgraph AdminUI["👨‍💼 Interfaz Administrador"]
        AU1[Header: Panel Administrativo]
        AU2[Tab: Usuarios]
        AU3[Tab: Inspecciones]
        AU4[Tab: Búsqueda]
        AU5[Formulario Crear Usuario]
        AU6[Tabla de Usuarios]
        AU7[Filtros de Búsqueda]
        AU8[Tabla de Resultados]
    end
```

---

**Fecha de creación**: 12 de diciembre de 2025  
**Versión**: 1.0  
**Formato**: Diagramas Mermaid (compatibles con GitHub, GitLab, y editores Markdown)

---

## 📝 Notas sobre los Diagramas

- Todos los diagramas están en formato **Mermaid**
- Se pueden visualizar en:
  - GitHub/GitLab (automáticamente)
  - Editores como VS Code con extensión Mermaid
  - Herramientas online: https://mermaid.live/
- Los diagramas muestran el flujo completo del sistema desde el inicio
- Incluyen todas las funcionalidades: login, creación de usuarios, inspecciones, búsqueda, etc.

