// 搜索按鈕

function search(){
    var checkboxes  = document.querySelectorAll('input[name="requirement"]:checked')
    var arr = []
    
    for (var i = 0; i < checkboxes.length; i++) {
        arr.push(checkboxes[i].value);
        console.log(checkboxes[i].value);
    }
    var slider = document.getElementById('money-slider');
    budget = slider.value;

    $.ajax({
        url: '/modify',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({"requirements": arr, "budget": budget}),
        success: function(res){console.log(res)},
        error:function(err){console.log(err)},
    });
    
    $.ajax({
        url: '/search',
        method: 'POST',
        success: function(res){console.log(res)},
        error:function(err){console.log(err)},
    });

}

// 選單按鈕
function menuBtnClicked(elem){
    let menu
    if (elem.id == "itinerary_style_btn") {
        menu = document.querySelector("#menu1");
    }
    else if (elem.id == "attractions_btn") {
        menu = document.querySelector("#menu2");
    }  
    else if (elem.id == "food_btn") {
        menu = document.querySelector("#menu3");
    }
    else if (elem.id == "entertainment_btn") {
        menu = document.querySelector("#menu4");
    }
    else if (elem.id == "distance_btn") {
        menu = document.querySelector("#menu5");
    }

    if (menu.style.visibility == "visible") {  
        menu.style.visibility="hidden";
    }
    else {
        menu.style.visibility="visible";
    }
}
// 行程
function show_itinerary(itn){
    name_list = ['./test/result0.json',
                 './test/result1.json',  
                 './test/result2.json']
    fname = name_list[itn.getAttribute('value')]
    console.log(itn.getAttribute('value'))
    $.ajax({
        url: '/show/place_detail',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({"fname": fname}),
        success: function(res){
            $("#detail").html(res);
            route(fname);
            console.log(res);},
        error:function(err){console.log(err)},
    });
    
}

// 預算

function show_money_slider_value(slider) {
  var valueDisplay = document.getElementById('slider-value');
  const value = slider.value;
  valueDisplay.textContent = value;
}
