import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.google import Gemini

load_dotenv()

agente = Agent(
    name="Tutor IA",

    model=Gemini(
        id="gemini-2.0-flash",
        api_key=os.getenv("GOOGLE_API_KEY"),
    ),

    instructions=[
        "Responde siempre en español.",
        "Actúa como un profesor universitario con experiencia.",
        "Explica el tema de forma clara y detallada.",
        "Adapta la explicación al nivel del estudiante.",
        "Incluye ejemplos prácticos.",
        "Utiliza analogías cuando sean útiles.",
        "Finaliza con una pregunta de evaluación.",
        "Utiliza formato Markdown."
    ],

    markdown=True,
)


def crear_agente_tutor():
    return agente
