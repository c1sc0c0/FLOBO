import chromadb

client = chromadb.PersistentClient(path="chromadb")
collection = client.get_or_create_collection(name="yoga-poses-deck")

document = "Vajrasana is a Yoga pose"
metadata = {"source": "yoga-deck"}
identifier = "vajrasana"
collection.add(
    documents=[document],
    metadatas=[metadata],
    ids=[identifier]
)

