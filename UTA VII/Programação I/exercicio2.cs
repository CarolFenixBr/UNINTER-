using System;
using System.Collections.Generic;
public class Produto //declarando a classe produto
{
//declarando abaixo as variáveis nome, preço e quantidade
public string Nome { get; set; }
public double Preco { get; set; }
public int Quantidade { get; set; }
public double TotalEmEstoque() //declarando que o total de estoque é
o preço * a quantidade
{
return Preco * Quantidade;
}

Produto
- Nome: string
- Preco: double
- Quantidade: int
+ ValorTotalEmEstoque(): double
+ AdicionarProduto(quantidade: int) : void
+ RemoverProdutos(quantidade : int) : void

public void AddProduto(int quantidade) //adicionar a quantidade
{
Quantidade += quantidade;
}
public void RemoverProdutos(int quantidade) //removendo a quantidade
{
if (Quantidade >= quantidade) //condição
Quantidade -= quantidade;
else

Console.WriteLine("Não há produtos suficientes no esto-
que.");

}
}
class Program //declarando a classe
{
static void Main(string[] args)
{
Produto prod = new Produto();
prod.Nome = "TV";
prod.Preco = 900.00;
prod.Quantidade = 10;
Console.WriteLine($"Dados do produto: {prod.Nome}, $

{prod.Preco}");

Console.WriteLine($"{prod.Quantidade} unidades");
Console.WriteLine($"Total: $ {prod.TotalEmEstoque()}");
Console.WriteLine("Digite o número de produtos a ser adicionado

ao estoque:"); //mensagem a ser imprimida na tela
int add = Convert.ToInt32(Console.ReadLine());
prod.AddProduto(add);
Console.WriteLine($"Dados atualizados: {prod.Nome}, $

{prod.Preco}, {prod.Quantidade} unidades, Total: $ {prod.TotalEmEsto-
que()}");

Console.WriteLine("Digite o número de produtos a ser removido do

estoque:"); //mensagem a ser imprimida na tela

int remove = Convert.ToInt32(Console.ReadLine());
prod.RemoverProdutos(remove);
Console.WriteLine($"Dados atualizados: {prod.Nome}, $

{prod.Preco}, {prod.Quantidade} unidades, Total: $ {prod.TotalEmEsto-
que()}");

}
}
