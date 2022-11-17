import PySimpleGUI as sg

listaClientes = ['Cliente1', 'Cliente2', 'Cliente3']
listPets = []
listVets = ['Vet1', 'Vet2']
pets1 = ['Cachorro1', 'Gato1']
pets2 = ['Cachorro1', 'Gato1', 'Hamster1']
pets3 = ['Hamster1', 'Coelho1', 'Cachorro1', 'Gato1', 'Gato2']
especies = ['Cachorro','Coelho','Gato', 'Hamster', 'Pássaros']

def janela_inicial():
    sg.theme('LightGray1')
    menu_def = [["Menu", ["Sobre", "Equipe", "Contato"]]]
    layout_inicial = [[sg.MenubarCustom(menu_def, background_color='purple', bar_text_color='purple')],
                        [sg.T('Bem-vindo ao Clinica Veterinária Mi-Au', text_color='purple' ,font='_ 18', justification='c', expand_x=True)],
                        [sg.Image('gato-cachorro2.png')],
                       [sg.Cancel('Sair', button_color='red'), sg.Ok('Logar', button_color='purple')]
                       ]

    return sg.Window('Clinica Veterinária Mi-Au - Inicio', layout=layout_inicial, finalize=True)

def janela_login():
    sg.theme('LightGray1')
    layout_login = [[sg.T('Fazer Login', font=40, text_color='purple')],
                        [sg.Text("Usuario:", text_color='purple'), sg.Input("", k='-LOGIN-')],
                       [sg.Text("Senha:", text_color='purple'), sg.Input("", k='-SENHA-', password_char="*")],
                       [sg.Cancel('Voltar', button_color='gray'), sg.Ok('Logar', button_color='purple')]
                       ]

    return sg.Window('Clinica Veterinária Mi-Au - Login', layout=layout_login, finalize=True)

def janela_secretario():
    sg.theme('LightGray1')
    layout_secretario = [[sg.T('Painel do Secretario - Inicio', font=40, text_color='purple')],
                        [sg.Button('Marcar consulta', button_color='purple'), sg.Button('Consultas agendadas', button_color='purple')],
                        [sg.Button('Voltar', button_color='gray')]]

    return sg.Window('Clinica Veterinária Mi-Au - Painel Secretario', layout=layout_secretario, finalize=True)

def janela_cadastrar():
    sg.theme('LightGray1')
    layout_marcar_consulta = [[sg.T('Painel do Secretario - Cadastrar', font=40, text_color='purple')],
                        [sg.Ok('Cadastrar cliente', button_color='purple'), sg.Ok('Cadastrar pet', button_color='purple')],
                              [sg.Ok('Cadastrar veterinario', button_color='purple'),
                               sg.Ok('Cadastrar especies', button_color='purple')],
                        [sg.Ok('Voltar', button_color='gray')]]

    return sg.Window('Clinica Veterinária Mi-Au - Cadastrar', layout=layout_marcar_consulta, finalize=True)

def cadastro_cliente():
    sg.theme('LightGray1')
    layout_cad_cliente = [[sg.T('Painel do Secretario - Cadastrar cliente', font=40, text_color='purple')],
                        [sg.T('Nome:'), sg.Input()],
                        [sg.T('Endereço:'), sg.Input()],
                          [sg.T('Celular:'), sg.Input()],
                          [sg.T('CPF'), sg.Input()],
                         [sg.Ok('Cancelar', button_color='gray'), sg.Button('Enviar', button_color='purple')]]

    return sg.Window('Clinica Veterinária Mi-Au - Cadastrar cliente', layout=layout_cad_cliente, finalize=True)

def cadastro_vet():
    sg.theme('LightGray1')
    layout_cad_vet = [[sg.T('Painel do Secretario - Cadastrar veterinario', font=40, text_color='purple')],
                        [sg.T('Nome:'), sg.Input()],
                        [sg.T('CFMV:'), sg.Input()],
                        [sg.T('Endereço'), sg.Input()],
                        [sg.T('Celular:'), sg.Input()],
                        [sg.Ok('Cancelar', button_color='gray'), sg.Button('Enviar', button_color='purple')]]

    return sg.Window('Clinica Veterinária Mi-Au - Cadastrar cliente', layout=layout_cad_vet, finalize=True)

def cadastro_pet():
    sg.theme('LightGray1')
    layout_cad_pet = [[sg.T('Painel do Secretario - Cadastrar pet', font=40, text_color='purple')],
                      [sg.T('Cliente'), sg.LB(listaClientes, size=(10, 4), k='-LCLIENTES-', enable_events=True), sg.Button('Adicionar cliente', button_color='purple')],
                        [sg.T('Nome do pet:'), sg.Input()],
                        [sg.T('Especie:'), sg.Input()],
                         [sg.Ok('Cancelar', button_color='gray'), sg.Button('Enviar', button_color='purple')]]

    return sg.Window('Clinica Veterinária Mi-Au - Cadastrar pet', layout=layout_cad_pet, finalize=True)

def cadastro_especies():
    sg.theme('LightGray1')
    layout_cad_especie = [[sg.T('Painel do Secretario - Cadastrar especie', font=40, text_color='purple')],
                      [sg.T('Cliente'), sg.LB(listVets, size=(10, 4), enable_events=True), sg.Button('Adicionar veterinario', button_color='purple')],
                        [sg.T('Especie:'), sg.Input()],
                         [sg.Ok('Cancelar', button_color='gray'), sg.Button('Enviar', button_color='purple')]]

    return sg.Window('Clinica Veterinária Mi-Au - Cadastrar especies', layout=layout_cad_especie, finalize=True)

def janela_marcar_consulta():
    sg.theme('LightGray1')
    layout_marcar_consulta = [[sg.T('Painel do Secretario - Marcar consulta', font=40, text_color='purple')],
                              [sg.T('Cliente'), sg.LB(listaClientes, size=(10, 4), k='-LCLIENTES-', enable_events=True),
                               sg.T('Pet'), sg.LB(listPets, size=(10, 4), k='-LPETS-', enable_events=True),
                               sg.T('Veterinario'), sg.LB(listVets, size=(10, 4), k='-LVETS-', enable_events=True)
                               ],
                              [sg.T('Buscar cliente pelo nome'),
                               sg.Input(size=(25, 1), enable_events=True, key='-FILTER-'),
                               sg.T(size=(15, 1), k='-FILTER NUMBER-')],
                            [sg.Button('Cadastrar', button_color='purple')],
                            [sg.Ok('Cancelar', button_color='gray'), sg.Button('Agendar', button_color='purple')]]

    return sg.Window('Clinica Veterinária Mi-Au - Marcar consulta', layout=layout_marcar_consulta, finalize=True)


def janela_veterinario():
    sg.theme('LightGray1')
    layout_veterinario= [[sg.T('Painel do Veterinario', font=40, text_color='purple')],
                        [sg.Ok('Realizar consulta', button_color='purple'), sg.Button('Consultas agendadas', button_color='purple')],
                         [sg.Cancel('Voltar', button_color='gray')]]

    return sg.Window('Clinica Veterinária Mi-Au - Veterinario', layout=layout_veterinario, finalize=True)

def janela_consulta():
    sg.theme('LightGray1')
    layout_consulta= [[sg.T('Painel do Veterinario - Consulta', font=40, text_color='purple')],
                      [sg.Ok('Informações do Pet', button_color='purple')],
                        [sg.Ok('Marcar exame', button_color='purple')],
                         [sg.Ok('Finalizar consulta', button_color='purple'), sg.Cancel('Voltar', button_color='gray')]]

    return sg.Window('Clinica Veterinária Mi-Au - Veterinario Consulta', layout=layout_consulta, finalize=True)


janela1, janela2, janela3, janela4, janela5, janela6, janela7, janela8, janela9, janela10 \
    = janela_inicial(), None, None, None, None, None, None, None, None, None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    if event == 'Sobre':
        sg.popup('Trabalhando com o compromisso de preservar a vida, contamos com profissionais experientes e qualificados, procurando sempre manter uma estreita relação de confiança e satisfação com nossos clientes e pacientes. !!', text_color='purple', title='Sobre')

    if event == 'Equipe':
        sg.popup('Nossa equipe é formada por veterinarios conceituados, que trabalham sempre com zelo e amor! ', text_color='purple', title='Equipe')

    if event == 'Contato':
        sg.popup('Instagram: @clinicavetMi-Au \n'
                 'WhatsApp: (16)99999-9999 \n'
                 'E-mail: clinicavetmi-au@vet.com \n'
                 'Telefone: (16)3333-3333', text_color='purple', title='Contato')


    if window == janela1 and event == 'Logar':
        janela1.hide()
        janela2 = janela_login()

    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela2.un_hide()

    if window == janela2 and event == 'Logar':
        if values['-LOGIN-'] == 'secretaria' and values['-SENHA-'] == '123':
            janela2.hide()
            janela3 = janela_secretario()
        if values['-LOGIN-'] == 'veterinaria' and values['-SENHA-'] == '123':
            janela2.hide()
            janela3 = janela_veterinario()


    if window == janela3 and event == 'Deslogar':
        janela3.hide()
        janela2.un_hide()

    if window == janela3 and event == 'Realizar consulta':
        janela3.hide()
        janela4 = janela_consulta()

    if window == janela4 and event == 'Finalizar consulta':
        sg.Popup('Consulta finalizada com sucesso!')
        janela4.hide()
        janela3.un_hide()

    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela3.un_hide()

    if event == 'Cadastrar':
        janela5 = janela_cadastrar()
        janela6.hide()

    if window == janela5 and event == 'Voltar':
        janela5.hide()
        janela6.un_hide()

    if window == janela3 and event == 'Marcar consulta':
        janela3.hide()
        janela6 = janela_marcar_consulta()

    new_list = []
    if window == janela6 and event == '-FILTER-':
        new_list = [i for i in listaClientes if values['-FILTER-'].lower() in i.lower()]
        window['-LCLIENTES-'].update(new_list)
        window['-FILTER NUMBER-'].update(f'{len(new_list)} cliente(s)')


    if window == janela6 and event == '-LCLIENTES-':
        if values['-LCLIENTES-'] == ['Cliente1']:
            window['-LPETS-'].update(pets1)
        if values['-LCLIENTES-'] == ['Cliente2']:
            window['-LPETS-'].update(pets2)
        if values['-LCLIENTES-'] == ['Cliente3']:
            window['-LPETS-'].update(pets3)

    if window == janela6 and event == 'Agendar':
        sg.popup('Consulta agendada com sucesso!')
        janela6.hide()
        janela3.un_hide()

    if window == janela6 and event == 'Cancelar':
        janela6.hide()
        janela3.un_hide()
    if window == janela5 and event == 'Cadastrar cliente':
        janela5.hide()
        janela7 = cadastro_cliente()
    if window == janela7 and event == 'Enviar':
        sg.popup('Cliente cadastrado com sucesso!')
        janela7.hide()
        janela5.un_hide()
    if window == janela7 and event == 'Cancelar':
        janela7.hide()
        janela5.un_hide()
    if window == janela5 and event == 'Cadastrar pet':
        janela5.hide()
        janela8 = cadastro_pet()
    if window == janela8 and event == 'Adicionar cliente':
        janela8.hide()
        janela7 = cadastro_cliente()
    if window == janela8 and event == 'Enviar':
        sg.popup('Pet cadastrado com sucesso!')
        janela8.hide()
        janela5.un_hide()
    if window == janela8 and event == 'Cancelar':
        janela8.hide()
        janela5.un_hide()
    if window == janela5 and event == 'Cadastrar veterinario':
        janela5.hide()
        janela9 = cadastro_vet()
    if window == janela5 and event == 'Cadastrar especies':
        janela5.hide()
        janela10 = cadastro_especies()
    if window == janela10 and event == 'Adicionar veterinario':
        janela10.hide()
        janela9 = cadastro_vet()
    if window == janela10 and event == 'Enviar':
        sg.popup('Especie cadastrada com sucesso!')
        janela10.hide()
        janela5.un_hide()
    if window == janela10 and event == 'Cancelar':
        janela10.hide()
        janela5.un_hide()
    if window == janela9 and event == 'Enviar':
        sg.popup('Veterinario cadastrado com sucesso!')
        janela9.hide()
        janela5.un_hide()
    if window == janela9 and event == 'Cancelar':
        janela9.hide()
        janela5.un_hide()
