# Conversor de Imagens para WebP (Python)

Este script converte automaticamente todas as imagens de uma pasta para o formato `.webp`, mantendo o tamanho original da imagem e com compressão de qualidade máxima (mínima perda).

---

## ✅ Requisitos

- Python 3.x instalado
- Biblioteca [Pillow](https://python-pillow.org/) instalada

Instale com:

```bash
pip install pillow
```

---

## 📁 Estrutura esperada

Crie a seguinte estrutura de pastas:

```
projeto/
├── converter.py        # Script principal
├── imagens/            # Coloque aqui suas imagens (.jpg, .png, etc.)
└── convertidas_webp/   # Pasta de saída (será criada automaticamente)
```

> ⚠️ **Importante**: você deve criar a pasta `imagens/` e colocar suas imagens dentro dela antes de rodar o script.

---

## ▶️ Como usar

1. Coloque suas imagens na pasta `imagens/`
2. Execute o script:

```bash
python converter.py
```

As imagens convertidas serão salvas automaticamente na pasta `convertidas_webp/`.

---

## 🔧 Ajustes (opcional)

- O script usa `quality=100`, o que garante compressão mínima.  
  Se preferir **sem perda alguma**, edite o script para usar `lossless=True`.

---

## 📄 Licença

Este projeto é livre para uso pessoal ou profissional.