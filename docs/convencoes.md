# Convenções do Projeto

Para manter a consistência do código, seguimos as seguintes diretrizes:

## Nomenclatura

- **Arquivos**: `snake_case.py`
- **Classes**: `PascalCase`
- **Funções e Variáveis**: `snake_case`
- **Constantes**: `UPPER_SNAKE_CASE`

## Padrões de Código

- Seguimos a [PEP 8](https://peps.python.org/pep-0008/).
- Docstrings em todas as classes e funções públicas.
- Uso de Type Hints sempre que possível.

## Git Flow

- `main`: Código estável em produção.
- `develop`: Integração de novas funcionalidades.
- `feature/*`: Desenvolvimento de novas funcionalidades.
- `fix/*`: Correção de bugs.

## Commits

- Mensagens de commit claras e objetivas, preferencialmente em inglês ou português conforme padrão da equipe (padrão atual: pt-BR).
- Exemplo: `feat: adiciona lógica de destaque por hash`
