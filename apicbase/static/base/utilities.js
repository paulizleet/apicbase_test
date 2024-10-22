$(document).ready(function(){

    var ingredientChooser = document.getElementById("id_ingredient_choices");
    // when page is loaded, add NewIngredient option to the ingredient dropdown

    // $(ingredientChooser).append("<option value=\"-1\">--New Ingredient--</option>")

    $("#ingredient-dialogue").on('shown.bs.modal', function() {
        $("#id_name").trigger("focus");
    })

    $(" option ").on("click", function( event ){
        // add a new line containing the choice and give an option for quantity
        var selection = event.target.value
        var selectionText = event.target.textContent

        // if the user chooses to add a new ingredient, 
        // display the dialogue, add to db, and add to this list

        if(selection == -1){
            newIngredientDialogue();
            return
        }


        if(selectionText.trim() == ""){ return }


        //ensure this item hasn't already been added
        if($(".ingredient-number").hasClass(selection)){return}

        var newListEntry = "<tr class=\"ingredient-row\">"+
                            "<td class=\"ingredient-number "+ selection+"\" hidden>"+selection+"</td>"+
                            "<td>"+ selectionText+"</td>"+
                            "<td class=\"ingredient-quantity\"><input></input></td>"+
                            "<td><button type=\"button\" class=\"delbutton\" >❌</button></td></tr>"
                            
        console.log(newListEntry)
        $("#ingredients-list").append(newListEntry)
    });



    //whichever delete button is clicked, delete that row
    $("#ingredients-list").on('click', ".delbutton", function(){
        this.closest("tr").remove();
    });

  
    
    $(" #recipe-form ").on("submit", function(event){
        errors = []
        event.preventDefault();
        console.log("Submitted")
        var chosenIngredients = ""

        //Start by serializing everything normal in the form
        var formSubmission = $( this ).serializeArray();

        //Then manually serialize the ingredients table

        //throw some validations in here for good measure
        if ($(".ingredient-number").length == 0){
            alert("Please add some ingredients")
            return
        }
        $(".ingredient-number").each(function(ele){
            console.log(this.textContent)
            var ingredientNumber = this.textContent
            
            //'this' is the current td w/ class .ingredient-number
            //we want the input(child) of "this's" sibling belonging to class .ingredient-quantity
            var ingredientQuantity =  $(this).siblings(".ingredient-quantity").children("input")[0].value

            if(parseInt(ingredientQuantity) == NaN){
                alert("Letters aren't allowed in the quantity box")
                return
            }
            
            if(parseInt(ingredientQuantity) != Number(ingredientQuantity)){
                alert("Integers only please")
                return
            }

            if(parseInt(ingredientQuantity) <= 0){
                alert("Only positive quantities allowed")
                return
            }

            //parameter-ize ingredients list because $.param() is failing me
            chosenIngredients += ingredientNumber+","+ingredientQuantity+";"
            console.log([ingredientNumber, ingredientQuantity])
            chosenIngredients[ingredientNumber] = ingredientQuantity
        });


        //replace the automatically filled "ingredients" key with our own
        formSubmission[3] = {
            name:"ingredients",
            value: chosenIngredients
        }
        console.log(JSON.stringify(formSubmission))
        //ajax time
        $.ajax({
            method: "POST",
            url: window.location.pathname,
            data: $.param(formSubmission),
            success: function(data, status, xhr){
                

                //fix this jank
                $("html").empty();
                $("html").append(data);


            },
            fail: function(){console.log("Fail")}
        })
    });

})



function newIngredientDialogue(response){
    $("#ingredient-dialogue").toggle()
}
console.log("loaded");