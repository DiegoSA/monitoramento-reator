## Usando Markdown

É possível também escrever o conteúdo do relatório em Markdown (outra linguagem de marcado, como LaTeX ou Typst) e importar no arquivo de Typst.

### Código

Esse código aqui também é processado pelo Typst.

```python
import pandas as pd

data = {
    "name": ["Ana", "Bruno", "Carla"],
    "age": [28, 34, 25],
    "city": ["Natal", "João Pessoa", "Recife"],
}

df = pd.DataFrame(data)

print(df)
```
