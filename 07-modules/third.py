def hello_advanced(name: str, age: int, time: str):
    if time == '12:00':
        return f"Good afternoon {name} with age {age}"
    if time == '10:00':
        return f"Good morning {name} with age {age}"
    if time == '18:00':
        return f"Good evening1 {name} with age {age}"
