const socket = io.connect('http://127.0.0.1:5000');

$(document).ready(function() {
    const room = $('#room-name').html();
    console.log(socket.id)
    socket.emit('join', {
        username: 'jura',
        room: room
    });

    socket.on('join_announcement', function(msg){
        $("#messages").append('<li>'+msg+'</li>');
    });
    
    socket.on('leave_announcement', function(msg){
        $("#messages").append('<li>'+msg+'</li>');
    });

    socket.on('message', function(msg) {
        $("#messages").append('<li>'+msg+'</li>');
    });
    
    $('#sendbutton').on('click', function() {
        let message = $('#myMessage').val();
        socket.emit('message', {
            message: message,
            room: room
        });
        $('#myMessage').val('');
    });
});
