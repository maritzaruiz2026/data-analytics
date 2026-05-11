# if/elif/else logic to determine and print department name based on a department code
  
#def convert_dept_code(dept_code):
#    if dept_code == "1":
#        return "Marketing"
#    elif dept_code == "5":
#        return "Human Resources"
#    elif dept_code == "10":
#        return "Accounting"    
#    elif dept_code == "12":
#        return "Legal"
#    elif dept_code == "18":
#        return "IT"
#    elif dept_code == "20":
#        return "Customer Relations"
#    else:
#        return "Error: Unknown Department Code"
    
#print(convert_dept_code(input("Enter a department code: ")  ))

def convert_dept_code(dept_code):
    match dept_code:
        case "1":
            return "Marketing"
        case "5":
            return "Human Resources"
        case "10":
            return "Accounting"
        case "12":
            return "Legal"
        case "18":
            return "IT"
        case "20":
            return "Customer Relations"
        case _:
            return "Error: Unknown Department Code"

print(convert_dept_code(input("Enter a department code: ")))
