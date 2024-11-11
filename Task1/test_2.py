import requests
import yaml
import pytest

# Загружаем данные из config.yaml
with open("config.yaml") as f:
    data = yaml.safe_load(f)

@pytest.mark.parametrize("testtext1", ["яяяяяя"]) 
def test_step1(login, testtext1):
    headers = {"X-Auth-Token": login}
    res = requests.get(
        data["address"] + "/api/posts",
        #params={"owner": "notMe"},
        headers=headers
    )
    print("Ответ от сервера:", res.json())
    listres = [i["title"] for i in res.json().get("data", [])]
    assert testtext1 in listres

