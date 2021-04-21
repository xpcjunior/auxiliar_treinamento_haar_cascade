from PySimpleGUI import PySimpleGUI as sg
from service import repartidor as service
from model.aux_haar_cascade import AuxHaarCascade
from util import aux_haar_cascade_factory

def construir_view():
    sg.theme('Reddit')
    layout = [
        [
            sg.Text('Scr imagens: ', size=(10, 1)),
            sg.Input(key='inImagens', size=(45, 1)),
            sg.FolderBrowse('Buscar', key='fbSrc', target='inImagens')
        ],
        [
            sg.Text('Dst imagens: ', size=(10, 1)),
            sg.Input(key='inDstImagens', size=(45, 1)),
            sg.FolderBrowse('Buscar', key='fbDst', target='inDstImagens')
        ],
        [
            sg.Text('Tipo de img: ', size=(10, 1)),
            sg.Radio('PNG', "tipo_img", default=True, key='rTipoPNG'),
            sg.Radio('JPG', "tipo_img", default=False, key='rTipoJPG'),
        ],
        [
            sg.Text('Função: ', size=(10, 1)),
            sg.Radio('Crop', "RADIO1", default=False, key='rCrop', change_submits = True, enable_events=True),
            sg.Radio('Retangulos', "RADIO1", default=False, key='rRet', change_submits = True, enable_events=True),
            sg.Radio('Repartidor', "RADIO1", default=False, key='rRep', change_submits = True, enable_events=True),
            sg.Radio('Cinza & Eq', "RADIO1", default=False, key='rCeE', change_submits = True, enable_events=True)
        ],
        [
            sg.Text('', key='lbSrelecione', visible=True, size=(10, 1)),
            sg.Input('', key='inExtra', size=(45, 1), visible=False),
        ],
        [
            sg.Text('Progresso: ', size=(10, 1)),
            sg.ProgressBar(1, orientation='h', size=(20, 20), key='progress')
        ],
        [
            sg.Button('OK', key='btOK', size=(5, 1)),
            sg.Button('Sair', size=(5, 1))
        ]
    ]

    janela = sg.Window('Auxiliar de HAAR Cascade', layout)

    while (True):
        eventos, valores = janela.read()

        if (eventos == sg.WIN_CLOSED):
            break

        if (eventos == 'btOK'):

            try:
                aux_haar_cascade: AuxHaarCascade = aux_haar_cascade_factory.executar(
                    valores['inImagens'],
                    valores['inDstImagens'],
                    valores['rTipoPNG'],
                    valores['rCrop'],
                    valores['rRet'],
                    valores['rRep'],
                    valores['rCeE'], 
                    valores['inExtra'])

                progress_bar = janela.FindElement('progress')

                if (valores['rRep'] == True):
                    for seq, arquivo in enumerate(aux_haar_cascade.lista_imagens):
                        service.cropH(aux_haar_cascade.dst, arquivo, aux_haar_cascade.slice_height, aux_haar_cascade.slice_width)
                        progress_bar.UpdateBar(seq + 1, aux_haar_cascade.total_imgs)
                
                if (valores['rCrop'] == True):
                    for seq, arquivo in enumerate(aux_haar_cascade.lista_imagens):
                        service.crop(aux_haar_cascade.dst, arquivo, aux_haar_cascade.lista_areas)
                        progress_bar.UpdateBar(seq + 1, aux_haar_cascade.total_imgs)

                if (valores['rRet'] == True):
                    for seq, arquivo in enumerate(aux_haar_cascade.lista_imagens):
                        service.desenharetangulo(aux_haar_cascade.dst, arquivo, aux_haar_cascade.lista_areas)
                        progress_bar.UpdateBar(seq + 1, aux_haar_cascade.total_imgs)

                if (valores['rCeE'] == True):
                    for seq, arquivo in enumerate(aux_haar_cascade.lista_imagens):
                        service.acinzentar(aux_haar_cascade.dst, arquivo)
                        progress_bar.UpdateBar(seq + 1, aux_haar_cascade.total_imgs)
                
                
            except Exception as e:
                print(e)
                sg.popup_error('Falha ao executar função', e)
            else:
                teste = sg.popup_yes_no('Procedimento realizado com sucesso!', 'Deseja continuar?')

                if (teste == 'Yes'):
                    progress_bar.UpdateBar(0, 0)
                else:
                    break
        
        if (valores['rCrop'] == True):
            janela.FindElement('lbSrelecione').update('Areas')
            janela.FindElement('inExtra').update(visible=True)
        elif (valores['rRet'] == True):
            janela.FindElement('lbSrelecione').update('Areas')
            janela.FindElement('inExtra').update(visible=True)
        elif (valores['rRep'] == True):
            janela.FindElement('lbSrelecione').update('Dimensões')
            janela.FindElement('inExtra').update(visible=True)
        elif (valores['rCeE'] == True):
            janela.FindElement('lbSrelecione').update('')
            janela.FindElement('inExtra').update(visible=False)