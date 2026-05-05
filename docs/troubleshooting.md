# Troubleshooting

Guia para solução de problemas comuns.

## Erro: `NameError: name 'nltk' is not defined`
- **Causa**: O pacote NLTK é utilizado mas não foi importado no arquivo `app.py`.
- **Solução**: Adicione `import nltk` no topo do arquivo e certifique-se de que o pacote está instalado.

## Erro: `AttributeError: 'NoneType' object has no attribute 'text'` (Googletrans)
- **Causa**: A biblioteca `googletrans` pode falhar devido a mudanças na API do Google ou bloqueios de IP.
- **Solução**: Verifique a conexão com a internet ou tente alternar para o motor de tradução avançado (`tradutor.py`).

## Lentidão ao iniciar `tradutor.py`
- **Causa**: O modelo de tradução (MarianMT) é baixado na primeira execução e carregado na memória RAM/VRAM.
- **Solução**: Aguarde o download completar (aprox. 300MB a 1GB dependendo do modelo) e certifique-se de ter memória disponível.
