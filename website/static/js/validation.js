$(document).ready(function(){

    $.validator.addMethod("strongPassword", function(values, element){
        
    });

    $("#register-form").validate({
        rules: {
            username: "required",
            password: {
                required: true,
                minlength: 8
            },
            password_repeat: "required"
        }
    });
});