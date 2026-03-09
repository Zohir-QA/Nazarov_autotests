import requests

url = "https://osdr.nasa.gov/geode-py/ws/api/biospecimens"

def test_get_biospecimen():
    response = requests.get(url)
    biospecimen = response.headers
    cookie = biospecimen.items()
    regular_dict = dict(cookie)
    val = "SAMEORIGIN"
    for key in regular_dict:
        reg_key = regular_dict.get(key)
        if val == regular_dict.get(key):
            pass
    print(response.status_code)
    assert response.status_code == 200