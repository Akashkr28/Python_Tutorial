chai_type = "plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irani"
    kitchen()

front_desk()
print("Final chai type:", chai_type)