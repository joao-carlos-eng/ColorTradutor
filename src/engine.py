import hashlib
from deep_translator import GoogleTranslator
import re

class TranslationEngine:
    def __init__(self):
        # deep-translator é mais moderno e compatível com Python 3.13+
        self.translator = GoogleTranslator(source='en', target='pt')
        self.color_map = {}

    def get_token_color(self, token):
        """Gera uma cor única e estável para um token."""
        clean_token = re.sub(r'[^\w]', '', token.lower().strip())
        if not clean_token: return "#888888"
        
        if clean_token not in self.color_map:
            hash_obj = hashlib.md5(clean_token.encode())
            hex_color = hash_obj.hexdigest()[:6]
            self.color_map[clean_token] = f"#{hex_color}"
        return self.color_map[clean_token]

    def translate(self, text):
        """Traduz o texto usando deep-translator e alinha tokens."""
        if not text.strip():
            return []

        try:
            # Tradução via Google (Deep Translator)
            translated_text = self.translator.translate(text)
        except Exception as e:
            print(f"Erro na tradução: {e}")
            return [{"src": text, "tgt": "Erro na tradução", "color": "#ff0000"}]

        # Tokenização melhorada: captura '...' como um único token e separa pontuação
        src_tokens = re.findall(r"[\w']+|\.\.\.|[.,!?;]", text)
        tgt_tokens = re.findall(r"[\w']+|\.\.\.|[.,!?;]", translated_text)
        
        alignment = []
        
        # Heurística de Alinhamento MVP 2.0: 
        # Tenta alinhar palavras baseando-se na ordem, mas permite agrupar
        # artigos e preposições curtas em português (o, a, em, de...)
        
        j = 0
        for i in range(len(src_tokens)):
            s_word = src_tokens[i]
            t_word = ""
            
            if j < len(tgt_tokens):
                # Se a palavra atual no alvo for um artigo/preposição curta e não bater com a original
                # tentamos agrupar com a próxima para manter o alinhamento substantivo
                skip_list = ['o', 'a', 'os', 'as', 'em', 'de', 'do', 'da', 'um', 'uma', 'no', 'na']
                if tgt_tokens[j].lower() in skip_list and i < len(src_tokens) and j < len(tgt_tokens) - 1:
                    # Agrupa o artigo com a próxima palavra
                    t_word = tgt_tokens[j]
                    j += 1
                    t_word += " " + tgt_tokens[j]
                else:
                    t_word = tgt_tokens[j]
                
                j += 1
            
            color = self.get_token_color(s_word)
            
            alignment.append({
                "src": s_word,
                "tgt": t_word if t_word else "---",
                "color": color
            })
            
        # Adicionar sobras do target se houver
        while j < len(tgt_tokens):
            alignment.append({
                "src": "",
                "tgt": tgt_tokens[j],
                "color": "#888888"
            })
            j += 1
            
        return alignment
