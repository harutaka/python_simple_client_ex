import httpx

def fetch_data():
    with httpx.Client() as client:
        response = client.get("https://jsonplaceholder.typicode.com/todos/1")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.json()}")

if __name__ == "__main__":
    fetch_data()
