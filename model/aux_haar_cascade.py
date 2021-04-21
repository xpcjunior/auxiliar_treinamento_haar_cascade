class AuxHaarCascade():

    def __init__(self) -> None:
        self.__scr = ''
        self.__dst = ''
        self.__extensao_imagens = ''
        self.__lista_imagens = []
        self.__total_imgs = 0
        self.__slice_height = 0
        self.__slice_width = 0
        self.__lista_areas = []

    
    @property
    def scr(self):
        return self.__scr
    
    @scr.setter
    def scr(self, scr: str):
        self.__scr = scr

    @property
    def dst(self):
        return self.__dst
    
    @dst.setter
    def dst(self, dst):
        self.__dst = dst
    
    @property
    def extensao_imagens(self):
        return self.__extensao_imagens
    
    @extensao_imagens.setter
    def extensao_imagens(self, extensao_imagens):
        self.__extensao_imagens = extensao_imagens

    @property
    def lista_imagens(self):
        return self.__lista_imagens
    
    @lista_imagens.setter
    def lista_imagens(self, lista_imagens):
        self.__lista_imagens = lista_imagens
        self.__total_imgs = len(self.__lista_imagens)
    
    @property
    def total_imgs(self):
        return self.__total_imgs
    
    @property
    def slice_height(self):
        return self.__slice_height
    
    @slice_height.setter
    def slice_height(self, slice_height):
        self.__slice_height = slice_height
    
    @property
    def slice_width(self):
        return self.__slice_width
    
    @slice_width.setter
    def slice_width(self, slice_width):
        self.__slice_width = slice_width

    @property
    def lista_areas(self):
        return self.__lista_areas