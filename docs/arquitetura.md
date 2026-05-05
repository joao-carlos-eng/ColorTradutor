# Arquitetura do Projeto

O ColorTradutor é um aplicativo desktop moderno construído com Python.

## Estrutura de Pastas

- `/`: Raiz do projeto.
  - `app.py`: Ponto de entrada.
- `src/`: Código fonte.
  - `ui.py`: Interface gráfica (`CustomTkinter`).
  - `engine.py`: Lógica de tradução e alinhamento.
- `docs/`: Documentação técnica.

## Fluxo de Dados

1. O usuário insere o texto no `CTkTextbox`.
2. O `TranslationEngine` envia o texto para a API `deep-translator`.
3. O motor tokeniza o texto original e o traduzido.
4. **Alinhamento Heurístico**: Artigos e preposições são agrupados com substantivos/verbos subsequentes.
5. As cores são aplicadas via `tag_config` no componente de texto rico.

## Decisões Técnicas

- **UI**: Uso de `CustomTkinter` para garantir uma interface Premium nativa.
- **Tradução**: Uso de `deep-translator` para garantir compatibilidade com Python 3.14 (evitando bibliotecas que dependem do módulo removido `cgi`).
- **Tokenização**: Regex nativo para evitar dependências de compilação C++ (como `nltk` exige no Windows com Python 3.14).
