using System;
using System.Collections.Generic;
using System.Threading;
class Program
{
static void Main(string[] args)
{
Console.Write("Digite os dois últimos dígitos do RU do aluno:

"); //digita os números do RU

int N = Convert.ToInt32(Console.ReadLine());
if (N == 0) //se N for igual a 0
{
Console.Write("O valor é zero, por favor digite outro valor:

"); // imprime na tela a mensagem

N = Convert.ToInt32(Console.ReadLine());
}
List<Thread> threads = new List<Thread>();
for (int i = 0; i <= N; i += 10)
{
int start = i;
Thread thread = new Thread(() => PrintPrimes(start,
Math.Min(start + 10, N))); //função PrintPrimes executa o valor dez
vezes

threads.Add(thread);

thread.Start();
}
foreach (Thread thread in threads)
{
thread.Join();
}
}

static void PrintPrimes(int start, int end) //função PrintPrimes ex-
ecuta o valor dez vezes

{
for (int i = start; i < end; i++)
{
if (IsPrime(i))
{
Console.WriteLine(i);
}
}
}
static bool IsPrime(int number) //função que verifica se o número é
primo
{
if (number <= 1) return false;
if (number == 2) return true;
if (number % 2 == 0) return false;
var boundary = (int)Math.Floor(Math.Sqrt(number));
for (int i = 3; i <= boundary; i += 2)
if (number % i == 0)
return false;

return true;
}
}
