function collect_email(email, onSuccess) {
    $.ajax({
        url: "collect_email",
        data: {
            email_address: email
        },
        dataType: "json",
        type: "GET"
        success: function(response) {
            onSuccess(response);
        }
    });
}

$("#enter-button").on("click", function() {
    let email = $("#email-address").val()
    collect_email(email, function(user_email) {
        $("#user_email").text(user_email);
    });
});
