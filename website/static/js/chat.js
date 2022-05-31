const socket = io.connect('http://127.0.0.1:5000');
const private = io.connect('http://127.0.0.1:5000/private')
let usernameActive, sender, senderPublicKey, derivedKey;

async function openChat(params) {
    /* 
    Function for starting the chat with another user 
    
    Sends sin request to selected user which includes exporing public and sending it
    */
    usernameActive = params
    let exportedKey = await exportKey(keyPair)
    $('.chat-box').empty();
    private.emit('sin', {
        sender: sender,
        recepient: usernameActive,
        senderPublicKey: exportedKey
    });
    console.log("sin");
    $('.chat-box').attr('id', usernameActive)
}

async function ack(data) {
    /* 
    Function for accepting user request for chatting 
    
    Imports senders public key derives key for encryption and sends
    */
    senderPublicKey = await importKey(data["senderPublicKey"])
    derivedKey = await deriveKey(keyPair.privateKey, senderPublicKey)
    $('<span/>', {
        class: 'badge badge-danger',
        text: '!'
    }).appendTo('#'+data['senders']);
    $('div#'+data['sender']).append(data['sender']+' has joined you in private chat<br>')
    console.log("ack");
}

async function encrypt(derivedKey) {
    /* 
    Function for encrypting and sending message
    */
    const message = $('#myMessage').val()
    let encodedMessage = new TextEncoder().encode(message)
    const iv = window.crypto.getRandomValues(new Uint8Array(12));
    let encryptedMessage = await window.crypto.subtle.encrypt( {name: "AES-GCM", iv: iv }, derivedKey, encodedMessage)

    private.emit('message', {
        sender: sender,
        recepient: usernameActive,
        message: encryptedMessage,
        iv: iv
    });
    $('div#'+usernameActive).append('<div>'+message+'</div>');
    $('#myMessage').val('');
    console.log("sent message");
}

async function decrypt(data, derivedKey) {
    /* 
    Functio for decrypting recived message and displing it
    */
    const iv = data["iv"]
    const ciphertext = data["message"];
    let decryptedMessage = await window.crypto.subtle.decrypt( { name: "AES-GCM", iv: iv }, derivedKey, ciphertext );
    const decoded = new TextDecoder().decode(decryptedMessage);
    $('div#'+data['sender']).append('<div class="recevied">'+decoded+'</div>');
    console.log("recived message");
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

    //Listening for new messages
    private.on('deliver_message', function(data) {
        decrypt(data, derivedKey)
    });
    
    //Funciton for sending message
    $('#sendbutton').on('click', function() {
        encrypt(derivedKey)
    });

    //Waiting for ack response
    private.on('ack', function (data) {
        ack(data)
    });
});
