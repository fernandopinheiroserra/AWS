import tkinter as tk
import boto3

#pip install boto3

def authAws():
    access_key = access_entry.get()
    secret_key = secret_entry.get()

    try:
        s3_client = boto3.client('s3',
                                 aws_access_key_id=access_key,
                                 aws_secret_access_key=secret_key)
        s3_client.list_buckets()
        status_label.config(text="Authentication successful!", fg="green")
    except Exception as e:
        status_label.config(text="Failed to authenticate: " + str(e), fg="red")

window = tk.Tk()
window.title("AWS S3 Authentication")
window.iconbitmap('main.ico')
window.geometry("640x480")

access_label = tk.Label(window, text="Access Key:")
access_label.pack()
access_entry = tk.Entry(window)
access_entry.pack()

secret_label = tk.Label(window, text="Secret Key:")
secret_label.pack()
secret_entry = tk.Entry(window, show="*")
secret_entry.pack()

authenticate_button = tk.Button(window, text="Authenticate", command=authAws)
authenticate_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()

