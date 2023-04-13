$(document).ready(function(){
    alert(1);
    const loadbtn = document.getElementById('load_more')
    const hidebtn = document.getElementById('show_less')
    const content_container = document.getElementById('content-container')

    function loadmoreStock(){
        var current_lenght = $('.content-section').length;
        $.ajax({
            url : "{% url 'load-more' %}",
            // url : 'load',
            type : 'GET',
            data : {
                'total_item' : current_lenght
            },
            beforeSend: function(){
            },
            success: function(response){
                console.log(2);
                const data = response.stocks;
                data.map(stock => {
                    content_container.innerHTML += `<article class="media content-section" id=stock_${stock.id}>
                                                        <div class="media-body">
                                                            <div class="article-metadata">
                                                                <a class="mr-2" href="${stock.id}">${ stock.title }</a>
                                                                <small class="text-muted">${stock.name }</small>
                                                            </div>
                                                            <p class="article-content">Price ${ stock.price } INR on ${ stock.date_posted}</p>
                                                        </div>
                                                    </article>`
                });
                current_lenght = $('.content-section').length;
                if (current_lenght > 5){
                    hidebtn.style.display = "block";                       
                }
                if(current_lenght == response.total_obj_length){
                    console.log(1);
                    loadbtn.style.display = "none";                      
                }
            },
            error: function(){
            }
        });
    }

    function showlessStock(){
        var current_lenght = $('.content-section').length;
        $.ajax({
            url : 'load',
            type : 'GET',
            data : {
                'total_item' : current_lenght
            },
            beforeSend: function(){
            },
            success: function(response){
                var data = response.stocks
                data.map(stock => {
                    $('#stock_'+stock.id).remove();
                });
                if ($('.content-section').length <= 5){
                    hidebtn.style.display = "none";
                }
                loadbtn.style.display = "block";
            },
            error: function(){
            }
        });
    }

    loadbtn.addEventListener('click', ()=> {
        loadmoreStock();
    });

    hidebtn.addEventListener('click', ()=> {
        showlessStock();
    });
});