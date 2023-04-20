function load_chats(reciver_id) 
{
    $.ajax({
        type: 'GET',
        url: 'http://localhost:9000/user/' + reciver_id + '/chats',
        success: function(chats, status) {
            console.table(chats)
            console.table(status)
        }
    })
}

load_chats(9)