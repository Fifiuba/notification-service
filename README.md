# Notification service 
---

[![GitHub Workflow Status](https://github.com/Fifiuba/notification-service/actions/workflows/python-app.yml/badge.svg?event=push)](https://github.com/Fifiuba/notification-service/commits/main)
[![codecov](https://codecov.io/gh/Fifiuba/notification-service/branch/main/graph/badge.svg?token=WQLIP37828)](https://codecov.io/gh/Fifiuba/notification-service)\
[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://notifications-service-alejovillores.cloud.okteto.net/)


## Indice de informacion
1. **Instalacion del entorno**
2. **Propósito del servicio de notificaciones**



### Instalación del entorno

Version de python
```shell
python --version
Python 3.8.5
 ```
Version de poetry
```bash
poetry --version
Poetry (version 1.2.0)
 ```

Pasos para levantar el servidor local una vez clonado el repo
```bash
poetry install
poetry run uvicorn admin_service.app:app --reload
```

Pasos para correr los test
```bash
poetry run pytest
```

Pasos para correr el formatter
```bash
poetry run black <carpeta>
```

Pasos para correr el linter
```bash
poetry run flake8 <carpeta>
```

Pasos para levantar el entorno Docker
```bash
docker-compose build --no-cache
clear
docker-compose up
```

Pasos para bajar el entorno Docker
```bash
docker-compose down -v
```

### Propósito del servicio de notificaciones
---

El proposito del servicio de notificaciones es enviar notificaciones push a los diferentes usuarios.
