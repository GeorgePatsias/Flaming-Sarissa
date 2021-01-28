$(document).ready(function () {
    var table = $('#tbl_users').DataTable({
        dom: 'l<"toolbar">frtip',
        responsive: true,
        LengthMenu: [
            [10, 25, 50, -1],
            [10, 25, 50, "All"]
        ],
        DisplayLength: 25,
        dom: 'lfrtip',
        ajax: {
            url: "/user-management/get/users",
            type: "GET",
            dataSrc: function (json) {
                var obj = json.data;
                return obj;
            }
        },
        columns: [{
            defaultContent: "-",
            data: "email",
            // className: 'text-center'
        }, {
            defaultContent: "-",
            data: "last_activity",
            // className: 'text-center'
        }, {
            defaultContent: "-",
            data: "createdAt",
            // className: 'text-center'
        }, {
            data: "actions",
            // className: 'text-center'
        }],
        columnDefs: [{
            targets: [3],
            data: null,
            defaultContent: "<button type='button' id='btnDelete' class='btn btn-danger'>Delete</button>"
        }],
    });

    $('#addUserModal').on('hidden.bs.modal', function (e) {
        $(this)
            .find("input")
            .val('')
            .end();
    });

    $('#tbl_users tbody').on('click', '#btnDelete', function () {
        let data = table.row($(this).parents('tr')).data();

        document.getElementById("email_delete").innerHTML = data.email;
        $("#deleteUserModal").modal('show');
    });


    $("#btnDeleteUser").click(function () {
        let email = document.getElementById("email_delete").innerHTML;

        $.ajax({
            type: 'POST',
            url: '/user-management/delete/user',
            dataType: 'json',
            data: JSON.stringify({
                "email": email.trim()
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




});