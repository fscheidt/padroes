# from models import Image, JPG, PNG 
from image_factory import (
    create_image, 
    ImageType
)

if __name__ == "__main__":
    ### CLASSE CLIENTE (1 of 50) ###
    # Define em tempo de execução:
    #   (a) caminho do arquivo da imagem origem
    #   (b) formato para exportação 
    image_path = "/tmp/image.jpg"
    export_type = ImageType.PNG
    
    # -------------------------------
    # SEM factory:
    # -------------------------------
    # image.export(image_path)
    # image = PNG(channels=16)
    # image.export(image_path)
    
    # ==============================
    # USANDO Factory:
    # ==============================
    # Cliente desconhece quais são as classes concretas
    # de imagens disponíveis, portanto pede ao factory
    # pela instância delegando a responsabilidade a este.
    # -------------------------------
    image = create_image(export_type)  # <= solicita imagem PNG
    image.export(image_path, rgba=True)
    
    # -------------------------------
    image = create_image(ImageType.JPG) # <= solicita imagem JPG
    image.export("/tmp/profile.gif")  
