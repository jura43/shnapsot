const socket = io.connect('http://127.0.0.1:5000');
const private = io.connect('http://127.0.0.1:5000/private')
let usernameActive, sender;

function openChat(params) {
    //Function for changing chat box to selected user
    usernameActive = params
    $('.chat-box').empty();
    private.emit('tooltip', {
        sender: sender,
        recepient: usernameActive
    });
    $('.chat-box').attr('id', usernameActive)
}

$(document).ready(function() {
    
    //Showing message that client is online
    socket.on('join_announcement', function(data){
        $('<li/>', {
            text: data + ' has joined!'
        }).appendTo('#general') //Client join announcement
        $('<button/>', {
            type: 'button',
            class: 'btn btn-primary tablinks',
            id: data,
            onclick: 'openChat("'+data+'")',
            text: data
        }).appendTo('#client-list') //Add client to client list
        $("#client-list").append('<br>')
    });

    //Creating list of users on join
    socket.on('user_list', function (users) {
        $.each(users, function (username, sid) {
            if ($('#'+username).length) { sender = username; return true; }
            $('<button/>', {
                type: 'button',
                class: 'btn btn-primary tablinks',
                id: username,
                onclick: 'openChat("'+username+'")',
                text: username
            }).appendTo('#client-list')
        })
    });
    
    //Showing message that client has disconnected
    socket.on('leave_announcement', function(data){
        $("#general").append('<li>'+data+' went offline!</li>');
        $("#"+data).remove();
    });

    //Displaying client message
    private.on('deliver_message', function(data) {
        $('div#'+data['sender']).append('<div class="recevied">'+data['message']+'</div>');
    });
    
    //Funciton for sending client message
    $('#sendbutton').on('click', function() {
        let message = $('#myMessage').val();
        private.emit('message', {
            sender: sender,
            recepient: usernameActive,
            message: message
        });
        $('div#'+usernameActive).append('<div>'+message+'</div>');
        $('#myMessage').val('');
    });

    private.on('notification', function (data) {
        $('<span/>', {
            class: 'badge badge-danger',
            text: '!'
        }).appendTo('#'+data['sender']);
        $('div#'+data['sender']).append(data['sender']+' has joined you in private chat<br>')
    });
});
