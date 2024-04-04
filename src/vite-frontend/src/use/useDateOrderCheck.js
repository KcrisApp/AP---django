export function useDateOrderCheck(dateOrder) {
 
       //define two date object variables with dates inside it  
       let data1 = new Date();  
       let data2 = new Date(dateOrder);  

       const differenzaMillisecondi = data1.getTime() - data2.getTime();
       const giorni = Math.floor(differenzaMillisecondi / (1000 * 60 * 60 * 24));
       
       return giorni;
  // return new Date(date).toLocaleString().split(',')[0];
}
