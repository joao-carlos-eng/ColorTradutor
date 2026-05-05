# LLM Handoff - ColorTradutor

## Estado Atual
O MVP está 100% funcional e estável no Python 3.14. A interface é moderna e o alinhamento de cores lida bem com a estrutura EN-PT.

## O que foi feito recentemente
- Entrega do MVP com `CustomTkinter`.
- Correção de bugs de compatibilidade (Python 3.14 / `cgi` module).
- Implementação da Heurística de Alinhamento 2.0 (agrupamento de artigos).
- Documentação completa atualizada.

## Próximos Passos Sugeridos
1. **Internacionalização**: Adicionar suporte a múltiplos idiomas de destino.
2. **Persistência**: Salvar as cores geradas em um arquivo local para que palavras mantenham as mesmas cores entre sessões diferentes.
3. **Refino de UI**: Adicionar um botão de "Copiar" para o texto traduzido.

## Bloqueios / Pendências
- Bibliotecas de Deep Learning (`torch`, `transformers`) continuam apresentando dificuldades de instalação no Python 3.14 em ambiente Windows sem compiladores; por isso, o motor atual é baseado em API Web.
