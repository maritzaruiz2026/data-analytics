contact_info = {
    "name": "Maria Contreras",
    "address": "123 Sesemee St",
    "city": "Chicago",
    "state": "IL",  
    "zip": "60601"
}

print(contact_info) #This prints everything in the dictionary
print(contact_info.get("name")) #This outputs the name ONLY
print(f"""The contact information for {contact_info.get('name')} is:
      
    Address: {contact_info.get('address')}
    City: {contact_info.get('city')}
    State: {contact_info.get('state')}
    Zip: {contact_info.get('zip')}
    """)
#This printed everything out in different lines


#print(f"The contact information for {contact_info.get('name')} is:\n "Address: {contact_info.get('address')}"\n"City: {contact_info.get('city')}"\n"State: {contact_info.get('state')}"\n"Zip: {contact_info.get('zip')}")
#I got an error for unterminated string literal

print(
    f"The contact information for {contact_info.get('name')} is:\n"
    f"Address: {contact_info.get('address')}\n"
    f"City: {contact_info.get('city')}\n"
    f"State: {contact_info.get('state')}\n"
    f"Zip: {contact_info.get('zip')}"
)
#Asked Copilot for assistance and informed me of having to add " after \n and including f in the beginning of each string (after the \n).

del contact_info["name"]
print(contact_info) #Prints dictionary entirely without name

full_name = {
    "first name": "Martin",
    "last name": "Rosas"
}


full_name.update({'honorific': 'Dr.'})
contact_info.update({"full_name": full_name})


print(f"""
The contact information for {contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']} is:

    Address: {contact_info.get('address')}
    City: {contact_info.get('city')}
    State: {contact_info.get('state')}
    Zip: {contact_info.get('zip')}
""")
