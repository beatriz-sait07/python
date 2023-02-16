//crie um arquivo que escriva dados do tipo char, int, float em um arquivo

#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *arq;
    char nome[20];
    int idade;
    float altura;

    arq = fopen("arquivo.txt", "w");
    if(arq == NULL)
    {
        printf("Erro, nao foi possivel abrir o arquivo \n");
        system("pause");
        exit(1);
    }

    printf("Digite seu nome: ");
    scanf("%s", nome);
    printf("Digite sua idade: ");
    scanf("%d", &idade);
    printf("Digite sua altura: ");
    scanf("%f", &altura);

    fprintf(arq, "Nome: %s \t Idade: %d \t Altura: %.2f \n", nome, idade, altura);

    fclose(arq);

    // ler dados de um arquivo e imprimir eles na tela na ordem de leitura
    arq = fopen("arquivo.txt", "r");
    if(arq == NULL)
    {
        printf("Erro, nao foi possivel abrir o arquivo \n");
        system("pause");
        exit(1);
    }
    
    fscanf(arq, "Nome: %s \t Idade: %d \t Altura: %f \n", nome, &idade, &altura);
    printf("Nome: %s \t Idade: %d \t Altura: %.2f \n", nome, idade, altura);
    

    return 0;
}