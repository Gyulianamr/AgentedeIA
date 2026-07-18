import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai.like import OpenAILike

load_dotenv()

agente = Agent(
    name="Tutor IA",

    model=OpenAILike(
        id="llama-3.1-8b-instant",
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"),
    ),

    instructions=[
        "Responde siempre en español.",
        "Actúa como un profesor universitario.",
        "Explica los temas de manera clara y detallada.",
        "Incluye ejemplos prácticos.",
        "Adapta la explicación al nivel del estudiante.",
        "Finaliza con una pregunta de evaluación.",
        "Usa formato Markdown."
    ],

    markdown=True,
)


def crear_agente_tutor():
    return agente
