import requests

host="http://localhost:5000"
prefix="/api/v1"

def lista():
    result=requests.get(host+prefix+"/tasks").json()
    for task in result:
        print(task[1])
    print("")

def lista_singolo(id):
    result=requests.get(host+prefix+"/tasks"+"/"+str(id)).json()
    print(result[0][1])
    print("")

if __name__ == '__main__':

    lista()

    new=["Pippo Baudo",0]
    requests.post(host+prefix+"/tasks", json=new)

    lista()

    lista_singolo(10)

    upd = ["Andrea Bocelli", 1]
    requests.put(host + prefix + "/tasks"+"/4", json=upd)

    lista()

    requests.delete(host + prefix + "/tasks" + "/27")

    lista()