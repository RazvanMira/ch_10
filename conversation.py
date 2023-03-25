import time

def alice():
    print("Discussion about Alice started.")
    time.sleep(2)
    bob()
    david()
    print("Discussion about Alice ended.")
    time.sleep(2)
    return None

def bob():
    print("Discussion about Bob started.")
    time.sleep(2)
    carol()
    print("Discussion about Bob ended.")
    time.sleep(2)
    return None

def carol():
    print("Discussion about Carol started.")
    time.sleep(2)
    print("Discussion about Carol ended.")
    time.sleep(2)
    return None

def david():
    print("Discussion about David started.")
    time.sleep(2)
    print("Discussion about David ended.")
    time.sleep(2)
    return None

alice()