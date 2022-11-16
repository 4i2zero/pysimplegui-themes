import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Roboto 14', button_element_size=(6, 3))
    button_size = (6, 3)
    layout = [
        [sg.Text(
            'CLICK HERE',
            font='Franklin 26',
            justification='center',
            expand_x=True,
            pad=(10, 20),
            right_click_menu=theme_menu,
            enable_events=True,
            key='-TEXT-')],
        [sg.Button('Enter', expand_x=True, size=(36, 1))],
        [sg.Spin(themes, expand_x=True, key='-KEY-')],
    ]

    return sg.Window('Calculator', layout, finalize=True)

themes = sg.theme_list()
theme_menu = ['menu', sg.theme_list()]
window = create_window('dark')


current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
        window['-TEXT-'].update(event)
        window['-KEY-'].update(event)

    if event == 'Enter':
        window.close()
        window = create_window(values['-KEY-'])
        window['-TEXT-'].update(values['-KEY-'])
        window['-KEY-'].update(values['-KEY-'])

    if event == '-TEXT-':
        window.close()
        window = create_window('random')

window.close()