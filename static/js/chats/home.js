let active_user
const time_for_makeing_chat_request = 2000

function ActivateChattingForReceiver(receiver_id) {
    // if (!active_user)
    //     clearInterval(active_user)

    // active_user = setInterval(() => {
    //     LoadChats(receiver_id)
    // }, time_for_makeing_chat_request)

    LoadChats(receiver_id)
}

function LoadChats(receiver_id) 
{
    $.ajax({
        type: 'GET',
        url: 'http://localhost:9000/receiver/' + receiver_id + '/chats',
        success: function(chats, status) {
            if(status == 'success') 
            {
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
    return (
        '<div class="' + className + '">' +
            '<pre>' + chat.text + '</pre>' +
            '<button>' + 
                '<a href="user/chat/' + chat.pk + '/delete"'> +
                    '<i class="fa fa-trash" aria-hidden="true"></i>' + 
                '</a>' +
            '</button>' +
        '</div>')
}