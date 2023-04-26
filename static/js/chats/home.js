let active_user
const time_for_makeing_chat_request = 2000

$(document).ready(function() {
    $('#message_send_btn').click(function() {
        console.log('send btn clicked...')
    });
})

function ActivateChattingForReceiver(receiver_id) {
    // if (!active_user)
    //     clearInterval(active_user)

    // active_user = setInterval(() => {
    //     LoadMessages(receiver_id)
    // }, time_for_makeing_chat_request)

    LoadMessages(receiver_id)
    // change receiver
    document.getElementById('msg_receiver').value = receiver_id;
}

function LoadMessages(receiver_id) {
    $.ajax({
        type: 'GET',
        url: 'http://localhost:9000/receiver/' + receiver_id + '/chats',
        success: function(chats, status) {

            if(status == 'success') 
            {
                $('#my-chats').html('')
                chats.forEach(chat => {
                    if(chat.msg_sender == receiver_id) 
                        $('#my-chats').append(ChatRowHtml(chat, 'receiver'));
                    else 
                        $('#my-chats').append(ChatRowHtml(chat, 'sender'));
                });
            }
        }
    })
}

function ChatRowHtml(chat, className='sender') {
    return ('<div class="' + className + '">' +
        '<pre>' + chat.text + '</pre>' +
        '<button>' + 
            '<a href="user/chat/' + chat.id + '/delete">' +
                '<i class="fa fa-trash" aria-hidden="true"></i>' + 
            '</a>' +
        '</button>' +
    '</div>')
}