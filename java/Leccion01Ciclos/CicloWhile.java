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
            System.out.println("contando =" + contando);
        }


        }
    }
}