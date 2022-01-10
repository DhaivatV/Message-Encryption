import base64
import pandas as pd
import tkinter as tk

data = pd.read_csv('data.csv')

lst = data['Encrypted_Msg'].tolist()
key_lst = data['Key'].tolist()
for items in key_lst:
    print(type(items))


def decode_msg():
    enc_msg = e1.get()

    if enc_msg in lst:
        key = int(e2.get())

    else:
        decoded_msg = "Message does not exist"
        return decoded_msg

    if key in key_lst:
        enc_msg_bytes = enc_msg.encode("ascii")
        msg_decode_bytes = base64.b64decode(enc_msg_bytes)
        decoded_msg = msg_decode_bytes.decode("ascii")
        return decoded_msg

    else:
        decoded_msg = "Wrong Key Entered"
        return decoded_msg


def show_msg():
    master = tk.Tk()
    Message = decode_msg()
    tk.Message(master, text=f"Message : {Message}").grid(row=2, column=1)
    tk.Button(master,
              text='Quit',
              command=master.quit).grid(row=3,
                                        column=1,
                                        sticky=tk.W,
                                        pady=4)


master = tk.Tk()
tk.Label(master,
         text="Encrypted Message").grid(row=0)

tk.Label(master,
         text="Key").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)

e2.grid(row=1, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Decode', command=show_msg).grid(row=3,
                                                column=1,
                                                sticky=tk.W,
                                                pady=4)

tk.mainloop()

print(lst)
