function load_chats(receiver_id) 
{
    $.ajax({
        type: 'GET',
        url: 'http://localhost:9000/user/chats',
        contentType: 'application/json',
        data: {
            'receiver_id': receiver_id
        },
        dataType: 'json',
        success: function(chats, status) {
            if(status == 'success') {
                console.table(chats)
            }
        }
    })
}

load_chats(9)