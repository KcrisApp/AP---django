export function useDateFormatted(dateInput) {
 
       let data = new Date(dateInput);  
       return data.toLocaleString("en-GB").split(',')[0];

}
