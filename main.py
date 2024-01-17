def hello():
    with open('./hello-world.txt', 'a') as file:
        file.write('Hello, Compute Canada!')
        file.close()
        
if __name__ == "__main__":
    hello()