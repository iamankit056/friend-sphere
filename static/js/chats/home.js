let active_user
const time_for_makeing_chat_request = 2000

function ActivateChattingForReceiver(receiver_id) {
    if (!active_user)
        clearInterval(active_user)

    active_user = setInterval(() => {
        LoadChats(receiver_id)
    }, time_for_makeing_chat_request)
}

function LoadChats(receiver_id) 
{
    $.ajax({
        type: 'GET',
        url: 'http://localhost:9000/receiver/' + receiver_id + '/chats',
        success: function(chats, status) {
            if(status == 'success') {
                // load sender chats
                chats.sender.forEach(chat => {
                    $('#sender_chats').append(ChatRowHtml(chat))
                });
                // load reveiver chats
                chats.reciver.forEach(chat => {
                    $('#receiver_chats').append(ChatRowHtml(chat))
                });
            }
        }
    })
}

function ChatRowHtml(chat) {
    return ('<tr>' + 
        '<td>' + chat.id + '</td>' +
        '<td>' + chat.text + '</td>' +
        '<td>' + chat.file + '</td>' +
        '<td>' + chat.msg_sender + '</td>' +
        '<td>' + chat.msg_receiver + '</td>' +
        '<td>' + chat.is_read + '</td>' +
    '</tr>')
}