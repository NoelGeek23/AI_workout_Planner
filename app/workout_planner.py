import json
from cryptography.fernet import Fernet

class WorkoutPlanner:
    def __init__(self, user_data):
        self.user_data = user_data
        self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)

    def encrypt_data(self):
        json_data = json.dumps(self.user_data).encode()
        encrypted_data = self.cipher.encrypt(json_data)
        return encrypted_data

    def generate_workout_plan(self):
        # Placeholder for AI logic to generate workout plans
        return f"Generated workout plan for {self.user_data['name']} based on BMI: {self.user_data['bmi']}"

# Example usage
if __name__ == '__main__':
    user_info = {
        'name': 'John Doe',
        'age': 30,
        'bmi': 24.5,
        'fitness_level': 'intermediate',
        'available_time': '1 hour'
    }
    planner = WorkoutPlanner(user_info)
    encrypted_user_data = planner.encrypt_data()
    print(planner.generate_workout_plan())