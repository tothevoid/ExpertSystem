$(document).ready(function() {
    $('.btn-submit').click(function(event){
        event.preventDefault();
        if (!validateForm($('#form').serializeArray())){
            return;
        }
        sendForm();
    });
});

function sendForm(){
    dataObject = convertForm($('#form').serializeArray());
    console.log(JSON.stringify(dataObject))
    $.ajax ({
        url: "/get_user_form",
        type: "POST",
        data: JSON.stringify(dataObject),
        dataType: "json",
        contentType: 'application/json',
        crossDomain: true,
        contentType: "application/json; charset=utf-8",
        success: function(data){
            window.location.replace("/tree");
        }
    });
}

function validateForm(formArray){
    isCorrect = true;
    for (var i = 0; i < formArray.length; i++){
        var name = formArray[i]['name'];
        var value = formArray[i]['value'];
        var element = document.querySelector('.field>[name='+name+']');
        if (value.trim() === "" && !element.classList.contains('error')){
            if (!element.hasAttribute('required'))
                continue;
            element.classList.add('error')
            var ul = document.createElement("ul");
            ul.innerHTML = "<li>Поле должно быть заполнено</li>"
            element.after(ul);
            isCorrect = false;
        }
        else if (value.trim() !== "" && element.classList.contains('error')){
            element.classList.remove('error')
            element.nextElementSibling.remove();
        }
        else if (value.trim() === "" && element.classList.contains('error')){
            isCorrect = false;
        }
    }
    return isCorrect;
}

function convertForm(formArray) {
    var returnArray = {};
    for (var i = 0; i < formArray.length; i++){
        var name = formArray[i]['name']
        var value = formArray[i]['value'];
        returnArray[name] = value;
    }
    return returnArray;
}
