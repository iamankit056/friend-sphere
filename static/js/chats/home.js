function LoadChats(receiver_id) 
{
    $.ajax({
        type: 'GET',
        url: 'http://localhost:9000/receiver/'+ receiver_id + '/chats',
        success: function(chats, status) {
            if(status == 'success') {
                chats.forEach(chat => {
                    $('#my_chats').append(ChatRowHtml(chat))
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

LoadChats(2)