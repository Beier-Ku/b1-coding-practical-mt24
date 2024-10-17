import pandas as pd

class Mission:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_csv(cls, file_path):
        # Use pandas to read CSV file
        data = pd.read_csv(file_path)
        return cls(data)
    
    # Method: Get the total reference duration
    def get_mission_reference_range(self):
        return self.data['reference'].iloc[-1] - self.data['reference'].iloc[0]

    # Method: Get maximum cave height
    def get_max_cave_height(self):
        return self.data['cave_height'].max()

    # Method: Get minimum cave height
    def get_min_cave_height(self):
        return self.data['cave_height'].min()

    # Method: Get maximum cave depth
    def get_max_cave_depth(self):
        return self.data['cave_depth'].max()

    # Method: Get minimum cave depth
    def get_min_cave_depth(self):
        return self.data['cave_depth'].min()

    # Method: Calculate average cave height change
    def get_average_cave_height_change(self):
        height_changes = self.data['cave_height'].diff().dropna()  # Calculate height changes
        return height_changes.mean()

    # Method: Calculate average cave depth change
    def get_average_cave_depth_change(self):
        depth_changes = self.data['cave_depth'].diff().dropna()  # Calculate depth changes
        return depth_changes.mean()