
function togglePass() {
    //alert("Just testing");
    var x = document.getElementById("init_pass");
    var y = document.getElementById("conf_pass");

    if (x.type === "password") {

        x.type = "text";
        y.type = "text";

    } else {

        x.type = "password";
        y.type = "password";

    }

   // alert("Just trying");
}




$(document).ready(function(){
    $('.collapse').collapse();
    $('.dropdown-toggle').dropdown('toggle');

    $("#sidebarCollapse").on('click', function(){
        //alert("click");
        $("#sidebar").toggleClass("active");
        var x = $("#toggler-icon").attr("class");

        if(x == 'fa fa-arrow-left'){
            $("#toggler-icon").removeClass("fa fa-arrow-left").addClass("fa fa-arrow-right");
        }else{
            $("#toggler-icon").removeClass("fa fa-arrow-right").addClass("fa fa-arrow-left");
        }

    });

//    $('.dropdownx').dropdown();
//    alert("Document ready");
});
