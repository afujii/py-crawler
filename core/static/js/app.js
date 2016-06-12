document.addEventListener('DOMContentLoaded', init)

function init(e) {
    console.log('hello')
}

$(document).ready(function(){
    $('#btn-login').on('click', function(){
        $.post('/api/login', {username:$('#login-username').val(), password:$('#login-password').val()}, function(res){
            console.log(res)
        });
    });
    $('#btn-register').on('click', function(){
        $.post('/api/register', {username:$('#register-username').val(), password:$('#register-password').val()}, function(res){
            console.log(res)
        });
    });
});
