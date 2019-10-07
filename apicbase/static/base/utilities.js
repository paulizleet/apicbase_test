$(document).ready(function(){

    var ingredientChooser = document.getElementById("id_ingredient");

    ingredientChooser.addEventListener("click", function( event ){
        // add a new line containing the choice and give an option for quantity
        var selection = event.originalTarget.firstChild
        if(selection.textContent.trim() == ""){ return }


        //ensure this item hasn't already been added
        if($(".ingredient-number").hasClass(event.originalTarget.value)){return}

        var newListEntry = "<tr class=\"ingredient-row\">"+
                            "<td class=\"ingredient-number "+ event.originalTarget.value+"\" hidden>"+event.originalTarget.value+"</td>"+
                            "<td>"+ selection.textContent+"</td>"+
                            "<td class=\"ingredient-quantity\"><input></input></td>"+
                            "<td><button type=\"button\" class=\"delbutton\" >❌</button></td></tr>"
                            
        console.log(newListEntry)
        $("#ingredients-list").append(newListEntry)
    });



    //whichever delete button is clicked, delete that row
    $("#ingredients-list").on('click', ".delbutton", function(){
        this.closest("tr").remove();
    });

    
    $(" form ").on("submit", function(event){
        event.preventDefault();
        console.log("Submitted")
        var chosenIngredients = ""

        //Start by serializing everything normal in the form
        var formSubmission = $( this ).serializeArray();

        //Then manually serialize the ingredients table

        //throw some validations in here for good measure
        $(".ingredient-number").each(function(ele){
            console.log(this.textContent)
            var ingredientNumber = this.textContent
        
            //'this' is the current td w/ class .ingredient-number
            //we want the input(child) of "this's" sibling belonging to class .ingredient-quantity
            var ingredientQuantity =  $(this).siblings(".ingredient-quantity").children("input")[0].value


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
            type: "POST",
            url: window.location.pathname,
            data: $.param(formSubmission),
            success: function(){console.log("success!")},
            fail: function(){console.log("Fail")}
        })
    });
})

console.log("loaded");