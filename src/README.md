# Dados de processo industrial

O arquivo `data/process.csv` tem dados medidos numa usina.

O objetivo é fazer uma análise exploratória de dados (EDA) para entender o processo.

1. Crie um histograma para cada uma das colunas numéricas.
2. Calcule a média ($\mu$, `.mean()`) e o desvio padrão ($\sigma$, `.std()`), e os valores mínimo e máximo para cada uma das colunas numéricas.
3. Calcule a temperatura média do reator (`reactor_temp`) no regime de operação `A` (_normal_) e em `B` (_stressed_). Utilize uma operação `for` com `match`-`case`. Tem diferença?

> A "correlação de Pearson" entre dois grupos de dados é um número entre -1 e 1 que define se esses dados estão linealmente relacionados. Por exemplo: uma correlação de 1 entre a temperatura e a pressão indica que si a pressão aumenta duas vezes, a temperatura aumenta duas vezes também. Se a correlação é negativa, quer dizer que o aumento de uma quantidade implica a diminuição da outra. Uma correlação de zero indica que a mudança de um valor não tem efeito no outro.

4. Calcule a correlação entre:

- `reactor_temp` e `reactor_pressure`
- `feed_flow_rate` e `power_consumption_kw`
- Duas mais da sua escolha
