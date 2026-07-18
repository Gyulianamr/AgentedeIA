import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai.like import OpenAILike

load_dotenv()

agente = Agent(
    name="Tutor IA",
  model=OpenAILike(
    id=r"C:\Users\genes\.lmstudio\models\wangkanai\qwen2.5-vl-3b-instruct\qwen2.5-vl-3b-instruct-abliterated-q4-k-m.gguf",
    base_url=os.getenv("LM_STUDIO_BASE_URL"),
    api_key="lm-studio",
),
    instructions=[
    "Responde siempre en español.",
    "Actúa como un profesor universitario con experiencia.",
    "Explica el tema de forma clara y detallada.",
    "Adapta la profundidad de la explicación al nivel del estudiante.",
    "Incluye conceptos importantes y definiciones relevantes.",
    "Proporciona uno o dos ejemplos prácticos.",
    "Utiliza analogías cuando ayuden a comprender el tema.",
    "Menciona aplicaciones del tema en la vida real.",
    "Finaliza con una pregunta de evaluación y su respuesta esperada.",
    "Utiliza formato Markdown con títulos, subtítulos y listas."
],
    markdown=True,
)

def crear_agente_tutor():
    return agente