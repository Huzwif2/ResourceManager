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

def main():
    resource_manager = ResourceManager()

    while True:
        print("\nMenu:")
        print("1. Create Resource")
        print("2. Search Resources")
        print("3. Edit Resource")
        print("4. Delete Resource")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter resource name: ")
            description = input("Enter resource description: ")
            resource_manager.create_resource(name, description)
            print("Resource created successfully.")

        elif choice == '2':
            keyword = input("Enter search keyword: ")
            found_resources = resource_manager.search_resources(keyword)
            print_resources(found_resources)

        elif choice == '3':
            index = int(input("Enter the index of the resource to edit: ")) - 1
            if 0 <= index < len(resource_manager.resources):
                new_name = input("Enter new name: ")
                new_description = input("Enter new description: ")
                resource_manager.edit_resource(index, new_name, new_description)
                print("Resource edited successfully.")
            else:
                print("Invalid index. Please try again.")

        elif choice == '4':
            index = int(input("Enter the index of the resource to delete: ")) - 1
            if 0 <= index < len(resource_manager.resources):
                resource_manager.delete_resource(index)
                print("Resource deleted successfully.")
            else:
                print("Invalid index. Please try again.")

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()