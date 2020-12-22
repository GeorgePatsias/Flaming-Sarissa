$(document).ready(function () {

    $('.server-specs tr').click(function () {
        $(this).children('td').children('input').prop('checked', true);
        $('.server-specs tr').removeClass('selected');
        $(this).toggleClass('selected');
    });


    $("#ipList").change(function(){
        console.log($("#ipList").val());

        $("#ip_number").html();
    });

    // GETS SELECTED SERVER SPEC 
    // $('input[name="server_spec"]:checked').val();
    // $('input[name="server_spec"]:checked').attr("data-price");


});


function init_overview(){
    $("#ip_number").html('0');
    $("#server_number").html('0');
    $("#price_number").html();
}