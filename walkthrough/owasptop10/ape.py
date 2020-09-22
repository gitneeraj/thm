import requests

url = "http://10.10.251.254/note.php?note="

for i in range(20):
    new_url = ""
    new_url = f"{url}{i}"
    # print(new_url)
    response = requests.get(new_url)
    if not response.text is None:
        print(response.text)
        break