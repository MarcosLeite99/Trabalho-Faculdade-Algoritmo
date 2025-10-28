# Sistema de Gerenciamento de Alunos (CRUD)

Este é um sistema simples baseado em console (linha de comando) escrito em Python para gerenciar um cadastro de alunos. Ele implementa as operações **C**riar, **R**eceber (Listar), **U**pdate (Atualizar) e **D**elete (Excluir) de registros de alunos, seguindo o padrão CRUD.

## Funcionalidades

O sistema permite as seguintes operações através de um menu interativo:

1.  **Cadastrar Aluno**: Adiciona um novo aluno à lista, solicitando Nome, Idade e Curso.
2.  **Listar Alunos**: Exibe todos os alunos cadastrados, numerados para facilitar a seleção.
3.  **Atualizar Aluno**: Permite modificar os dados de um aluno existente, selecionado pelo seu número na lista. Campos vazios não são alterados.
4.  **Excluir Aluno**: Remove um aluno do sistema, selecionado pelo seu número na lista.
5.  **Sair**: Encerra a execução do programa.

## Estrutura de Dados

Os dados dos alunos são armazenados em uma lista global chamada `alunos`, onde cada aluno é representado por um dicionário com as seguintes chaves:

* `"nome"`
* `"idade"`
* `"curso"`

## Como Executar

1.  **Pré-requisitos**: Certifique-se de ter o **Python** instalado em seu sistema (versão 3.x recomendada).
2.  **Salvar**: Salve o código Python fornecido em um arquivo, por exemplo, `gerenciador_alunos.py`.
3.  **Executar**: Abra o terminal ou prompt de comando, navegue até o diretório onde salvou o arquivo e execute o script com o seguinte comando:

    ```bash
    python gerenciador_alunos.py
    ```

4.  **Interagir**: O menu principal será exibido. Digite o número correspondente à operação desejada e pressione Enter.

## Exemplo de Uso