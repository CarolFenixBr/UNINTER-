
import java.util.Scanner;
/*Em “import java.util.Scanner” nós importamos a classe Scanner para ler os dados.*/
public class Media{
    /*Em “public class Media” criamos a classe Media */

public static void main(String args[]){
    java.util.Scanner nota = new Scanner(System.in);
    float nota1, nota2, media;
System.out.println("Digite a primeira nota");
nota1 =nota.nextFloat();
System.out.println("Digite a segunda nota");
nota2 =nota.nextFloat();
media =(nota1 +nota2)/2;
if(media >=7)
System.out.println("Aprovado");
else
System.out.println("Reprovado");

}
}
