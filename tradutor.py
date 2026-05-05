from transformers import MarianMTModel, MarianTokenizer

class TradutorAvancado:
    def __init__(self):
        # Carregar modelo e tokenizador para tradução inglês-português
        self.model_name = "recogna-nlp/bode-13b-alpaca-por-eng"
        self.model = MarianMTModel.from_pretrained(self.model_name)
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)

    def traduzir_texto(self, texto):
        # Tokenizar e traduzir o texto
        input_ids = self.tokenizer.encode(texto, return_tensors="pt")
        output_ids = self.model.generate(input_ids)
        traducao = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return traducao

if __name__ == "__main__":
    tradutor = TradutorAvancado()

    texto_original = "we have made it"
    resultado_traducao = tradutor.traduzir_texto(texto_original)

    print(f"Texto Original: {texto_original}")
    print(f"Tradução: {resultado_traducao}")
