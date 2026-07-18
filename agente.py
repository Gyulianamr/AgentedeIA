import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai.like import OpenAILike

load_dotenv()

agente = Agent(
    name="Tutor IA",

    model=OpenAILike(
        id="meta-llama/Llama-3.2-3B-Instruct",
        base_url="https://api-inference.huggingface.co/v1",
        api_key=os.getenv("HF_TOKEN"),
    ),

    instructions=[
        "Responde siempre en español.",
        "Actúa como un profesor universitario.",
        "Explica el tema de manera clara y detallada.",
        "Incluye ejemplos prácticos.",
        "Adapta la explicación al nivel del estudiante.",
        "Finaliza con una pregunta de evaluación.",
        "Usa formato Markdown."
    ],

    markdown=True,
)


def crear_agente_tutor():
    return agente
