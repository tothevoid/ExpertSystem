$(document).ready(function() {
    ruleBackup = document.getElementById('main-rule').cloneNode(1)
    console.log(ruleBackup)
    $('.btn-submit').click(function(event){
        event.preventDefault();
       
        if (!validateForm($('#form').serializeArray())){
            return;
        }
        sendForm();
    });

    $('.btn-submit-other').click(function(event){
        event.preventDefault();
       
        // if (!validateForm($('#form').serializeArray())){
        //     return;
        // }
        res = JSON.stringify($('#form').serializeControls(), null, 2)
        console.log(res)
    });
});

var ruleBackup;


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

function deleteRule(e){
    event.target.parentNode.parentNode.remove();
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

var currentRuleIndex = 1

function addRule(e){
    var div = document.createElement("div");
    div.classList.add('rule')
    currentRuleIndex++

    var newElm = ruleBackup.cloneNode(1) 
    for (var i = 0; i <= 3; i++) {
        var elm = newElm.children[i].children[1];
        var name = elm.getAttribute('name').replace('[1]',"["+currentRuleIndex+"]")
        newElm.children[i].children[1].setAttribute("name",name);
    }
    document.querySelector('.rules').appendChild(newElm)
}


$.fn.serializeControls = function() {
    var data = {};
  
    function buildInputObject(arr, val) {
      if (arr.length < 1)
        return val;  
      var objkey = arr[0];
      if (objkey.slice(-1) == "]") {
        objkey = objkey.slice(0,-1);
      }  
      var result = {};
      if (arr.length == 1){
        result[objkey] = val;
      } else {
        arr.shift();
        var nestedVal = buildInputObject(arr,val);
        result[objkey] = nestedVal;
      }
      return result;
    }
  
    $.each(this.serializeArray(), function() {
      var val = this.value;
      var c = this.name.split("[");
      var a = buildInputObject(c, val);
      $.extend(true, data, a);
    });
    
    return data;
}