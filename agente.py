import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.huggingface import HuggingFace

load_dotenv()

agente = Agent(
    name="Tutor IA",

 model=HuggingFace(
    id="mistralai/Mistral-7B-Instruct-v0.2",
    api_key=os.getenv("HF_TOKEN"),
),

    instructions=[
        "Responde siempre en español.",
        "Actúa como un profesor universitario.",
        "Explica los temas de forma clara y detallada.",
        "Incluye ejemplos prácticos.",
        "Adapta la explicación al nivel del estudiante.",
        "Finaliza con una pregunta de evaluación.",
        "Usa formato Markdown."
    ],

    markdown=True,
)


def crear_agente_tutor():
    return agente
