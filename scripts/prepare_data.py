import requests
import os
import hashlib
import zipfile
import pandas as pd

expected_wine_sha256 = "3ed56667f4b828242bd732d7d1dd7f2861e54432239d7fa63877014cbb0304d4"

wine_url = "https://archive.ics.uci.edu/static/public/186/wine+quality.zip"

response_wine = requests.get(wine_url)


if not os.path.exists('data'):
    os.mkdir('data')

zip_file_path = 'data/wine+quality.zip'

with open('data/wine+quality.zip', mode='wb') as f:
    f.write(response_wine.content)


with open('data/wine+quality.zip', mode='rb') as f:
    data = f.read()
    computed_wine_sha256hash = hashlib.sha256(data).hexdigest()

print(computed_wine_sha256hash)
if (computed_wine_sha256hash != expected_wine_sha256):
    print("WARNING: Computed wine hash does not match expected wine hash")
else:
    print("Computed wine matches expected wine hash")

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall('data')

