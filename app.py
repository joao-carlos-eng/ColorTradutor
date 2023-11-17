from tkinter import Tk, Text, Button, Label
from googletrans import Translator
from tkhtmlview import HTMLLabel


class TradutorGUI:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Tradutor com Legendas Coloridas")

        self.texto_original_label = Label(janela, text="Texto Original:")
        self.texto_original_label.grid(row=0, column=0, padx=10, pady=10)

        self.texto_original = Text(janela, height=5, width=40, wrap='word')
        self.texto_original.grid(row=0, column=1, padx=10, pady=10)

        self.botao_traduzir = Button(janela, text="Traduzir", command=self.traduzir_texto)
        self.botao_traduzir.grid(row=1, column=0, columnspan=2, pady=10)

        self.legendas_label = Label(janela, text="Legendas:")
        self.legendas_label.grid(row=2, column=0, padx=10, pady=10)

        self.legendas = HTMLLabel(janela, html="")
        self.legendas.grid(row=2, column=1, padx=10, pady=10)

    def traduzir_texto(self):
        texto = self.texto_original.get("1.0", "end-1c")
        tradutor = Translator()
        resultado_traducao = tradutor.translate(texto, dest='pt')
        palavras_coloridas = self.destacar_palavras(texto, resultado_traducao.text)

        self.legendas.set_html(palavras_coloridas)

    def destacar_palavras(self, original, traducao):
        palavras_original = original.split()
        palavras_traducao = traducao.split()
        print(palavras_original)
        print(palavras_traducao)
        palavras_coloridas = ""
        for palavra_original, palavra_traducao in zip(palavras_original, palavras_traducao):
            cor = f'#{hash(palavra_original) % 0xFFFFFF:06x}'
            palavras_coloridas += f'<span style="color:{cor}; display:inline-block; margin-right:5px;">{palavra_original}</span>'
            palavras_coloridas += f'<span style="color:{cor}; display:inline-block; margin-right:5px;">({palavra_traducao})</span>'

        return palavras_coloridas


if __name__ == "__main__":
    root = Tk()
    app = TradutorGUI(root)
    root.mainloop()
