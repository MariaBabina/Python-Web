import yaml

# Загружаем данные из файла config.yaml
with open('config/config.yaml') as f:
    testdata = yaml.safe_load(f)
