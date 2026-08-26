import os

from groq import Groq


SYSTEM_PROMPT = """
You are ComicNerd AI.

You are an expert comic book assistant.

Rules:

- Give spoiler-free answers unless asked.
- You are an expert in comic books, including Marvel, DC,
  and other publishers.
- Do not answer questions unrelated to comic books,
  characters, storylines, or recommendations.
- If you don't know the answer, say "I don't know"
  instead of making up an answer.
- Be polite, friendly, and concise in your responses.
"""


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)


def ask_ai(question, history, collection):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    if collection:

        collection_text = "\n".join(collection)

        messages.append(
            {
                "role": "system",
                "content": f"""
The user currently owns these comics:

{collection_text}

When recommending comics:

- Never recommend comics already owned.
- Use the collection to infer the user's interests.
- Recommend 5 comics that fit naturally.
"""
            }
        )

    messages.extend(history)

    messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    response = client.chat.completions.create(
        model=os.environ.get(
            "GROQ_MODEL",
            "openai/gpt-oss-20b"
        ),
        messages=messages,
    )

    return response.choices[0].message.content
