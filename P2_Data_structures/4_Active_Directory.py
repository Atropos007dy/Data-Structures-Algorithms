class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
        
        
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    
    #check if user in the group
    if user in group.users:
        return True
    
    #check if user in the subgroup
    for sub_group in group.groups:
        if is_user_in_group(user,sub_group):
            return True
            
    return False




first_layer=Group("1st_layer")
second_layer=Group("2nd_layer")
third_layer=Group("3rd_layer")

user_1st_layer = "1_user"
user_2nd_layer = "2_user"
user_3rd_layer = "3_user"

first_layer.add_user(user_1st_layer )
second_layer.add_user(user_2nd_layer)
third_layer.add_user(user_3rd_layer)

second_layer.add_group(third_layer)
first_layer.add_group(second_layer)



print("Test 1: whether can detect user in current group ,should be True.")
print(is_user_in_group(user_1st_layer, first_layer)) 
print("Test 2: whether can detect user in the subgroup of current group ,should be True.")
print(is_user_in_group(user_3rd_layer, first_layer)) 
print("Test 3: check the user doesn't exist in the group,should be False.")
print(is_user_in_group(user_1st_layer, second_layer)) 




