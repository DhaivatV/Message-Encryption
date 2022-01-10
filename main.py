import tkinter as tk
import base64
import random
import pandas as pd
from csv import DictWriter


def encrypt_msg():
    message = str(e1.get())
    message_bytes = message.encode("ascii")
    key = int((random.random()) * 10000000000)
    encryptedmsg = base64.b64encode(message_bytes)
    encrypted_msg = encryptedmsg.decode("ascii")

    field_names = ['Message', 'Key']
    Sec_dict = {'Message':encrypted_msg, 'Key':key}



    try:
        with open('/home/spartan07/Desktop/Projects/Ten_Task_4/data.csv') as f:
            f.close()
    except IOError:
        df = pd.DataFrame(list())
        df.to_csv("data.csv")

    with open('data.csv', 'a') as f:
        dictwriter_object = DictWriter(f, fieldnames= field_names)
        dictwriter_object.writerow(Sec_dict)
        f.close()

    return  key, encrypted_msg


def show_key():
    master = tk.Tk()
    ke_y , enc = encrypt_msg()
    tk.Message(master, text=f"Key : {ke_y} \n Message: {enc}").grid(row=2, column=1)
    tk.Button(master,
              text='Quit',
              command=master.quit).grid(row=3,
                                        column=1,
                                        sticky=tk.W,
                                        pady=4)

master = tk.Tk()
tk.Label(master,
         text="Message").grid(row=0)


e1 = tk.Entry(master)


e1.grid(row=0, column=1)


tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='submit', command=show_key).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)


tk.mainloop()