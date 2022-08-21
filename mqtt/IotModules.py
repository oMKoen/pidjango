
def IotModulesCheck(tag):
    if tag.find("ESP", 0, 7) >= 0:
        print(f"valid module: {tag}")
        return True
    else:
        print(f"invalid module: {tag}")
        return False
