//when page is loading:
$(document).ready(function(){
    // $('div.all.good').hide()
    setInterval(digitalclock, 1000);
    function digitalclock(){
        $('div.all.clock').empty();
        $('div.all.clock').append($('<h4 style="background-color: yellow;"></h4>').text(Date($.now())));
    }
});

//showing good
$(function () {
    $('button#how').click(function () {
        $('div.all.good').toggle("slow"); 
    });
});