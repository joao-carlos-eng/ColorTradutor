# Decisões Arquiteturais (ADR)

Este arquivo registra as decisões técnicas significativas tomadas no projeto.

## ADR 1: Uso do Poetry para Gestão de Dependências

- **Contexto**: O projeto depende de pacotes complexos como `torch` e `transformers`.
- **Decisão**: Utilizar Poetry em vez de `pip` e `requirements.txt`.
- **Consequência**: Maior controle sobre versões e resolução de dependências, além de facilitar a criação de ambientes virtuais isolados.

## ADR 2: Renderização de Cores via HTML no Tkinter

- **Contexto**: Tkinter não suporta nativamente formatação rica de texto (como cores em palavras específicas no meio de frases) de forma simples sem manipulação manual de tags de texto.
- **Decisão**: Utilizar `tkhtmlview`.
- **Consequência**: Permite o uso de `<span>` com CSS inline para definir as cores, facilitando a lógica de exibição.
