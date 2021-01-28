$(document).ready(function () {

    $(".server-specs tr").click(function () {
        $(this).children('td').children('input').prop('checked', true);
        $('.server-specs tr').removeClass('selected');
        $(this).toggleClass('selected');

        updateTotalCost();
    });

    $(".server-specs>tr:first").trigger('click');
    initOverview();


    $("#ipList").change(function () {
        let ipList = $("#ipList").tagsinput('items');

        let lastIP = ipList[ipList.length - 1];

        if (lastIP === "127.0.0.1") {
            alert("You have entered an invalid IP address!")
            $('#ipList').tagsinput('remove', lastIP);
        }

        if (lastIP && !ValidateIPaddress(lastIP)) {
            $('#ipList').tagsinput('remove', lastIP);
        }

        $("#ip_number").html(ipList.length);
    });

    // Update Overview for Servers for Distribution
    $("#serversList").change(function () {
        $("#server_number").html($('#serversList').val());

        $(".regions:checkbox").prop('checked', false);

        updateTotalCost();
    });



    $("#startNmap").click(function () {
        let ipList = $("#ipList").tagsinput('items');
        let serversDistribution = $('#serversList').val();
        let nmapParameters = $('#parameterList').tagsinput('items');
        let doServer = $('input[name="server_spec"]:checked').val();
        let regionsList = $(".regions:checkbox:checked").map(function () {
            return $(this).val();
        }).get();

        if (!ipList || !serversDistribution || !doServer || !regionsList) {
            alert('Please fill the form correctly! You have some missing parts.');
            return; //CHECK HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEREEEEEEEEEEEEEEEEEEEEEEEEEE!!!!
        }

        $.ajax({
            type: 'POST',
            url: '/nmap/create',
            dataType: 'json',
            data: JSON.stringify({
                "ip_list": ipList,
                "server_distribution": serversDistribution,
                "nmap_parameters": nmapParameters,
                "do_server": doServer,
                "regions_list": regionsList
            }),
            contentType: "application/json; charset=utf-8",
            statusCode: {
                200: function () {
                    location.reload();
                },
                400: function () {
                    location.reload();
                },
                500: function () {
                    location.reload();
                }
            }
        });
    });


    $(".regions").click(function () {
        let regionsList = $(".regions:checkbox:checked").map(function () {
            return $(this).val();
        }).get();

        if (regionsList.length > Number($('#serversList').val())) {
            let lastRegion = regionsList[regionsList.length - 1];
            regionsList.pop(lastRegion);

            $('.regions:checkbox[value="' + lastRegion + '"]').prop('checked', false);

            alert('Please increase the Server Distribution for more regions!');
        }
    });

});


function initOverview() {
    $("#server_number").html($('#serversList').val());
    updateTotalCost();
}

function updateTotalCost() {
    let no_servers = Number($('#serversList').val());
    let server_cost = Number($('input[name="server_spec"]:checked').attr("data-price").replace('$', ''));

    let total = no_servers * server_cost;

    $("#price_number").html("$" + total + " per hour");
}

function ValidateIPaddress(ipaddress) {
    if (/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(ipaddress)) {
        return (true)
    }
    alert("You have entered an invalid IP address!")
    return (false)
}