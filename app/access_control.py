class AccessControl:
    def __init__(self):
        self.roles_permissions = {
            'admin': ['read', 'write', 'delete'],
            'user': ['read'],
        }

    def check_permission(self, role, action):
        if action in self.roles_permissions.get(role, []):
            return True
        return False

# Example usage
if __name__ == '__main__':
    ac = AccessControl()
    print(ac.check_permission('admin', 'write'))  # True
    print(ac.check_permission('user', 'delete'))  # False