from model.aux_haar_cascade import AuxHaarCascade
import glob
import os

def executar(src, dst, extensao_png: bool, is_crop, is_ret, is_rep, is_cee, extra) -> AuxHaarCascade:
    aux_haar_cascade: AuxHaarCascade = AuxHaarCascade()

    if ((not is_crop) and (not is_ret) and (not is_rep) and (not is_cee)):
        raise Exception('Selecione uma função')

    if (type(src) == str):
        if(os.path.exists(src)):
            aux_haar_cascade.scr = src
        else:
            raise Exception(f'Não foi possivel encontrar a pasta {src}')
    else:
        raise Exception('O caminho src deve ser uma String')

    if (type(dst) == str):
        if(os.path.exists(dst)):
            aux_haar_cascade.dst = dst
        else:
            raise Exception(f'Não foi possivel encontrar a pasta {dst}')
    else:
        raise Exception('O caminho dst deve ser uma String')
    
    aux_haar_cascade.extensao_imagens = 'png' if extensao_png else 'jpg'

    aux_haar_cascade.lista_imagens = glob.glob(f'{src}/*.{aux_haar_cascade.extensao_imagens}')


    if (is_rep):
        dimensoes_array = extra.split("x")

        try:
            aux_haar_cascade.slice_height = int(dimensoes_array[0])
            aux_haar_cascade.slice_width = int(dimensoes_array[1])
        except (ValueError, Exception) as verr:
            raise Exception(f'Por favor utilize o formato AlturaxLargura para definir a dimensão')

    if (is_crop or is_ret):

        try:
            lista_tuplas_array = extra.split("/")
            tuplas_array = []
            areas = []
            for i, tupla in enumerate(lista_tuplas_array):
                tuplas_array = tupla.split(", ")
                aux_haar_cascade.lista_areas.append((int(tuplas_array[0]), int(tuplas_array[1]), int(tuplas_array[2]), int(tuplas_array[3])))

            print(aux_haar_cascade.lista_areas)
        except Exception as e:
            print(e)
            raise Exception(f'Por favor utilize o formato x, y, x, y/x, y, x, y.... para definir as áreas')
    
    return aux_haar_cascade
