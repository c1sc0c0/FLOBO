import chromadb

client = chromadb.PersistentClient(path="chromadb")
collection = client.get_or_create_collection(name="yoga-poses-deck")

results = collection.query(
    query_texts=["Give me a Yoga pose"],
    n_results=1,
)

print(results)