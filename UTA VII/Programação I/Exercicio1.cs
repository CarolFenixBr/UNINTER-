using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
 
namespace Exercicio1
{
    class Program
    {
        static void Main(string[] args)
        {
            bool convercao;
            double a, b, c; //número inteiro que ira receber os valores, declarando as variáveis
 
            Console.WriteLine("Equação 2 grau");
 
            Console.Write("Digite o valor para a letra A: "); //recebe o valor de A, que é igual ao primeiro número do RU
            convercao = Double.TryParse(Console.ReadLine(), out a);
 
            Console.Write("Digite o valor para a letra B: "); //recebe o valor de B, que é igual ao segundo número do RU
            convercao = Double.TryParse(Console.ReadLine(), out b);
 
            Console.Write("Digite o valor para a letra C: ");
            convercao = Double.TryParse(Console.ReadLine(), out c);  //recebe o valor de C, que é igual ao terceiro número do RU
 
            Console.WriteLine(); //Pula uma linha
            
            //realizando a equação, e colocando condições caso o delta for menor que zero não terá raiz
 
            Bhaskara1(a, b, c);
            Bhaskara2(a, b, c);
 
        }
 
        static void Bhaskara1(double a1, double b1, double c1) 
        {
            double delta = Math.Sqrt(Math.Pow(b1, 2) - (4 * a1 * c1));
            string sX1;
            double x1 = (((b1 * (-1)) + delta) / (2 * a1));
 
            if (delta > 0)
            {
                sX1 = String.Format("x1 é igual a: " + x1);
            }
            else if (delta == 0)
            {
                sX1 = String.Format("Como o valor do descriminante é igual a 0\n\tx é igual a: " + x1);
            }
            else
            {
                sX1 = "A equação não possui raízes reais, pois o descriminante é menor do que 0.";
            }
 
            Console.WriteLine(sX1 + "\n\n");
        }
 
        static void Bhaskara2(double a2, double b2, double c2) //número inteiro positivo
        {
            double delta = Math.Sqrt(Math.Pow(b2, 2) - (4 * a2 * c2));
 
            if (delta > 0)
            {
                double x2 = (((b2 * (-1)) - delta)/2*a2);
                Console.WriteLine("x2 é igual a: " + x2 + "\n\n");
            }
        }
    }
}
