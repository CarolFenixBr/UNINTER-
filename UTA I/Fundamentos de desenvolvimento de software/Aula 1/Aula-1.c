#include <stdio.h>

// ou /* para comentários. Obter notas; calcular media; verificar se o aluno foi aprovado ou não//
//se a media >=7 aprovado senão reprovado

int main(){
    //variáveis 
    float n1, n2, media;

    //obter as notas
    printf("Digite a primeira nota: ");
    scanf("%f" , &n1);

    printf("Digite a segunda nota: ");
    scanf("&f", &n2);
 
 // calcular a média
    media = (n1 + n2)/2;

    //verificação da aprovação ou não
    if(media >=7)
    printf("Aprovado");
    else
    printf("Reprovado");

    return 0;
    

}