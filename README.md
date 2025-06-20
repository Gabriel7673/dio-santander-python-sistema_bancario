# dio-santander-python-sistema_bancario

# Sistema Bancário - Versão 1

## 💡 Objetivo Geral

Criar um sistema bancário com as seguintes operações:

- Sacar
- Depositar
- Visualizar extrato

## 🏦 Funcionalidades

### Depósito

- Permite depósitos de **valores positivos**.
- Todos os depósitos são armazenados em uma variável.
- Os depósitos são exibidos na operação de extrato.


### Saque

- São permitidos **até 3 saques diários**.
- Limite de **R$ 500,00 por saque**.
- O sistema verifica se há **saldo suficiente** antes de efetuar o saque.
- Em caso de saldo insuficiente, uma **mensagem de erro** será exibida.
- Todos os saques são armazenados em uma variável e exibidos no extrato.

### Extrato

- Lista **todos os depósitos e saques** realizados na conta.
- Exibe o **saldo atual** ao final da listagem.
- Os valores são formatados como `R$ xxx.xx`.

## 📌 Observações

- O sistema é básico e **não possui interface gráfica**.
- Esta versão suporta **apenas um usuário**, portanto **não há necessidade de identificar agência ou número da conta**.
- Projetado para fins de aprendizado e prática com estruturas de controle, condicionais e manipulação de variáveis em Python.

---

Desenvolvido como exercício de lógica de programação para construção de sistemas financeiros simples no Bootcamp Santander Python 2025.

