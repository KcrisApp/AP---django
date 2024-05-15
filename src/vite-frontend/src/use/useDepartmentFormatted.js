export function useDepartmentFormatted(role) {
    

    switch (role) {
        case "O":
            return "Office"

        case "T":
            return "Testing"
        
        case "V":
            return "Verify"
        
        case "S":
            return "SMT"
    
        case "W":
            return "Welding"
            
        case "A":
            return "Shipping"
    
        default:
            break;
    }

}
