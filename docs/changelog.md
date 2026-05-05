# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

## [0.1.0] - 2026-05-05
### Adicionado
- **MVP Funcional**: Interface moderna com `CustomTkinter`.
- **Motor de Tradução**: Migração para `deep-translator` (compatível com Python 3.14).
- **Lógica de Cores**: Destaque por hashing de tokens.
- **Alinhamento 2.0**: Heurística para agrupar artigos e preposições, evitando deslocamento visual.
- **Documentação**: Estrutura completa na pasta `docs/`.

### Corrigido
- Erro de importação do módulo `cgi` (removido no Python 3.13) via migração de biblioteca.
- Crash no `CTkTextbox` ao tentar configurar fontes em tags (restrição do CustomTkinter).
- Tokenização de reticências (`...`) para evitar desalinhamento.
