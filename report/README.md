# Como criar um relatório com Typst

[Typst](https://typst.app/) é uma linguagem de marcação para criar documentos com alta qualidade tipográfica. É uma alternativa ao LaTeX, com sintaxe mais simples e moderna.

O documento é escrito em um arquivo de texto com extensão `.typ` e compilado para gerar um PDF.

Antes de começar, instale o Typst.

## Instalação

No Linux, você pode usar o `Homebrew` para instalar o Typst. Se ainda não tiver o Homebrew, siga os passos abaixo.

### Homebrew

Instale o Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Depois, adicione o Homebrew ao ambiente da sua sessão:

```bash
echo >> /home/codespace/.bashrc
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv bash)"' >> /home/codespace/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv bash)"
```

### Typst

Instale o Typst:

```bash
brew install typst
```

Verifique a instalação:

```bash
typst --version
```

## Compilar um documento

Numa nova sessão do terminal, rode o comando abaixo para compilar o arquivo `report.typ` e gerar o PDF `report.pdf` (os dois estão em `docs`).

```bash
typst watch docs/report.typ docs/report.pdf
```

A opção `watch` mantém o Typst observando o arquivo `.typ` e recompila o PDF automaticamente sempre que houver uma alteração salva.

Para mais informações, consulte a [documentação oficial do Typst](https://typst.app/docs/).
