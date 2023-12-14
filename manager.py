import json

class Resource:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_dict(self):
        return {'name': self.name, 'description': self.description}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['description'])

class ResourceManager:
    def __init__(self, file_path='resources.json'):
        self.file_path = file_path
        self.resources = self.load_resources()

    def load_resources(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Resource.from_dict(item) for item in data]
        except FileNotFoundError:
            return []

    def save_resources(self):
        with open(self.file_path, 'w') as file:
            data = [resource.to_dict() for resource in self.resources]
            json.dump(data, file)

    def create_resource(self, name, description):
        new_resource = Resource(name, description)
        self.resources.append(new_resource)
        self.save_resources()

    def search_resources(self, keyword):
        return [resource for resource in self.resources if keyword.lower() in resource.name.lower()]

    def edit_resource(self, index, new_name, new_description):
        if 0 <= index < len(self.resources):
            self.resources[index].name = new_name
            self.resources[index].description = new_description
            self.save_resources()

    def delete_resource(self, index):
        if 0 <= index < len(self.resources):
            del self.resources[index]
            self.save_resources()
            
def print_resources(resources):
    if not resources:
        print("No resources found.")
    else:
        for i, resource in enumerate(resources):
            print(f"{i + 1}. {resource.name} - {resource.description}")
