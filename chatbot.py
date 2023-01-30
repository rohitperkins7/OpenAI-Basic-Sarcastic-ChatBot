import tkinter as tk
import openai

# Setting the OpenAI API Key
openai.api_key = "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"
def on_submit(event=None):
    user_input = input_field.get()
    output_field.config(state='normal')
    output_field.config(wrap='word')
    output_field.insert('end','User: ' + user_input + '\n', 'red')

    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = "Give sarcastic reply to" + user_input + "this question",
        temperature = 0,
        max_tokens = 3000,
        top_p = 1,
        frequency_penalty = 0.5,
        presence_penalty = 0
    )

    response_text = response['choices'][0]['text'].replace("\n","")
    output_field.insert('end','AI : ' + response_text + '\n' ,)
    input_field.delete(0,'end')
    output_field.config(state="disabled")

root = tk.Tk()
root.title("Chatbot")

output_frame = tk.Frame(root)
output_frame.pack(side='top',fill='both',expand=True)

output_label = tk.Label(output_frame,text="Chatbot : ")
output_label.pack(side='left',padx=5,pady=5)

output_field = tk.Text(output_frame)
output_field.pack(side='left',fill='both',expand=True,padx=5,pady=5)
output_field.config(state="disabled")
output_field.tag_config('blue',foreground='blue')
output_field.tag_config('red',foreground='red')
output_field.config(font=('Futura',16))

input_frame = tk.Frame(root)
input_frame.pack(side='bottom',fill='x')

input_label = tk.Label(input_frame,text='User : ')
input_frame.pack(side='left',padx=5,pady=5)

input_field = tk.Entry(input_frame,width=150)
input_field.pack(side='left',padx=5,pady=5)
input_field.bind("<Return>",on_submit)

submit_button = tk.Button(input_frame,text="Submit",command=on_submit)
submit_button.pack(side='left')

root.mainloop()
