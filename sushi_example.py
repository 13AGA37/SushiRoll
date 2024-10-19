import json
class JSONWorker:
    def __init__(self, data):

        if isinstance(data, list) and len(data) == 3 and all(isinstance(item, dict) and len(item) == 2 for item in data):
            self.data = data
        else:
            raise ValueError("Данные должны быть списком из 3-х словарей, каждый из которых содержит 2 пары ключ-значение.")
    def write_to_json(self, filename):

        with open(filename, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)
        print(f"Данные успешно записаны в файл {filename}.")
    def read_from_json(self, filename):

        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
if __name__ == "__main__":
    data = [
        {"key1": "value1", "key2": "value2"},
        {"key3": "value3", "key4": "value4"},
        {"key5": "value5", "key6": "value6"}
    ]
    json_worker = JSONWorker(data)

    json_worker.write_to_json('data.json')

    read_data = json_worker.read_from_json('data.json')
    print("Данные, прочитанные из файла:", read_data)