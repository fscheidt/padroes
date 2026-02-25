# SEM FACTORY:
# Exige que o cliente conheca as classes concretas de imagens
# from models import Image, JPG, PNG 

from image_factory import createImage, ImageFormat

if __name__ == "__main__":
    # ---------------------------------------
    # CLIENTE
    # Define em tempo de execução:
    #   (a) caminho do arquivo da imagem origem
    #   (b) formato para exportação

    image_path = "/tmp/image.jpg"
    image_format = ImageFormat.JPG
    
    # ---------------------------------------
    # (1) SEM FACTORY 
    # ---------------------------------------
    """
    if image_format == "jpg":
        image = JPG(image_path) 
    if image_format == "png":
        image = PNG(image_path) 
    image.export()
    """
    # ---------------------------------------
    # (2) USANDO FACTORY
    # ---------------------------------------
    # cliente desconhece quais são as Classes Concretas
    # de imagens disponíveis, portanto Pede ao factory
    # pela instância delegando a responsabilidade a este.
    image = createImage(image_format, image_path) # JPG
    image.export()

    image = createImage(ImageFormat.PNG, image_path) # PNG
    image.export()

    