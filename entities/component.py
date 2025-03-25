class Component:
    def __init__(self, component_id):
        self.component_id = component_id  # Унифицированный идентификатор
        self.connected_to = []

    def connect(self, other_component):
        if other_component not in self.connected_to:
            self.connected_to.append(other_component)
            print(f"{self.component_id} -> {other_component.component_id}")
        else:
            print(f"Уже подключено: {self.component_id} -> {other_component.component_id}")

    def update_connected(self, param_name, value):
        for component in self.connected_to:
            if hasattr(component, param_name):
                setattr(component, param_name, value)
                print(f"Передача параметра: {param_name}={value} -> {component.component_id}")