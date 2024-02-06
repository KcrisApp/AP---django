export function useDateFormat(date){
       return new Date(date).toLocaleString().split(',')[0];
}