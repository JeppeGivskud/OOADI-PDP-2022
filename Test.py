import pickle
from User import*
from Client import*


if __name__ == "__main__":
    GUI =  Client()
    GUI.connect()
    filename = "TwoTestCostumers.txt"
    with open(filename, "rb") as pickle_file:       # Open the file to read from
        GUI.send(pickle.load(pickle_file))
        GUI.disconnect()
        User1 = pickle.load(pickle_file)             # Load first object
        #User2 = pickle.load(pickle_file)  # Load first object


    print(User1.get_user_name())
