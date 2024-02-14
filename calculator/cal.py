from tkinter import *


calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")



root = Tk()
root.title("Simple Calculator")
root.geometry("309x315+400+150")
root.resizable(False, False)
root.configure(bg="#17161b")


text_result = Text(root, height=2, width=17, font=("Arial",24))
text_result.grid(columnspan=5)


btn_1 = Button(root, text="1", command=lambda: add_to_calculation(1), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=10, y=225)
btn_2 = Button(root, text="2", command=lambda: add_to_calculation(2), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=85, y=225)
btn_3 = Button(root, text="3", command=lambda: add_to_calculation(3), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=160, y=225)
btn_4 = Button(root, text="4", command=lambda: add_to_calculation(4), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=10, y=180)
btn_5 = Button(root, text="5", command=lambda: add_to_calculation(5), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=85, y=180)
btn_6 = Button(root, text="6", command=lambda: add_to_calculation(6), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=160, y=180)
btn_7 = Button(root, text="7", command=lambda: add_to_calculation(7), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=10, y=135)
btn_8 = Button(root, text="8", command=lambda: add_to_calculation(8), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=85, y=135)
btn_9 = Button(root, text="9", command=lambda: add_to_calculation(9), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=160, y=135)
btn_0 = Button(root, text="0", command=lambda: add_to_calculation(0), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=85, y=265)

btn_add = Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=237, y=90)
btn_sub = Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=237, y=135)
btn_mul = Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=237, y=180)
btn_div = Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=237, y=225)
btn_op = Button(root, text="(", command=lambda: add_to_calculation("("), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=85, y=90)
btn_cp = Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=160, y=90)
btn_pt = Button(root, text=".", command=lambda: add_to_calculation("."), width=5, height=1, bd=1, fg="#fff", bg="#212d36", font=("Arial",14)).place(x=10, y=265)
btn_c = Button(root, text="C", command=clear_field, width=5, height=1, bd=1, fg="#fff", bg="#3697f5", font=("Arial",14)).place(x=10, y=90)
btn_eq = Button(root, text="=", command=evaluate_calculation, width=12, height=1, bd=1, fg="#fff", bg="#fe9037", font=("Arial",14)).place(x=160, y=265)



root.mainloop()