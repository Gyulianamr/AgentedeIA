import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai import OpenAIChat

load_dotenv()

agente = Agent(
    name="Tutor IA",

    model=OpenAIChat(
    id="gpt-4.1-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
)
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
