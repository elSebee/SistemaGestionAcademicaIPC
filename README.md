# Sistema de Gestión Académica IPC

Este proyecto es un software diseñado para gestionar automáticamente las equivalencias de asignaturas entre el plan común de ingeniería y las ingenierías de destino. Facilita a los estudiantes y administradores académicos la consulta y validación de asignaturas homologadas.

## Tecnologías Utilizadas

- **Backend:** Node.js con Express
- **Base de datos:** MySQL
- **Frontend:** React
- **Contenedores:** Docker y Docker Compose

## Despliegue del Software con Docker

Para desplegar el sistema en un entorno local utilizando Docker, sigue los siguientes pasos:

### 1. Clonar el Repositorio

```bash
git clone https://github.com/elSebee/SistemaGestionAcademicaIPC.git
```

### 2. Construcción y Ejecución con Docker Compose

Ejecuta el siguiente comando para construir y desplegar los contenedores en segundo plano:

```bash
docker compose up -d
```

Esto iniciará los servicios necesarios y el sistema quedará corriendo en `localhost:3006`.

### 3. Verificación del Estado del Sistema

Para comprobar que el sistema está funcionando correctamente y revisar posibles errores, usa el siguiente comando:

```bash
docker compose logs -f
```

Este comando muestra en tiempo real los logs generados por los servicios desplegados.
