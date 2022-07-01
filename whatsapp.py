import pywhatkit

# Send message to a contact
phone_number = input("Enter phone number: ")

pywhatkit.sendwhatmsg(phone_number, "Test", 12, 34)
pywhatkit.sendwhatmsg(phone_number, "Test", 12, 55, 55, True, 2)

# Send message to a group
group_id = input("Enter group id: ")

pywhatkit.sendwhatmsg_to_group(group_id, "Test Group", 12, 59)
