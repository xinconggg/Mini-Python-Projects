import tkinter

window = tkinter.Tk()
window.title("Miles to KM Coverter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

miles_input = tkinter.Entry(width=7)
miles_input.grid(row=0, column=1)


miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)


is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)


km_result_label = tkinter.Label(text="0")
km_result_label.grid(row=1, column=1)


km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)


calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
