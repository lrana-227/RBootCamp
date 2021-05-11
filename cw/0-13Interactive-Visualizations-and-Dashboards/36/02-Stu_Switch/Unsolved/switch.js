// Switch function
function  chooseOne(choice){
    var con_choice = choice.toUpperCase()
    switch(con_choice){
        case "A": 
            console.log(1);
            break;
        case "B": 
            console.log(2);
            break;
        case "C": 
            console.log(3);
            break;
        case "D": 
            console.log(4);
            break;
        case "E": 
            console.log(5);
            break;
        default:
            console.log(0);
    }

}

chooseOne("A");
chooseOne("C");
chooseOne("D");
chooseOne("B");
chooseOne("E");
chooseOne("H");
