# 🤖 Agente Tutor de Inteligencia Artificial

Proyecto educativo desarrollado con **Python**, **Agno**, **LM Studio** y **Streamlit**.

## Objetivo

Desarrollar un agente inteligente que explique un tema según el nivel del estudiante.

El usuario escribe un tema y selecciona su nivel de conocimiento. El agente responde con:

- Una explicación sencilla.
- Un ejemplo práctico.
- Una analogía (cuando sea útil).
- Una pregunta de evaluación.

---

## Tecnologías utilizadas

- Python 3.10+
- Streamlit
- Agno
- LM Studio
- Modelo Qwen2.5-VL-3B-Instruct
- python-dotenv

---

## Estructura del proyecto

```
AgenteTutorIA/
│
├── app.py
├── agente.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Instalación

### 1. Clonar el proyecto

```bash
git clone <URL_DEL_REPOSITORIO>
cd AgenteTutorIA
```

### 2. Crear el entorno virtual

Windows

```bash
python -m venv .venv
```

Activar

```bash
.venv\Scripts\activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configuración de LM Studio

1. Instalar LM Studio.
2. Descargar un modelo compatible, por ejemplo:

- Qwen2.5-VL-3B-Instruct
- Llama-3.2-3B-Instruct
- Phi-3.5-mini-instruct

3. Cargar el modelo.
4. Abrir la pestaña **Developer**.
5. Iniciar el servidor local (**Start Server**).

Puerto recomendado:

```
1234
```

---

## Archivo .env

Crear un archivo llamado `.env` con el siguiente contenido:

```env
LM_STUDIO_BASE_URL=http://127.0.0.1:1234/v1
LM_STUDIO_API_KEY=lm-studio
LM_STUDIO_MODEL=qwen2.5-vl-3b-instruct
```

> Si LM Studio utiliza otro puerto, reemplazar **1234** por el puerto correspondiente.

---

## Ejecutar la aplicación

```bash
streamlit run app.py
```

o

```bash
python -m streamlit run app.py
```

Luego abrir en el navegador:

```
http://localhost:8501
```

---

## Funcionamiento

1. Seleccionar el nivel del estudiante.
2. Escribir el tema.
3. Presionar **Explicar tema**.
4. El agente generará:

- Explicación.
- Ejemplo.
- Analogía.
- Pregunta de evaluación.

---

## Dependencias

```
agno
openai
streamlit
python-dotenv
```

---

## Autor

Gene Ramos

Proyecto académico para la asignatura de Inteligencia Artificial.