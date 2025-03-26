from oops_project import chatbook

user1 = chatbook()
print(user1.id)

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)

# print(user1.get_name())

"""
user1.set_name("Agent X")
print(user1.get_name())
"""