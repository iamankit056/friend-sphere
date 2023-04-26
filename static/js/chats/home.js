let active_user
const time_for_makeing_chat_request = 2000

function SendMessage() {
        console.log('send btn clicked...')
        msg_sender = $('#msg_sender').val();
        msg_receiver = $('#msg_receiver').val();
        text = $('#text').val()

        if(!msg_sender || !msg_receiver) {
            alert('sender or receiver missing...');
            return;
        }

        if(!text) {
            alert('please type any text before send');
        }

        $.ajax({
            type: 'get',
            url: 'http://localhost:9000/receiver/' + msg_receiver + '/chat/send?text=' + text,
            success: function() {
                console.log('message send...');
            }
        })

        return false;
}

function ActivateChattingForReceiver(receiver_id) {
    if (!active_user)
        clearInterval(active_user)

    active_user = setInterval(() => {
        LoadMessages(receiver_id)
    }, time_for_makeing_chat_request)

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
        '<button onclick="delete_chat(' + chat.id + ')">' + 
                '<i class="fa fa-trash" aria-hidden="true"></i>' + 
        '</button>' +
    '</div>')
}

function delete_chat(chat_id) {
    $.ajax({
        type: 'get',
        url: 'http://localhost:9000/user/chat/' + chat_id + '/delete',
        success: function() {
            console.log(`message with id ${chat_id} deleted successesfully...`)
        }
    })
}