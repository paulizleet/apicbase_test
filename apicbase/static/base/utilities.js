$(document).ready(function(){

    var ingredientChooser = document.getElementById("id_ingredient_choice_field");

    ingredientChooser.addEventListener("click", function( event ){
        console.log(event);
        console.log(event.originalTarget)
        // add a new line containing the choice and give an option for quantity
        var selection = event.originalTarget.firstChild
        if(selection.textContent.trim() == ""){ return }
        console.log(selection)
        var newListEntry = "<tr class=\"ingredient-row\">"+
                            "<td class=\"ingredient-number\" hidden>"+ event.originalTarget.value+"\"></td>"+
                            "<td>"+ selection.textContent+"</td>"+
                            "<td><span><input class=\".ingredient-quantity\"></input></span></td>"+
                            "<td><button type=\"button\" class=\"delbutton\" >❌</button></td></tr>"
                            
        console.log(newListEntry)
        $("#ingredients-list").append(newListEntry)
    });


    //whichever delete button is clicked, delete that row
    $("#ingredients-list").on('click', ".delbutton", function(){
        this.closest("tr").remove();
    })

    $("#formsubmit").on("click"), function(event){
        event.preventDefault();
        console.log("Submitted")
        var chosenIngredients = {}
        $("ingredients-list").find("tr").each(function(row){
            var ingredientValue = row.find(".ingredient-number").textContent
            var ingredientQuantity = row.find(".")
        })
    }
})

console.log("loaded");