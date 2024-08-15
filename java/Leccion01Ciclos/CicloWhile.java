public class CicloWhile{
    public static void main(String[] args){
        //ciclo while
        var conteo = 0; // INFERENCIA DE TIPOS
        while(conteo<3){
            System.out.println("conteo = " + conteo);
            conteo++;

        //ciclo do while
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador<7);

        for(var contando = 0;contando<7;contando++){
            if(contando % 2 == 0){
            System.out.println("contando =" + contando);
            break;

            }
        }

        for(var contando = 0;contando<7;contando++){
            if(contando % 2 != 0){
                continue; // vamos a la siguiente iteracion
            
        
            }
            System.out.println("contando =" + contando);
        }


        }
    }
}