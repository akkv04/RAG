import chromadb
import uuid

#the data is stored only on runtime, and is saved in memory
chroma_client = chromadb.Client()

#persistent client allows data to saved in local path
#chroma_client=chromadb.PersistentClient(path="./chromadata")
#can use http client as well

#collection = chroma_client.create_collection(name= "test_collection")
#create_collection only creates teh collection

#use get or create collections for future uses, as collection names are unique
collection = chroma_client.get_or_create_collection(name= "test_collection")




with open("policies.txt","r",encoding="utf-8") as f:
    policies: list[str]=f.read().splitlines()
#policies is a list of string 
# from the stream, it reads and split lines

collection.add(

    ids= [str(uuid.uuid4()) for _ in policies],
    documents = policies,
    metadatas = [{"line":line} for line in range(len(policies))]

)

#it prints the first 10 lines
#print(collection.peek())

#this converts it into vector and searches it against the chroma db
result= collection.query(
    query_texts= [
        "What is the return policy time",
        "How many days can i return the customised items"
    ],
    n_results =5
)

for i, query_results in enumerate(result["documents"]):
    print(f"Query :{i}")
    print("\n".join(query_results))
