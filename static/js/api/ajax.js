$(document).ready(function(){  
  $(".shopping-list__button").click(function(){
    $.ajax({  
      method: "GET",
      type: 'json',
      data: {
      },
      url: '/api/v1/delete-button',
      success: function(response){
        console.log(response.data)
        if (response.data == true){
          $('#download_button').remove()
          $('#download_link').remove()
        }
      }}
    )}
  )
})
