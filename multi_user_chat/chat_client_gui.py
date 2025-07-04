import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("TCP Chat Client")

        # Username prompt
        self.username = simpledialog.askstring("Username", "Enter your name", parent=master)
        if not self.username:
            messagebox.showerror("Error", "Username required")
            master.quit()
            return

        # Chat area
        self.text_area = scrolledtext.ScrolledText(master, state='disabled', width=50, height=20)
        self.text_area.pack(padx=10, pady=5)

        # Entry field
        self.entry_msg = tk.Entry(master, width=40)
        self.entry_msg.pack(side=tk.LEFT, padx=(10, 5), pady=5)
        self.entry_msg.bind("<Return>", self.send_message)

        # Send button
        self.send_btn = tk.Button(master, text="Send", command=self.send_message)
        self.send_btn.pack(side=tk.LEFT, padx=(0, 10), pady=5)

        # Connect to server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(('127.0.0.1', 5000))
            self.client_socket.send(self.username.encode())
        except Exception as e:
            messagebox.showerror("Connection Error", str(e))
            master.quit()
            return

        # Start receiving thread
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self, event=None):
        msg = self.entry_msg.get()
        if msg:
            try:
                self.client_socket.send(msg.encode())
                self.entry_msg.delete(0, tk.END)
            except:
                messagebox.showerror("Send Error", "Failed to send message")
                self.master.quit()

    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode()
                self.text_area.config(state='normal')
                self.text_area.insert(tk.END, msg + "\n")
                self.text_area.config(state='disabled')
                self.text_area.see(tk.END)
            except:
                break

    def on_closing(self):
        try:
            self.client_socket.close()
        except:
            pass
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.protocol("WM_DELETE_WINDOW", client.on_closing)
    root.mainloop()
