import customtkinter as ctk
from .engine import TranslationEngine
import threading

class ColorTradutorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ColorTradutor MVP")
        self.geometry("900x650")
        
        # Configuração de Tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Engine
        self.engine = None
        
        self.setup_ui()
        
        # Carregar engine em background
        threading.Thread(target=self.init_engine, daemon=True).start()

    def init_engine(self):
        self.update_status("Inicializando Tradutor...")
        self.engine = TranslationEngine()
        self.update_status("Pronto para traduzir.")
        self.btn_traduzir.configure(state="normal")

    def setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        
        self.header = ctk.CTkLabel(self.header_frame, text="ColorTradutor", font=ctk.CTkFont(size=28, weight="bold"))
        self.header.pack(side="left")

        self.status_label = ctk.CTkLabel(self.header_frame, text="Inicializando...", font=ctk.CTkFont(size=12))
        self.status_label.pack(side="right")

        # Main Container
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=2)

        # Entrada de Texto
        self.txt_input = ctk.CTkTextbox(self.main_frame, height=150, font=ctk.CTkFont(size=15))
        self.txt_input.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        self.txt_input.insert("0.0", "Enter English text here...")

        # Botão Traduzir
        self.btn_traduzir = ctk.CTkButton(self.main_frame, text="Traduzir com Cores", 
                                         font=ctk.CTkFont(size=16, weight="bold"),
                                         height=45,
                                         command=self.on_traduzir, state="disabled")
        self.btn_traduzir.grid(row=1, column=0, padx=15, pady=5)

        # Resultado (Rich Text via Textbox para evitar problemas com Pillow/HTML)
        self.txt_result = ctk.CTkTextbox(self.main_frame, font=ctk.CTkFont(size=16), state="disabled")
        self.txt_result.grid(row=2, column=0, padx=15, pady=15, sticky="nsew")

    def update_status(self, text):
        self.status_label.configure(text=text)

    def on_traduzir(self):
        text = self.txt_input.get("1.0", "end-1c")
        if not text.strip():
            return

        self.btn_traduzir.configure(state="disabled", text="Traduzindo...")
        self.txt_result.configure(state="normal")
        self.txt_result.delete("1.0", "end")
        self.txt_result.insert("end", "Traduzindo...\n")
        self.txt_result.configure(state="disabled")
        
        threading.Thread(target=self.run_translation, args=(text,), daemon=True).start()

    def run_translation(self, text):
        try:
            alignment = self.engine.translate(text)
            self.after(0, lambda: self.show_result_rich(alignment))
        except Exception as e:
            self.after(0, lambda: self.update_status(f"Erro: {e}"))
            self.after(0, lambda: self.btn_traduzir.configure(state="normal", text="Traduzir com Cores"))

    def show_result_rich(self, alignment):
        self.txt_result.configure(state="normal")
        self.txt_result.delete("1.0", "end")
        
        for item in alignment:
            color = item['color']
            src = item['src']
            tgt = item['tgt']
            
            if not src and not tgt: continue
            
            # Criar tag de cor se não existir
            tag_name = f"tag_{color.replace('#', '')}"
            self.txt_result.tag_config(tag_name, foreground=color)
            
            # Inserir Original
            self.txt_result.insert("end", f"{src} ", tag_name)
            # Inserir Tradução em subscrito ou menor
            self.txt_result.insert("end", f"({tgt})  ", "small_gray")
        
        self.txt_result.tag_config("small_gray", foreground="#888888")
        self.txt_result.configure(state="disabled")
        self.btn_traduzir.configure(state="normal", text="Traduzir com Cores")
        self.update_status("Tradução concluída.")

if __name__ == "__main__":
    app = ColorTradutorApp()
    app.mainloop()
