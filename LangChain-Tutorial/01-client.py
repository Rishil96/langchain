from langserve import RemoteRunnable

# Create remote runnable to hit langserve endpoint
remote_chain = RemoteRunnable("http://localhost:8000/chain/")
# Hit the remote runnable LLM using invoke and pass the placeholder values
result = remote_chain.invoke({"language": "italian", "text": "hi"})

print(result)
