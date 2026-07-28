#import "@preview/cmarker:0.1.10"
#set document(
  title: [Relatório de análise de dados],
)
#set text(lang: "pt")

#align(center)[
  (Nome do estudante)
  #title()
]

= Resumo

Nesse relatório, apresentamos uma análise detalhada dos dados.

= Introdução

Agora, vamos explorar os dados coletados e identificar padrões significativos.

#figure(
  image("../images/advanced-options.webp", width: 50%),
  caption: [
    Uma imagem de exemplo.
  ],
)

Adicionamos fórmulas matemáticas também.

$ 
sum_(k=0)^n k
    &= 1 + ... + n \
    &= (n(n+1)) / 2 
$

E tabelas.

#table(
  columns: 2,
  [*Quantidade*], [*Ingrediente*],
  [360g], [Farinha para panificação],
  [250g], [Manteiga (temperatura ambiente)],
  [150g], [Açúcar mascavo],
  [100g], [Açúcar de cana],
  [100g], [Chocolate 70% cacau],
  [100g], [Chocolate 35-40% cacau],
  [2], [Ovos],
  [Pitada], [Sal],
  [Fio], [Extrato de baunilha],
)

#cmarker.render(read("report.md"))