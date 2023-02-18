import tkinter as tk
import requests

class ChatGPTGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("ChatGPT Proxy V1")
        self.geometry("400x300")
        
        label = tk.Label(self, text="Welcome to ChatGPT Proxy V1", font=("TkDefaultFont", 14))
        label.pack(pady=10)
        
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)
        input_label = tk.Label(input_frame, text="Enter your query:", font=("TkDefaultFont", 10))
        input_label.pack(side="left")
        self.input_text = tk.Text(input_frame, height=2, width=50)
        self.input_text.pack(side="left")
        
        submit_button = tk.Button(self, text="Submit", command=self.submit)
        submit_button.pack(pady=10)
        
        output_frame = tk.Frame(self)
        output_frame.pack(pady=10)
        output_label = tk.Label(output_frame, text="Response:", font=("TkDefaultFont", 10))
        output_label.pack(side="left")
        self.output_text = tk.Text(output_frame, height=10, width=50)
        self.output_text.pack(side="left")
    
    def submit(self):
        input_query = self.input_text.get("1.0", "end").strip()
        response = self.get_response_from_chatgpt(input_query)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", response)
    
    def get_response_from_chatgpt(self, input_query):
        # Replace "API_ENDPOINT" with the actual endpoint of the ChatGPT API
        headers = {'Content-Type': 'application/json'}
        response = requests.post("API_ENDPOINT", headers=headers, json={"prompt": input_query})
        response_json = response.json()
        return response_json["response"]

if __name__ == "__main__":
    app = ChatGPTGUI()
    app.mainloop()
