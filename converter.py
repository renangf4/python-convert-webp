import os
from PIL import Image

# Caminho da pasta com as imagens
input_dir = "imagens"
output_dir = "convertidas_webp"

# Cria a pasta de saída, se não existir
os.makedirs(output_dir, exist_ok=True)

# Extensões que vamos considerar
extensoes_validas = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

# Loop pelos arquivos da pasta
for nome_arquivo in os.listdir(input_dir):
    if nome_arquivo.lower().endswith(extensoes_validas):
        caminho_entrada = os.path.join(input_dir, nome_arquivo)
        nome_base = os.path.splitext(nome_arquivo)[0]
        caminho_saida = os.path.join(output_dir, f"{nome_base}.webp")

        try:
            with Image.open(caminho_entrada) as img:
                img.save(caminho_saida, format="WEBP", quality=100)
                print(f"Convertido: {nome_arquivo} → {nome_base}.webp")
        except Exception as e:
            print(f"Erro ao converter {nome_arquivo}: {e}")
