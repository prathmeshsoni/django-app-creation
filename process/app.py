from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Variable, messagebox
import threading
from .run_all import call_process

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("img/")

main_list = []


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def generate_project():
    messagebox.showinfo("Please Wait", "Project is Generating.....!")


def GENERATE():
    generate_btn.configure(state="disabled")

    project_input = project_name.get()
    app_input = app_name.get()
    login_input = login_name.get()
    register_input = register_name.get()
    logout_input = logout_name.get()
    profile_input = profile_name.get()
    client_ip_input = client_ip_name.get()
    if app_input:
        last_name = app_input.split(',')[0].strip().replace(' ', '_').replace('-', '_').replace('.', '_')
    else:
        last_name = 'User'

    global main_list
    main_list = {
        "project_name": project_input,
        "app_name": app_input,
        "login": login_input,
        "register": register_input,
        "logout": logout_input,
        "profile": profile_input,
        "client_ip": client_ip_input,
        "last_name": last_name,
    }

    if not project_input:
        messagebox.showerror("Error", "Project Name is required")
        generate_btn.configure(state="normal")
        return False

    project_thread = threading.Thread(target=generate_project)
    project_thread.start()

    generate_btn.configure(state="normal")
    return True


def submit_btn(option):
    if option == "settings":
        messagebox.showinfo("Settings", "Version : 1.0.0\nWords per Minute : 200")
    elif option == "generate":
        try:
            if GENERATE():
                global main_list
                call_process(main_list)
                messagebox.showinfo("Project Generation", "Project Generated Successfully")
                window.destroy()

                check = 1
            else:
                check = 1
        finally:
            pass

        if check != 1:
            messagebox.showinfo("Error", "Something went wrong")
            generate_button_image.configure(file=relative_to_assets("create.png"))
            generate_btn.configure(state="normal")


def login_on():
    login_img.configure(file=relative_to_assets("toggle_btn_on.png"))
    login_btn.configure(command=login_off)
    login_name.set(value="True")


def login_off():
    login_img.configure(file=relative_to_assets("toggle_btn_off.png"))
    login_btn.configure(command=login_on)
    login_name.set(value="False")


def register_on():
    register_img.configure(file=relative_to_assets("toggle_btn_on.png"))
    register_btn.configure(command=register_off)
    register_name.set(value="True")


def register_off():
    register_img.configure(file=relative_to_assets("toggle_btn_off.png"))
    register_btn.configure(command=register_on)
    register_name.set(value="False")


def logout_on():
    logout_img.configure(file=relative_to_assets("toggle_btn_on.png"))
    logout_btn.configure(command=logout_off)
    logout_name.set(value="True")


def logout_off():
    logout_img.configure(file=relative_to_assets("toggle_btn_off.png"))
    logout_btn.configure(command=logout_on)
    logout_name.set(value="False")


def profile_on():
    profile_img.configure(file=relative_to_assets("toggle_btn_on.png"))
    profile_btn.configure(command=profile_off)
    profile_name.set(value="True")


def profile_off():
    profile_img.configure(file=relative_to_assets("toggle_btn_off.png"))
    profile_btn.configure(command=profile_on)
    profile_name.set(value="False")


def client_ip_on():
    client_ip_img.configure(file=relative_to_assets("toggle_btn_on.png"))
    client_ip_btn.configure(command=client_ip_off)
    client_ip_name.set(value="True")


def client_ip_off():
    client_ip_img.configure(file=relative_to_assets("toggle_btn_off.png"))
    client_ip_btn.configure(command=client_ip_on)
    client_ip_name.set(value="False")


window = Tk()
window.title("Django Project Generator")
window.geometry("450x600")
window.configure(bg="#202020")

canvas = Canvas(
    window,
    bg="#202020",
    width=450,
    height=600,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# Logo Image
logo = PhotoImage(file=relative_to_assets("logo.png"))
logo_image = canvas.create_image(
    225.0,
    37.0,
    image=logo
)

# Settings Button
setting_image = PhotoImage(file=relative_to_assets("setting.png"))
setting_btn = Button(
    image=setting_image,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#202020",
    command=lambda: submit_btn("settings"),
    relief="flat",
    cursor="hand2"
)
setting_btn.place(
    x=400.0,
    y=22.0,
    width=30.0,
    height=30.0
)

# Project Name Input
canvas.create_text(
    20.0,
    96.0,
    anchor="nw",
    text="Project Name",
    fill="#FFFFFF",
    font=("Roboto Medium", 15 * -1)
)
canvas.create_text(
    112.0,
    96.0,
    anchor="nw",
    text="*",
    fill="red",
    font=("Roboto Medium", 15 * -1)
)
project_name_image = PhotoImage(file=relative_to_assets("input_text.png"))
name_image = canvas.create_image(
    224.5,
    137.5,
    image=project_name_image
)
project_name = Entry(
    bd=0,
    bg="#2D2D2D",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Roboto Medium", 14 * -1)
)
project_name.place(
    x=37.0,
    y=123.0,
    width=346.0,
    height=30.0
)

# App Name Input
canvas.create_text(
    20.0,
    169.0,
    anchor="nw",
    text="App Name",
    fill="#FFFFFF",
    font=("Roboto Medium", 14 * -1)
)
project_app_image = PhotoImage(file=relative_to_assets("input_text.png"))
app_image = canvas.create_image(
    224.5,
    210.5,
    image=project_app_image
)
app_name = Entry(
    bd=0,
    bg="#2D2D2D",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Roboto Medium", 14 * -1),
)
app_name.place(
    x=37.0,
    y=195.0,
    width=346.0,
    height=30.0
)

# Include Intro Toggle Button
canvas.create_text(
    160.0,
    250.0,
    anchor="nw",
    text="FUNCTIONS",
    fill="#FFFFFF",
    font=("Roboto Regular", 20 * -1)
)
canvas.create_text(
    0.0,
    265.0,
    anchor="nw",
    text="_________________________________________",
    fill="#FFFFFF",
    font=("Roboto Regular", 20 * -1)
)

# Login Toggle Button
login_name = Variable(value="False")

login_img = PhotoImage(file=relative_to_assets("toggle_btn_off.png"))
login_btn = Button(
    image=login_img,
    activebackground="#202020",
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=login_on,
    cursor="hand2"
)
login_btn.place(
    x=27.0,
    y=310.0
)
canvas.create_text(
    80.0,
    313.0,
    anchor="nw",
    text="Login Page",
    fill="#FFFFFF",
    font=("Roboto Regular", 14 * -1)
)

# Register Toggle Button
register_name = Variable(value="False")

register_img = PhotoImage(file=relative_to_assets("toggle_btn_off.png"))
register_btn = Button(
    image=register_img,
    activebackground="#202020",
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=register_on,
    cursor="hand2"
)
register_btn.place(
    x=200.0,
    y=310.0
)
canvas.create_text(
    253.0,
    313.0,
    anchor="nw",
    text="Register Page",
    fill="#FFFFFF",
    font=("Roboto Regular", 14 * -1)
)

# Logout Toggle Button
logout_name = Variable(value="False")

logout_img = PhotoImage(file=relative_to_assets("toggle_btn_off.png"))
logout_btn = Button(
    image=logout_img,
    activebackground="#202020",
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=logout_on,
    cursor="hand2"
)
logout_btn.place(
    x=27.0,
    y=350.0
)
canvas.create_text(
    80.0,
    353.0,
    anchor="nw",
    text="Logout",
    fill="#FFFFFF",
    font=("Roboto Regular", 14 * -1)
)

# Profile Toggle Button
profile_name = Variable(value="False")

profile_img = PhotoImage(file=relative_to_assets("toggle_btn_off.png"))
profile_btn = Button(
    image=profile_img,
    activebackground="#202020",
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=profile_on,
    cursor="hand2"
)
profile_btn.place(
    x=200.0,
    y=350.0
)
canvas.create_text(
    253.0,
    353.0,
    anchor="nw",
    text="Profile",
    fill="#FFFFFF",
    font=("Roboto Regular", 14 * -1)
)

# Client Ip Toggle Button
client_ip_name = Variable(value="False")

client_ip_img = PhotoImage(file=relative_to_assets("toggle_btn_off.png"))
client_ip_btn = Button(
    image=client_ip_img,
    activebackground="#202020",
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=client_ip_on,
    cursor="hand2"
)
client_ip_btn.place(
    x=27.0,
    y=390.0
)
canvas.create_text(
    80.0,
    393.0,
    anchor="nw",
    text="Client Ip",
    fill="#FFFFFF",
    font=("Roboto Regular", 14 * -1)
)

# Create Project Button
generate_button_image = PhotoImage(
    file=relative_to_assets("create.png"))

generate_btn = Button(
    image=generate_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: submit_btn("generate"),
    activebackground="#202020",
    relief="flat"
)
generate_btn.place(
    x=18.0,
    y=532.0,
    width=414.0,
    height=47.0
)

window.resizable(False, False)
window.mainloop()
