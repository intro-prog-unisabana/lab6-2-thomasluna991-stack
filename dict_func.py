def employee_print(employee_info):
    print("Name:", employee_info.get("Name", "N/A"))
    print("Salary:", employee_info.get("Salary", "N/A"))
    print("Role:", employee_info.get("Role", "N/A"))
    
    extra_info = employee_info.copy()
    
    extra_info.pop("Name", None)
    extra_info.pop("Salary", None)
    extra_info.pop("Role", None)
    
    if extra_info:
        for key, value in extra_info.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")
