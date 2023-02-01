#include<conio.h>
#include<stdio.h>
#include<ctype.h>

int main(){
	char num;

	printf("Ingrese un numero decimal del 1 al 9\n");
	scanf("%c",&num);
	
	if(isdigit(num)){
		if(num == '0'){	printf("\n Numero Binario: 0");	}
	
		else if(num == '1'){	printf("\nNumero Binario: 1");	}
		else if(num == '2'){	printf("\nNumero Binario: 10");	}
		else if(num == '3'){	printf("\nNumero Binario: 11");	}
		else if(num == '4'){	printf("\nNumero Binario: 100");	}
		else if(num == '5'){	printf("\nNumero Binario: 101");	}
		else if(num == '6'){	printf("\nNumero Binario: 110");	}
		else if(num == '7'){	printf("\nNumero Binario: 111");	}
		else if(num == '8'){	printf("\nNumero Binario: 1000");	}
		else if(num == '9'){	printf("\nNumero Binario: 1001");	}
		
		else{
			printf("\nValor fuera de rango");
		}
	}
	
	else{
		printf("\nValor fuera de rango");
	}
	getch();
}
