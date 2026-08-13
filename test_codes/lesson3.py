import os
from dotenv import load_dotenv
from openai import OpenAI
import chromadb
import chromadb.utils.embedding_functions as ef

load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GITHUB_TOKEN"),
)

db=chromadb.PersistentClient(path="./chroma_db")
memories=db.get_or_create_collection("my_facts")

#3 facts
memories.upsert(
    documents=[
        "do homework",
        "eat breakfast",
        "eat lunch",
        "eat dinner",
        "travel to Italy",
        "read books",
        "My name is Scarlett"
    ],
    ids=[f"fact{memories.count()+1}"],
)

print("\nstored:", memories.count(), "facts")

while True:
    question=str(input(""))
    if question.lower=="quit":
        break

    results=memories.query(query_texts=[question], n_results=3)
    notes="\n".join(results["documents"][0]) #n is for new line
    print(results["documents"], results["distances"])

    prompt=f"""
    Use these notes {notes} to answer my question {question}"""

    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )

    # print(r)   # uncomment to see the whole messy response
    print(r.choices[0].message.content)


