student_name = input("Enter your name: ")
student_major = input("Enter your major code: ")

def convert_major_code(major_code):
    match major_code:
        case "BIOL":
            return "Biology"
        case "CSCI":
            return "Computer Science"
        case "ENG":
            return "English"
        case "HIST":
            return "History"
        case "MKT":
            return "Marketing"
        case _:
            return "<unknown>"
        
def convert_major_office(major_code):
    match major_code:
        case "BIOL":
            return "Science Bld, Room 310"
        case "CSCI":
            return "Sheppard Hall, Room 314"
        case "ENG":
            return "Kerr Hall, Room 201"
        case "HIST":
            return "Keer Hall, Room 114"
        case "MKT":
            return "Westly Hall, Room 310"
        case _:
            return " "

    
print("Your major is", convert_major_code(student_major), "and your Department Office is at", convert_major_office(student_major))