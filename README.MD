# 🚀 Flask App Deployment with Ansible + CI/CD

Este proyecto automatiza el despliegue de una aplicación Flask en un servidor EC2 utilizando Ansible, empaquetado para flujos de trabajo de CI/CD con Jenkins y Docker. Está estructurado profesionalmente usando roles, buenas prácticas y validaciones.

---

## 📦 Características

* Automatiza:

  * Clonación del código desde GitHub
  * Compresión local y transferencia al servidor
  * Extracción y despliegue en el servidor
  * Configuración de systemd para app Flask
  * Variables de entorno en `/etc/environment`
  * Verificación del despliegue con `uri`
* Compatible con Jenkins y pipelines
* Preparado para escalar con `group_vars`, `inventory`, y `roles`

---

## 📁 Estructura del Proyecto

```
.
├── app/                         # Código fuente Flask (app.py, templates)
├── collections/                # Requisitos de colecciones Ansible
├── compressed/                 # Archivos .tar.gz generados (locales)
├── roles/
│   └── deploy/
│       ├── tasks/
│       │   ├── clone_repo.yml
│       │   ├── setup_app.yml
│       │   ├── configure_service.yml
│       │   └── validate.yml
│       ├── handlers/
│       │   └── main.yml
│       └── vars/
│           └── main.yml
├── deploy.yml                  # Playbook principal
├── Jenkinsfile                 # Pipeline CI/CD (opcional)
├── Dockerfile                  # Contenedor para pruebas o deploy
├── install_dependencies.sh     # Script auxiliar (opcional)
└── README.md                   # Este archivo
```

---

## 🚀 Ejecución del Playbook

```bash
ansible-playbook -i inventory/dev.ini deploy.yml
```

* Puedes adaptar tu `inventory.ini` o usar AWS Dynamic Inventory.
* La variable `current_date` genera backups/versiones distintas automáticamente.

---

## 🔐 Requisitos

* Python 3.8+
* Ansible 2.14+
* Colección `community.general`:

```bash
ansible-galaxy collection install -r collections/requirements.yml
```

---

## 🌐 Tecnologías

* Ansible
* Flask
* Linux / systemd
* EC2 / Ubuntu
* Jenkins (CI/CD)
* Docker (opcional)

---

